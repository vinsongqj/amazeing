from typing import Dict, Any


class ConfigError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__("Config Error: " + msg)


def validate_fields(config: Dict[str, Any]) -> None:
    check_for_empty_field(config)
    field_validation_rules(config)


def check_for_empty_field(config: Dict[str, Any]) -> None:
    for key, value in config.items():
        if key in ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT',
                   'OUTPUT_FILE', 'PERFECT']:
            if value is None:
                raise ConfigError(f"Invalid or empty data in field: '{key}'")


def field_validation_rules(config: Dict[str, Any]) -> None:
    size_x, size_y = (config["WIDTH"], config["HEIGHT"])
    entry_x, entry_y = config["ENTRY"]
    exit_x, exit_y = config["EXIT"]

    if (entry_x >= size_x or entry_y >= size_y) or (entry_x < 0
                                                    or entry_y < 0):
        raise ConfigError(f"Entry coordinates out of bounds {config["ENTRY"]}")
    if (exit_x >= size_x or exit_y >= size_y) or (exit_x < 0 or
                                                  exit_y < 0):
        raise ConfigError(f"Exit coordinates out of bounds {config["EXIT"]}")
    if (entry_x == exit_x and entry_y == exit_y):
        raise ConfigError("Entry and Exit coordinates cannot occupy "
                          "the same space")
