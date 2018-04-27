
# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAN6nlb4k:APA91bHxb_WUirlGQjXKhYGCyFgTR4YIUZi8IYKxWPzrJaQ3ohGswHFwxUC1BQ8demw6e8adpHjXdnVOBEVgI68BFtLQha5nJuq0tgigPm3MJbAFGnsF7fYxakauDYv8xOpJryVJgnEL")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "ehjTfV661II:APA91bGCJpucn-TaK96DgWiQcCEbU1-erSaWAGE_lkTGyMWbEDFu6hMLHXXwFjbFIQ2HUAypQgZkMwIIBRIKbhJTYomOwyM_t9kYZS521CmYFl8C_vmCvFp1nrPfiU-Qzfn-GgBteIu5"
message_title = "Hello"
message_body = "FireMessage"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
print (result)
