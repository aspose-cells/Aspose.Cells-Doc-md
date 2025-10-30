---  
title: Lägg till XML karta i arbetsboken med hjälp av XmlMapCollection.Add metod via Node.js och C++  
linktitle: Lägg till XML karta i arbetsboken med XmlMapCollection.Add metoden  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/  
description: Lär dig hur man lägger till XML karta i arbetsboken med XmlMapCollection.Add metod via Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells tillhandahåller [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) metod som du kan använda för att importera din XML-karta inuti arbetsboken.  

## **Lägg till XML-karta i arbetsboken med XmlMapCollection.Add-metoden**  

Följande exempelkod lägger till XML-karta inuti arbetsboken med hjälp av [**XmlMapCollection.add(string)**](https://reference.aspose.com/cells/nodejs-cpp/xmlmapcollection/#add-string-) metoden och sparar den som [utdata excelfil](5115434.xlsx). Skärmbilden visar den XML-karta som har importerats från [sample.xml](5115433.xml) inuti den resulterande excelfilen.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
