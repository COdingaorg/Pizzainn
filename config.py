class Config():
  '''
  defines general configurations
  '''
  pass

class ProdConfig(Config):

  pass

class DevConfig(Config):

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}