from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

import os.path as osp


ROOT = osp.dirname(osp.abspath(__file__))

# Package metadata lives in pyproject.toml; setup.py only declares the CUDA extensions.
setup(
    packages=['lietorch'],
    ext_modules=[
        CUDAExtension('lietorch_backends',
            include_dirs=[
                osp.join(ROOT, 'lietorch/include'),
                osp.join(ROOT, 'eigen')],
            sources=[
                'lietorch/src/lietorch.cpp',
                'lietorch/src/lietorch_gpu.cu',
                'lietorch/src/lietorch_cpu.cpp'],
            extra_compile_args={
                'cxx': ['-O2'],
                'nvcc': ['-O2',
                    '-gencode=arch=compute_80,code=sm_80',
                    '-gencode=arch=compute_86,code=sm_86',
                    '-gencode=arch=compute_90,code=sm_90',
                    '-gencode=arch=compute_90,code=compute_90',
                ]
            }),

        CUDAExtension('lietorch_extras',
            sources=[
                'lietorch/extras/altcorr_kernel.cu',
                'lietorch/extras/corr_index_kernel.cu',
                'lietorch/extras/se3_builder.cu',
                'lietorch/extras/se3_inplace_builder.cu',
                'lietorch/extras/se3_solver.cu',
                'lietorch/extras/extras.cpp',
            ],
            extra_compile_args={
                'cxx': ['-O2'],
                'nvcc': ['-O2',
                    '-gencode=arch=compute_80,code=sm_80',
                    '-gencode=arch=compute_86,code=sm_86',
                    '-gencode=arch=compute_90,code=sm_90',
                    '-gencode=arch=compute_90,code=compute_90',
                ]
            }),
    ],
    cmdclass={ 'build_ext': BuildExtension }
)


