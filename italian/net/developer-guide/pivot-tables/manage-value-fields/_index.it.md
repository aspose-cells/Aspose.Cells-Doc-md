---
title: Gestire i campi valore di una tabella pivot in Aspose.Cells for .NET
linktitle: Gestire i campi valore di una tabella pivot
description: Impara ad aggiungere campi base all'area dati di una tabella pivot, a modificare la funzione di riepilogo con PivotField.Function e a posizionare il campo valore sull'asse Riga o Colonna in Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tabella pivot, campo valore, PivotField, PivotField.Function, campo dati, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /it/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Aggiungere un campo all'area dati
Aggiungere un campo base all'area dati (valore) è il primo passo per modellare il modo in cui una tabella pivot aggrega i dati di origine. Aspose.Cells espone `PivotTable.AddFieldToArea(PivotFieldType, string)`, un overload che accetta la costante `PivotFieldType.Data` e il nome della colonna di origine. Una volta aggiunto un campo all'area dati, l'API lo espone tramite la raccolta `PivotTable.DataFields`, nell'ordine in cui i campi sono stati aggiunti. Per impostazione predefinita, una colonna di origine numerica viene sintetizzata con `ConsolidationFunction.Sum`, mentre una colonna non numerica utilizza `Count` come valore predefinito.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}
object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## Modifica della funzione di riepilogo
Una volta che un campo risiede nell'area dati, Aspose.Cells lo espone tramite l'oggetto `PivotField` su `PivotTable.DataFields`. Ogni `PivotField` dispone di una proprietà scrivibile `Function` di tipo `ConsolidationFunction`, che controlla l'aggregato applicato ai valori sottostanti del campo. `ConsolidationFunction` è un'enumerazione con i membri `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` e `Varp`: i primi sei coprono la stragrande maggioranza dei casi d'uso reali, mentre gli ultimi quattro sono aggregati statistici utili per l'analisi della varianza.

{{% alert color="primary" %}}
Modificare `Function` influenza solo l'aggregato; la colonna di origine e la struttura di righe/colonne della pivot non vengono modificate. Per cambiare l'aggregato di un campo dati esistente, impostare `pivotTable.DataFields[i].Function = ConsolidationFunction.<X>;` e quindi chiamare `pivotTable.CalculateData()` per ricalcolare la pivot.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}
object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;
pivotTable.CalculateData();
workbook.Save("output_function.xlsx");
```

## Posizionamento dei campi valore sull'asse Riga o Colonna
Quando una tabella pivot contiene due o più campi dati, Aspose.Cells espone un campo virtuale aggiuntivo denominato `PivotTable.ValuesField`. Questo campo virtuale rappresenta l'aggregato di ogni campo dati presente nell'area dati. È possibile trascinarlo nell'area Riga o Colonna come campo pivot di base, operazione utile per affiancare più misure.

{{% alert color="primary" %}}
`PivotTable.ValuesField` non funziona se non è presente alcun campo valore o se ne è presente uno solo.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}
object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020,  80 },
    { "Fruit",     "Banana", 2021,  90 },
    { "Vegetable", "Carrot", 2020,  50 },
    { "Vegetable", "Carrot", 2021,  60 },
    { "Vegetable", "Daikon", 2020,  40 },
    { "Vegetable", "Daikon", 2021,  45 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.DataFields[1].Function = ConsolidationFunction.Count;
pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);
pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```

{{< app/cells/assistant language="csharp" >}}