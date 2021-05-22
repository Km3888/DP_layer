#include <torch/extension.h>

#include <iostream>
#include <vector>

torch::Tensor d_sigmoid(torch::Tensor z) {
  auto s = torch::sigmoid(z);
  return (1 - s) * s;
}

torch::Tensor dp_forward(
    torch::Tensor input) {
  auto x=torch::sum (input);
  return x;
}

torch::Tensor d_tanh(torch::Tensor z) {
  return 1 - z.tanh().pow(2);
}

// elu'(z) = relu'(z) + { alpha * exp(z) if (alpha * (exp(z) - 1)) < 0, else 0}
torch::Tensor d_elu(torch::Tensor z, torch::Scalar alpha = 1.0) {
  auto e = z.exp();
  auto mask = (alpha * (e - 1)) < 0;
  return (z > 0).type_as(z) + mask.type_as(z) * (alpha * e);
}

std::vector<torch::Tensor> dp_backward(
    torch::Tensor grad_val,
    torch::Tensor input) {
  return {grad_val};
}


PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("forward", &dp_forward, "DP forward");
  m.def("backward", &dp_backward, "DP backward");
}
