# FMC-Terraform-Python
Automate FMC object creation with Terraform and Python.

Automate creation of Cisco FMC objects (host, ports, network-objects ) using Python and Terraform. 
The scripts located in this repo, have been tested to work as expected in Cisco FMC 6.6.5. 




Python will be used in order to fill the variables.tfvars of Terraform FMC provider. 

1) We will obtain the variables of each object (port, host, etc) that we want to configure in FMC from 
   a CSV file. In our case the CSV files are located in Python_FMC folder named "host_objects.csv , network_objects.csv and
   port_objects.csv

2) The "terraform_config_gen.py" python script will use the variables in these CSV files and will generate variables.tfvars. The 
   variables.tfvars will be saved automaticall to the correct folder of each object in Terraform. 
   
   
   Requirements
   
   Python 3.4 +
   
   Installation of Terraform 
   
   
   
   Usage
   
   Make your own CSV files, ensure that you will have the same headers (name, value description) as the example csv's located here. 
   
   All the values in the CSV files should be with "". 
   
   
   Run the python script which will generate the variables.tfvars files. After that, navigate to the directory where the variables.tfvars files
   are located and run Terraform script.
   
   terraform init    *** It will download all the providers that are referenced in your script
   
   
   terraform plan -var-file variables.tfvars       *** We need to define the location of variables.tfvars 
   
   
   terraform apply -var-file variables.tfvars     *** The change will be applied against the FMC
