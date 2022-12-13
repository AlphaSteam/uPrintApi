class CustomError(Exception):
  """Base class for other exceptions"""
  pass


class UpdatingNotExistentJob(CustomError):
  """Raised when it tries to update an job that doesn't exists in DB"""
  pass
