---  
title: Link Cells to XML Map Elements with Node.js via C++  
linktitle: Link Cells to XML Map Elements  
type: docs  
weight: 50  
url: /nodejs-cpp/link-cells-to-xml-map-elements/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**  

You can link your cells to XML Map elements using Aspose.Cells for Node.js via C++. Please use the [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#linkToXmlMap-string-number-number-string-) method for this purpose.  

## **Link Cells to XML Map Elements**  

The following sample code loads the [source Excel file](5115471.xlsx), which contains an XML map, and then links cells A1, B2, C3, D4, E5, and F6 to XML Map elements FIELD1, FIELD2, FIELD4, FIELD5, FIELD7, and FIELD8, respectively, and then saves the workbook in the [output Excel file](5115467.xlsx).  

If you open the output Excel file and click **Developer > Source**, you will see that the cells are linked to XML Map elements and they will also be highlighted by Microsoft Excel, as shown in this image.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-xml-map.xlsx"));

// Access the Xml Map inside it
const map = workbook.getWorksheets().getXmlMaps().get(0);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Map FIELD1 and FIELD2 to cells A1 and B2
ws.getCells().linkToXmlMap(map.getName(), 0, 0, "/root/row/FIELD1");
ws.getCells().linkToXmlMap(map.getName(), 1, 1, "/root/row/FIELD2");

// Map FIELD4 and FIELD5 to cells C3 and D4
ws.getCells().linkToXmlMap(map.getName(), 2, 2, "/root/row/FIELD4");
ws.getCells().linkToXmlMap(map.getName(), 3, 3, "/root/row/FIELD5");

// Map FIELD7 and FIELD8 to cells E5 and F6
ws.getCells().linkToXmlMap(map.getName(), 4, 4, "/root/row/FIELD7");
ws.getCells().linkToXmlMap(map.getName(), 5, 5, "/root/row/FIELD8");

// Save the workbook in XLSX format
workbook.save(path.join(dataDir, "output.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
