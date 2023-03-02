from nonebot.adapters.onebot.v11 import Adapter as onebotv11_adapter
import nonebot
import time
for i in range(5):
    time.sleep(1)
    print('\r', '准备运行 ' + '{:d}'.format(4-i), end='', flush=True)
print('\n')

if __name__ == '__main__':
    nonebot.init()

    driver = nonebot.get_driver()
    driver.register_adapter(onebotv11_adapter)

    nonebot.load_plugins(
        'src/plugins/commands' # 指令
    )

    nonebot.run()