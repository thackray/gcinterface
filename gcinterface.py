# rough sketch of functionality

import os, shutil
#from gchem import gchem

class GCFile(object):
     def __init__(self, filename):
          self.filename = filename
          self.content = ''
     def write(self,):
          with open(self.filename, 'w') as f:
               f.write(self.content)
          return
     def load_template(self, template_filename):
          with open(template_filename, 'r') as f:
               self.content = f.read()
          return
     def set_value(self, tag, value):
          # put @tags in the template to replace with value using this function
          if not tag.startswith('@'):
               tag = '@'+tag
          self.content = self.content.replace(tag, value)
          return
     def set_values(self, dictionary):
          # dictionary of paramtag:value pairs
          for param in dictionary:
               self.content = self.content.replace('@'+param,dictionary[param])
          return

class InputGeos(GCFile):
     def set_dates(self, run_start_date, run_end_date):
          self.template = self.template.replace('@STARTDATE', run_start_date)
          self.template = self.template.replace('@ENDDATE', run_end_date)
          return
     def set_emis(self, emis_filename):
          self.template = self.template.replace('@EMISFILEPATH', emis_filename)
          return

class RunDir(object):
     def write_file(self, fileobj):
          fileobj.write()
          return
     def copy_file(self, origin, destination):
          shutil.copy( os.path.join( origin, destination ) )
          return

class EmisFile(GCFile):
     def scale_emissions(self,):
          return
     def convert_emis_format(self,):
          return
     
class RestartFile(GCFile):
     def init_from_prior(self,):
          return
     def scale_tracers(self,):
          return
     def add_tracer(self,):
          return
     def remove_tracer(self,):
          return

if __name__=='__main__':
     i = GCFile('testinputfile')
     i.load_template('input.template')
     i.set_value('@EMISFILEPATH','new/emis/path')
     i.write()

     
