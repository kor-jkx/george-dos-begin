import typing, json, os

class Config(object):

    #########################
    # Begin Singleton Section
    #########################

    _CONFIG_FILE: typing.Optional[str] = None
    _CONFIG: typing.Optional[dict] = None

    def __init__(self, config_file = None):
        if config_file is None:
            config_file = Config.get_required_env_var("CONFIG_FILE")

        # Check that specified config file exists
        assert os.path.exists(config_file)

        # Use singleton pattern to store config file location/load config once
        Config._CONFIG_FILE = config_file
        with open(config_file, 'r') as f:
            Config._CONFIG = json.load(f)

    @staticmethod
    def get_config_file() -> str:
        return Config._CONFIG_FILE

    @staticmethod
    def get_required_env_var(envvar: str) -> str:
        if envvar not in os.environ:
            raise ConfigException(f"Please set the {envvar} environment variable")
        return os.environ[envvar]

    @staticmethod
    def get_required_env_var(envvar: str) -> str:
        if envvar not in os.environ:
            raise Exception("Please set the {envvar} environment variable")
        return os.environ[envvar]

    @staticmethod
    def get_required_config_var(configvar: str) -> str:
        assert Config._CONFIG
        if configvar not in Config._CONFIG:
            raise Exception(f"Please set the {configvar} variable in the config file {Config._CONFIG_FILE}")
        return Config._CONFIG[configvar]

    #############################
    # Begin Configuration Section
    #############################

    _FOO: typing.Optional[str] = None
    _BAR: typing.Optional[str] = None

    @classmethod
    def get_foo_var(cls) -> str:
        """Example variable that is set in the config file (preferred)"""
        if cls._FOO is None:
            cls._FOO = Config.get_required_config_var('foo')
        return cls._FOO

    @classmethod
    def get_bar_var(cls) -> str:
        """Example variable that is set via env var (not preferred)"""
        if cls._BAR is None:
            cls._BAR = Config.get_required_env_var('BAR')
        return cls._BAR

    @classmethod
    def get_wuz(cls) -> str:
        if cls._WUZ is None:
            if 'wuz' not in cls._CONFIG:
                cls._WUZ = Config.get_required_env_var('WUZ')
            else:
                cls._WUZ = cls._CONFIG['wuz']
        if not os.path.isdir(cls._WUZ):
            raise Exception(f"Error: Path {cls._WUZ} is not a directory")
        return cls._WUZ

    @classmethod
    def reset(cls) -> None:
        cls._CONFIG_FILE = None
        cls._CONFIG = None
        cls._FOO = None
        cls._BAR = None
        cls._WUZ = None