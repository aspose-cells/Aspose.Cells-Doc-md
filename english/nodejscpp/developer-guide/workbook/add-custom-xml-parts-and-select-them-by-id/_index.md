---  
title: Add Custom XML Parts and Select them by ID with Node.js via C++  
linktitle: Add Custom XML Parts and Select them by ID  
type: docs  
weight: 70  
url: /nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Learn how to add custom XML parts to Excel documents and select them by ID using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Custom XML Parts are the XML data that is stored inside the Microsoft Excel documents and are used by the applications that deal with them. There is no direct way of adding them using Microsoft Excel UI at the moment. However, you can add them programmatically in various ways, e.g., using VSTO, using Aspose.Cells, etc. Please use [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method if you want to add Custom XML Part using Aspose.Cells API. You can also set its ID using the [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--) property. Similarly, if you want to select Custom XML Part by ID, you can use [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method.  

## **Add Custom XML Parts and Select them by ID**  

The following sample code first adds four Custom XML Parts using [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method. It then sets their IDs using [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--) property. Finally, it finds or selects one of the added Custom XML Part using [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method. Please also see the console output of the code given below for reference.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **Console Output**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
