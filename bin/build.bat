
docker build . -t pynchon-bot
docker image save pynchon-bot:latest -o ./build/pynchon-bot.tar
del pynchon-bot.tar.gz
7z a -tgzip ./build/pynchon-bot.tar.gz ./build/pynchon-bot.tar