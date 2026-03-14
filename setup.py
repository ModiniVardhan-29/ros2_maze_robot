from setuptools import setup
import os
from glob import glob

package_name = 'bumper_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),

        # URDF files
        (os.path.join('share', package_name, 'urdf'),
            glob('urdf/*.urdf')),

        # World files
        (os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.world')),

        # Models (for obstacles)
        (os.path.join('share', package_name, 'models/box'),
            glob('models/box/*.sdf')),
            
        (os.path.join('share', package_name, 'models/actor'),
        glob('models/actor/*.sdf')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='modini',
    maintainer_email='modini@example.com',
    description='Bumper Bot Simulation Package',
    license='Apache License 2.0',

    entry_points={
        'console_scripts': [
            'obstacle_avoidance = bumper_bot.obstacle_avoidance:main',
        ],
    },
)
