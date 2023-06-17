from setuptools import find_packages,setup

HYPHEN='-e .'
def get_requirements(file_path:str)->list[str]:
    """
    This will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace('\n','') for r in requirements]
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

setup(
    name='ml_algorithms',
    version='0.0.1',
    author='govardhan',
    author_email='vgovardhanvarma.vh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)