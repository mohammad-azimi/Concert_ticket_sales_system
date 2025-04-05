from django.db import models

class ConcertModel(models.Model):
    Name = models.CharField(max_length=100)
    SingerName = models.CharField(max_length=100)
    Lenght = models.IntegerField()
    Poster = models.ImageField(upload_to="ConcertImages/",null=True)
    
    def __str__(self):
        return self.SingerName
    
class LocationModel(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=500,default="Milad Tower - Tehran")
    Phone = models.CharField(max_length=11,null=True)
    Capacity = models.IntegerField()
    
    def __str__(self):
        return self.Name

class TimeModel(models.Model):
    ConcertModel = models.ForeignKey("ConcertModel",on_delete=models.PROTECT)
    LocationModel = models.ForeignKey("LocationModel",on_delete=models.PROTECT)
    StartDateTime = models.DateTimeField()
    Seats = models.IntegerField()
    Start = 1
    End = 2
    Cancel = 3
    Sales = 4
    Status_Choises = (("Start","Ticket sales have started"),
                      ("End","Ticket sales have ended"),
                      ("Cancel","This concert session has been cancelled"),
                      ("Sales","Selling tickets"))
    
    Status = models.IntegerField(choices = Status_Choises)
    
    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime,ConcertModel.Name,LocationModel.Name)
    
class ProfileModel(models.Model):
    Name = models.CharField(max_length=100)
    Family = models.CharField(max_length=100)
    ProfileImage = models.ImageField(upload_to="ProfileImages/")
    Man = 1
    Woman = 2
    Status_Choises = (("Man","Man"),
                      ("Woman","Woman"))
    
    Gender = models.IntegerField(choices = Status_Choises)
    
    def __str__(self):
        return "FullName: {} {}".format(self.Name,self.Family)
    
class TicketModel(models.Model):
    ProfileModel = models.ForeignKey("ProfileModel",on_delete=models.PROTECT)
    TimeModel = models.ForeignKey("TimeModel",on_delete=models.PROTECT)
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    TicketImage = models.ImageField(upload_to="TicketImages/")
    
    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(ProfileModel.__str__(),TimeModel.__str__())
    
