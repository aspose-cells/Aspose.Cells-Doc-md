---
title: 验证加密文件的密码
type: docs
weight: 10
url: /zh/java/verify-password-of-encrypted-excel-and-ods-files/
description: 使用Java代码验证加密的Excel（xlsx，xlsb，xls，xlsm）和开放办公（ODS）文件的密码。
---

{{% alert color="primary" %}}
如果Excel（xlsx、xlsb、xls、xlsm）和Open office（ODS）文件被密码锁定，Aspose.Cells for Java支持对文件进行简单密码验证，无需解析文件的特定数据。
{{% /alert %}}

## **验证加密文件的密码**

要验证加密文件的密码，Aspose.Cells for Java提供了 [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) 方法。该方法接受两个参数，文件流和需要验证的密码。
以下代码片段演示了使用[**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String))方法来验证提供的密码是否有效。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

