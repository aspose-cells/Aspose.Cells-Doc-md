---
title: 添加工作表
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb，添加，工作表，添加GridWorksheet
description: 本文介绍了如何在GridWeb中添加工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

工作表是Aspose.Cells.GridWeb的一个重要部分。所有数据都以工作表的形式进行管理和存储。Aspose.Cells.GridWeb允许开发人员向Aspose.Cells.GridWeb控件添加一个或多个工作表。本主题展示了向Aspose.Cells.GridWeb添加工作表的简单方法。

{{% /alert %}} 
## **添加工作表**
### **不指定工作表名称**
向Aspose.Cells.GridWeb添加工作表的最简单方法是调用GridWeb控件的GridWorksheetCollection集合中的Add方法。这将创建使用默认名称（即Sheet1、Sheet2、Sheet3等）的工作表，并将它们添加到GridWeb控件。

**输出：已将具有默认名称的工作表添加到GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Add方法返回新工作表的索引，该索引可用于访问该工作表的实例。有关如何访问工作表的详细信息，请阅读[访问工作表](/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}} 
### **使用指定的表名称**
要向GridWeb控件添加具有特定名称的工作表，而不是使用默认命名方案，请调用Add方法的重载版本，该版本接受指定的SheetName。例如，下面的示例添加了名为Invoice的工作表。

**输出：已向GridWeb添加了一个具有指定名称的工作表** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

接受字符串工作表名称的Add方法返回GridWorksheet的实例。

{{% /alert %}}
