# rough sketch of functionality

import os, shutil
from gchem import gchem

class GCFileObj(object):
     def init(self, filename):
          self.filename = filename

class InputGeos(gcfileobj):
     def write(self,):
          # self.filename is set
          return
     def open_from_template(self, template_filename):
          return
     def set_dates(self, run_start_date, run_end_date):
          self.run_start_date = run_start_date
          self.run_end_date = run_end_date
          return
     def set_emis(self, emis_filename):
          self.emission_filename = emis_filename
          return
     def set_params(self, params):
          for param in params:
               self.param = params[param]
          return

class RunDir(object):
     def write_file(self, fileobj):
          fileobj.write()
          return
     def copy_file(self, origin, destination):
          shutil.copy( os.path.join( origin, destination ) )
          return

class EmisFile(GCFileObj):
     def scale_emissions(self,):
          return
     def convert_emis_format(self,):
          return
     def write(self, ):
          return
     
class RestartFile(GCFileObj):
     def init_from_prior(self,):
          return
     def scale_tracers(self,):
          return
     def add_tracer(self,):
          return
     def remove_tracer(self,):
          return
     def write(self,):
          # write at self.filename
          return


     
