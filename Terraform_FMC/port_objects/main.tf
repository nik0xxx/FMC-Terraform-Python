terraform {
  required_providers {
    fmc = {
      source = "CiscoDevNet/fmc"
      # version = "0.1.1"
    }
  }
}

provider "fmc" {
  fmc_username = var.fmc_username
  fmc_password = var.fmc_password
  fmc_host = var.fmc_host
  fmc_insecure_skip_verify = var.fmc_insecure_skip_verify
}


resource "fmc_port_objects" "port_object" {
  for_each     = var.port_objects
  name        = each.value.name
  port       = each.value.port
  protocol       = each.value.protocol
 
}



output "port_object_name" {
  value = fmc_port_objects.port_object
}