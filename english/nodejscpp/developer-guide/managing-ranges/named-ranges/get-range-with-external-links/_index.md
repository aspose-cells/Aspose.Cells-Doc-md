---
title: Get Range with External Links using Node.js via C++
linktitle: Get Range with External Links
type: docs
weight: 120
url: /nodejs-cpp/get-range-with-external-links/
description: Learn how to get ranges with external links using Aspose.Cells for Node.js via C++. Retrieve data from different Excel files efficiently.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Get Range with External Links**

Often Excel files access data from other Excel files using external links. Aspose.Cells for Node.js via C++ provides the option to retrieve these external links by using the [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) method. The [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) method returns an array of type [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). The [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) class provides a [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--) property which returns the name of the external file. The [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) class exposes the following members.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): The end column of the area
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): The end row of the area
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Get the external file name if this is an external reference
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Indicates whether this is an area
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Indicates whether this is an external link
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Indicates the sheet this reference is in
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): The start column of the area
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): The start row of the area

The sample code given below demonstrates the use of the [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) method to get ranges with external links.

## **Sample Code**

```javascript
try 
{
    const path = require("path");
    const AsposeCells = require("aspose.cells.node");

    // Source directory
    const sourceDir = path.join(__dirname, "data");

    // Load source Excel file
    const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
    const workbook = new AsposeCells.Workbook(filePath);
    console.log(filePath);
    const names = workbook.getWorksheets().getNames();
    const namesCount = names.getCount();
    for (let i = 0; i < namesCount; i++) 
    {
        const namedRange = names.get(i);
        const referredAreas = namedRange.getReferredAreas(true);
        if (referredAreas) 
        {
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
    }
}
catch (e) 
{
    console.error(e);
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
