---
title: Verify Password of Encrypted Files
type: docs
weight: 10
url: /java/verify-password-of-encrypted-excel-and-ods-files/
description: Verify the passord of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files using Java codes.
---

{{% alert color="primary" %}}
If Excel (xlsx, xlsb, xls, xlsm) and Open office (ODS) files are locked with password, Aspose.Cells for Java supports simple password verification without parsing specific data of the files.
{{% /alert %}}

## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for Java provides the [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) method. The methods accepts two parameters, the file stream and the password that needs to be verified.
The following code snippet demonstrates the use of the [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) method to verify whether the provided password is valid or not.

### **Sample Code:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}