import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 5000))
proc_name = 'flask_app'
workers = 1
