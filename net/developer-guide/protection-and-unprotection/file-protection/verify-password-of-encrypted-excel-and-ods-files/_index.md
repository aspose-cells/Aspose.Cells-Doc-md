---
title: Verify Password of Encrypted Files
type: docs
weight: 10
url: /net/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the passord of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files using CShape codes.
---

{{% alert color="primary" %}}
If Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files are locked with password, Aspose supports simple password verification without parsing specific data of the files.
{{% /alert %}}

## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for .NET provides the [**VerifyPassword**](https://apireference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) method. These methods accept two parameters, the file stream and the password that needs to be verified.
The following code snippet demonstrates the use of the [**VerifyPassword**](https://apireference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) method to verify whether the provided password is valid or not.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

