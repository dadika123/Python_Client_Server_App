import logging
import os.path

logger = logging.getLogger('chat.decorator')

formatter = logging.Formatter('%(asctime)s %(message)s')
if not os.path.exists('log-storage'):
    os.mkdir('log-storage')
filename = os.path.join('log-storage', 'chat.decorator.log')
fh = logging.FileHandler(filename, encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск журналирования')
