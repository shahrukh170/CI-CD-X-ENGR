terraform {
  backend "gcs" {
    bucket  = "tf-state-dev"
    prefix  = "envs/gcp/dev"
  }
}
