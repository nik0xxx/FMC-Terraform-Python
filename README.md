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
   
   
   
Special thanks to "adyanth" for providing in his repo various examples of terraform and FMC, which part of them are used also here. I would like to take them one step further and automate the configuration. The end goal is the user to apply the changes to the firewall by using only the csv files. 
By the way, in case some of you want to learn more about FMC, I found the videos of adyanth in youtube one of the best resources for it. 

   
   
   # Requirements 
   
   Python 3.4 +
   
   Installation of Terraform 
   
   
   
   # Usage
   
   Make your own CSV files, ensure that you will have the same headers (name, value description) as the example csv's located here. 
   
   All the values in the CSV files should be with "". 
   
   
   Run the python script which will generate the variables.tfvars files. After that, navigate to the directory where the variables.tfvars files
   are located and run Terraform script.
   
   terraform init    *** It will download all the providers that are referenced in your script
   
   
   terraform plan -var-file variables.tfvars       *** We need to define the location of variables.tfvars 
   
   
   terraform apply -var-file variables.tfvars     *** The change will be applied against the FMC
