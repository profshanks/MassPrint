import tempfile
import win32api
import win32print
import os
import easygui

def print_file(filename):
    open(filename)
    win32api.ShellExecute (
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter (),
        ".",
        0
    )

rootdir = (easygui.diropenbox()+'/')
didPrint = ['The following files made it to the printer:\n']
problems = ['The following files had problems printing:\n']

os.chdir(rootdir)

for subdir, dirs, files in os.walk(rootdir):  
    for file in files:
        try:
            filename = rootdir+file
            print_file(filename)
            didPrint.append(file)
                        
        except:
            problems.append(file)

success = '\n'
success = success.join(didPrint)
fail = '\n'
fail = fail.join(problems)

temp = tempfile.mktemp('.txt')
printLog = open(temp, "w")
printLog.write('\n\n')
printLog.write(success)
printLog.write('\n\n\n\n')
printLog.write(fail)
print_file(temp)
printLog.close()



            

