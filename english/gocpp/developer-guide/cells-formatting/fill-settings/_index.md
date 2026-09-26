---
title: Fill Settings with Golang via C++
linktitle: Fill Settings
description: Aspose.Cells is a Go library for working with spreadsheet files. It supports setting the fill settings of cells, allowing users to customize the background and style of cells. This article will introduce how to use the Aspose.Cells library to set cell fill settings.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /go-cpp/cells-fill-settings/
---

## **Colors and Background Patterns**

Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn how to use these features with Aspose.Cells.

### **Setting Colors and Background Patterns**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) class.

The [**Cell**](https://reference.aspose.com/cells/go-cpp/cell/) has the [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/go-cpp/cell/setstyle_style/) methods that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/go-cpp/style/) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [**BackgroundType**](https://reference.aspose.com/cells/go-cpp/backgroundtype/) enumeration that contains a set of pre‑defined types of background patterns which are given below.

| **Background Patterns**      | **Description**                                 |
| ---------------------------- | ------------------------------------------------ |
| DiagonalCrosshatch           | Represents diagonal crosshatch pattern           |
| DiagonalStripe               | Represents diagonal stripe pattern               |
| Gray6                        | Represents 6.25% gray pattern                    |
| Gray12                       | Represents 12.5% gray pattern                    |
| Gray25                       | Represents 25% gray pattern                      |
| Gray50                       | Represents 50% gray pattern                      |
| Gray75                       | Represents 75% gray pattern                      |
| HorizontalStripe             | Represents horizontal stripe pattern             |
| None                         | Represents no background                         |
| ReverseDiagonalStripe        | Represents reverse diagonal stripe pattern      |
| Solid                        | Represents solid pattern                         |
| ThickDiagonalCrosshatch      | Represents thick diagonal crosshatch pattern    |
| ThinDiagonalCrosshatch       | Represents thin diagonal crosshatch pattern     |
| ThinDiagonalStripe           | Represents thin diagonal stripe pattern         |
| ThinHorizontalCrosshatch     | Represents thin horizontal crosshatch pattern   |
| ThinHorizontalStripe         | Represents thin horizontal stripe pattern        |
| ThinReverseDiagonalStripe    | Represents thin reverse diagonal stripe pattern |
| ThinVerticalStripe           | Represents thin vertical stripe pattern          |
| VerticalStripe               | Represents vertical stripe pattern               |

In the example below, the foreground color of the A1 cell is set, but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FillSettings.go" >}}

### **Important to Know**

{{% alert color="primary" %}}

- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's **SetForegroundColor()** or **SetBackgroundColor()** methods. Both methods will take effect only if the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's **GetPattern()** property is configured.  
- The **SetForegroundColor()** method sets the cell's shade color. The **GetPattern()** property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/go-cpp/backgroundtype/), that contains a set of pre‑defined background patterns.  
- If you select **BackgroundType::None**, the foreground color is not applied. Likewise, the background color is not applied if you select **BackgroundType::None** or **BackgroundType::Solid**.  
- When retrieving a cell's shading/fill color, if **Style.GetPattern()** returns **BackgroundType::None**, **Style.GetForegroundColor()** will return **Color.Empty**.

{{% /alert %}}

### **Applying Gradient Fill Effects**

To apply your desired gradient fill effects to a cell, use the [**Style**](https://reference.aspose.com/cells/go-cpp/style/) object's **SetTwoColorGradient** method accordingly.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FillSettings-1.go" >}}

## **Colors and Palette**

A palette is the set of colors available for creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

### **Adding Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class provides a **ChangePalette** method that takes the following parameters to add a custom color to modify the palette:

- **Custom Color** – the custom color to be added.  
- **Index** – the index of the color in the palette that the custom color will replace. Should be between 0‑55.

The example below adds a custom color (Orchid) to the palette before applying it to a font.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FillSettings-2.go" >}}

{{% alert color="primary" %}}

The palette holds only 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is also changed. Therefore, when you modify the palette, please be very careful. Moreover, this limitation exists only in the XLS (Excel 97‑2003) file format; there is no such limitation for XLSX or other advanced MS Excel (2007/2010/2013) file formats.

{{% /alert %}}
{{< app/cells/assistant language="go" >}}
