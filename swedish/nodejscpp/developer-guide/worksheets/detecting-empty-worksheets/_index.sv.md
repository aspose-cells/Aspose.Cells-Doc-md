---  
title: Identifiera tomma kalkylblad med Node.js via C++  
linktitle: Upptäcka tomma kalkylblad  
type: docs  
weight: 410  
url: /sv/nodejs-cpp/detecting-empty-worksheets/  
description: Den här artikeln visar kod som förklarar hur man kan upptäcka tomma kalkylblad i Excel arbetsböcker programmässigt med Node.js API med C++ bibliotek.  
keywords: identifiera tomt kalkylblad Node.js via C++, hitta tomt excel kalkylblad Node.js via C++  
---  

## **Kontrollera Populerade celler**

Kalkylblad kan ha ett eller flera celler fyllda med värden där ett värde kan vara enkelt (text, numeriskt, datum/tid) eller en formel eller ett formelbaserat värde. I så fall är det lätt att upptäcka om ett givet kalkylblad är tomt eller inte. Det vi behöver kontrollera är [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) eller [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) egenskaperna. Om dessa egenskaper returnerar noll eller positiva värden, innebär det att ett eller flera celler har fyllts; dock, om något av dessa egenskaper returnerar -1, indikerar det att inget av cellerna har fyllts i det givna kalkylbladet.

{{% alert color="primary" %}}

Kollektionerna för rader & kolumner har nollbaserade index; därför betyder en cell vid rad 0 och kolumn 0 den första cellen i kalkylbladet, vilket är A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler med värden är automatiskt initialiserade; dock finns det en möjlighet att ett kalkylblad har celler endast med formatering. I ett sådant scenario kommer egenskaperna [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) eller [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) att returnera -1, vilket indikerar att inga fyllda värden finns, men initialiserade celler på grund av cellformatering kan inte upptäckas med denna metod. För att kontrollera om ett kalkylblad har tomma initierade celler rekommenderas att använda `Enumerator.MoveNext`-metoden på enumeratorn som erhållits från [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen. Om `Enumerator.MoveNext`-metoden returnerar **true**, betyder det att det finns en eller flera initialiserade celler i det givna kalkylbladet.

## **Kontrollera former**

Det är möjligt att ett givet kalkylblad inte har några fyllda celler; dock kan det innehålla former & objekt såsom kontroller, diagram, bilder och så vidare. Om vi behöver kontrollera om ett kalkylblad innehåller någon form kan vi göra det genom att inspektera [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--)-egenskapen. Positiva värden indikerar att det finns former i kalkylbladet.

## **Programmeringsexempel**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
