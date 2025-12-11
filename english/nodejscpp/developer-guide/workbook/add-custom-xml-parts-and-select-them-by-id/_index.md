---  
title: Add Custom XML Parts and Select Them by ID with Node.js via C++  
linktitle: Add Custom XML Parts and Select Them by ID  
type: docs  
weight: 70  
url: /nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Learn how to add custom XML parts to Excel documents and select them by ID using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Custom XML Parts are XML data stored inside Microsoft Excel documents and are used by applications that work with them. There is currently no direct way to add them using the Microsoft Excel UI. However, you can add them programmatically in various ways, e.g., using VSTO or Aspose.Cells. Please use [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method if you want to add a Custom XML Part using the Aspose.Cells API. You can also set its ID using the [**CustomXmlPart.setID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#setID--) method. Similarly, if you want to select a Custom XML Part by ID, you can use the [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#selectByID--) method.  

## **Add Custom XML Parts and Select Them by ID**  

The following sample code first adds four Custom XML Parts using the [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) method. It then sets their IDs using the [**CustomXmlPart.setID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#setID--) method. Finally, it finds or selects one of the added Custom XML Parts using the `selectByID` method. Please also see the console output of the code given below for reference.  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of a byte array.
// Please use correct XML and schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom XML parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign IDs to the custom XML parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

 // Specify the search custom XML part ID.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search the custom XML part by the specified ID.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not‑found message on the console.
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
