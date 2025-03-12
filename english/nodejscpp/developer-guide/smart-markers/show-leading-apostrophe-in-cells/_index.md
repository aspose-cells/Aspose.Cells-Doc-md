---  
title: Show leading apostrophe in cells with Node.js via C++  
linktitle: Show leading apostrophe in cells  
type: docs  
weight: 70  
url: /nodejs-cpp/show-leading-apostrophe-in-cells/  
---  

In Microsoft Excel, the leading apostrophe in the cell's value is hidden. Aspose.Cells for Node.js via C++ provides the feature to display the apostrophe by default. For this, the API provides [WorkbookSettings.getQuotePrefixToStyle()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getQuotePrefixToStyle--) property. This property indicates whether to set the [getQuotePrefix()](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) property when entering a string value starting with a single quote to the cell. Setting the [WorkbookSettings.getQuotePrefixToStyle()](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getQuotePrefixToStyle--) property to **false** will display the leading apostrophe in the output Excel file.

The following screenshot shows the output Excel file with the visible apostrophe.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

The following code snippet demonstrates this by adding data with Smart Markers in the source Excel file. The source and output Excel files are attached for reference.

[Source File](98107425.xlsx)

[Output File](98107426.xlsx)  
## **Sample Code**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Instantiating a WorkbookDesigner object
const designer = new AsposeCells.WorkbookDesigner();

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AllowLeadingApostropheSample.xlsx"));
workbook.getSettings().setQuotePrefixToStyle(false);

// Open a designer spreadsheet containing smart markers
designer.setWorkbook(workbook);

const list = [
    { Id: 1, Name: "demo" },
    { Id: 2, Name: "'demo" }
];

// Set the data source for the designer spreadsheet
designer.setDataSource("sampleData", list);

// Process the smart markers
designer.process();

designer.getWorkbook().save(path.join(outputDir, "AllowLeadingApostropheSample_out.xlsx"));
```  

The implementation of *DataObject* class is given below

```javascript
class DataObject {
    constructor() {
        this.id = 0;
        this.name = '';
    }

    get Id() {
        return this.id;
    }

    set Id(value) {
        this.id = value;
    }

    get Name() {
        return this.name;
    }

    set Name(value) {
        this.name = value;
    }
}
```  
  