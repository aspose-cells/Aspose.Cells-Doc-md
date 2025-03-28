---
title: Filter Objects while loading Workbook or Worksheet with Node.js via C++
linktitle: Filter Objects while loading Workbook or Worksheet
type: docs
weight: 330
url: /nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Learn how to filter data while loading workbooks or worksheets using Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**
Please use [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) property while filtering data from the workbook. But if you want to filter data from individual worksheets, then you will have to override the [LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-) method. Please provide appropriate value from the [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) enumeration while creating or working with [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter).

The [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) enumeration has the following possible values.

- All
- BookSettings
- CellBlank
- CellBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Chart
- ConditionalFormatting
- DataValidation
- DefinedNames
- DocumentProperties
- Formula
- Hyperlinks
- MergedArea
- PivotTable
- Settings
- Shape
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap

## **Filter Objects while loading Workbook**
The following sample code illustrates how to filter charts from the workbook. Please check the [sample excel file](5115258.xlsx) used in this code and the [output PDF](5115257.pdf) generated by it. As you can see in the output PDF, all charts have been filtered out of the workbook.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **Filter Objects while loading Worksheet**
The following sample code loads the [source excel file](5115255.xlsx) and filters the following data from its worksheets using a custom filter.

- It filters Charts from worksheet named NoCharts.
- It filters Shapes from worksheet named NoShapes.
- It filters Conditional Formatting from worksheet named NoConditionalFormatting.

Once, it loads the [source excel file](5115255.xlsx) with a custom filter, it takes the images of all worksheets one by one. Here are the output images for your reference. As you can see, the first image does not have charts, the second image does not have shapes and the third image does not have conditional formatting.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

This is how to use the CustomLoadFilter class as per worksheet names.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
