"""
    Praemunio Python SDK

    Python client for the Praemunio public API.

    The version of the OpenAPI document: 1.0.0
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "praemunio-sdk"
VERSION = "1.0.2"
PYTHON_REQUIRES = ">= 3.11"
REQUIRES = [
    "urllib3 >= 2.7.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2.11",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Python client for the Praemunio public API",
    author="Praemunio",
    author_email="team@praemunio.org",
    url="https://github.com/praemunio/sdks",
    project_urls={
        "Repository": "https://github.com/praemunio/sdks",
        "Documentation": "https://docs.praemunio.org",
    },
    keywords=["praemunio", "api", "sdk", "openapi-client"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Python client for the Praemunio public API.

    Install with:

        pip install praemunio-sdk

    Quick start:

        from praemunio_sdk import PraemunioClient

        client = PraemunioClient.sandbox("YOUR_PUBLIC_KEY", "YOUR_SECRET_KEY")
        client.authenticate()
        api = client.create_api()
        result = api.workspaces_drive_get()
        print(result)
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)
