---
title: Data Filtering with Node.js via C++
type: docs
weight: 85
url: /nodejs-cpp/data-filtering/
description: Learn how to add data filter by using the Aspose.Cells for Node.js via C++ API.
keywords: Add Filter by Color Node.js via C++, Add Date Filters Node.js via C++, Add Number Filters Node.js via C++, Add Dynamic Filter Node.js via C++, Add Text Filters Node.js via C++, Add custom filter with Contains Node.js via C++, Add custom filter with NotContains Node.js via C++, Add custom filter with BeginsWith Node.js via C++, Add custom filter with EndsWith Node.js via C++
---

{{% alert color="primary" %}}
Microsoft Excel provides some good features to autofilter worksheet data. Aspose.Cells fully supports Microsoft Excel's autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells for Node.js via C++.
{{% /alert %}}

## **Autofilter Data**

Autofiltering is the quickest way to select only those items from the worksheet that you want to display in a list. The autofilter feature allows users to filter items in a list according to a set criteria. Filter based on text, numbers or dates.

### **Autofilter in Microsoft Excel**

To activate the autofilter feature in Microsoft Excel:

1. Click the heading row in a worksheet.
1. From the **Data** menu, select **Filter** and then **AutoFilter**.

When you apply an autofilter to a worksheet, filter switches (black arrows) appear to the right of the column headings.

1. Click a filter arrow to see a list of filter options.

Some of the autofilter options are:

|**Options**|**Description**|
| :- | :- |
|All|Show all items in the list once.|
|Custom|Customize filter criteria like contains/not contains|
|Filter by Color|Filters based on filled color|
|Date Filters|Filters rows based on different criteria on date|
|Number Filters|Different types of filter on numbers like comparison, averages and Top 10 etc.|
|Text Filters|Different filters like begins with, ends with, contains etc,|
|Blanks/Non Blanks|These filters can be implemented through Text Filter Blank|

Users manually filter their worksheet data in Microsoft Excel using these options.

### **Autofilter with Aspose.Cells for Node.js via C++**

Aspose.Cells provides a class, Workbook that represents an Excel file. The Workbook class contains a Worksheets collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the Worksheet class. The Worksheet class provides a wide range of properties and methods to manage worksheets. To create an autofilter, use the AutoFilter property of the Worksheet class. The AutoFilter property is an object of the AutoFilter class, which provides the Range property for specifying the range of cells that make up a heading row. An autofilter is applied to the range of cells that is the heading row.

In each worksheet, you can only specify one filter range. This is limited by Microsoft Excel. For custom data filtering, use the AutoFilter.Custom method.

In the example given below, we have created the same AutoFilter using Aspose.Cells for Node.js via C++ as we created using Microsoft Excel in the above section.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating AutoFilter by giving the cells range of the heading row
worksheet.getAutoFilter().setRange("A1:B1");

// Saving the modified Excel file
workbook.save(dataDir + "output.out.xls");
```

#### **Different types of Filter**

Aspose.Cells provides multiple options to apply different type of filters like Color Filter, Date Filter, Number Filter, Text Filter, Blank Filters and None Blank Filters.

##### **Fill Color**

Aspose.Cells provides a function AddFillColorFilter to filter data based upon the fill color property of the cells. In the example given below, a template file having different fill colors in the first column of the sheet is used to test the color filtering function. Sample files can be downloaded from the following links.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Source directory
const sourceDir = dataDir;

// Output directory
const outputDir = dataDir;

// Instantiating a Workbook object
// Opening the Excel file through the file stream
let workbook = new AsposeCells.Workbook(path.join(sourceDir, "ColouredCells.xlsx"));

// Instantiating a CellsColor object for foreground color
let clrForeground = workbook.createCellsColor();
clrForeground.color = AsposeCells.Color.fromArgb(255, 0, 0); // Red color

// Instantiating a CellsColor object for background color
let clrBackground = workbook.createCellsColor();
clrBackground.color = AsposeCells.Color.fromArgb(255, 255, 255); // White color

// Accessing the first worksheet in the Excel file
let worksheet = workbook.getWorksheets().get(0);

// Call AddFillColorFilter function to apply the filter
worksheet.getAutoFilter().addFillColorFilter(0, AsposeCells.BackgroundType.Solid, clrForeground, clrBackground);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(outputDir, "FilteredColouredCells.xlsx"));
```

##### **Date**

Different types of date filters can be implemented like filtering all the rows having dates in January 2018. Following sample code demonstrates this filter using AddDateFilter function. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Date.xlsx"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call AddDateFilter function to apply the filter
worksheet.getAutoFilter().addDateFilter(0, AsposeCells.DateTimeGroupingType.Month, 2018, 1, 0, 0, 0, 0);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(outputDir, "FilteredDate.xlsx"));
```

##### **Dynamic Date**

Sometimes dynamic filters are required based on date like all the cells having dates in January irrespective of the year. In this case DynamicFilter function is used as given in the following sample code. Sample files are given below.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data/");
const outputDir = path.join(__dirname, "output/");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(`${sourceDir}Date.xlsx`);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call DynamicFilter function to apply the filter
worksheet.getAutoFilter().dynamicFilter(0, AsposeCells.DynamicFilterType.January);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(`${outputDir}FilteredDynamicDate.xlsx`);
```

