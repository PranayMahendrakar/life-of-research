"""
Life Of Research — Setup Configuration
By Pranay Mahendrakar
"""

from setuptools import setup, find_packages
import os

# Read README for long description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='life-of-research',
    version='5.0.0',
    description='14-Agent Autonomous AI Research Lab — Generate publication-quality papers with GPT-4o',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pranay Mahendrakar',
    author_email='pranay@sonytech.in',
    url='https://github.com/PranayMahendrakar/life-of-research',
    project_urls={
        'Bug Reports': 'https://github.com/PranayMahendrakar/life-of-research/issues',
        'Source': 'https://github.com/PranayMahendrakar/life-of-research',
        'Website': 'https://PranayMahendrakar.github.io/life-of-research',
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: X11 Applications :: Qt',
    ],
    keywords=[
        'research', 'AI', 'GPT-4o', 'academic', 'paper', 'generation',
        'autonomous', 'agent', 'pipeline', 'peer-review', 'NLP'
    ],
    python_requires='>=3.9',
    install_requires=[
        'PySide6>=6.5.0',
        'requests>=2.31.0',
        'python-docx>=1.1.0',
    ],
    entry_points={
        'console_scripts': [
            'life-of-research=life_of_research_app:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
