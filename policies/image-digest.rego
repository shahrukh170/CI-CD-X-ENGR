package k8s

deny[msg] {
  input.kind == "Deployment"
  not endswith(input.spec.template.spec.containers[_].image, "@sha256")
  msg := "Images must be pinned by digest"
}
