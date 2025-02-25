---
title: Get Range with External Links using Node.js via C++
linktitle: Get Range with External Links
type: docs
weight: 120
url: /nodejs-cpp/get-range-with-external-links/
description: Learn how to get ranges with external links using Aspose.Cells for Node.js via C++. Retrieve data from different Excel files efficiently.
---

## **Get Range with External Links**

A lot of times Excel files access data from other Excel files using external links. Aspose.Cells for Node.js via C++ provides the option to retrieve these external links by using the [**Name.getReferredAreas**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas) method. The [**Name.getReferredAreas**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). The [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) class provides an [**externalFileName**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#externalFileName) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) class exposes the following members.

- [**endColumn**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#endColumn): The end column of the area
- [**endRow**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#endRow): The end row of the area
- [**externalFileName**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#externalFileName): Get the external file name if this is an external reference
- [**isArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea): Indicates whether this is an area
- [**isExternalLink**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink): Indicates whether this is an external link
- [**sheetName**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#sheetName): Indicates which sheet this reference is in
- [**startColumn**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#startColumn): The start column of the area
- [**startRow**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#startRow): The start row of the area

The sample code given below demonstrates the use of [**Name.getReferredAreas**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas) method to get Ranges with external links.

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const names = workbook.getWorksheets().getNames();
names.forEach(namedRange => {
    const referredAreas = namedRange.getReferredAreas(true);
    if (referredAreas) {
        referredAreas.forEach(referredArea => {
            // Print the data in Referred Area
            console.log("IsExternalLink: " + referredArea.isExternalLink());
            console.log("IsArea: " + referredArea.isArea());
            console.log("SheetName: " + referredArea.getSheetName());
            console.log("ExternalFileName: " + referredArea.getExternalFileName());
            console.log("StartColumn: " + referredArea.getStartColumn());
            console.log("StartRow: " + referredArea.getStartRow());
            console.log("EndColumn: " + referredArea.getEndColumn());
            console.log("EndRow: " + referredArea.getEndRow());
        });
    }
});
```
