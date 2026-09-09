# A SECOND fixture directory, so the smoke test exercises the multi-directory
# loop rather than a single iteration. The loops used to abort on the first
# directory that reported anything; a one-directory fixture could never show that.
terraform {
  required_version = ">= 1.6.0"
}

resource "terraform_data" "second" {
  input = "iac-actions-smoke-second"
}
