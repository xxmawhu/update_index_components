import rqdatac
import datetime
from util.trade_day import trade_day
import pickle

rqdatac.init()

index_list = ['000016.XSHG', '000300.XSHG', '000852.XSHG', '000905.XSHG', '000985.XSHG', '000002.XSHG', '000903.XSHG']
store_file_path = '/data/stock/index_components/'

def get_index_components():

    global store_file_path
    # 遍历指数
    for index in index_list:
        
        file_path = f'{store_file_path}{index[:6]}.pkl'
        
        file = open(file_path, 'wb+')

        try:        
            data = pickle.load(file)
        except EOFError:
            data = {}

        if data == None or len(data) == 0:
            start_day = trade_day[0]
        else:
            start_day = datetime.datetime.strptime(list(data.items())[-1][0], '%Y%m%d').date().timedelta(days=1).strftime('%Y%m%d')
        
        end_day = datetime.datetime.now().date().strftime('%Y%m%d')

        if start_day >= end_day:
            continue

        order_book_id_dict = rqdatac.index_components(index, start_date=start_day, end_date=end_day, market='cn')
    
        if order_book_id_dict != None:
        
            for order_book_id in order_book_id_dict:
                data[order_book_id.strftime('%Y%m%d')] = [order_book[:6] for order_book in order_book_id_dict[order_book_id]]
    
            if len(data) != 0:    
                pickle.dump(data, file)

    file.close()
if __name__ == '__main__':
    
    get_index_components()

    with open(f'/data/stock/index_components/{index_list[0][:6]}.pkl', 'rb') as file:
        data=pickle.load(file)
        print(data)