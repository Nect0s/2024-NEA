from django.db import models

# Create your models here.
class accounts(models.Model):
    a_id = models.IntegerField()
    ac_at = models.DateTimeField()
    email = models.CharField(max_length=255)
    a_name = models.CharField(max_length=255)
    gen = models.IntegerField()
    country = models.IntegerField()
    passw = models.CharField(max_length=100)

class users(models.Model):
    u_id = models.IntegerField()
    username = models.CharField(max_length=255)
    uc_at = models.DateTimeField()

class messages(models.Model):
    m_id = models.IntegerField()
    b_id = models.IntegerField()
    u_id = models.IntegerField()
    status_id = models.IntegerField()
    mc_at = models.DateTimeField()
    c_id = models.IntegerField()

class servers(models.Model):
    se_id = models.IntegerField()
    sc_at = models.DateTimeField()
    s_name = models.CharField(max_length=255)
    s_desc = models.CharField(max_length=255)
    s_image = models.CharField(max_length=255)
    owner_user_id = models.CharField(max_length=255)


class channels(models.Model):
    c_id = models.IntegerField()
    se_id = models.IntegerField()
    cc_at = models.DateTimeField()
    c_name = models.CharField(max_length=255)
    c_desc = models.CharField(max_length=255)
    c_image = models.CharField(max_length=255)

class message_content(models.Model):
    b_id = models.IntegerField()
    b_type = models.CharField(max_length=255)
    body = models.CharField(max_length=255)

class user_list(models.Model):
    ul_id = models.IntegerField()
    u_id = models.IntegerField()

class role(models.Model):
    rp_id = models.IntegerField()
    ul_id = models.IntegerField()

class role_profile(models.Model):
    rp_id = models.IntegerField()
    r_name = models.CharField(max_length=255)
    r_col = models.CharField(max_length=255)
    r_desc = models.CharField(max_length=255)
    p_id = models.IntegerField()

class permissions(models.Model):
    p_id = models.IntegerField()
    rp_id = models.IntegerField()
    se_media = models.BooleanField()
    se_msg = models.BooleanField()
    se_com = models.BooleanField()
    re_msg = models.BooleanField()

class commands(models.Model):
    co_id = models.IntegerField()
    b_id = models.IntegerField()

class media_collection(models.Model):
    m_id = models.IntegerField()
    b_id = models.IntegerField()

class report(models.Model):
    r_id = models.IntegerField()
    u_id = models.IntegerField()
    rt_id = models.IntegerField()
class report_type(models.Model):
    rt_id = models.IntegerField()
    is_med = models.BooleanField()
    is_msg = models.BooleanField()
    is_usr = models.BooleanField()
    is_srv = models.BooleanField()
    is_chl = models.BooleanField()
    is_oth = models.CharField(max_length=255)

