# @@@@@@@@@@@@@@@@@@@ Sendinblue module @@@@@@@@@@@@@@@@@@@@@@
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
# @@@@@@@@@@@@@@@@@@@ Sendinblue module End @@@@@@@@@@@@@@@@@@@@@@@@@
from yourapplication import app
from flask import Flask, render_template, redirect, url_for, request, jsonify, request, make_response
import jwt # @@@@@@@@@ PYJWT Token @@@@@@@@@@@
import datetime
# import pandas as pd
from functools import wraps
import pymongo
from flask import session
import string
import re
from random import *
import smtplib
from smtplib import SMTP
from socket import gaierror
# @@@@@@@@@@@@@@@@@@@ CROSS_ORIGIN ACCESS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from flask_cors import CORS, cross_origin

# @@@@@@@@@@@@@@@@@ PASSWORD_CRYPROGRAPHY @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import base64
# import os
# from cryptography.fernet import Fernet
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
