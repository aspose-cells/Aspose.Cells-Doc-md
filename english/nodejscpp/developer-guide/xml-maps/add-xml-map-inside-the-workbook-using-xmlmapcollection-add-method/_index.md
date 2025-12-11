---  
title: Add XML Map inside the Workbook using XmlMapCollection.Add method with Node.js via C++  
linktitle: Add XML Map inside the Workbook using XmlMapCollection.Add method  
type: docs  
weight: 10  
url: /nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Learn how to add an XML map into the workbook using the XmlMapCollection.Add method with Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Aspose.Cells provides the [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) method, which you can use to import an XML map into a workbook.  

## **Add XML Map inside the Workbook using XmlMapCollection.Add method**  

The following sample code adds an XML map into the workbook using the [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) method and saves it as an output Excel file ([output.xlsx](5115434.xlsx)). The screenshot shows the XML map that has been imported from [sample.xml](5115433.xml) into the output Excel file.  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add XML map from sample.xml into the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in XLSX format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
