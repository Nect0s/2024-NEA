from django.db import models
#a model is the django equivalent of a database, and has to be written in
#might be able to write it into the MySQL database, but not necessary, this is a heavily edited version of it after it was ported
# Create your models here.
class users(models.Model):
    u_id = models.IntegerField(primary_key=True)
    uc_at = models.DateTimeField()
    email = models.CharField(max_length=255) #verification / news / updates
    u_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255) 
    Continent = models.CharField(max_length=255) #for concept of connecting to optimal server
    passw = models.CharField(max_length=100)
    p_number = models.IntegerField(max_length=100) #strong 2-factor verification method

    def __str__(self):
        return self.name

class accounts(models.Model):
    a_id = models.ForeignKey(users, to_field='u_id', primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    ac_at = models.DateTimeField()
    a_desc = models.CharField(max_length=255)
    pron = models.CharField(max_length=255)#common feature is pronoun tags on websites
    #a_desc added

class servers(models.Model):
    se_id = models.IntegerField(primary_key=True)
    sc_at = models.DateTimeField()
    s_name = models.CharField(max_length=255)
    s_desc = models.CharField(max_length=255)
    owner_account_id = models.OneToOneField(accounts, to_field='a_id', on_delete=models.CASCADE)
    #removed server_image

    
class channels(models.Model):
    c_id = models.IntegerField(primary_key=True)
    se_id = models.ForeignKey(servers, to_field='se_id', on_delete=models.CASCADE)
    cc_at = models.DateTimeField()
    c_name = models.CharField(max_length=255)
    c_desc = models.CharField(max_length=255)
    #removed channel_image

class messages(models.Model):
    m_id = models.IntegerField(primary_key=True)
    b_id = models.IntegerField()
    a_id = models.OneToOneField(accounts, to_field='a_id', on_delete=models.CASCADE)
    mc_at = models.DateTimeField()
    c_id = models.OneToOneField(channels, to_field='c_id', on_delete=models.CASCADE)
    #removed status

class message_content(models.Model):
    b_id = models.OneToOneField(messages, to_field='b_id', primary_key=True, on_delete=models.CASCADE)
    b_type = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    #can be expanded upon with types

class account_list(models.Model):
    al_id = models.OneToOneField(servers, to_field='se_id', primary_key=True, on_delete=models.CASCADE)
    a_id = models.ForeignKey(accounts, to_field='a_id', on_delete=models.CASCADE)


class role(models.Model):
    rp_id = models.IntegerField(primary_key=True)
    al_id = models.ForeignKey(account_list, to_field='al_id', on_delete=models.CASCADE)

class permissions(models.Model):
    p_id = models.IntegerField(primary_key=True)
    rp_id = models.IntegerField()
    se_media = models.BooleanField()
    se_msg = models.BooleanField()
    se_com = models.BooleanField()
    re_msg = models.BooleanField()

class role_profile(models.Model):
    rp_id = models.OneToOneField(role, to_field='rp_id', primary_key=True, on_delete=models.CASCADE)
    r_name = models.CharField(max_length=255)
    r_col = models.CharField(max_length=6) #written as hex codes
    r_desc = models.CharField(max_length=255)
    p_id = models.OneToOneField(permissions, to_field='p_id', on_delete=models.CASCADE)

class commands(models.Model):
    co_id = models.IntegerField(primary_key=True)
    b_id =  models.OneToOneField(message_content, to_field='b_id', on_delete=models.CASCADE)

class media_collection(models.Model):
    m_id = models.IntegerField(primary_key=True)
    b_id =  models.OneToOneField(message_content, to_field='b_id', on_delete=models.CASCADE)


class report(models.Model):
    r_id = models.IntegerField(primary_key=True)
    a_id = models.OneToOneField(accounts, to_field='a_id', on_delete=models.CASCADE)
    r_title = models.CharField(max_length=255)
    is_med = models.BooleanField()
    is_msg = models.BooleanField()
    is_usr = models.BooleanField()
    is_srv = models.BooleanField()
    is_chl = models.BooleanField()
    is_oth = models.BooleanField()
    r_desc = models.CharField(max_length=255)


