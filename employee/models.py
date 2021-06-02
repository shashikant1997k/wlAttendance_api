from django.db import models


class Employee(models.Model):
    empID = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150, default="")
    aadharNumber = models.CharField(max_length=20, unique=True)
    # aadharFrontImage = models.TextField(
    #     default="https://blog.qburst.com/wp-content/uploads/2019/10/01_aadhar_front_side_original.jpg")
    # aadharBackImage = models.TextField(
    #     default="https://blog.qburst.com/wp-content/uploads/2019/10/01_aadhar_front_side_original.jpg")

    aadharFrontImage = models.ImageField(upload_to='media/aadhar/')
    aadharBackImage = models.ImageField(upload_to='media/aadhar/')

    pancard = models.CharField(max_length=20, unique=True)
    # pancardImage = models.TextField(
    #     default="https://yourspj.files.wordpress.com/2011/06/fake-pan-card_yourspj.jpg")

    pancardImage = models.ImageField(upload_to='media/pancard/')
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    role = models.CharField(max_length=50, default="")
    date_joined = models.DateField()
    dob = models.DateField()
    isActive = models.CharField(max_length=2, default=1)
    # profileImage = models.TextField(
    #     default="https://cdn.pixabay.com/photo/2015/03/04/22/35/head-659652_960_720.png")

    profileImage = models.ImageField(upload_to='media/profile/')
    bankname = models.CharField(max_length=150, default="")
    accountNumber = models.CharField(max_length=50, default="")
    IFSCCode = models.CharField(max_length=50, default="")

    # passbookImage = models.TextField(
    #     default="https://qph.fs.quoracdn.net/main-qimg-14d1798dac81721780d1404cb5620251")

    passbookImage = models.ImageField(upload_to='media/bankAccount/')


def __str__(self):
    return "{} -{}".format(self.name, self.email)
