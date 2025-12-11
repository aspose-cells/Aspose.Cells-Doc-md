---
title: How to Use Color Palette with Golang via C++
linktitle: How to Use Color Palette
type: docs
weight: 80
url: /go-cpp/excel-color-palette/
description: C++ code to add custom colors to the palette and use Excel color palette with Aspose.Cells for C++ API.
keywords: c++ add custom colors to the palette, c++ programmatically excel color palette, programmatically how to use color palette in workbook, c++ how to use color palette in excel
---

## **Colors and Palette**

A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also to use custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

## **Add Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) class provides a [**ChangePalette**](https://reference.aspose.com/cells/go-cpp/workbook/changepalette/) method that takes the following parameters to modify the palette:

- **Custom color** – the custom color to be added.  
- **Index** – the index of the color in the palette that the custom color will replace. It should be between 0 and 55.

The example below adds a custom color (Orchid) to the palette before applying it to a font.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ColorPalette.go" >}}
{{% alert color="primary" %}}

The palette holds only 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is also changed. Therefore, be very careful when modifying the palette. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format; there is no such limitation for XLSX or other newer Excel formats (2007, 2010, 2013, etc.).

{{% /alert %}}