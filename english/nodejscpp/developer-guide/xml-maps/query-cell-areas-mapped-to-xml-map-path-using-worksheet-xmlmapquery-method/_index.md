---
title: Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method with Node.js via C++
linktitle: Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method
type: docs
weight: 60
url: /nodejs-cpp/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Possible Usage Scenarios**

You can query cell areas mapped to the XML map path with Aspose.Cells for Node.js via C++ using the [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/xmlmapquery) method. If the path exists, it will return the list of cell areas related to that path inside the XML map. The first parameter of the [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/xmlmapquery) method specifies the XML element path and the second parameter specifies an XML map you want to query.

## **Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method**

The following screenshot shows Microsoft Excel displaying XML Map inside the [sample Excel file](55541790.xlsx) used in the code. The code queries the XML map two times and prints the list of cell areas returned by the [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/xmlmapquery) method on the console as shown below.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleXmlMapQuery.xlsx");

// Load sample Excel file having Xml Map
const wb = new AsposeCells.Workbook(filePath);

// Access first XML Map
const xmap = wb.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Query Xml Map from Path - /MiscData
console.log("Query Xml Map from Path - /MiscData");
let ret = ws.XmlMapQuery("/MiscData", xmap);

// Print returned ArrayList values
for (let i = 0; i < ret.length; i++) {
    console.log(ret[i]);
}

console.log("");

// Query Xml Map from Path - /MiscData/row/Color
console.log("Query Xml Map from Path - /MiscData/row/Color");
ret = ws.XmlMapQuery("/MiscData/row/Color", xmap);

// Print returned ArrayList values
for (let i = 0; i < ret.length; i++) {
    console.log(ret[i]);
}
```

### **Console Output**

{{< highlight javascript >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Get XML path from List Object/Table**

XML data can be imported to worksheets. Sometimes XML path is required from the ListObjects of the worksheet. This feature is available in Excel by using an expression like Sheet1.ListObjects(1).XmlMap.DataBinding. The same feature is available in Aspose.Cells for Node.js via C++ by calling [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/nodejs-cpp/listobject/properties/xmlmap).  The following example demonstrates this feature. Template file and other source files can be downloaded from the following links:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "XML Data.xlsx");
// Load XLSX file containing data from XML file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const ws = workbook.getWorksheets().get(0);

// Access ListObject from the first sheet
const listObject = ws.getListObjects().get(0);

// Get the url of the list object's xml map data binding
const url = listObject.getXmlMap().getDataBinding().getUrl();

// Display XML file name
console.log(url);
```
