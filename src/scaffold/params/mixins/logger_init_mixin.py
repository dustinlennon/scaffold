from scaffold.params.logger_factory import LoggerFactory, logging
from scaffold.params.base_mixin import BaseMixin
from scaffold.params import _printf_debug

class LoggerInitMixin(BaseMixin):
  def assign_args(self, args):
    _printf_debug("LoggerInitMixin.assign_args")
    super().assign_args(args)
    factory = LoggerFactory()
    factory.configure(
      config_file = str(args.log_config_path),
      logs_path   = str(args.logs_path)
    )
    self._factory = factory

  def get_logger(self, qualname) -> logging.Logger:
    return self._factory(qualname)