---
title: 添加工作表
type: docs
weight: 20
url: /zh/net/add-worksheets/
---
{{% alert color="primary" %}} 

工作表是 Aspose.Cells.GridWeb 的组成部分。所有数据都以工作表的形式进行管理和存储。 Aspose.Cells.GridWeb 允许开发人员向 Aspose.Cells.GridWeb 控件添加一个或多个工作表。本主题展示了将工作表添加到 Aspose.Cells.GridWeb 的简单方法。

{{% /alert %}} 
## **添加工作表**
### **不指定工作表名称**
向 Aspose.Cells.GridWeb 添加工作表的最简单方法是在 GridWeb 控件中调用 GridWorksheetCollection 集合的 Add 方法。这将创建使用默认名称（即 Sheet1、Sheet2、Sheet3 等）的工作表并将它们添加到 GridWeb 控件。

**输出：具有默认名称的工作表已添加到 GridWeb** 

![待办事项：图像_替代_文本](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Add 方法返回新工作表的索引，该索引可用于访问此工作表的实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/net/access-worksheets/).

{{% /alert %}} 
### **具有指定的工作表名称**
若要将具有特定名称的工作表添加到 GridWeb 控件而不是使用默认命名方案，请调用采用指定 SheetName 的 Add 方法的重载版本。例如，下面的示例添加了一个名为 Invoice 的工作表。

**输出：具有指定名称的工作表已添加到 GridWeb** 

![待办事项：图像_替代_文本](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

接受工作表名称作为字符串的 Add 方法返回 GridWorksheet 的一个实例。

{{% /alert %}}
