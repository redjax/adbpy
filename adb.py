"""Script ADB backup and restore commands."""

import subprocess


backuploc = 'C:\\users\\jack\\desktop\\andback'


def menu():
    """Display options displayed when script is run."""
    choice = input('(B)ackup or (R)estore: ')
    choice = choice.upper()

    if choice == 'B':
        adbfullbackup()

    elif choice == 'R':
        adbrestore()

    else:
        input('''Invalid choice.
              Please type \"B\" or \"R\". Press any key to try again: ''')
        menu()


def adbfullbackup():
    """Back up everything."""
    global backuploc
    adbcmd = 'adb backup -apk -shared -all  '

    runfullcmd(adbcmd)


def adbrestore():
    """Restore backed up data."""
    global backuploc
    adbcmd = 'adb restore ' + backuploc + 'backup.ab'

    runfullcmd(adbcmd)


def runfullcmd(c):
    """Run the command prompt with the chosen operation(s)."""
    global backuploc

    subprocess.call(['runas', '/user:Jack', 'cmd /c ' + ' cd ' + backuploc + ' && ' + c])


def backupmanage():
    """Move backups around to save previous versions."""
    """
    TODO:
        * File management options for user
        * Backup retention
        * Work with restore command (rename to backup.ab)
    """


menu()
