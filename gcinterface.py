# rough sketch of functionality

class GCFileObj(object):
     def init(self, filename):
          self.filename = filename

class InputGeos(gcfileobj):
     def write
     def open_from_template
     def set_dates
     def set_emis
     def set_params
     
class RunDir(object):
     def write_file
     def copy_file
     def make_restart
     
class EmisFile(GCFileObj):
     def scale_emissions
     def convert_emis_format
     
class RestartFile(GCFileObj):
     def init_from_prior
     def scale_tracers
     def add_tracer
     def remove tracer
     
