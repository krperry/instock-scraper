# instock-scraper
This is a simple web page scraper to check stock of some items.

Multi-Script Repository
## Overview
This repository contains multiple scripts for various tasks along with instructions on how to use them and install the necessary modules.
The original script now called instock.py was written by Willo Free.  It was used to show how to do web scraping in a python coding club.
Ken Perry modified the original to create the others and show different ways to display the data.

## Scripts

instock.py:
    Original script by Willo Free that shows several items instock status from Aph web site.
instock_single.py:
Shows the stock of a single item.
instock_loop.py:
Re-creates the instock.py with a loop rather than copying each item.

instock_clip.py
Recreates the original script but adds all the items to the clipboard.

instock_wx:
Re-creates the original and shows the information in a dialog.

## Installation

Before running the scripts, ensure you have Python installed on your system. You can download Python from the official Python website.

## Installing Required Modules

Each script may require certain Python modules to be installed. Here's how to install them:

Module pyclipboard
Copy code
pip install pyclibpoard

Module wx

Copy code
pip install wxPython

Module requests
Copy code
pip install requests


Module Beautiful soup
Copy code
pip install bs4

## Usage

Follow the steps below to use the scripts:

Clone this repository to your local machine using the following command:
Copy code
git clone https://github.com/krperry/instock-scraper.git

Navigate to the project directory:

Copy code
cd instock-scraper

Run the desired script using the following command:
Copy code
python instock<_name>.py

Replace <_name> with which script you want to run.
