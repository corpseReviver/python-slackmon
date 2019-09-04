from distutils.core import setup

setup(
  name = 'slackmon',
  packages = ['slackmon'],
  version = '1.2',
  license='GNU GENERAL PUBLIC LICENSE', 
  description = 'A Slack channel message retriever. This script obtains \
  Slack messages for all channels (public, private, direct, and group) for \
  a specified amount of time for a Workspace.',
  author = 'Rob Sitro',                   # Type in your name
  author_email = 'rsitro4@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/corpseReviver/python-slackmon',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/corpseReviver/python-slackmon/archive/v_1_2.tar.gz',    # I explain this later on
  keywords = ['slack auditor', 'slack', 'slack message retriever', 'slack logging', 'logging'],   # Keywords that define your package best
  install_requires=[ 
          'pathvalidate',
          'argparse'
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
