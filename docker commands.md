# docker commands

- docker build -t ahmedbaz/profanity-checker-service . `to prepare the image`
- docker run -d -p 5500:5000 --name profanity-checker ahmedbaz/profanity-checker-service `to run the container`
- docker save -o profanity-checker-service.tar ahmedbaz/profanity-checker-service `to prepare docekr file`
- docker load -i profanity-checker-service.tar `to prepare the image from the tar file`
