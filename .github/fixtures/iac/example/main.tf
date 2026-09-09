# Fixture for the iac-lint / iac-checkov smoke test. Deliberately trivial and
# deliberately VALID: the smoke test proves the actions LOAD and RUN, not that
# they detect anything — a fixture with real findings would make the test fail
# for the thing it is not testing, and would need a baseline to stay green.
terraform {
  required_version = ">= 1.6.0"
}

resource "terraform_data" "example" {
  input = "iac-actions-smoke"
}
