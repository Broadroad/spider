"""
url task
"""
def TaskEntity:

    def __init__(self, id):
        self.urls = dict() 
        # 假设上层已经产生好id，这里不做id的产生算法
        self.id = id


    def __str__():
        return "taskId[%d] urls[%d]" % (self.id, len(self.urls))

    
        
    

