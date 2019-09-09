from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'slackmon',
  packages = ['slackmon'],
  version = '1.4.2',
  license='GNU GENERAL PUBLIC LICENSE', 
  description = 'A Slack channel message retriever. This script obtains \
  Slack messages for all channels (public, private, direct, and group) for \
  a specified amount of time for a Workspace.',
  long_description=long_description,
    long_description_content_type='text/markdown', 
  author = 'Rob Sitro',  
  author_email = 'rsitro4@gmail.com',
  url = 'https://github.com/corpseReviver/python-slackmon',
  download_url = 'https://github.com/corpseReviver/python-slackmon/archive/v_1_4_2.tar.gz',
  keywords = ['slack auditor', 'slack', 'slack message retriever', 'slack logging', 'logging'],
  install_requires=[ 
          'pathvalidate',
          'argparse',
	  'slackclient'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',    'License :: OSI Approved :: MIT License',   # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7', 
  ],
  entry_points={
        "console_scripts": [
            "slackmon=slackmon.__main__:main",
        ]
    },
)
