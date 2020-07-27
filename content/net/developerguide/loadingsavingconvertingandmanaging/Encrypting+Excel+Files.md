+++
title = "Encrypting Excel Files" 
description = "" 
weight = 12068 
+++

Aspose.Cells for .NET : Encrypting Excel Files  

# Aspose.Cells for .NET : Encrypting Excel Files


Microsoft Excel (97 - 2007) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking systems.

Aspose.Cells allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Using Microsoft Excel](#EncryptingExcelFiles-UsingMicrosoftExcel)
*   2 [Encryption with Aspose.Cells](#EncryptingExcelFiles-EncryptionwithAspose.Cells)
    *   2.1 [Specifying Password to modify Option](#EncryptingExcelFiles-SpecifyingPasswordtomodifyOption)
*   3 [Encryption/Decryption of ODS file with Aspose.Cells](#EncryptingExcelFiles-Encryption/DecryptionofODSfilewithAspose.Cells)
{{< /panel >}}
 

 

## Using Microsoft Excel

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1.  From the **Tools** menu, select **Options**. A dialog will appear.
2.  Select the **Security** tab.
3.  Input a password and click **Advanced**
4.  Choose the encryption type and confirm the password.

## Encryption with Aspose.Cells

The following example shows how to encrypt and password protect an excel file using the Aspose.Cells API.

### Specifying Password to modify Option

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.

## Encryption/Decryption of ODS file with Aspose.Cells

Aspose.Cells allows to encrypt and decrypt ODS file. Decrypted ODS file can be opened both in Excel and OpenOffice, however encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise warning message. The Encryption options are not applicable for ODS file unlike other file types. For encrypting an ODS file, load the file and set the **WorkbookSettings.Password** value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

For decrypting an ODS file, load the file by providing a password in the **LoadOptions.Password**. Once the file is loaded, call function **Workbook.Unprotect()** with actual password as an argument and finally set the **WorkbookSettings.Password** string to null.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [effect-of-TxtSaveOptions.TrimLeadingBlankRowAndColumn-property.png.png](https://docs2.aspose.com/cells/net/attachments/5024978/25395205.png) (image/png)  

