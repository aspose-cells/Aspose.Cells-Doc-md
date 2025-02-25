---
title: Generate Conditional Formatting DataBars Images with Node.js via C++
linktitle: Generate Conditional Formatting DataBars Images
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports the generation of conditionally formatted data bars and images, allowing users to customize the display of the spreadsheet based on the value of the cells. This article will introduce how to use the Aspose.Cells library to generate conditionally formatted data bars and images.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets, Node.js via C++
type: docs
weight: 40
url: /nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells.

{{% /alert %}}

The following sample code generates the DataBar image of cell C1. First, it accesses the format condition object of the cell, and then from that object, it accesses the [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) object and uses its [**toImage()**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage) method to generate the image of the cell. Finally, it saves the image on disk.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Create workbook object from source excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleGenerateDatabarImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the cell which contains conditional formatting databar
const cell = worksheet.getCells().get("C1");

// Create and get the conditional formatting of the worksheet
const idx = worksheet.getConditionalFormattings().add();
const fcc = worksheet.getConditionalFormattings().get(idx);
fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

// Access the conditional formatting databar
const dbar = fcc.get(0).getDataBar();

// Create image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);

// Get the image bytes of the databar
const imgBytes = dbar.toImage(cell, opts);

// Write image bytes on the disk
fs.writeFileSync(path.join(outputDir, "outputGenerateDatabarImage.png"), imgBytes);
```
