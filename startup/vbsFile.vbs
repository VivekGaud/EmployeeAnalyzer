do
   MyCode
   wscript.sleep 1500000
loop

Sub MyCode
Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c setup.bat"
oShell.Run strArgs, 0, false

End Sub



