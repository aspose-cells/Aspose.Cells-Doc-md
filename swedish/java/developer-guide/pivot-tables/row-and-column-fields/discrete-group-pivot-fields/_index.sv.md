---
title: Diskret gruppering av objekt i pivotfält
linktitle: Diskret gruppering
description: Lär dig hur du skapar anpassade grupper av objekt i pivotfält, till exempel frukt och grönsaker, med DiscreteGroupItem och PivotFieldGroupOptions.DiscreteGroupItems i Aspose.Cells for Java.
keywords: Aspose.Cells for Java, pivottabell, diskret gruppering, DiscreteGroupItem, PivotFieldGroupOptions, gruppera objekt i pivotfält, anpassade grupper, PivotField.group, Java, Excel-pivottabell
type: docs
weight: 90
url: /sv/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenier**
- Automatisk gruppering samlar objekt efter datatyp, till exempel datum i månader och kvartal eller tal i intervall. Diskret gruppering löser det motsatta problemet genom att samla specifika, orelaterade objekt i anpassade grupper med egna namn, till exempel produkter i frukt och grönsaker, butiker i regioner eller redovisningskonton i zoner. Aspose.Cells erbjuder diskret gruppering med hjälp av klassen `DiscreteGroupItem` och egenskapen `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- En `DiscreteGroupItem` består av ett gruppnamn och de objekt som ingår i gruppen. Objekten kan identifieras på två sätt: med sina namn (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) eller med sina nollbaserade positioner i källdatan (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Båda formerna ger samma resultat.
- Diskret gruppering tillämpas på ett fält i rad- eller kolumnområdet i pivottabellen genom att skicka alternativobjektet till `PivotField.group(PivotFieldGroupOptions)`.

## **Gruppera objekt i pivotfält efter objektnamn**
Följande exempel bygger en liten försäljningslista (produkt, datum och belopp), skapar en pivottabell från listan med `product` i radområdet, `date` i kolumnområdet och `amount` i dataområdet och definierar sedan två anpassade grupper utifrån objektnamn: frukt (`grape`, `cherry`) och grönsaker (`carrot`, `potato`). Resultatet visar en layout med två nivåer i radområdet, där gruppnamnet utgör den yttre nivån och de ursprungliga objekten är nästlade under den nivån, så att trender kan läsas för varje anpassad grupp och varje objekt.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Efter `calculateData()` visar pivottabellens radområde frukt (`grape` 50, `cherry` 80) och grönsaker (`carrot` 60, `potato` 70), med totalsumman 260. Kolumnrubrikerna behåller de fyra datumen (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Gruppera objekt i pivotfält efter objektindex**
När objektnamnen är långa eller lokaliserade identifierar den andra konstruktören för `DiscreteGroupItem` objekten med index. Indexen är nollbaserade och anger i vilken ordning objekten förekommer i källdatan, inte i alfabetisk ordning. I exempeldata ovan har `grape` index 0, `carrot` index 1, `potato` index 2 och `cherry` index 3, så frukt motsvarar `{ 0, 3 }` och grönsaker `{ 1, 2 }`. Resultatet är detsamma som i det namnbaserade exemplet.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Obs**

{{% alert color="primary" %}}
- Objekt som inte tilldelas någon anpassad grupp tappas inte bort. De stannar i pivottabellen på samma nivå som de anpassade grupperna, som egna poster med ett objekt vardera. I exemplet ovan, där endast fruktgruppen definieras, ligger `carrot` och `potato` kvar i radområdet som fristående poster bredvid fruktgruppen.
- Egenskapen `PivotFieldGroupOptions.getNewPivotField()` styr layouten för diskret gruppering. Standardvärdet är `true`, vilket lägger till det grupperade fältet som ett nytt yttre fält bredvid det ursprungliga och skapar den layout med två nivåer som visas ovan (`getRowFields()` ökar till 2). Ange värdet till `false` med `setNewPivotField(false)` för att i stället ersätta det ursprungliga fältet. Radområdet visar då en enda nivå som endast innehåller gruppnamnen med deras aggregerade värden: frukt 130 (50 + 80) och grönsaker 130 (60 + 70).
- Konstruktorerna för `DiscreteGroupItem` som baseras på namn respektive index kan kombineras i samma `getDiscreteGroupItems()`-array.
{{% /alert %}}

## **Relaterade artiklar**
- [Gruppera pivotfält i pivottabellen](/cells/sv/java/group-pivot-fields-in-the-pivot-table/)
- [Lägg till rad- och kolumnfält i pivottabellen](/cells/sv/java/pivot-table-add-row-and-column-fields/)
- [Filtrera pivottabeller efter etikett eller värde](/cells/sv/java/filter-by-label-or-value-of-pivot-table/)
- [Tillämpa formatering på pivottabellen](/cells/sv/java/apply-style-to-pivot-table/)
- [Uppdatera pivottabellen](/cells/sv/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}