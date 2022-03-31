# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------
# logger.py - Controls all aspects of logging for the bot.
#
# Description:
# This module allows customized logging of all input and output of the bot
# all of which can be stored on-disk or in-memory; with added encryption.
# -------------------------------------------------------------------------
import os, sys, discord.ext.commands
from datetime import datetime
from src.helpers.tools.colors import Colors

# Obtains the current working directory and appends the log folder and current datetime as the log file.
_default_log_file = f"{sys.path[0]}\\logs\\{datetime.now().strftime('%Y-%m-%d')}.txt"


class Logger:
    """Logging class with high degree of customization."""

    def __init__(self: "Logger", module_name: __name__, write_output: bool = True, log_file: str = _default_log_file):
        self.module_name = module_name
        self.write_output = write_output
        self.log_file = log_file

    class Verbosity:
        """Encapsulates the varying degrees of logging output detail."""
        low = 0
        default = 1
        high = 2
        debug = 3

    def _write(self: "Logger", entry: str) -> bool:
        """Internal method which allows the writing of a string message to a file."""
        # Check if the log file is the default one and create its directory if it doesn't exist.
        if self.log_file == _default_log_file:
            if not os.path.exists(sys.path[0] + "/logs/"):
                os.mkdir(sys.path[0] + "/logs/")
        try:
            # Log the entry into the log file and return a result flag.
            with open(self.log_file, "a") as log:
                log.write(entry + "\n")
                return True
        except:
            pass
        # self.error(f"The log file or its directory does not exist: {self.log_file}", write_output=False)
        return False

    def info(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes a non-critical information based message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.darkgrey}INFO{Colors.reset} | {Colors.Foreground.blue}{self.module_name}{Colors.reset} > {message}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def note(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes a note-worthy information based message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.lightgrey}NOTE{Colors.reset} | {Colors.Foreground.blue}{self.module_name}{Colors.reset} > {message}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def success(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes a success message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.green}PASS{Colors.reset} | {Colors.Foreground.blue}{self.module_name}{Colors.reset} > {message}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def warning(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes a warning message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.yellow}WARN{Colors.reset} | {Colors.Foreground.blue}{self.module_name}{Colors.reset} > {message}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def error(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes an error based message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.red}FAIL{Colors.reset} | {Colors.Foreground.blue}{self.module_name}{Colors.reset} > {Colors.Foreground.red}{message}{Colors.reset}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def debug(self: "Logger", message: str, write_output: bool = True) -> None:
        """Displays and or writes a debug based message to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        entry = (
            f"{Colors.Foreground.pink}{timestamp}{Colors.reset} | {Colors.Foreground.pink}{Colors.bold}DEVS{Colors.reset} | {Colors.Foreground.pink}{Colors.bold}{self.module_name}{Colors.reset} > {Colors.Foreground.pink}{message}{Colors.reset}")
        if write_output:
            if self.write_output:  # Make sure the global flag allows us to print.
                self._write(entry)
        print(entry)

    def log_command(self: "Logger", ctx: discord.ext.commands.Context) -> str:
        """Displays and or writes a Discord command and its details to the console and or a logging file."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        command = str(ctx.command)
        guild = ctx.guild.name if ctx.guild is not None else 'DM'
        user = str(ctx.author)
        return f"{command:27} > {guild} | {user} | \"{ctx.message.content}\""

    def custom_command_format(self: "Logger", ctx: discord.ext.commands.Context, keyword: str) -> str:
        """Displays and or writes a Discord command and its details to the console and or a logging file using a custom format."""
        timestamp = datetime.now().strftime("%Y-%m-%d @ %H:%M:%S")
        guild = ctx.guild.name if ctx.guild is not None else 'DM'
        user = str(ctx.author)
        return f"{f'custom({keyword})':>24} > {guild} | {user} | \"{ctx.message.content}\""
