##Encrypt And Decrypt ODS files
password-protect and encrypt ODS files using Aspose.Cells for Python via .NET which is a pure net library.
OpenOffice.org is a full-featured office suite which supports password-protecting and encrypting files. However encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise warning message.The Encryption options are not applicable for ODS file unlike other file types.
Aspose.Cells for Python via .NET allows to encrypt and decrypt ODS file. Decrypted ODS file can be opened both in Excel and OpenOffice,
## **Encrypt with OpenOffice Calc**
1. Select **Save as** and Click the **Save With Password** box.
1. Click the **Save** button.
1. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.
1. Click the **OK** button to save the file.
## **Encrypt ODS file with Aspose.Cells for Python via .NET**
For encrypting an ODS file, load the file and set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.
## **Decrypt ODS file with Aspose.Cells for Pythohn via .NET**
For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Once the file is loaded, set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) string to null.
