---
title: 验证加密文件的密码
type: docs
weight: 10
url: /zh/net/verify-password-of-encrypted-excel-and-ods-files/
description: 使用 CShape 代码验证加密的 Excel（xlsx、xlsb、xls、xlsm）和 Open office (ODS) 文件的密码。
---
{{% alert color="primary" %}}
如果Excel（xlsx、xlsb、xls、xlsm）和Open office（ODS）文件被密码锁定，Aspose支持简单的密码验证，无需解析文件的具体数据。
{{% /alert %}}

## **验证加密文件的密码**

验证加密文件密码，Aspose.Cells for .NET提供[**验证密码**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)方法。这些方法接受两个参数，文件流和需要验证的密码。
下面的代码片段演示了使用[**验证密码**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword)验证提供的密码是否有效的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

