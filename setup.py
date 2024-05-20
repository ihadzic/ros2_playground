from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'play'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ilija Pantelija',
    maintainer_email='ilija.pantelija@nowhere.com',
    description='My play package',
    license='proprietary',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_pub = play.play_pub:main'
        ],
    },
)
