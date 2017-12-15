# import
import os, Crypto_files


def list_hdd_files():
    """
    List all external HDD letters and files
    """
    files = []
    # C drive is not in the list, no need for it
    # We only want the secondary partition and external drives
    drive_letters = 'ABDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in drive_letters if os.path.exists('%s:' % d)]

    for drive in drives:
        # Add all drives files to "hdds_files" variable
        files += Crypto_files.list_files(drive + "\\test\\")
    return files