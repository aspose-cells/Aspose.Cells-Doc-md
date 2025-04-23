---
title: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，一个电子表格可能包含一个或多个密码保护的工作表，但电子表格本身可能已被保护，也可能未被保护。Aspose.Cells for Python via .NET API 提供检测某个工作表是否被密码保护的方式。本文演示如何使用Aspose.Cells for Python via .NET API实现相同功能。

{{% /alert %}}

Aspose.Cells for Python via .NET 已暴露 [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) 属性，用于检测工作表是否受密码保护。布尔类型的 [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) 属性如果 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 被密码保护则返回 **true**，否则返回 **false**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

