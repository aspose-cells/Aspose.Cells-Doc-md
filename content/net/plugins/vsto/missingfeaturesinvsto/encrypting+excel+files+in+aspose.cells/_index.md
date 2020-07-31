---
title : "Encrypting Excel Files in Aspose.Cells" 
description : "" 
weight : 16825 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/encrypting+excel+files+in+aspose.cells/
---

# Aspose.Cells for .NET : Encrypting Excel Files in Aspose.Cells


Microsoft Excel (97 - 2007) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be a weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking systems.

Aspose.Cells allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.

#### Using Microsoft Excel

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1.  From the **Tools** menu, select **Options**.  
    A dialog appears.
2.  Select the **Security** tab.
3.  Input a password and click **Advanced**  
    **Options dialog**  
    ![](https://docs2.aspose.com/cells/net/attachments/5020766/5115073.png)  
      
    
4.  Choose the encryption type and confirm the password.  
      
    **Encryption Type dialog**  
    ![](https://docs2.aspose.com/cells/net/attachments/5020766/5115075.png)  
      
    

#### Encryption with Aspose.Cells

The following example shows how to encrypt and password protect an excel file using the Aspose.Cells API.

**C#**

{{< code lang="c#" >}}
//Instantiate a Workbook object.
//Open an excel file.
Workbook workbook = new Workbook("Book1.xls");

//Specify XOR encryption type.
workbook.SetEncryptionOptions(EncryptionType.XOR,40);

//Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.SetEncryptionOptions(EncryptionType.StrongCryptographicProvider, 128);

//Password protect the file.
workbook.Settings.Password = "1234";

//Save the excel file.
workbook.Save("encryptedBook1.xls");
 
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsnet.codeplex.com/SourceControl/latest#Plugins/Aspose For VSTO/Aspose.Cells Features missing in VSTO/Encrypting Excel Files/)
*   [CodePlex](https://asposevsto.codeplex.com/SourceControl/latest#Aspose Only features Unavailable in VSTO/Aspose.Cells/Encrypting Excel Files/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Encrypting%20Excel%20Files)
*   [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836/view/SourceCode#content)

## Download Sample Code

*   [CodePlex](https://asposecellsnet.codeplex.com/releases/view/618484)
*   [CodePlex](https://asposevsto.codeplex.com/releases/view/618289)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/Missing-features-in-VSTO-ac9ea836#content)

