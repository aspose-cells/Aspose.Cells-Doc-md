---  
title: XML Karte in die Arbeitsmappe mit der XmlMapCollection.Add Methode in Node.js via C++ einfügen  
linktitle: XML Map innerhalb der Arbeitsmappe mit der XmlMapCollection.Add Methode hinzufügen  
type: docs  
weight: 10  
url: /de/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Erfahren Sie, wie Sie eine XML Karte in die Arbeitsmappe mit der XmlMapCollection.Add Methode in Aspose.Cells for Node.js via C++ einfügen.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells bietet die Methode [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-), die Sie verwenden können, um Ihre XML-Map in die Arbeitsmappe zu importieren.  

## **XML Map innerhalb der Arbeitsmappe mit der XmlMapCollection.Add Methode hinzufügen**  

Der folgende Beispielcode fügt mithilfe der Methode [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) eine XML-Map in die Arbeitsmappe ein und speichert sie als [Ausgabedatei](5115434.xlsx). Der Screenshot zeigt die XML-Map, die aus [sample.xml](5115433.xml) in die Ausgabedatei importiert wurde.  

![add-xml-map](add-xml-map.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Add xml map found inside the sample.xml inside the workbook
wb.getWorksheets().getXmlMaps().add(path.join(dataDir, "sample.xml"));

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```  

