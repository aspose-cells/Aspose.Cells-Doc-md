---
title: 验证加密文件的密码
type: docs
weight: 10
url: /zh/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: 使用 CShape 代码验证加密的 Excel (xlsx、xlsb、xls、xlsm) 和 Open Office (ODS) 文件的密码。
---

{{% alert color="primary" %}}
如果 Excel (xlsx、xlsb、xls、xlsm) 和 Open Office (ODS) 文件被锁定密码，Aspose 支持通过简单密码验证而无需解析文件的特定数据。
{{% /alert %}}

## **验证加密文件的密码**

要验证加密文件的密码，Aspose.Cells for Python via .NET 提供了[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)方法。这些方法接受两个参数，文件流和需要验证的密码。
以下代码片段演示了使用[**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)方法来验证提供的密码是否有效。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


