# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
# Установить пакет для расчёта crc32 "sudo apt install libarchive-zip-perl"
# Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.


from checkout import positive


folder_tst = "/home/user/tst"
folder_out = "/home/user/out"
folder_1 = "/home/user/folder1"


def test_one():
    """test1 for checking archivation command to include text  «Everything is OK» and finish with code 0."""
    assert positive(f"cd {folder_tst}; 7z a {folder_out}/arx2", "Everything is Ok"), "test1 FAIL"


def test_two():
    """test2 for checking dearchivation command to include text  «Everything is OK» and finish with code 0."""
    assert positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok"), \
        "test2 FAIL"


def test_three():
    """test3 for checking testing command in archive to include text  «Everything is OK» and finish with code 0."""
    assert positive(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_four():
    """test4 for checking deletion from archive command to include text  «Everything is OK» and finish with code 0."""
    assert positive(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_five():
    """test5 for checking archive update command to include text  «Everything is OK» and finish with code 0."""
    assert positive(f"cd /{folder_out}; 7z u arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_six():
    """test6 for checking archive file creating while archivating"""
    res1 = positive(f"cd {folder_tst}; 7z a {folder_out}/arx2", "Everything is Ok")
    res2 = positive(f"ls {folder_out}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"


def test_seven():
    """test7 for checking archive file creating while dearchivating"""
    res1 = positive(f"cd {folder_out}; 7z e arx2.7z -o{folder_1} -y", "Everything is Ok")
    res2 = positive(f"ls {folder_1}", "test1.txt")
    res3 = positive(f"ls {folder_1}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"


def test_eight():
    """test8 for checking archive empty, file list output"""
    assert positive(f"cd {folder_out}; 7z l arx2.7z", "2 files")


def test_nine():
    """test9 for checking dearchivation with paths"""
    assert positive(f"cd {folder_out}; 7z x arx2.7z -o{folder_1} -y", "Everything is Ok"), \
        "test9 FAIL"


def test_ten():
    """test10 for checking hash matches crc32 command hash"""
    assert positive(f"cd {folder_out}; 7z h arx2.7z", "F2107E5F")