---
title: Värdefält i Aspose.Cells for Java
linktitle: Värdefält i Aspose.Cells for Java
description: Lär dig hur du lägger till basfält i dataområdet i en pivottabell, ändrar sammanfattningsfunktionen med PivotField.Function och placerar värdefältet på Rad- eller Kolumn-axeln i Aspose.Cells for Java.
keywords: Aspose.Cells, Java, pivottabell, värdefält, PivotField, PivotField.Function, datafält, PivotTable.ValuesField, Summa, Medel
type: docs
weight: 230
url: /sv/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Lägga till ett fält i dataområdet

Att lägga till ett basfält i data- (värde-) området är det första steget i att forma hur en pivottabell aggregerar din källdata. Aspose.Cells exponerar `PivotTable.addFieldToArea(PivotFieldType, String)`, en överlagring som accepterar konstanten `PivotFieldType.DATA` och namnet på källkolumnen. När ett fält har lagts till i dataområdet exponeras det via samlingen `PivotTable.getDataFields()`, i den ordning som fälten lades till. Som standard sammanfattas en numerisk källkolumn med `ConsolidationFunction.SUM`, medan en icke-numerisk kolumn som standard blir `COUNT`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Rubriker i A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// Datarader A2:D9 med kapslade slingor som förgrenar sig på j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
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
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivotlayout: Kategori och Objekt på Rad, År på Kolumn, Belopp som datafält
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Ändra sammanfattningsfunktionen

Varje fält som placeras i dataområdet är internt inpackat som en `PivotField`-instans, och dess `getFunction()`-egenskap returnerar ett värde från `ConsolidationFunction`-uppräkningen. Samma `setFunction(...)`-setter låter dig växla mellan de tillgängliga aggregeringarna, inklusive `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` och `VARP`.

{{% alert color="primary" %}}
Att ändra `Function` påverkar bara aggregeringen, källkolumnen ändras inte.
{{% /alert %}}
Du kan därför låta ett datafält vara `SUM` medan du lägger till ett andra datafält som riktar sig mot samma källkolumn men använder `COUNT` eller `AVERAGE`, allt i en enda pivot.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");

pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField countField = pivotTable.getDataFields().get(1);
countField.setFunction(ConsolidationFunction.COUNT);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Placera värdefält på Rad- eller Kolumn-axeln

När en pivottabell innehåller två eller flera datafält, exponerar Aspose.Cells ett ytterligare virtuellt fält som heter `PivotTable.getValuesField()`. Detta virtuella fält representerar aggregeringen av varje datafält som finns i dataområdet. Du kan dra det till Rad- eller Kolumn-området som ett pivotbasfält, vilket är användbart för att lägga ut flera mått sida vid sida.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` fungerar inte om det inte finns något eller bara ett värdefält.
{{% /alert %}}
Scenarierna nedan går igenom tre kompletta exempel som demonstrerar varje funktion som beskrivs ovan mot samma pivotstruktur.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="java" >}}