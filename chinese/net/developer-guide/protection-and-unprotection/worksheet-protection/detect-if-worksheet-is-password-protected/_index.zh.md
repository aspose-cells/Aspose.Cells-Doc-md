---
title: 检测工作表是否受密码保护
type: docs
weight: 360
url: /zh/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但是，电子表格本身可能会或可能不会受到保护。 Aspose.Cells API 提供了检测给定工作表是否受密码保护的方法。本文演示了使用 Aspose.Cells for .NET API 来实现相同的目的。

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0暴露了[**保护.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)属性来检测工作表是否受密码保护。布尔型[**保护.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)财产回报**真的**如果[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)受密码保护，并且**错误的**如果不。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
