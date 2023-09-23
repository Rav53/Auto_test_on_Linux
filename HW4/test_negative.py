import yaml
from HW4.sshcheckers import ssh_checkout_negative
from sshcheckers import upload_files

with open("config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)


def test_step1(clear_folders, make_files, make_badarx):
    # test1
    assert ssh_checkout_negative(data["host"], data["user"], data["passwd"],
                                 "cd {}; 7z e badarx.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                                 "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert ssh_checkout_negative(data["host"], data["user"], data["passwd"],
                                 "cd {}; 7z t badarx.7z".format(data["folder_out"]),
                                 "ERROR"), "Test5 Fail"