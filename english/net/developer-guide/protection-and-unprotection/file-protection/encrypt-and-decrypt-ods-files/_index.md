---
title: Encrypt And Decrypt ODS files
type: docs
weight: 10
url: /net/encrypt-and-decrypt-ods-files/
description: Password‑protect and encrypt ODS files using Aspose.Cells for .NET, which is a pure .NET library.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
OpenOffice.org is a full‑featured office suite which supports password‑protecting and encrypting files. However, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable to ODS files, unlike other file types.  
Aspose.Cells allows encrypting and decrypting ODS files. A decrypted ODS file can be opened both in Excel and OpenOffice.
{{% /alert %}}

## **Encrypt with OpenOffice Calc**
1. Select **Save As** and click the **Save With Password** box.  
2. Click the **Save** button.  
3. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.  
4. Click the **OK** button to save the file.

## **Encrypt ODS file with Aspose.Cells for .NET**
For encrypting an ODS file, load the file and set the [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Decrypt ODS file with Aspose.Cells for .NET**

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Once the file is loaded, set the [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) string to `null`.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
