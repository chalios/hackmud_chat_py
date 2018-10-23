from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='hackmud_chat',
      version='0.1a3',
      description='Python binding to Hackmud\'s chat API',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Communications :: Chat',
        'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)'
      ],
      keywords='hackmud chat api',
      url='https://bitbucket.org/chalios/hackmud_chat/',
      author='Chalios',
      author_email='chalios@protonmail.com',
      license='MIT',
      packages=['hackmud_chat'],
      install_requires=[
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)
