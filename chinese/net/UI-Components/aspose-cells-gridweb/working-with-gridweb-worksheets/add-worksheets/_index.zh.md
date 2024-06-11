---
title: 添加工作表
type: docs
weight: 20
url: /zh/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: 本文介绍了如何在GridWeb中添加工作表（GridWorksheet）。
---

{{% alert color="primary" %}} 

工作表是Aspose.Cells.GridWeb的一个组成部分。所有数据以工作表的形式进行管理和存储。Aspose.Cells.GridWeb允许开发人员向Aspose.Cells.GridWeb控件添加一个或多个工作表。本主题展示了向Aspose.Cells.GridWeb添加工作表的简单方法。

{{% /alert %}} 
## **添加工作表**
### **不指定工作表名称**
向Aspose.Cells.GridWeb添加工作表的最简单方法是通过GridWeb控件的GridWorksheetCollection类的Add方法。这将创建工作表并使用默认名称（如Sheet1、Sheet2、Sheet3等），然后将它们添加到GridWeb控件中。

**输出：一个带有默认名称的工作表已添加到GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Add方法返回新工作表的索引，可以用于访问此工作表的实例。有关如何访问工作表的更多细节，请阅读[访问工作表](/cells/zh/net/aspose-cells-gridweb/access-worksheets/)。

{{% /alert %}} 
### **使用指定的表格名称**
要向GridWeb控件添加具有特定名称的工作表，而不使用默认的命名方案，可调用Add方法的重载版本，该重载版本接受指定的SheetName。例如，下面的示例添加了名为Invoice的工作表。

**输出：已向GridWeb添加了具有指定名称的工作表** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

接受工作表名称作为字符串的 Add 方法返回 GridWorksheet 的实例。

{{% /alert %}}
