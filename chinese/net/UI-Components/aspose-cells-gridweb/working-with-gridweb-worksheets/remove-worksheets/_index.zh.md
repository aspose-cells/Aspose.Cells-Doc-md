---
title: 删除工作表
type: docs
weight: 30
url: /zh/net/remove-worksheets/
---
{{% alert color="primary" %}} 

本主题提供有关如何使用 Aspose.Cells.GridWeb API 从 Microsoft Excel 文件中删除工作表的信息。可以通过指定工作表索引或名称来删除工作表。

{{% /alert %}} 
## **删除工作表**
### **使用图纸索引**
下面的代码显示了如何通过在 GridWorksheetCollection 的 RemoveAt 方法中指定工作表索引来删除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的代码显示了如何通过在 GridWorksheetCollection 的 RemoveAt 方法中指定工作表名称来删除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

也可以使用其引用或实例删除工作表。为此，请使用 GridWorksheetCollection 的 Remove 方法。这种方法很常用。

{{% /alert %}}
