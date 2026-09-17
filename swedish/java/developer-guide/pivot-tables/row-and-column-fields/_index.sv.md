---
title: Lägg till rad- och kolumnfält i pivottabeller med Aspose.Cells for Java
description: Lär dig hur du lägger till basfält i rad- och kolumnområdena för en pivottabell och styr pivotfältets delsummor med PivotField.setSubtotals i Aspose.Cells for Java.
linktitle: Rad- och kolumnfält
keywords: Aspose.Cells, Java, pivottabell, radfält, kolumnfält, PivotField, setSubtotals, PivotFieldSubtotalType, delsummor
type: docs
weight: 220
url: /sv/java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Lägga till ett fält i rad- eller kolumnområdet**
Metoden `PivotTable.addFieldToArea(int fieldType, String fieldName)` flyttar ett basfält från källdatan till en av de fyra pivotområdena. Argumentet `fieldType` accepterar något av följande `PivotFieldType`-värden.
- `ROW` — fält placerade vertikalt till vänster
- `COLUMN` — fält placerade horisontellt överst
- `DATA` — fält vars värden aggregeras
- `PAGE` — fält som används som rapportfilter
Ordningen på fältnästning spelar roll. Att lägga till `Category` i radområdet först och sedan `Item` ger en pivottabell vars yttre gruppering är `Category` och vars inre gruppering är `Item`. Att vända ordningen vänder hierarkin.

## **Delsummor för pivotfält**
Metoden `PivotField.setSubtotals(int subtotalType, boolean shown)` styr vilka delsummarader som visas för ett pivotfält. Varje anrop växlar en enskild delsummatyp oberoende. Att skicka `shown = true` visar delsummoraden, medan `shown = false` döljer den. Eftersom varje anrop endast påverkar en typ, bygger upprepade anrop med olika `subtotalType`-värden en anpassad delmängd av delsummor.
Enumerationen `PivotFieldSubtotalType` definierar de tillgängliga delsummatyperna.
- `AUTOMATIC` — Aspose.Cells väljer standardvalet (vanligtvis `SUM` för numeriska fält)
- `NONE` — undertryck varje delsummarad
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Delsummor renderas endast när det finns två eller fler pivotfält i radområdet (eller i kolumnområdet). Ett enskilt fält ger inte upphov till meningsfulla delsummor, så `setSubtotals`-anrop har ingen synlig effekt i det fallet. Den här artikeln placerar därför två radfält (`Category` ytter, `Item` inner) i varje exempel så att delsummegränsen mellan varje `Category`-grupp är synlig.
{{% /alert %}}

## **Scenario 1 — Automatiska (standard) delsummor**
När du inte anropar `setSubtotals` alls, tillämpar Aspose.Cells `AUTOMATIC`-valet på numeriska fält. Följande exempel bekräftar uttryckligen detta beteende genom att anropa `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` på det yttre `Category`-radfältet.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Undertrycka alla delsummor (ingen)**
Att anropa `setSubtotals(PivotFieldSubtotalType.NONE, true)` tar bort varje delsummarad från pivottabellen och lämnar endast fältraderna och totalsumman längst ner. Detta är användbart när du vill ha den råa grupperade datan utan några summarader.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Scenario 3 — Anpassad delsummeuppsättning (Summa + Medelvärde)**
Du är inte begränsad till en enskild delsummatyp. Varje `setSubtotals`-anrop fungerar oberoende på en typ, så att anropa metoden två gånger — en gång med `SUM` och en gång med `AVERAGE` — ger en anpassad delmängd av två delsummarader för varje `Category`-grupp.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTableCollection pivotTables = worksheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Sammanfattning**

## **Relaterade artiklar**
- [Sidfält i pivottabeller](/cells/sv/java/add-page-field-in-pivot-table/)
- [Uppdatera pivottabeller i Aspose.Cells for Java](/cells/sv/java/refresh-pivot-table/)
- [Tillämpa stilar på pivottabeller](/cells/sv/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}