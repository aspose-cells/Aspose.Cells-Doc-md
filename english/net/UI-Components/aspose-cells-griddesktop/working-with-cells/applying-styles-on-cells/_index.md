---
title: Apply Style on Cell
type: docs
weight: 50
url: /net/aspose-cells-griddesktop/apply-style-on-cell/
keywords: GridDesktop,format,style,number formats,number format,NumberFormat
description: This article introduces how to get or set style format in the cell in the Worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This topic deals with applying a style format to a cell; we will cover almost every related property that can be used to apply a style to a cell. In addition to some basic formatting settings, we will also discuss drawing borders and setting number formats on a cell in detail.

{{% /alert %}} 
## **Applying a Custom Style on a Cell - An Example**
To change the font and color of a cell using Aspose.Cells.GridDesktop, please follow the steps below:

- Access any desired **Worksheet**
- Access a **Cell** on which we want to apply a **Style**
- Get **Style** of the **Cell**
- Set **Style** properties according to your custom needs
- Finally, set the **Style** of the **Cell** with the updated one

There are many useful properties and methods offered by the **Style** object that can be used by developers to customize the style according to their requirements. The code below demonstrates how to apply a custom style to a cell.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-ApplyStyle.cs" >}}
## **Drawing Borders of Cells**
Using the **Style** object, we can draw borders of a cell very easily. The borders can be drawn in any color. Moreover, developers have the flexibility to choose a specific type of line that will be used to draw borders around the cell. Developers can use the **SetBorderLine** and **SetBorderColor** methods of the **Style** object to draw borders of any type and color. Similarly, to get border information of any cell, developers can also make use of the **GetBorderLine** and **GetBorderColor** methods of the **Style** object.
### **Types of Borders**
There are six types of borders supported by Aspose.Cells.GridDesktop as follows:

- **Left**, represents left border
- **Right**, represents right border
- **Top**, represents top border
- **Bottom**, represents bottom border
- **DiagonalDown**, represents diagonal‑down border
- **DiagonalUp**, represents diagonal‑up border
### **Types of Border Lines**
A border is composed of a line. Changing the type of line changes the appearance of a border. There are many types of border lines supported by Aspose.Cells.GridDesktop, which are also listed below:

- **None**, represents no border
- **Thin**, represents solid line border
- **Medium**, represents solid line border with line width equal to 2 f
- **Dashed**, represents dashed line border
- **Dotted**, represents dotted line border
- **Thick**, represents solid line border with line width equal to 3 f
- **MediumDashed**, represents dashed line border with line width equal to 2 f
- **ThinDashDotted**, represents dash‑dotted line border
- **MediumDashDotted**, represents dash‑dotted line border with line width equal to 2 f
- **ThinDashDotDotted**, represents dash‑dot‑dotted line border
- **MediumDashDotDotted**, represents dash‑dot‑dotted line border with line width equal to 2 f
## **Putting It All Together - Example**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SummingUp.cs" >}}
## **Setting Number Formats**
Aspose.Cells.GridDesktop also provides various number format settings. There are 58 built‑in number formats offered by Aspose.Cells.GridDesktop. To see a complete list of all supported number formats, please refer to [Supported Number Formats](/cells/net/list-of-supported-number-formats/).

All built‑in number formats are assigned an **Index** number. **For example**, the **Index** number of the **0.00E+00** number format is **11**. To use a built‑in number format in any cell, developers can set the **NumberFormat** property of the **Style** object to the **Index** number of that specific number format. However, if developers need to have their own custom number format, they can also use the **Custom** property of the **Style** object.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-ApplyStyleOnCells-SetNumberFormat.cs" >}}
