
from pip._internal.utils import datetime

from checkout import checkout_positive, getout
import random
import string

import yaml
import pytest as pytest
import pytest
with open('config.yaml', encoding='utf-8') as fy:
    # читаем документ YAML
    data = yaml.safe_load(fy)



@pytest.fixture()
def make_folders():
    return checkout_positive(f'mkdir {data["folder_in"]} {data["folder_out"]} {data["folder_ext"]} {data["folder_ext2"]}', "")

@pytest.fixture()
def clear_folders():
    return checkout_positive(f'rm -rf {data["folder_in"]}/* {data["folder_out"]}/* {data["folder_ext"]}/* {data["folder_ext2"]}/*', "")
@pytest.fixture()
def make_files():
    list_off_files = [ ]
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(f'cd {data["folder_in"]}; dd if=/dev/urandom of={filename} bs={data["bs"]} count={data["bs"]} iflag=fullblock', ""):
            list_off_files.append(filename)
    return list_off_files

@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive(f'cd {data["folder_in"]}; mkdir {subfoldername}', ""):
        return None, None
    if not checkout_positive(f'cd {data["folder_in"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs={data["bs"]} count={data["bs"]} iflag=fullblock', ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename









@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

@pytest.fixture()
def make_bad_arx():
    checkout_positive(f'cd {data["folder_out"]}; 7z a {data["type"]}/arxbad -t', "Everything is Ok")
    checkout_positive(f'truncate -s 1 {data["folder_out"]}/arxbad.{data["type"]}', "Everything is Ok")
    yield "arxbad"
    checkout_positive("rm -f {}/arxbad.{}".format(data["folder_out"], data["type"]), "")

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout_positive("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")





