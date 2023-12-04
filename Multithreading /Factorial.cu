#include <iostream>
#include <cuda_runtime.h>

const int N = 10;  // Factorial of N

// CUDA kernel to calculate factorial
__global__ void factorialKernel(int *result) {
    int tid = threadIdx.x;

    if (tid == 0) {
        *result = 1;  // Initialize result
    }

    __syncthreads();

    for (int i = tid + 1; i <= N; i += blockDim.x) {
        atomicMul(result, i);  // Multiply result by i
    }
}

int main() {
    int result;
    int *d_result;

    // Allocate device memory for result
    cudaMalloc((void**)&d_result, sizeof(int));

    // Launch kernel with one block and as many threads as N
    factorialKernel<<<1, N>>>(d_result);

    // Copy result from device to host
    cudaMemcpy(&result, d_result, sizeof(int), cudaMemcpyDeviceToHost);

    // Print the result
    std::cout << "Factorial of " << N << " is: " << result << std::endl;

    // Free device memory
    cudaFree(d_result);

    return 0;
}
