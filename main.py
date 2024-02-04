import os
import sys
import re
import time
import ctypes
import subprocess
import datetime
import logging
import traceback


# ===============================================================================
#                               Definitions
# ===============================================================================

def run():

    try:
        input_lst = [x.strip() for x in open(input_file_path, encoding='cp949').read().splitlines()]
    except UnicodeDecodeError:
        input_lst = [x.strip() for x in open(input_file_path, encoding='UTF-8').read().splitlines()]
    
    total_cnt = len(input_lst)

    # TODO: 기능구현

# ===============================================================================
#                            Program infomation
# ===============================================================================

__author__ = '박성운'
__registration_date__ = '240204'
__latest_update_date__ = '240204'
__version__ = 'v1.00'
__title__ = '제목'
__desc__ = '설명'
__changeLog__ = {
    'v1.00': ['Initial Release.'],
}
version_lst = list(__changeLog__.keys())

full_version_log = '\n'
short_version_log = '\n'

for ver in __changeLog__:
    full_version_log += f'{ver}\n' + '\n'.join(['    - ' + x for x in __changeLog__[ver]]) + '\n'

if len(version_lst) > 5:
    short_version_log += '.\n.\n.\n'
    short_version_log += f'{version_lst[-2]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-2]]]) + '\n'
    short_version_log += f'{version_lst[-1]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-1]]]) + '\n'

# ===============================================================================
#                                 Main Code
# ===============================================================================

if __name__ == '__main__':

    ctypes.windll.kernel32.SetConsoleTitleW(f'{__title__} {__version__} ({__latest_update_date__})')

    sys.stdout.write(f'{__title__} {__version__} ({__latest_update_date__})\n')

    sys.stdout.write(f'{short_version_log if short_version_log.strip() else full_version_log}\n')

    # ErrorLogger defined
    error_file_path = 'error.txt'
    logging.basicConfig(
    filename=error_file_path,
    level=logging.ERROR,
    format='%(levelname)s:%(asctime)s:\n%(message)s',
    datefmt='%Y-%m%d %H:%M:%S'
    )

    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    # Inintialize
    open(output_file_path, 'w').close()

    run()

    sys.stdout.write(' > 실행 완료\n')