---
title: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但电子表格本身可能受保护，也可能不受保护。Aspose.Cells API提供了检测给定工作表是否受密码保护的方法。本文演示了使用 Aspose.Cells for .NET API 实现相同功能的用法。

{{% /alert %}}

Aspose.Cells for .NET 8.7.0已公开了[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性，用于检测工作表是否受密码保护。布尔型[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性返回 **true** 如果工作表被密码保护，**false** 如果没有。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
