---
title: 移除工作表
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb,删除,移除GridWorksheet,移除工作表
description: 本文介绍了如何在GridWeb中删除工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

本主题提供有关如何使用Aspose.Cells.GridWeb API从Microsoft Excel文件中删除工作表的信息。可以通过指定工作表索引或名称来删除工作表。

{{% /alert %}} 
## **删除工作表**
### **使用工作表索引**
下面的代码显示了如何通过在GridWorksheetCollection的RemoveAt方法中指定工作表索引来删除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的代码显示了如何通过在GridWorksheetCollection的RemoveAt方法中指定工作表名称来删除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

还可以使用其引用或实例删除工作表。要这样做，请使用GridWorksheetCollection的Remove方法。这种方法通常被使用。

{{% /alert %}}
