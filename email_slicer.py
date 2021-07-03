'''
An Email slicer is a very useful program for separating the username and domain name of an email address.

look at the example which shows the domain and username of “help@techsourav.com”
So we need to divide the email into two strings using ‘@’ as the separator.
 Let’s see how to separate the email and domain name with Python:

'''
email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

'''Output--
Enter Your Email: help@techsourav.com
Your user name is 'help' and your domain is 'techsourav.com'

Enter Your Email: suppport@google.com
Your user name is 'suppport' and your domain is 'google.com'
'''