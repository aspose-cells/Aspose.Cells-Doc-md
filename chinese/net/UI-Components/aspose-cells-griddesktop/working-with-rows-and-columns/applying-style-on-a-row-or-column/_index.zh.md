---
title: 在行或列上应用样式
type: docs
weight: 50
url: /zh/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

在本主题中，我们将讨论如何更改工作表的行和列的字体和字体颜色。这是 Aspose.Cells.GridDesktop 提供的基本级别的格式化功能，它使开发人员能够自定义工作表的视图，使其更易于呈现。

{{% /alert %}} 
## **在列上应用样式**
要使用 Aspose.Cells.GridDesktop 在列上应用自定义样式，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 访问一个**柱子**我们要在其上应用**风格**
- 得到**风格**的**柱子**
- 放**风格**根据您的自定义需求属性
- 最后，设置**风格**的**柱子**与更新的

提供了许多有用的属性和方法**风格**开发人员可以使用该对象根据他们的要求自定义样式。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **在行上应用样式**
要使用 Aspose.Cells.GridDesktop 在一行上应用自定义样式，请按照以下步骤操作：

- 访问任何想要的**工作表**
- 访问一个**排**我们要在其上应用**风格**
- 得到**风格**的**排**
- 放**风格**根据您的自定义需求属性
- 最后，设置**风格**的**排**与更新的

提供了许多有用的属性和方法**风格**开发人员可以使用该对象根据他们的要求自定义样式。



{{< highlight "csharp" >}}

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
