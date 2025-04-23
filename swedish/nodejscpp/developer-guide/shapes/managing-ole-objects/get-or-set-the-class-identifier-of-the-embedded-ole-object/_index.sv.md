---  
title: Hämta eller ange klassidentifikatorn för det inbäddade OLE objektet med Node.js via C++  
linktitle: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet  
type: docs  
weight: 200  
url: /sv/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Lär dig hur du hämtar eller sätter klassidentifikatorn för inbäddade OLE objekt i Node.js med Aspose.Cells via C++.  
---  

## **Möjliga användningsscenario**  
Aspose.Cells tillhandahåller egenskapen [OleObject.getClassIdentifier()](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getClassIdentifier--) som du kan använda för att få eller ange klassidentifikatorn för ett inbäddat OLE-objekt. OLE-objektets klassidentifikatorer är i själva verket GUIDs, dvs. Globally Unique Identifiers. GUID är alltid 16 byte lång; därför är även klassidentifierare 16 byte långa. De finns ofta i Windows-registret och ger information till värdapplikationen om hur man öppnar inbäddade OLE-objekt som innehåller olika inbäddade resurser i klientapplikationen.

## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**  
Följande skärmbild visar klassidentifikatorn för OLE-objektet, dvs. GUID, som har lästs från [exempel-Excelfilen](5115190.xls) som innehåller det inbäddade PowerPoint OLE-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Exempelkod**  
Se följande exempel på kod som körs med [exempel-Excelfilen](5115190.xls) och dess konsolutmatning, vilken visar klassidentifieraren för OLE-objektet dvs. GUID. Den utskrivna GUID är exakt densamma som visas i skärmbilden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your sample workbook which contains embedded PowerPoint ole object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xls"));

// Access its first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first ole object inside the worksheet
const oleObject = worksheet.getOleObjects().get(0);

// Convert 16-bytes array into GUID
const guid = new Uint8Array(oleObject.getClassIdentifier()).reduce((acc, byte) => acc + String.fromCharCode(byte), '');

// Print the GUID
console.log(guid.toUpperCase());
```  
### **Konsoloutput**  
Detta är konsolutmatningen av ovanstående exempel på kod när det körs med [exempel-Excelfilen](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}  

