# rough sketch of functionality


import os, shutil
#from gchem import gchem

class GCFileObj(object):
     def __init__(self, filename):
          self.filename = filename

class InputGeos(GCFileObj):
     def write(self,):
          # self.filename is set
          with open(self.filename, 'w') as f:
               f.write(self.template)
          return
     def load_template(self, template_filename):
          self.template = open(template_filename, 'r').read()
          return
     def set_dates(self, run_start_date, run_end_date):
          self.template = self.template.replace('@STARTDATE', run_start_date)
          self.template = self.template.replace('@ENDDATE', run_end_date)
          return
     def set_emis(self, emis_filename):
          self.template = self.template.replace('@EMISFILEPATH', emis_filename)
          return
     def set_params(self, params):
          for param in params:
               self.template = self.template.replace('@'+param, params[param])
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

if __name__=='__main__':
     i = InputGeos('testinputfile')
     i.load_template('input.template')
     i.set_emis('new/emis/path')
     i.write()

     
