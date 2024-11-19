#Will be responsible for creating my ml application as a pacakage and can deploy it as a pipeline
from setuptools import find_packages,setup #Finds all the pacakages that are available in the entire ml application directory
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove new line characters and strip whitespace
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
name = "Generic-ml-project",
version = '0.0.1',
author = 'Shivam',
author_email = 'shivammahadik0@gmail.com',
packages = find_packages(),#find packages will find the folders having __init__.py and it will consider that folder as package itself and it will try to build that and once it builds we can import it anywhere we want like we import seaborn pandas etc. Entire project dev will happen in src
# install_requires=['pandas','numpy','seaborn'], #Tedeas manually so insted
install_requires = get_requirements('requirements.txt')

)