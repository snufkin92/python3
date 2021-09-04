from setuptools import setup

setup(
    name='python3_memo',
    version='0.1.0',
    packages=['syntax', 'syntax.lambda', 'syntax.closure', 'syntax.generator', 'syntax.comprehension', 'database',
              'database.rdb', 'database.nosql', 'database.graphdb', 'database.keyvalue', 'test'],
    url='https://github.com/snufkin92/python3',
    license='MIT',
    author='snufkin92',
    author_email='snufkin92@gmail.com',
    description='python備忘録'
)
