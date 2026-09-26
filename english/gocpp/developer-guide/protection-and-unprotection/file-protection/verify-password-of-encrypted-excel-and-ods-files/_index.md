---
title: Verify Password of Encrypted Files with Golang via C++
linktitle: Verify Password of Encrypted Files
type: docs
weight: 10
url: /go-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the password of encrypted Excel (xlsx, xlsb, xls, xlsm) and OpenOffice (ODS) files using C++ code.
---

{{% alert color="primary" %}} 
If Excel (xlsx, xlsb, xls, xlsm) and OpenOffice (ODS) files are locked with a password, Aspose supports simple password verification without parsing specific data in the files.
{{% /alert %}} 

## **Verify the password of an encrypted file**

To verify the password of the encrypted file, Aspose.Cells for Go via C++ provides the [**VerifyPassword**](https://reference.aspose.com/cells/go-cpp/fileformatutil/fileformatutil_verifypassword/) method. This method accepts two parameters, the file stream and the password that needs to be verified.  
The following code snippet demonstrates the use of the [**VerifyPassword**](https://reference.aspose.com/cells/go-cpp/fileformatutil/fileformatutil_verifypassword/) method to verify whether the provided password is valid.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyPasswordOfEncryptedExcelAndOdsFiles.go" >}}
{{< app/cells/assistant language="go" >}}
