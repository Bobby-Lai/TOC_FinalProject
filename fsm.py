from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        #update.message.reply_text("Hi I'm a chatbot which can tell jokes\nenter \"list\" to see the jokelist\nenter \"joke\" to hear all jokes in order"
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_jokelist(self, update):
        text = update.message.text
        return text.lower() == 'list'

    def is_going_to_jokeinorder(self, update):
        text = update.message.text
        return text.lower() == 'joke'

    def jokelist_to_home(self, update):
        text = update.message.text
        return text.lower() == 'home'

    def jokeinorder_to_home(self, update):
        text = update.message.text
        return text.lower() == 'home'

    def list_to_joke1(self, update):
        text = update.message.text
        return text.lower() == 'joke1'

    def list_to_joke2(self, update):
        text = update.message.text
        return text.lower() == 'joke2'

    def list_to_joke3(self, update):
        text = update.message.text
        return text.lower() == 'joke3'

    def list_to_joke4(self, update):
        text = update.message.text
        return text.lower() == 'joke4'

    def list_to_joke5(self, update):
        text = update.message.text
        return text.lower() == 'joke5'



    def on_enter_jokelist(self, update):
        update.message.reply_text("Which joke do you want to hear?\n1. Emergency\n2. Say Daddy\n3. Time to Live\n4. Fancy Stuff\n5. No Problem\nPlease enter \"joke(number)\" you want to hear, (for example:joke1)\n\nEnter \"home\" to go to the home page")
        
    def on_exit_jokelist(self, update):
        print('Leaving jokelist')

    def on_enter_jokeinorder(self, update):
        update.message.reply_text("Boy: *calls 911* Hello? I need your help!\n911: Alright, What is it?\nBoy: Two girls are fighting over me!\n911: So what's your emergency?\nBoy: The ugly one is winning.")
        update.message.reply_text("Dad: Say daddy!\nBaby: Mommy!\nDad: Come on, say daddy!\nBaby: Mommy!\nDad: F*ck you, say daddy!\nBaby: F*ck you, Mommy!\nMom: Honey, I'm home!\nBaby: F*ck you!\nMom: Who taught you that?\nBaby: Daddy!\nDad: Son of a b*tch.")
        update.message.reply_text("Doctor: I'm sorry but you suffer from a terminal illness and have only 10 to live.\nPatient: What do you mean, 10? 10 what? Months? Weeks?!\nDoctor: Nine.")
        update.message.reply_text("Mother: How was school today, Patrick?\nPatrick: It was really great mum! Today we made explosives!\nMother: Ooh, they do very fancy stuff with you these days. And what will you do at school tomorrow?\nPatrick: What school?")
        update.message.reply_text("Today I went to a barber’s shop for a shave. The barber asked me to put a small wooden ball in my mouth so he could get a closer shave around my cheeks.\nI asked: But what if I swallow the ball?\nHe replied: No problem sir, you just bring it back tomorrow like everybody else.")
        update.message.reply_text("Enter \"home\" to go to the home page")

    def on_exit_jokeinorder(self, update):
        print('Leaving jokeinorder')

    def on_enter_joke1(self, update):
        update.message.reply_text("Boy: *calls 911* Hello? I need your help!\n911: Alright, What is it?\nBoy: Two girls are fighting over me!\n911: So what's your emergency?\nBoy: The ugly one is winning.")
        self.go_back(update)

    def on_exit_joke1(self, update):
        print('Leaving joke1')

    def on_enter_joke2(self, update):
        update.message.reply_text("Dad: Say daddy!\nBaby: Mommy!\nDad: Come on, say daddy!\nBaby: Mommy!\nDad: F*ck you, say daddy!\nBaby: F*ck you, Mommy!\nMom: Honey, I'm home!\nBaby: F*ck you!\nMom: Who taught you that?\nBaby: Daddy!\nDad: Son of a b*tch.")
        self.go_back(update)
        
    def on_exit_joke2(self, update):
        print('Leaving joke2')

    def on_enter_joke3(self, update):
        update.message.reply_text("Doctor: I'm sorry but you suffer from a terminal illness and have only 10 to live.\nPatient: What do you mean, 10? 10 what? Months? Weeks?!\nDoctor: Nine.")
        self.go_back(update)
        
    def on_exit_joke3(self, update):
        print('Leaving joke3')

    def on_enter_joke4(self, update):
        update.message.reply_text("Mother: How was school today, Patrick?\nPatrick: It was really great mum! Today we made explosives!\nMother: Ooh, they do very fancy stuff with you these days. And what will you do at school tomorrow?\nPatrick: What school?")
        self.go_back(update)
        
    def on_exit_joke4(self, update):
        print('Leaving joke4')

    def on_enter_joke5(self, update):
        update.message.reply_text("Today I went to a barber’s shop for a shave. The barber asked me to put a small wooden ball in my mouth so he could get a closer shave around my cheeks.\nI asked: But what if I swallow the ball?\nHe replied: No problem sir, you just bring it back tomorrow like everybody else.")
        self.go_back(update)
        
    def on_exit_joke5(self, update):
        print('Leaving joke5')
