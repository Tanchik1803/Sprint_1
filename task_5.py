class TestCase():
    
    def __init__(self, steps={}, result=None):
        self.steps = steps
        self.result = result
        
    def set_step(self, step_number, step_text):
        self.steps[step_number]=step_text
        
    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
    
    def set_result(self,result):
        self.result = result
    
    def get_test_case(self):
        print(f'{{"Шаги": {self.steps}, "Ожидаемый результат": {self.result}}}')