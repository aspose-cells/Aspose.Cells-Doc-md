---  
title: Lägg till anpassade XML delar och välj dem efter ID med Node.js via C++  
linktitle: Lägg till anpassade XML delar och välj dem efter ID  
type: docs  
weight: 70  
url: /sv/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Lär dig hur du lägger till anpassade XML delar till Excel dokument och väljer dem efter ID med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Anpassade XML-delar är XML-data som lagras i Microsoft Exceldokument och används av de applikationer som hanterar dem. Det finns ingen direkt metod för att lägga till dem med Microsoft Excels användargränssnitt för närvarande. Du kan dock lägga till dem programmässigt på olika sätt, t.ex. med VSTO, med Aspose.Cells, etc. Använd [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-metoden om du vill lägga till en anpassad XML-del med Aspose.Cells API. Du kan också ställa in dess ID med hjälp av [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)-egenskapen. På liknande sätt, om du vill välja en anpassad XML-del efter ID, kan du använda [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-metoden.  

## **Lägg till anpassade XML-delar och välj dem efter ID**  

Följande exempelkod lägger först till fyra anpassade XML-delar med [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-metoden. Den ställer sedan in deras ID:n med [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)-egenskapen. Slutligen hittar eller markerar den en av de tillagda anpassade XML-delarna med [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-metoden. Se även kodens konsolutmatning nedan för referens.  

## **Exempelkod**  

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

## **Konsoloutput**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
