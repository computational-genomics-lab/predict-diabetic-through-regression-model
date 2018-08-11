from setuptools import setup, find_packages

setup(
    name='DiabeticPredict',
    version='0.1',
    packages=find_packages(exclude=['Data*']),
    license='MIT',
    description='Predict Diabetic using non-diabetic measurements',
    long_description=open('README.txt').read(),
    install_requires=['pandas', 'sklearn', 'argparse', 'scipy'],
    url='https://github.com/computational-genomics-lab/predict-diabetic-through-regression-model',
    author='Samrat Ghosh, Arijit Panda',
    author_email='samrat.ghosh2010@gmail.com, rjit17@gmail.com'
)
