---  
title: Generate Conditional Formatting DataBars Images  
linktitle: Generate Conditional Formatting DataBars Images  
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports the generation of conditionally formatted data bars and images, allowing users to customize the display of the spreadsheet based on the value of the cells. This article will introduce how to use the Aspose.Cells library to generate conditionally formatted data bars and images.  
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets, Node.js via C++  
type: docs  
weight: 40  
url: /nodejs-cpp/generate-conditional-formatting-databars-images/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  

Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells.  

{{% /alert %}}  

The following sample code generates the DataBar image of cell C1. First, it accesses the format‑condition object of the cell; then, from that object, it accesses the DataBar object and uses its [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) method to generate the cell’s image. Finally, it saves the image to disk.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}  
