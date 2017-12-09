# import
import os, Crypto_files


def list_hdd_files():
    """
    List all external HDD
    """
    list_of_all_files = []
    # C drive is not in the list, no need for it
    # We only want the secondary partition and external drives
    drive_letters = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in drive_letters if os.path.exists('%s:' % d)]
    print(drives)

    for drive in drives:
        # List files on each drives
        hdd_list_files = Crypto_files.list_files(drive + "\\test\\")
        # Add all drives files to "list_of_all_files" variable
        list_of_all_files += hdd_list_files
    return list_of_all_files