import torch

# Our module!
import dp_c

class DPFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input_array):
        length = dp_c.forward(input_array) 
        #TODO Make the above spit out a Q array and store it below
        #ctx.save_for_backward(*variables) 

        return length

    @staticmethod
    def backward(ctx, grad_length):
        outputs = lltm_cpp.backward(
            grad_h.contiguous(), grad_cell.contiguous(), *ctx.saved_tensors)
        d_old_h, d_input, d_weights, d_bias, d_old_cell = outputs
        return d_length


class DPLayer(torch.nn.Module):
    def __init__(self):
        super(DPLayer, self).__init__()

    def forward(self, input_array):
        return DPFunction.apply(input_array)
