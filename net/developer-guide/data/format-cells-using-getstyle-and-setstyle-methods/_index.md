---
title: Format Cells using GetStyle and SetStyle Methods
type: docs
weight: 40
url: /net/format-cells-using-getstyle-and-setstyle-methods/
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**GetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) and [**SetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) methods of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class, used to get/set the formatting style of a cell. Aspose.Cells also provides a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) class.

{{% /alert %}}

## **Format Cells using GetStyle and SetStyle Methods**

Apply different kinds of formatting styles on cells to set background or foreground colors, borders, fonts, horizontal and vertical alignments, indentation level, text direction, rotation angle and much more.

### **Using the GetStyle and SetStyle Methods**

If developers need to apply different formatting styles to different cells then it's better to get the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) of the cell using [**Cell.GetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) method, specify the style attributes and then apply the formatting using [**Cell.SetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) method. An example is given below to demonstrate this approach to apply various formatting on a cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Using Style Object to Format Different Cells**

If developers need to apply the Same formatting style to different cells then they can use [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object. Please follow the steps below to use the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object:

1. Add a [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object by calling the [**CreateStyle**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) method of the [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class
1. Access the newly added [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object
1. Set the desired properties/attributes of the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to apply desired formatting settings
1. Assign the configured [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object to your desired cells

This approach can greatly improve the efficiency of your applications and save memory too.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Using Microsoft Excel 2007 Predefined Styles**

If you need to apply different formatting styles for Microsoft Excel 2007, apply styles using the Aspose.Cells API. An example is given below to demonstrate this approach to apply a predefined style on a cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}

### **Applying Gradient Fill Effects**

To apply your desired Gradient Fill Effects to the cell, use the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object's [**SetTwoColorGradient**](https://apireference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) method accordingly.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}
