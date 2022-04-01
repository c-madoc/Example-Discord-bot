import os


class SystemUtils:
    """Encapsulation of common operating system identifiers."""
    windows = "nt"
    linux = "posix"
    macos = "posix"
    cygwin = "posix"

    def get_system(self: "SystemUtils") -> str:
        """Returns the name of the currently running operating system."""
        return os.name
