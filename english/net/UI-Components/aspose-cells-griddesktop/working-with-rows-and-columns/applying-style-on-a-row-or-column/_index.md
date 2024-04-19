---
title: Applying Style on a Row or Column
type: docs
weight: 50
url: /net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop,style,row,column
description: This article introduces how to apply style on row or column in GridDesktop.
---

{{% alert color="primary" %}} 

In this topic, we will discuss about changing the font and font color of rows and columns of a worksheet. This is a basic level of formatting feature offered by Aspose.Cells.GridDesktop that empowers developers to customize the view of their worksheets for making them more presentable.

{{% /alert %}} 
## **Applying Style on a Column**
To apply a custom style on a column using Aspose.Cells.GridDesktop, please follow the steps below:

- Access any desired **Worksheet**
- Access a **Column** on which we want to apply a **Style**
- Get **Style** of the **Column**
- Set **Style** properties according to your custom needs
- Finally, set **Style** of the **Column** with the updated one

There are many useful properties and methods offered by **Style** object that can be used by developers to customize the style according to their requirements.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Applying Style on a Row**
To apply a custom style on a row using Aspose.Cells.GridDesktop, please follow the steps below:

- Access any desired **Worksheet**
- Access a **Row** on which we want to apply a **Style**
- Get **Style** of the **Row**
- Set **Style** properties according to your custom needs
- Finally, set **Style** of the **Row** with the updated one

There are many useful properties and methods offered by **Style** object that can be used by developers to customize the style according to their requirements.



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
