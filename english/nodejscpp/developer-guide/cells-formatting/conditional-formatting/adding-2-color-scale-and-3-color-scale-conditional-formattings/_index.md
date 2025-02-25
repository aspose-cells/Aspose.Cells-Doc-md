---  
title: Adding 2-Color Scale and 3-Color Scale Conditional Formattings with Node.js via C++  
linktitle: Adding 2-Color Scale and 3-Color Scale Conditional Formattings  
description: How to use the Aspose.Cells library in Node.js via C++ to add conditional formatting for two color ratios and three color ratios. By adjusting these criteria, you have more control over how cells look and appear.  
keywords: Aspose.Cells, Conditional Formatting, Node.js via C++, Color Ratio, Two Color Scale, Three Color Scale  
type: docs  
weight: 20  
url: /nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/  
---  

{{% alert color="primary" %}}  
**2-Color Scale** and **3-Color Scale** Conditional Formattings are added in the same way except they are differed by [**FormatCondition.ColorScale.is3ColorScale**](https://reference.aspose.com/cells/nodejs-cpp/colorscale/#is3ColorScale) property. This property is **false** for 2-Color Scale and **true** for 3-Color Scale Conditional Formattings.  
{{% /alert %}}  

The following sample code adds 2-Color and 3-Color Scale Conditional Formattings. It generates the [output excel file](5115058.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add some data in cells
worksheet.getCells().get("A1").putValue("2-Color Scale");
worksheet.getCells().get("D1").putValue("3-Color Scale");

for (let i = 2; i <= 15; i++) {
    worksheet.getCells().get("A" + i).putValue(i);
    worksheet.getCells().get("D" + i).putValue(i);
}

// Adding 2-Color Scale Conditional Formatting
let ca = AsposeCells.CellArea.createCellArea("A2", "A15");

let idx = worksheet.getConditionalFormattings().add();
let fcc = worksheet.getConditionalFormattings().get(idx);
fcc.addCondition(AsposeCells.FormatConditionType.ColorScale);
fcc.addArea(ca);

let fc = worksheet.getConditionalFormattings().get(idx).get(0);
fc.getColorScale().setIs3ColorScale(false);
fc.getColorScale().setMaxColor(AsposeCells.Color.LightBlue);
fc.getColorScale().setMinColor(AsposeCells.Color.LightGreen);

// Adding 3-Color Scale Conditional Formatting
ca = AsposeCells.CellArea.createCellArea("D2", "D15");

idx = worksheet.getConditionalFormattings().add();
fcc = worksheet.getConditionalFormattings().get(idx);
fcc.addCondition(AsposeCells.FormatConditionType.ColorScale);
fcc.addArea(ca);

fc = worksheet.getConditionalFormattings().get(idx).get(0);
fc.getColorScale().setIs3ColorScale(true);
fc.getColorScale().setMaxColor(AsposeCells.Color.LightBlue);
fc.getColorScale().setMidColor(AsposeCells.Color.Yellow);
fc.getColorScale().setMinColor(AsposeCells.Color.LightGreen);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
  