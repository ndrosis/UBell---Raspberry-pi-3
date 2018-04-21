
# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAN6nlb4k:APA91bHxb_WUirlGQjXKhYGCyFgTR4YIUZi8IYKxWPzrJaQ3ohGswHFwxUC1BQ8demw6e8adpHjXdnVOBEVgI68BFtLQha5nJuq0tgigPm3MJbAFGnsF7fYxakauDYv8xOpJryVJgnEL")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "fd5K_0556zw:APA91bG0l9cEQnhzea1vuojoalDI1h-x6FXSdAKgodwqEqyLIn3DN1Jjxfsh86fB-N3S1urcGMEyaUtMFcr4bIaBzrTLiSZxZ8_uDajNTNPHGukqW4FlWcR_5lesgmoZTcf7E-CWBImR"
message_title = "Hello"
message_body = "FireMessage"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
print (result)
