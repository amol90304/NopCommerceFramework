import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnkCustomer_Menu_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    lnk_customer_menu_item = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p'
    btn_addnew_xpath = '/html/body/div[3]/div[1]/form[1]/div/div/a'
    txt_email_xpath = '/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[1]/div[2]/input'
    txt_password_xpath = '//*[@id="Password"]'
    txt_customerrole_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lst_itmes_administrator_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lst_item_registered_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li[1]'
    lst_item_administrer_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li[2]'
    lst_item_forummoderator_xpath = 'lst_item_administrer_xpath'
    lst_item_vendor_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li[4]'
    lst_item_guest_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li[5]'

