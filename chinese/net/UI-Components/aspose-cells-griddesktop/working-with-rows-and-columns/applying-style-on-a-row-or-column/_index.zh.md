---
title: 在行或列上应用样式
type: docs
weight: 50
url: /zh/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop，样式，行，列
description: 本文介绍了如何在 GridDesktop 中为行或列应用样式。
---

{{% alert color="primary" %}} 

在本主题中，我们将讨论如何更改工作表的行和列的字体和字体颜色。这是Aspose.Cells.GridDesktop提供的一项基本格式功能，使开发人员可以自定义工作表的视图，使其更具展示性。

{{% /alert %}} 
## **在列上应用样式**
要在列上应用自定义样式，请按以下步骤操作：

- 访问任何所需的**工作表**
- 访问要应用**样式**的**列**
- 获取**列**的**样式**
- 根据您的自定义需求设置**样式**属性
- 最后，使用更新后的样式设置**列**的**样式**

 **样式**对象提供了许多有用的属性和方法，开发人员可以使用这些属性和方法根据自己的需求来自定义样式。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **在行上应用样式**
要在行上应用自定义样式，请按照以下步骤操作：

- 访问任何所需的**工作表**
- 访问要应用**样式**的**行**
- 获取**行**的**样式**
- 根据您的自定义需求设置**样式**属性
- 最后，使用更新后的样式设置**行**的**样式**

 **样式**对象提供了许多有用的属性和方法，开发人员可以使用这些属性和方法根据自己的需求来自定义样式。



{{< highlight csharp >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
