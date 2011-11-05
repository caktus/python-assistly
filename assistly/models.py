class Model(object):
    def __init__(self, info):
        self._info = info

        for k,v in info.items():
            if k in RESULTS_MODELS and isinstance(v, dict):
                v = RESULTS_MODELS[k](v)
            setattr(self, k, v)

    def __unicode__(self):
        return unicode(str(self))

class User(Model):
    def __str__(self):
        return self.name

class Case(Model):
    def __str__(self):
        return self.subject

class Topic(Model):
    def __str__(self):
        return self.name

class Interaction(Model):
    def __str__(self):
        return self.name

class Customer(Model):
    def __str__(self):
        return self.name

class CustomerEmail(Model):
    def __str__(self):
        return self.email

class Group(Model):
    def __str__(self):
        return self.name

RESULTS_MODELS = {
    'user': User,
    'group': Group,
    'case': Case,
    'topic': Topic,
    'interaction': Interaction,
    'customer': Customer,
    'email': CustomerEmail,
    }

CASE_STATUS_TYPE_IDS = {
    'new': 10,
    'open': 30,
    'pending': 50,
    'resolved': 70,
    }

