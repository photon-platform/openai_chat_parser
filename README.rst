==================
OpenAI Chat Parser
==================

Overview
========

OpenAI Chat Parser is a Python script that downloads, extracts, and parses OpenAI chat conversation archives. The script takes a ZIP URL as input and processes the conversations, organizing them into separate folders with appropriate file formats based on the conversation content.

Features
========

* Download chat archives from a given URL
* Extract and parse conversations from the downloaded archives
* Organize conversations into separate folders with appropriate file formats
* Support for configuration file to customize various settings

Requirements
============

* Python 3.6 or higher
* `slugify` package

Installation
============

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/your_username/openai_chat_parser.git

2. Install the required packages:

   .. code-block:: bash

      pip install -r requirements.txt

Usage
=====

1. Modify the `config.json` file to customize settings such as destination path, archive folder, export folder, and download retry settings.

2. Run the script:

   .. code-block:: bash

      python openai_chat_parser.py

3. Enter the ZIP URL when prompted.

License
=======

This project is licensed under the MIT License.

Contributing
============

Feel free to create issues, submit pull requests, or contact the maintainers for any bugs, improvements, or feature requests.

