from setuptools import setup
import setuptools.command.build_py
import subprocess 

class MakeSharedObject(setuptools.command.build_py.build_py):
  def run(self):
    subprocess.run(["make", "all"])


setup(
    cmdclass={
        'build_py': MakeSharedObject
    }
)
