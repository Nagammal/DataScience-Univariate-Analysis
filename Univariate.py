class Univariate():
    
    def quan_qual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):   
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
               
          