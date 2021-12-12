# FMC-Terraform-Python
Automate FMC object creation with Terraform and Python
The content of this file will be updated soon

Automate Cisco FMC objects (host, ports, network ) using Python and Terraform. 
The scripts located in this repo, have been tested to work as expected in Cisco FMC 6.6.5




Python will be used in order to fill the variables.tfvars of Terraform FMC provider. 

1) We will obtain the variables of each object (port, host, etc) that we want to configure in FMC from 
   a CSV file. In our case the CSV files are located in Python_FMC folder named "host_objects.csv , network_objects.csv and
   port_objects.csv

2) The "terraform_config_gen.py" python script will use the variables in these CSV files and will generate variables.tfvars. The 
   variables.tfvars will be saved automaticall to the correct folder of each object in Terraform. 