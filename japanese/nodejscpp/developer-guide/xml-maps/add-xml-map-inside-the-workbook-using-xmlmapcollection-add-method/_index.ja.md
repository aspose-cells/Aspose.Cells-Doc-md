---  
title: XmlMapCollection.Addメソッドを使用して、Node.jsとC++を利用してワークブック内にXMLマップを追加  
linktitle: XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Aspose.Cells for Node.js via C++を用いて、ワークブック内にXMLマップをXmlMapCollection.Addメソッドで追加する方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.CellsはXMLマップをブック内にインポートするために使用できる[**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-)メソッドを提供します。  

## **XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する**  

以下のサンプルコードは、[output excel file](5115434.xlsx)として保存される[サンプル.xml](5115433.xml)からインポートされたXMLマップをブック内に追加する[**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-)メソッドを使用しています。  

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

