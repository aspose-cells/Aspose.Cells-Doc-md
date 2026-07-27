---
title: Gestire I campi valore di una tabella pivot in Aspose.Cells per Java
linktitle: Gestire I campi valore
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e tracciare il campo valore sugli assi Riga o Colonna in Aspose.Cells per Java.
keywords: Aspose.Cells, Java, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.getValuesField, Sum, Average
type: docs
weight: 230
url: /it/java/pivot-table-manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiungere un campo all'area dati

Aggiungere un campo base all'area dati (dei valori) è il primo passo per modellare il modo in cui una tabella pivot aggrega i dati di origine. Aspose.Cells espone PivotTable.addFieldToArea(PivotFieldType, string), un overload che accetta la costante PivotFieldType.DATA e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone attraverso la collezione PivotTable.getDataFields, nell'ordine in cui I campi sono stati aggiunti. Per impostazionè predefinita, una colonna numerica viene riepilogata con Sum, mentre una colonna non numerica è predefinita su Count.

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
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};

for (int i = 0; i < data.length; i++) {
    for (int j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Modificare la funzione di riepilogo

Ogni campo collocato nell'area dati è incapsulato internamente come istanza di PivotField, e la sua proprieta Function restituisce un valore dall'enum ConsolidationFunction. Lo stesso setter Function consente di passare tra gli aggregati disponibili, inclusi Sum, Count, Average, Max, Min, Product, StdDev, StdDevp, Var e Varp.

{{% alert color="primary" %}}
Modificare Function influisce solo sull'aggregato; la colonna di originè non cambia. È quindi possibile lasciare un campo dati come Sum mentre un secondo campo dati punta alla stessa colonna di origine ma usa Count o Average, tutto in un unica tabella pivot.
{{% /alert %}}

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
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};

for (int i = 0; i < data.length; i++) {
    for (int j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
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

## Tracciare I campi valore sugli assi Riga o Colonna

Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo chiamato PivotTable.getValuesField. Questo campo virtuale rappresenta l'aggregato di ogni campo dati che risiedè nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot base, utile per disporre più misure affiancate.

{{% alert color="primary" %}}
PivotTable.getValuesField non funziona sè non ci sono campi valore o se cè n e solo uno.
{{% /alert %}}

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
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};

for (int i = 0; i < data.length; i++) {
    for (int j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField().getName());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

## Related Articles

- [Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET](/cells/net/pivot-table-add-row-column-fields/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET](/cells/net/add-filter-field-in-pivot-table/)
- [Aggiornare tabelle pivot e cache pivot in Aspose.Cells per .NET](/cells/net/refresh-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells per .NET](/cells/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="java" >}}
