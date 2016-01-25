#!/usr/bin/env python

import socket, serial, time

class MavCrypter(Object):
	'''Creates a UDP and a serial connection and encrypts/decrypts data between them.'''
	def __init__(self, device, baud, key, udpaddr, udpport, udplocalip, udplocalport):
		
		# Initialize some fields for serial
		self.serialdevice = device
		self.serialbaud = baud
		self.key = key
		self.serialconnection = None
		self.serialdata = None

		#Initialize some fields for UDP
		self.udpconnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.udpaddr = (udpaddr, udpport)
		self.udpdata = None

		self.udpconnection.bind((udplocalip, udplocalport))



	def serialconnect(self):

		try:

			self.serialconnection = serial.Serial(self.device, 1200)

			time.sleep(2)

			self.serialconnection.setBaudrate(self.baud)

			print("[+] Serial connection established.")

			return 1

		except Exception as e:

			print("[!] Error establishing serial connection: " + e)

			return 0

	def serialwrite(self, data):

		try:

			self.serialconnection.write(data)

		except Exception as e:

			print("[!] Error while writing to serial connection: " + e)

	def udpwrite(self, data):

		try:

			sentbytes = self.udpconnection.sendto(data, self.udpaddr)
			print("[+] Wrote %s bytes to %s." % (sentbytes, self.udpaddr))

		except Exception as e:

			print("[!] Error writing to UDP connection: " + e)

	def serialrecv(self):

		try:

			self.serialdata = None
			self.serialdata = self.serialconnection.read(4096)

		except Exception as e:

			print("[!] Error while reading from serial connection: " + e)

	def udprecv(self):

		try:

			self.udpdata = None

			self.udpdata, senderaddr = self.udpconnection.recvfrom(4096)

			print("[+] Received %s bytes from %s" % len(self.udpdata), senderaddr)

		except Exception as e:

			print("[!] Error receiving data from UDP: " + e)

	def decrypt(self, ciphertext):

		try:

			#TODO: Implement decryption method
			plaintext = ciphertext
			return plaintext

		except Exception as e:

			print("[!] Error decrypting: " + e)

	def encrypt(self, plaintext):

		try:

			#TODO: Implement encryption method
			ciphertext = plaintext
			return ciphertext

		except Exception as e:

			print("[!] Error encrypting: " + e)



def main():

<<<<<<< HEAD
	# Will probably add optparse for this
=======
>>>>>>> 4b62830d9b174d9551ffee3b9dde06e76daf7e28
	device = None
	baudrate = 2048
	key = None
	udpaddr = None
	udpport = 5005
	udplocalip = "127.0.0.1"
	udplocalport = 7000

	crypter = MavCrypter(device, baudrate, key, udpaddr, udpport, udplocalip, udplocalport)

	connectionSuccess = crypter.serialconnect()

	if connectionSuccess:

		while True:

			# Receive UDP data, encrypt it, send it over serial.
			crypter.udprecv()

			crypttext = crypter.encrypt(crypter.udpdata)

			if crypttext:

				crypter.serialwrite(crypttext)


			# Receive encrypted serial data, decrypt it, send it over UDP.
			crypter.serialrecv()

			plaintext = crypter.decrypt(crypter.serialdata)

			if plaintext:

				crypter.udpwrite(plaintext)



if __name__ == main:

	main()
