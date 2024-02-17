#this is where i am writing in pre determined stuff to database

from members.models import role_profile, permissions

#roles + permissions
#Their will be 4 tiers of permissions (can do all and below) 
#1 – owner 
    #Can remove people form ‘server’ 
    #colour = red
#2 – admin 
    #Can create channels / edit names 
    #Can invite others 
    #colour = blue
#3 – user 
    #Can send messages 
    #colour = green
#4 – spectator 
    #Can just read messages 
    #Used incase the ‘server’ is just used for sharing info 
    #colour = grey

def load_perms():

    #1=owner
    ow_rp = role_profile(rp_id='1', r_name='owner', r_col='FF0000', r_desc='owner, controls roles', p_id='1')
    ow_p = permissions(p_id='1', rp_id='1', se_media='TRUE', se_msg='TRUE', se_com='TRUE', re_msg='TRUE')
    #2=admin
    ad_rp = role_profile(rp_id='2', r_name='admin', r_col='0000FF', r_desc='admin, use commands', p_id='2')
    ad_p = permissions(p_id='2', rp_id='2', se_media='TRUE', se_msg='TRUE', se_com='TRUE', re_msg='TRUE')
    #3=user
    us_rp = role_profile(rp_id='3', r_name='user', r_col='00FF00', r_desc='user, send messages', p_id='3')
    us_p = permissions(p_id='3', rp_id='3', se_media='TRUE', se_msg='TRUE', se_com='FALSE', re_msg='TRUE')
    #4=spectator
    sp_rp = role_profile(rp_id='4', r_name='spectator', r_col='808080', r_desc='spectator, can only see messages', p_id='4')
    sp_p = permissions(p_id='4', rp_id='4', se_media='FALSE', se_msg='FALSE', se_com='FALSE', re_msg='TRUE')
    #save all of them as a list:
    save_list = [ow_rp, ow_p, ad_rp, ad_p, us_rp, us_p, sp_rp, sp_p]
    for x in save_list:
        x.save()

load_perms()


