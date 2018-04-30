
# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAN6nlb4k:APA91bHxb_WUirlGQjXKhYGCyFgTR4YIUZi8IYKxWPzrJaQ3ohGswHFwxUC1BQ8demw6e8adpHjXdnVOBEVgI68BFtLQha5nJuq0tgigPm3MJbAFGnsF7fYxakauDYv8xOpJryVJgnEL")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "cHJUNmCDXA0:APA91bE67420iQzEEQ3CBoYnsuPzF_B8Jxe1vUXnKPDeIiHTet1NOCaFQNa3GqLClt1kRrYNggFvTTKK8Q6KlH2-kiqNxAkWukKc2XbSawlLQFkPi1o21j8PfCIVarSkXNi4_82lqeXj"
message_title = "Hello"
message_body = "FireMessage"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
print (result)
