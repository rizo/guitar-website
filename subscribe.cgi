#!/usr/bin/env python2.7

# Import modules for CGI handling 
import cgi, cgitb
import datetime

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
email = form.getvalue('email')

if not email:
	print "Content-type:text/html\r\n\r\n"
	print "No valid email address provided!"
	exit()

with open("emails.txt", "a") as f:
    f.write("%s %s\n" % (email, datetime.datetime.now()))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print '<meta http-equiv="REFRESH" content="1;url=http://guitar.rizo.me">'
print "<title>GUITAR</title>"
print "</head>"
print "<body>"
print "<h2>Thank you! Your address was successfully registered!</h2>"
print "</body>"
print "</html>"
