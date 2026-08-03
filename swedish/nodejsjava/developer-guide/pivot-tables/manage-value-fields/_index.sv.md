---
title: Hantera värdefält i en pivottabell i Aspose.Cells för .NET
linktitle: Värdefält
description: Lär dig hur du lägger till basfält i dataregionen i en pivottabell, ändrar sammanfattningsfunktionen med PivotField.Function och placerar värdefältet på rad- eller kolumnaxeln i Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, Node.js via Java, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Summa, Medelvärde
type: docs
weight: 230
url: /sv/nodejs-java/manage-value-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


## Lägga till ett fält i dataregionen

Att lägga till ett basfält i data- (värde-) regionen är det första steget för att forma hur en pivottabell aggregerar dina källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, string)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och källkolonnens namn. När ett fält har lagts till i dataregionen, exponeras det via samlingen `PivotTable.getDataFields()`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard är `COUNT`.

## Ändra sammanfattningsfunktionen

Varje fält som placeras i dataregionen omsluts internt som en `PivotField`-instans, och dess `getFunction()`-egenskap returnerar ett värde från enum-värdet `ConsolidationFunction`. Samma `setFunction()`-setter låter dig växla mellan de tillgängliga aggregaten, inklusive `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` och `VARP`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregatet – källkolumnen ändras inte.
{{% /alert %}}

Du kan alltså lämna ett datafält som `SUM` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `COUNT` eller `AVERAGE`, allt i en enda pivot.

## Placera värdefält på rad- eller kolumnaxeln

När en pivottabell innehåller två eller flera datafält, exponerar Aspose.Cells ett ytterligare virtuellt fält som kallas `PivotTable.getValuesField()`. Detta virtuella fält representerar aggregatet av varje datafält som finns i dataregionen. Du kan dra det till rad- eller kolumnregionen som ett baspivotfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` fungerar inte om det inte finns något eller endast ett värdefält.
{{% /alert %}}

Scenarierna nedan går igenom tre kompletta exempel som demonstrerar varje funktionalitet som beskrivs ovan mot samma pivotstruktur.

## **Dra ett basfält till värdeområdet**

Detta scenario visar hur man placerar ett enskilt basfält (`Amount`) i dataregionen för en befintlig pivottabell. Den delade pivotstrukturen placerar `Category` och `Item` på radaxeln och `Year` på kolumnaxeln. Efter operationen visas `Amount` i dataregionen och beräknas som `Sum` av `Amount` som standard.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Rubriker i A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Datarader A2:D9 med nästlade loopar som grenar på j
for (let i = 1; i <= 8; i++) {
 for (let j = 0; j < 4; j++) {
 switch (j) {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// Lägg till pivottabell vid F3 med namnet PivotTable1
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivotlayout: Category och Item på Rad, Year på Kolumn, Amount som datafält
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## **Ändra sammanfattningsfunktionen**

Detta scenario utgår från samma pivotstruktur sommen lägger till `Amount`-fältet i dataregionen två gånger. Båda datafälten refererar till samma källkolumn, men det andra fältet åsidosätts med hjälp av `PivotField.setFunction()`-settern så att det blir `COUNT` istället för standardvärdet `SUM`.

## **Placera värdefält på rad- eller kolumnaxeln**

Med två datafält på plats blir `PivotTable.getValuesField()` användbar. Detta scenario drar det aggregerade virtuella fältet till kolumnregionen så att varje mått i dataregionen visas som sitt eget kolumnblock bredvid `Year`.

Tillsammans täcker dessa tre scenarier varje aspekt av värdefältsmanipulation i Aspose.Cells for Node.js via Java, från ett enskilt datafält med standardvärdet `SUM` till en pivot med flera mått där det virtuella `ValuesField` styr layouten på rad- eller kolumnaxeln.

{{< app/cells/assistant language="nodejs-java" >}}