##### **Number**

Custom filters can be applied using Aspose.Cells like selecting cells having number between a given range. Following example demonstrates the usage of Custom() function to filter numbers. Sample files are given below.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "data");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Number.xlsx"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call Custom function to apply the filter
worksheet.getAutoFilter().custom(0, AsposeCells.FilterOperatorType.GreaterOrEqual, 5, true, AsposeCells.FilterOperatorType.LessOrEqual, 10);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(outputDir, "FilteredNumber.xlsx"));
```

##### **Text**

If a column contains text and cells are to be selected containing particular text, Filter() function can be used. In the following example, the template file contains a list of countries and the row is to be selected containing a particular country name. Following code demonstrates filtering text. Sample files are given below.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Text.xlsx"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call Filter function to apply the filter
worksheet.getAutoFilter().filter(0, "Angola");

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(outputDir, "FilteredText.xlsx"));
```

##### **Blanks**

If a column contains text such that few cells are blank, and filter is required to select those rows only where blank cells are present, MatchBlanks() function can be used as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Source directory
const sourceDir = path.join(dataDir, "source/");

// Output directory
const outputDir = path.join(dataDir, "output/");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(sourceDir + "Blank.xlsx");

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call MatchBlanks function to apply the filter
worksheet.getAutoFilter().matchBlanks(0);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(outputDir + "FilteredBlank.xlsx");
```

##### **Non Blanks**

When cells having any text are to be filtered, use MatchNonBlanks filter function as demonstrated below. Sample files are given below.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Source directory
const sourceDir = dataDir + "/"; // Assuming sourceDir is stored here
// Output directory
const outputDir = dataDir + "/"; // Assuming outputDir is stored here

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(sourceDir + "Blank.xlsx");

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Call MatchNonBlanks function to apply the filter
worksheet.getAutoFilter().matchNonBlanks(0);

// Call refresh function to update the worksheet
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(outputDir + "FilteredNonBlank.xlsx");
```

##### **Custom filter with Contains**

Excel provides custom filters like filter rows which contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file. Sample files are given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object containing sample data
let workbook = new AsposeCells.Workbook(path.join(dataDir, "sourseSampleCountryNames.xlsx"));

// Accessing the first worksheet in the Excel file
let worksheet = workbook.getWorksheets().get(0);

// Creating AutoFilter by giving the cells range
worksheet.getAutoFilter().setRange("A1:A18");

// Initialize filter for rows containing string "Ba"
worksheet.getAutoFilter().custom(0, AsposeCells.FilterOperatorType.Contains, "Ba");

// Refresh the filter to show/hide filtered rows
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outSourseSampleCountryNames.xlsx"));
```

##### **Custom filter with NotContains**

Excel provides custom filters like filter rows which do not contain some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object containing sample data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourseSampleCountryNames.xlsx"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating AutoFilter by giving the cells range
worksheet.getAutoFilter().setRange("A1:A18");

// Initialize filter for rows containing string "Ba"
worksheet.getAutoFilter().custom(0, AsposeCells.FilterOperatorType.NotContains, "Be");

// Refresh the filter to show/hide filtered rows
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outSourseSampleCountryNames.xlsx"));
```

##### **Custom filter with BeginsWith**

Excel provides custom filters like filter rows which begin with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data/");
const outputDir = path.join(__dirname, "output/");

// Instantiating a Workbook object containing sample data
let workbook = new AsposeCells.Workbook(sourceDir + "sourseSampleCountryNames.xlsx");

// Accessing the first worksheet in the Excel file
let worksheet = workbook.getWorksheets().get(0);

// Creating AutoFilter by giving the cells range
worksheet.getAutoFilter().setRange("A1:A18");

// Initialize filter for rows starting with string "Ba"
worksheet.getAutoFilter().custom(0, AsposeCells.FilterOperatorType.BeginsWith, "Ba");

// Refresh the filter to show/hide filtered rows
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(outputDir + "outSourseSampleCountryNames.xlsx");
```

##### **Custom filter with EndsWith**

Excel provides custom filters like filter rows which end with some specific string. This feature is available in Aspose.Cells and demonstrated below by filtering the names in the sample file given below.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data/");
const outputDir = path.join(__dirname, "output/");

// Instantiating a Workbook object containing sample data
const workbook = new AsposeCells.Workbook(sourceDir + "sourseSampleCountryNames.xlsx");

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating AutoFilter by giving the cells range
worksheet.getAutoFilter().setRange("A1:A18");

// Initialize filter for rows end with string "ia"
worksheet.getAutoFilter().custom(0, AsposeCells.FilterOperatorType.BeginsWith, "ia");

// Refresh the filter to show/hide filtered rows
worksheet.getAutoFilter().refresh();

// Saving the modified Excel file
workbook.save(outputDir + "outSourseSampleCountryNames.xlsx");
```

## **Advance topics**
- [Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria](/cells/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Get All Hidden Rows Indices after Refreshing AutoFilter](/cells/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
