from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="102383077_Ranveer_Topsis",  
    version="1.0.0",  
    author="Ranveer Raj", 
    author_email="Ranveerraj77@gmail.com",  
    description="A Python implementation of the TOPSIS algorithm for multi-criteria decision analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis",  
    
    packages=find_packages(), 
  
)
