from __future__ import print_function, unicode_literals
import csv
import os,sys
from pathlib import Path
from pprint import pprint
from typing import Dict
from PyInquirer import prompt, Separator, style_from_dict


# default config for jinja template initilization

from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)


# the following code is used to presend to user a list of options to choose
def selection ():
    global file1
    global template_hosts1
    global to_be_added1
    global template_output
    questions = [
    {
        'type': 'list',
        'name': 'theme',
        'message': 'Choose what kind of object you want to configure in FMC?',
        'choices': [
            'host',
            'port',
            "network-object"
        ]
    }
]

    answers = prompt(questions)
    
    pprint(f"{'you choosed to configure'.upper()} {answers['theme']} object in FMC ")
    pprint(f" {'The configuration will be according to the variables in the excel file'.upper()}")

 # Based on the user input we will choose which files will be used
    if answers["theme"] == "port":
        file1 = "port_objects.csv"
        template_hosts1 = "tera_port_template.j2"
        to_be_added1 = "port_objects = {\n"
        template_output = Path(r"C:\Automation\Terraform_Firepower\port_objects\variables.tfvars")
        
    
    elif answers["theme"] == "network-object":
        file1 = "network_objects.csv"
        template_hosts1 = "tera_network_objects_template.j2"
        to_be_added1 = "network_objects = {\n"
        template_output = Path(r"C:\Automation\Terraform_Firepower\network_objects\variables.tfvars")

    elif answers["theme"] == "host":
        file1 = "host_objects.csv"
        template_hosts1 = "tera_hosts_template.j2"
        to_be_added1 = "host_objects = {\n"
        template_output = Path(r"C:\Automation\Terraform_Firepower\host_objects\variables.tfvars")
       
        
        
        

    



class terraform_config_fmc:

    def __init__(self, file, template_hosts, to_be_added):

        # file is the csv file. Different for the hosts, or network objects etc..
        self.file = file

        # template_hosts is the jinja file that will be used (different for hosts, network objects etc)
        self.template_hosts = template_hosts

        # to_be_added is the additional that will be added in the final output to match the tera configuration 
        self.to_be_added = to_be_added 




      # with this method, we convert the csv file with the hosts to dictionary and then we fill the jinja template
      # with the values of this dictionary
    def create_objects(self):
        i = 0
        d = {}

#we remove any older existing configuration and we create the new file. 
        os.remove(template_output)

        with open(self.file, "r") as f:
            reader = csv.DictReader(f)

            # this additional loop is need in order to add hosts (that will be the names in the terraform config)
            for line in reader:
                i+=1
                d[i] = line


           # we define what is our template
        template = env.get_template(self.template_hosts)
       
#   we fill the template with the values of the dictionary
#   In order to create different templates from different objects (port, host, netowork_object, etc) we use the if statement
#   if for example, in the csv file there is a cell with name "port", then use the teamplte for port. If not , use the teamplt for
#   host (host and network objcet have the same template) 

        if "port" in d[i]:
            for each  in d:
                output = template.render(host= each, name=d[each]["name"], port =d[each]["port"], protocol = d[each]["protocol"] )
        

            # we write the output in a new file 
                with open(template_output, "a+") as z:
                    z.write(output)
        else:

            for each  in d:
                output = template.render(host= each, name=d[each]["name"], value =d[each]["value"], description = d[each]["description"] ) 
        

            # we write the output in a new file 
                with open(template_output, "a+") as z:
                    z.write(output)



            # we want to add to the file a new line at the top. We could append the new line in the existing file 
            # but this will add the new line at the bottom and not at the top as we want. The function below 
            # adds at the beggining at the end of the file, then it moves the cursor with seek at the beggining and 
            # adds a new line this time at the top of the file
    def line_prepender(self, line):
        with open(template_output, 'r+') as f:
            content = f.read()
            f.seek(0,0)
            f.write( self.to_be_added + content )
    def line_ending(self):
        with open(template_output, 'r+') as f:
            content = f.read()
            f.write( "\n }" )

    def main():
        selection()
        objects = terraform_config_fmc(file1, template_hosts1, to_be_added1)
        objects.create_objects()
        objects.line_prepender(1)
        objects.line_ending()

    

if __name__ == "__main__":
    main()
 

  
  
  

   

