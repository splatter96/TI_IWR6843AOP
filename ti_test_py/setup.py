import os
from glob import glob
from setuptools import setup

package_name = 'ti_test_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gyro',
    maintainer_email='lightinfected@hotmail.com',
    description='Read uart data from ti iwr6843aopevm mmwave sensor and publish the data in ros2 env',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pcl_pub = ti_test_py.pc_publisher:main',
        ],
    },
)
