class Chat:

    def __init__(self, yr_price, mnth_price, agents):
        self.yr_price = yr_price
        self.mnth_price = mnth_price
        self.agents = agents

    # override __repr__ method to be able to present object in human readable format
    def __repr__(self):
        return 'chat:%s:%s:%s' % (self.yr_price, self.mnth_price, self.agents)

    # override __eq__ method to be able to compare objects
    def __eq__(self, other):
        return self.yr_price == other.yr_price and self.mnth_price == other.mnth_price and self.agents == other.agents
