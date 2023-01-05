---
title: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells API增强了[**保护**](https://reference.aspose.com/cells/net/aspose.cells/protection)通过引入一些有用的属性和方法来类。一种这样的方法是[**验证密码**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)它允许指定一个密码作为一个实例*细绳*并验证是否使用了相同的密码来保护[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

这[**保护.验证密码**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)方法返回**真的**如果指定的密码与用于保护给定工作表的密码匹配，并且**错误的**如果指定的密码不匹配。下面的一段代码使用了[**保护.验证密码**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword)结合方法[**保护.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
