# run the terraform with the command    "terraform plan -var-file variables_hosts.tfvars"

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



resource "fmc_host_objects" "hosts" {

#  count = "${length(var.host_objects)}"
  for_each = var.host_objects
  name        = each.value.name
  value       = each.value.value
  description = each.value.description
}



