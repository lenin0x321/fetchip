import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "fetchip",
    packages = ["fetchip"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "5.0",
    description = "Get your public IP address and there Details",
    author = "lenin Royal",
    author_email = "leninroyal@outlook.com",
    keywords = "ip address",
    install_requires = ["requests"],
    url = "https://www.spyberrys.co.in",
    
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        'Source': 'https://gitlab.com/yoginth/publicip',
    },
)
