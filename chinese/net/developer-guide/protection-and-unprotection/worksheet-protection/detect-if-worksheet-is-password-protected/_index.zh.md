---
title: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但电子表格本身可能受保护，也可能未受保护。Aspose.Cells API提供了检测特定工作表是否受密码保护的手段。本文演示了使用Aspose.Cells for .NET API实现相同目的的方法。

{{% /alert %}}

Aspose.Cells for .NET 8.7.0公开了[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性，用于检测工作表是否受密码保护。布尔类型[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性如果[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)受到密码保护则返回**true**，如果未受保护则返回**false**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
