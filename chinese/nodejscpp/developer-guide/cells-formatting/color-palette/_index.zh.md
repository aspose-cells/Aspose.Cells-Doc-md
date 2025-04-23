---  
title: 如何使用颜色调色板
linktitle: 如何使用颜色调色板  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/excel-color-palette/  
description: 在 Node.js 中添加自定义颜色到调色板，并使用 Aspose.Cells for Node.js via C++ 的 Excel 颜色调色板。  
keywords: 在 Node.js 中添加自定义颜色到调色板，Node.js 程序matically 使用 Excel 颜色调色板，程序matically 在工作簿中使用调色板，Node.js 如何在 Excel 中使用颜色调色板  
---  

## **颜色和调色板**  

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。  

通过 Aspose.Cells for Node.js via C++，不仅可以使用调色板中的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。  

本主题讨论如何向调色板中添加自定义颜色。  

## **向调色板添加自定义颜色**  

Aspose.Cells 支持 Microsoft Excel 的 56 种颜色调色板。要使用在调色板中未定义的自定义颜色，需要将颜色添加到调色板中。  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) 类提供一个 [**changePalette(Color, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) 方法，接受以下参数以添加自定义颜色以修改调色板：  

- Custom Color，要添加的自定义颜色。  
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。  

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ColorPalette.js" >}}


{{% alert color="primary" %}}  

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。  

{{% /alert %}}  

