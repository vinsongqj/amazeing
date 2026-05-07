from typing import Dict, Tuple, Any
from maze_gen.validator import ConfigError


def extract_config_data(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r") as f:
        config = {
            "WIDTH": None,
            "HEIGHT": None,
            "ENTRY": None,
            "EXIT": None,
            "PERFECT": None,
            "OUTPUT_FILE": None,
            "SEED": None
        }
        filedata_lines = f.readlines()

        for line in filedata_lines:
            split_line = line.strip("\n").split("=")

            if len(split_line) == 2:
                key, value = extract_one_key_value_pair(split_line)

                if validate_key(key):
                    config[key] = parse_raw_value(key, value)
                else:
                    raise ConfigError("Invalid Key field detected")
        return config


def parse_raw_value(key: str, value: Any) -> Any:
    try:
        if key in ['WIDTH', 'HEIGHT']:
            return int(value)
        elif key in ['ENTRY', 'EXIT']:
            x, y = value.split(",")
            return (int(x), int(y))
        elif key in ['PERFECT']:
            if value == "True":
                return True
            elif value == "False":
                return False
            return None
        else:
            if value == '':
                return None
            return value
    except ValueError:
        return None


def validate_key(key: str) -> bool:
    valid_key_list = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT',
        'OUTPUT_FILE', 'PERFECT', 'SEED']
    
    if key not in valid_key_list:
        return False
    return True


def extract_one_key_value_pair(split_line: list[str]) -> Tuple[str, str]:
    if "#" in split_line[1]:
        seperated_values = split_line[1].partition("#")
        ph_value = ""

        for s in seperated_values:
            if "#" not in s:
                ph_value += s
            else:
                break
        return (split_line[0], ph_value.strip())
    else:
        return (split_line[0], split_line[1].strip())
        
