from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",             # 
    settings_files=['.settings.toml','.secrets.toml'],      # load config files
    environments=False,                  # enable layered environment config
    
)