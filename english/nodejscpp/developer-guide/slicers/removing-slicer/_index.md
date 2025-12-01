---
title: Removing Slicer with Node.js via C++
linktitle: Removing Slicer
type: docs
weight: 30
url: /nodejs-cpp/removing-slicer/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you want to remove a slicer in Excel, just select it and press the *Delete* button. Similarly, if you want to remove it using Aspose.Cells API programmatically, please use the [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-) method. It will remove the slicer from the worksheet.

## **Removing Slicer**

The following sample code loads the [sample Excel file](67338478.xlsx) that contains an existing slicer. It accesses the slicers and then removes it. Finally, it saves the workbook as [output Excel file](67338477.xlsx). The following screenshot shows the slicer that will be removed after the execution of the sample code.

![todo:image_alt_text](removing-slicer_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
