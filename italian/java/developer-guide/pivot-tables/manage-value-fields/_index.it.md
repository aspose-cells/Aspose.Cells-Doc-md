---
title: Gestire i Campi Valore di una Tabella Pivot in Aspose.Cells for Java
linktitle: Gestire i Campi Valore di una Tabella Pivot
description: Scopri come aggiungere campi base all'area dati di una tabella pivot, modificare la funzione di riepilogo con PivotField.Function e posizionare il campo valore sull'asse Riga o Colonna in Aspose.Cells for Java.
keywords: Aspose.Cells, Java, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /it/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiungere un Campo all'Area Dati
Aggiungere un campo base all'area dati (valori) è il primo passo per definire come una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.addFieldToArea(PivotFieldType, String)`, un overload che accetta la costante `PivotFieldType.DATA` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.getDataFields()`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna numerica di origine viene riepilogata con `ConsolidationFunction.SUM`, mentre una colonna non numerica ha come valore predefinito `COUNT`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Intestazioni in A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
// Righe di dati A2:D9 utilizzando cicli annidati che si diramano su j
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
// Aggiungi tabella pivot in F3 con nome PivotTable1
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Layout pivot: Category e Item su Row, Year su Column, Amount come campo dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Modificare la Funzione di Riepilogo
Una volta che un campo risiede nell'area dati, Aspose.Cells lo espone tramite l'oggetto `PivotField` su `PivotTable.DataFields`. Ogni `PivotField` dispone di una proprietà `Function` modificabile di tipo `ConsolidationFunction`, che controlla l'aggregato applicato ai valori sottostanti di quel campo. `ConsolidationFunction` è un'enumerazione con i membri `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`; i primi sei coprono la stragrande maggioranza dei casi d'uso reali, mentre gli ultimi quattro sono aggregati statistici utili per l'analisi della varianza.

{{% alert color="primary" %}}
La modifica di `Function` influisce solo sull'aggregato; la colonna di origine e la struttura di righe/colonne della pivot non vengono modificate. Per cambiare l'aggregato di un campo dati esistente, imposta `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` e quindi richiama `pivotTable.CalculateData()` per ridisegnare la pivot.
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

## Posizionare i Campi Valore sull'Asse Riga o Colonna
Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un ulteriore campo virtuale chiamato `PivotTable.getValuesField()`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot base, operazione utile per disporre più misure fianco a fianco.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` non funziona se non è presente alcun campo valore o se ne è presente solo uno.
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