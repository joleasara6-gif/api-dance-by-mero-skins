from setuptools import setup, find_packages

setup(
    name="freefire-bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.9.1",
        "requests>=2.31.0",
        "protobuf>=4.25.3",
        "pycryptodome>=3.20.0",
        "protobuf-decoder>=0.2.0",
        "flask>=2.3.3",
        "cfonts>=1.4.0",
        "pytz>=2023.3",
        "psutil>=5.9.6",
        "pyjwt>=2.8.0"
    ],
    python_requires=">=3.8",
)
