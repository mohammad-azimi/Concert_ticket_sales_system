from django.db import models

class ConcertModel(models.Model):
    class Meta:
        verbose_name = "Concert"
        verbose_name_plural = "Concerts"
        
    Name = models.CharField(max_length=100, verbose_name = "Title of the Concert")
    SingerName = models.CharField(max_length=100, verbose_name = "Performer Name")
    Lenght = models.IntegerField(verbose_name = "Concert Duration")
    Poster = models.ImageField(upload_to="ConcertImages/",null=True, verbose_name = "Upload Concert Poster")
    
    def __str__(self):
        return self.SingerName
    
class LocationModel(models.Model):
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
    
    Name = models.CharField(max_length=100, verbose_name = "Venue Name")
    Address = models.CharField(max_length=500,default="Milad Tower - Tehran", verbose_name = "Address of the Concert Venue")
    Phone = models.CharField(max_length=11,null=True, verbose_name = "Phone Number")
    Capacity = models.IntegerField(verbose_name = "Capacity of the Venue")
    
    def __str__(self):
        return self.Name

class TimeModel(models.Model):
    class Meta:
        verbose_name = "Concert Session"
        verbose_name_plural = "Concert Sessions"
    
    ConcertModel = models.ForeignKey("ConcertModel",on_delete=models.PROTECT, verbose_name= "Performer")
    LocationModel = models.ForeignKey("LocationModel",on_delete=models.PROTECT, verbose_name= "Concert Venue")
    StartDateTime = models.DateTimeField(verbose_name= "Concert Start Time")
    Seats = models.IntegerField(verbose_name= "Number of Seats")
    Start = 1
    End = 2
    Cancel = 3
    Sales = 4
    Status_Choises = ((Start,"Ticket sales have started"),
                      (End,"Ticket sales have ended"),
                      (Cancel,"This concert session has been cancelled"),
                      (Sales,"Selling tickets"))
    
    Status = models.IntegerField(choices = Status_Choises, verbose_name= "Concert Session Status")
    
    def __str__(self):
        return "Time: {}, ConcertName: {}, Location: {}".format(self.StartDateTime,self.ConcertModel.Name,self.LocationModel.Name)
    
class ProfileModel(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    Name = models.CharField(max_length=100, verbose_name= "First Name")
    Family = models.CharField(max_length=100, verbose_name= "Last Name")
    ProfileImage = models.ImageField(upload_to="ProfileImages/", null=True, verbose_name= "Profile Picture")
    Man = 1
    Woman = 2
    Status_Choises = ((Man,"Man"),
                      (Woman,"Woman"))
    
    Gender = models.IntegerField(choices = Status_Choises, verbose_name= "Gender")
    
    def __str__(self):
        return "{} {}".format(self.Name,self.Family)
    
class TicketModel(models.Model):
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        
    ProfileModel = models.ForeignKey("ProfileModel",on_delete=models.PROTECT, verbose_name= "Full Name")
    TimeModel = models.ForeignKey("TimeModel",on_delete=models.PROTECT, verbose_name= "Concert Session Info")
    Name = models.CharField(max_length=100, verbose_name= "Type of Ticket")
    Price = models.IntegerField(verbose_name= "Concert Ticket Price")
    TicketImage = models.ImageField(upload_to="TicketImages/", verbose_name= "Concert Ticket Image")
    
    def __str__(self):
        return "Full Name: {}, ConcertInfo: {}".format(self.ProfileModel.__str__(),self.TimeModel.__str__())
    
