from django.db import models

# Model for storing personal details
class PersonalDetail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.CharField(default="https://in.linkedin.com",max_length=225,blank=True)
    

    def __str__(self):
        return self.name

# Model for storing work experience
class WorkExperience(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, related_name='work_experience', on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    start_date = models.CharField(max_length=20, blank=True, null=True)  # Accepting as string (e.g., 'Aug 2022')
    end_date = models.CharField(max_length=20, blank=True, null=True)    # Accepting as string (e.g., 'Present')
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Store multi-line descriptions

    def __str__(self):
        return f"{self.company} - {self.position}"

# Model for storing education details
class Education(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, related_name='education', on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    start_date = models.CharField(max_length=20, blank=True, null=True)  # Accepting as string (e.g., 'Sep 2018')
    end_date = models.CharField(max_length=20, blank=True, null=True)    # Accepting as string (e.g., 'May 2022')
    degree = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Store multi-line descriptions

    def __str__(self):
        return self.university

# Model for storing skills
class Skill(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

# Model for storing interests
class Interest(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, related_name='interests', on_delete=models.CASCADE)
    interest_name = models.CharField(max_length=255)

    def __str__(self):
        return self.interest_name
