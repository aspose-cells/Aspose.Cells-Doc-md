---
title: 移除工作表
type: docs
weight: 30
url: /zh/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb，remove，移除GridWorksheet，移除工作表
description: 本文介绍了如何在GridWeb中移除工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

本主题提供了有关如何使用Aspose.Cells.GridWeb API从Microsoft Excel文件中移除工作表的信息。可以通过指定其工作表索引或名称来移除工作表。

{{% /alert %}} 
## **移除工作表**
### **使用工作表索引**
下面的代码显示了如何通过在GridWorksheetCollection的RemoveAt方法中指定其工作表索引来移除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **使用工作表名称**
下面的代码显示了如何通过在GridWorksheetCollection的RemoveAt方法中指定其工作表名称来移除工作表。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

也可以通过其引用或实例来移除工作表。为此，请使用GridWorksheetCollection的Remove方法。这种方法通常被使用。

{{% /alert %}}
