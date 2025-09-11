---
title: Verify Password of Encrypted Files
type: docs
weight: 10
url: /python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the passord of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files using CShape codes.
---

{{% alert color="primary" %}}
If Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files are locked with password, Aspose supports simple password verification without parsing specific data of the files.
{{% /alert %}}

## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for Python via .NET provides the [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) method. These methods accept two parameters, the file stream and the password that needs to be verified.
The following code snippet demonstrates the use of the [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) method to verify whether the provided password is valid or not.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


{{< app/cells/assistant language="python-net" >}}