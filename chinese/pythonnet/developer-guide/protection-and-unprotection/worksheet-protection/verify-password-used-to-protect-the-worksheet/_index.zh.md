---
title: 验证用于保护工作表的密码
type: docs
weight: 370
url: /zh/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET API增强了 [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) 类，加入了一些实用的属性和方法。其中一个方法是 [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password)，允许你将密码作为 *字符串* 实例传入，并验证相同的密码是否用于保护 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)。

{{% /alert %}}

[**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password)方法将返回**true**，如果指定的密码与用于保护给定工作表的密码匹配，并且如果指定的密码不匹配，则返回**false**。 下面的代码片段使用[**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password)方法与[**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password)属性结合使用，以检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

