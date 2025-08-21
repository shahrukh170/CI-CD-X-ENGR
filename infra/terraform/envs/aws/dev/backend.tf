terraform {
  backend "s3" {
    bucket         = "tf-state-dev"
    key            = "envs/aws/dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-state-locks"
    encrypt        = true
  }
}
