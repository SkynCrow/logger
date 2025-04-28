from io import StringIO
import logging
from logging import FileHandler, Logger as BaseLogger, StreamHandler
from os import makedirs, path
from logger.formatter import Formatter


class Logger(BaseLogger):
    """
    Personalización de la clase Formatter.
    - La idea es ahorrar tiempo en la creación de formatters.
    - Se Añade un custom formatter para el logger.
    - Se Añade un file handler para el logger, este almacenara los logs en un archivo en la carpeta .logs.
    - Se Añade un stream handler para el logger.
    """
    SUCCESS = 25

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        if name == "":
            name = "root"
        makedirs(".logs", exist_ok=True)
        super().__init__(name, level)
        self.string_buffer = StringIO(newline="\n")
        self.string_stream = StreamHandler(self.string_buffer)
        self.string_stream.setFormatter(Formatter())

        file_handler_path = path.join(".logs", name + ".log")
        file_handler = FileHandler(file_handler_path)
        file_handler.setLevel(level)
        self.addHandler(file_handler)
        self.addHandler(self.string_stream)
        self.propagate = False
        self._pause = False
        
    def success(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        if self.isEnabledFor(Logger.SUCCESS):
            self._log(Logger.SUCCESS, msg, args, **kwargs)
if __name__ == "__main__":
    logger = Logger("test")
    logger.info("This is a test")
    logger.debug("This is a test")
    logger.warning("This is a test")
    logger.error("This is a test")
    logger.critical("This is a test")
    print(logger.string_buffer.getvalue())