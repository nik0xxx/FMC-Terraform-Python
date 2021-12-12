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


resource "fmc_network_objects" "network_object_name" {
  for_each     = var.network_objects
  name        = each.value.name
  value       = each.value.value
  description = each.value.description
}



output "new_fmc_network_object_3" {
  value = fmc_network_objects.network_object_name
}