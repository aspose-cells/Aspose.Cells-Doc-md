---  
title: How to Use Color Palette
linktitle: How to Use Color Palette  
type: docs  
weight: 80  
url: /nodejs-cpp/excel-color-palette/  
description: Node.js code to add custom colors to the palette and use Excel color palette with Aspose.Cells for Node.js via C++.  
keywords: node.js add custom colors to the palette, node.js programmatically excel color palette, programmatically how to use color palette in workbook, node.js how to use color palette in excel  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  
  
## **Colors and Palette**  
  
A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.  
  
With Aspose.Cells for Node.js via C++, it is possible not only to use the palette's existing colors but also to use custom colors. Before using a custom color, add it to the palette first.  
  
This topic discusses how to add custom colors to the palette.  
  
## **Add Custom Colors to Palette**  
  
Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.  
  
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) class provides a [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) method that takes the following parameters to add a custom color to the palette:  
  
- Custom Color – the custom color to be added.  
- Index – the index of the color in the palette that the custom color will replace. It should be between 0 and 55.  
  
The example below adds a custom color (Orchid) to the palette before applying it to a font.  
  
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}

{{% alert color="primary" %}}  
  
The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. Therefore, be very careful when changing the palette. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format, as there is no such limitation for XLSX or other advanced Microsoft Excel (2007, 2010, or 2013) file formats.  
  
{{% /alert %}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
