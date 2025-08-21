terraform {
  backend "gcs" {
    bucket  = "tf-state-stage"
    prefix  = "envs/gcp/stage"
  }
}
