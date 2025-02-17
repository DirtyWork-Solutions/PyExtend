from reporting import log

try:
    from omegaconf import DictConfig, OmegaConf

    def load_config(config_path: str) -> DictConfig:  # TODO: Default paths
        try:
            return DictConfig(OmegaConf.load(config_path))
        except FileNotFoundError as e:
            log.debug(f"Config Error: Missing File '{config_path}'")
            raise e


    settings = load_config('config.yaml')  # TODO: Dynamic destination
except ImportError as e:
    # Fall back to ConfigParser / INI
    try:
        from configparser import ConfigParser

        def load_config(config_path: str) -> ConfigParser:  # TODO: Default paths
            config = ConfigParser()
            try:
                config.read(config_path)
                return config
            except FileNotFoundError as e:
                log.debug(f"Config Error: Missing File '{config_path}'")
                raise e
            finally:
                log.debug("Config LL")

        settings = load_config('config.ini')  # TODO: Dynamic destination

    except ImportError as e:
        raise e
    finally:
        # Fallback to native Python Dict
        log.warning("Dynamic Configuration Failed - Falling back to Python 'dict'")
        settings = {}
finally:
    if type(settings) is dict:
        log.info("Config is (partially) working.")
    else:
        log.success("Config is working.")

