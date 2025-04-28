"""Definicion de la clase Formatter"""

from io import StringIO
from logging import Formatter as BaseFormatter, DEBUG,INFO, WARNING, ERROR, CRITICAL
from os import path
from logger.ANSII import ANSII


class Formatter(BaseFormatter):
    """Personalización de la clase Formatter.
    La idea es ahorrar tiempo en la creación de formatters.
    Se Añade un custom formatter para el logger.
    Se Añade un file handler para el logger, este almacenara los logs en un archivo en la carpeta .logs.
    Se Añade un stream handler para el logger.

    """
    SUCCESS = 25
    FORMATS = {
        DEBUG: f"{ANSII.DARK_GREY}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
        INFO: f"{ANSII.GREEN}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
        WARNING: f"{ANSII.YELLOW}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
        ERROR: f"{ANSII.RED}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
        CRITICAL: f"{ANSII.BOLD_RED}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
        SUCCESS: f"{ANSII.GREEN}%(asctime)s{ANSII.RESET} - %(message)s (%(filename)s:%(lineno)d)",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = BaseFormatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)
