---
title: Fill Settings
description: Aspose.Cells is a .NET library for working with spreadsheet files. It supports setting the fill settings of cells, allowing users to customize the background and style of cells. This article will introduce how to use the Aspose.Cells library to set cell fill settings.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /net/cells-fill-settings/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Colors and Background Patterns**

Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features **with** Aspose.Cells.

### **Setting Colors and Background Patterns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class.

The [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) has the [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) and [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) methods that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) enumeration that contains a set of predefined types of background patterns which are given below.

| **Background Patterns**          | **Description**                                 |
| -------------------------------- | ------------------------------------------------ |
| DiagonalCrosshatch               | Represents diagonal crosshatch pattern          |
| DiagonalStripe                   | Represents diagonal stripe pattern               |
| Gray6                            | Represents 6.25% gray pattern                   |
| Gray12                           | Represents 12.5% gray pattern                   |
| Gray25                           | Represents 25% gray pattern                     |
| Gray50                           | Represents 50% gray pattern                     |
| Gray75                           | Represents 75% gray pattern                     |
| HorizontalStripe                 | Represents horizontal stripe pattern             |
| None                             | Represents no background                         |
| ReverseDiagonalStripe            | Represents reverse diagonal stripe pattern      |
| Solid                            | Represents solid pattern                         |
| ThickDiagonalCrosshatch          | Represents thick diagonal crosshatch pattern    |
| ThinDiagonalCrosshatch           | Represents thin diagonal crosshatch pattern     |
| ThinDiagonalStripe               | Represents thin diagonal stripe pattern         |
| ThinHorizontalCrosshatch         | Represents thin horizontal crosshatch pattern   |
| ThinHorizontalStripe             | Represents thin horizontal stripe pattern       |
| ThinReverseDiagonalStripe        | Represents thin reverse diagonal stripe pattern |
| ThinVerticalStripe               | Represents thin vertical stripe pattern          |
| VerticalStripe                   | Represents vertical stripe pattern               |

In the example below, the foreground color of **cell A1** is set, but **A2** is configured to have both foreground and background colors with a vertical stripe background pattern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Important to Know**

{{% alert color="primary" %}}

- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object's [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) or [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) properties. Both properties will take effect only if the [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object's [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) property is configured.
- The [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) property sets the cell's shade color. The [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) that contains a set of predefined types of background patterns.
- If you select *BackgroundType.None* value from the [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) enumeration, the foreground color is not applied. Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.
- When retrieving a cell's shading/fill color, if [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) is *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) will return *Color.Empty*.

{{% /alert %}}

### **Applying Gradient Fill Effects**

To apply your desired gradient fill effects to the cell, use the [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object's [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) method accordingly.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Colors and Palette**

A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also **to** use custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

### **Adding Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class provides a [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) method that takes the following parameters to modify the palette:

- **Custom Color** – the custom color to be added.  
- **Index** – the index of the color in the palette that the custom color will replace. Should be between 0‑55.

The example below adds a custom color (Orchid) to the palette before applying it on a font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format, as there is no such limitation for XLSX or other advanced MS Excel (2007/2010/2013) file formats.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
