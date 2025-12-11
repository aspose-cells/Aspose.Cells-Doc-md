---
title: Encrypt And Decrypt ODS files
type: docs
weight: 10
url: /python-net/encrypt-and-decrypt-ods-files/
description: password-protect and encrypt ODS files using Aspose.Cells for Python via .NET, which is a pure .NET library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
OpenOffice.org is a full-featured office suite that supports password‑protecting and encrypting files. However, encrypted ODS files can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable to ODS files unlike other file types.  
Aspose.Cells for Python via .NET allows encrypting and decrypting ODS files. Decrypted ODS files can be opened both in Excel and OpenOffice.
{{% /alert %}}

## **Encrypt with OpenOffice Calc**
1. Select **Save As** and click the **Save With Password** box.  
2. Click the **Save** button.  
3. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.  
4. Click the **OK** button to save the file.

## **Encrypt ODS file with Aspose.Cells for Python via .NET**
For encrypting an ODS file, load the file and set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

## **Decrypt ODS file with Aspose.Cells for Python via .NET**

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Once the file is loaded, set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) property to `null`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
