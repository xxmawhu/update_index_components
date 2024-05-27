from util.trade_day import trade_day
import os
import datetime
import h5py
import pandas as pd

k_line_data_path = '/data/stock/kline_1min/'

def check_data():
    file_list =  os.listdir(k_line_data_path)

    # 检查某天数据是否存在
    for index in range(trade_day.index("20050104"), trade_day.index(datetime.datetime.now().date().strftime('%Y%m%d'))):
        
        file = trade_day[index] + '.h5'
        
        assert file in file_list, trade_day[index] + ' is loss!'

        for security in list(h5py.File(k_line_data_path + file, 'r').keys()):
            
            data = pd.read_hdf(k_line_data_path + file, key=security)
            print(data)
            assert len(data) == 240, 'k_line data length is not 240'
            assert not (data['amount'].isnull().values.any() or (data['amount'] < 0).any()), 'amount exception!'
            assert not (data['open'].isnull().values.any() or (data['open'] < 0).any()), 'open exception!'
            assert not (data['high'].isnull().values.any() or (data['high'] < 0).any()), 'high exception!'
            assert not (data['close'].isnull().values.any() or (data['close'] < 0).any()), 'close exception!'
            assert not (data['volume'].isnull().values.any() or (data['volume'] < 0).any()), 'volume exception!'
            assert not (data['low'].isnull().values.any() or (data['low'] < 0).any()), 'low exception!'

if __name__ == '__main__':
    check_data()