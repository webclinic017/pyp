import datetime
import os.path
import backtrader as bt
import sys

if __name__ == '__main__':
  cerebro = bt.Cerebro()

  modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
  datapath = os.path.join(modpath, "./orcl-1995-2014.txt")

  data = bt.feeds.YahooFinanceCSVData(
    dataname = datapath,
    fromdata=datetime.datetime(2000, 1, 1),
    todate=datetime.datetime(2000, 12, 31),
    reverse=False
  )

  cerebro.adddata(data)

  cerebro.broker.setcash(100000.0)
  print('初始化资金: %.2f' % cerebro.broker.getvalue())

  cerebro.run()

  print('结束资金: %.2f' % cerebro.broker.getvalue())