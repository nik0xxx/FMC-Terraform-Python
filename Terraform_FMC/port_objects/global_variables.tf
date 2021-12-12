variable "fmc_username" {
    type = string
    sensitive = true
    default = "userapi"
}

variable "fmc_password" {
    type = string
    sensitive = true
    default = "userapi"
}

variable "fmc_insecure_skip_verify" {
    type = bool
    default = true
}


variable "fmc_host" {
    type = string
    default = "10.0.176.140"
}

variable "port_objects" {
type = map
}