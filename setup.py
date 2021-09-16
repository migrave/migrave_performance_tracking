#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['migrave_performance_tracking', 'migrave_performance_tracking_wrapper'],
    package_dir={'migrave_performance_tracking': 'common/src/migrave_performance_tracking',
                 'migrave_performance_tracking_wrapper': 'ros/src/migrave_performance_tracking_wrapper'}
)

setup(**d)
