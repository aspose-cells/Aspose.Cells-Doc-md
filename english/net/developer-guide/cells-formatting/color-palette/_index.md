---
title: How to Use Color Palette
type: docs
weight: 80
url: /net/excel-color-palette/
description: C# code to add custom colors to the palette and use excel color palette with Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---

## **Colors and Palette**

A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

## **Add Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class provides a [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) method that takes the following parameters to add a custom color to modify the palette:

- Custom Color, the custom color to be added.
- Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.

The example below adds a custom color (Orchid) to the palette before applying it on a font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.

{{% /alert %}}