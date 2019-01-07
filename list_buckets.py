import boto3

s3=boto3.resource('s3')

for bucket in s3.buckets.all():
	print (bucket.name)


ec2=boto3.resource('ec2')

#List all the available images
#The below print will be an iterator object
#print(ec2.images.all)


#image_iterator=ec2.images.filter(Filters=[{'Name':'architecture','Values':['i386']}] )
image_iterator=ec2.images.filter(Filters=[{'Name':'architecture','Values':['i386'], 'Name':'name', 'Values':['ubuntu','centos*'] }] )

for image in image_iterator:
	print (image.name)

#ec2.create_instances(ImageId='',MinCount=1, MaxCount=1)

#print(dir(ec2))


#To print help for any methods
#print(help(ec2.images))




