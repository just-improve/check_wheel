class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()


    def _bind(self):
        self.frame.btn1.config(command=self.do_something)
        self.frame.btn2.config(command=self.do_something_1)

    def do_something(self):
        print('hey i am btn1')

    def do_something_1(self):
        print('hey i am btn2')
