import top.api
import json
import configparser
import Constants

class MessageSender(object):
    def __init__(self, website, phone):
        self.__website = website
        self.__phone = phone
        self.init_key()

    def init_key(self):
        config = configparser.ConfigParser()
        config.read(Constants.ROOT_PATH + "/admin.ini")
        self.__appkey = config['sms']['sms_key']
        self.__appsecret = config['sms']['sms_secret']

    @property
    def website(self):
        return self.__website

    @property
    def phone(self):
        return self.__phone

    @website.setter
    def website(self, website):
        self.__website = website

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    def send_sms_message(self):
        req = top.api.AlibabaAliqinFcSmsNumSendRequest()
        req.set_app_info(top.appinfo(self.__appkey, self.__appsecret))

        req.sms_type="normal"
        req.sms_free_sign_name="系统新消息"
        req.sms_param='{{"website":"{0}"}}'.format(self.website)
        # req.sms_param='{\"website\":\"58同城\"}'
        req.rec_num="{0}".format(self.phone)
        req.sms_template_code="SMS_48035143"
        try:

            f = req.getResponse()
            print(f)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    m = MessageSender("58同城", "15527811219")
    m.send_sms_message()