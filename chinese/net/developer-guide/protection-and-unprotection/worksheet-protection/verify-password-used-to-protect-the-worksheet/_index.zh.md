---
title: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API通过引入一些有用的属性和方法增强了[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection)类。其中一种方法是[**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)，允许将密码指定为*string*实例，并验证是否已使用相同密码来保护[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)。

{{% /alert %}}

如果指定的密码与用于保护给定工作表的密码匹配，则[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)方法返回**true**，如果指定的密码不匹配，则返回**false**。以下代码片段结合使用[**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)方法和[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性来检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
