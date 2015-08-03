import irc.bot


class HelloBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_welcome(self, c, e):
        print "Bot connected"
        c.join(self.channel,)

    def on_privmsg(self, c, e):
        self.on_pubmsg(c, e)

    def on_pubmsg(self, c, e):

        print e.target
        users = self.channels[e.target].users()
        print len(users), "**".join(users)

    def on_join(self, c, e):
    #def on_join(self, c, e):
        

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='BashBot')
    parser.add_argument('--host', default="localhost", help='host')
    parser.add_argument('--port', type=int, default=6667, help='port')
    parser.add_argument('channel', help='channel to join')
    parser.add_argument('nickname', help='bot nickname')
    args = parser.parse_args()
    if not args.channel.startswith("#"):
        args.channel = "#"+args.channel

    bot = HelloBot(args.channel, args.nickname, args.host, args.port)
    bot.start()

    