---  
title: Добавьте XML карту внутри книги с помощью метода XmlMapCollection.Add через Node.js и C++  
linktitle: Добавить XML отображение внутри книги с использованием метода XmlMapCollection.Add  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Узнайте, как добавлять XML карту внутри книги с помощью метода XmlMapCollection.Add с Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells предоставляет метод [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-), который вы можете использовать для импорта вашей XML-схемы внутри книги.  

## **Добавить XML-отображение внутри книги с использованием метода XmlMapCollection.Add**  

В следующем образце кода добавляется XML-схема внутри книги с помощью метода [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) и сохраняется как [файл Excel вывода](5115434.xlsx). На скриншоте показана XML-схема, которая была импортирована из [sample.xml](5115433.xml) в файл Excel вывода.  

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

