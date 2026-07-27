---
title: Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells per .NET
linktitle: Campi riga e colonna
description: Impara come aggiungere campi di base alle aree righe e colonne di una tabella pivot e controllare i subtotali dei campi pivot usando PivotField.SetSubtotals in Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tabella pivot, campo riga, campo colonna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

I campi riga e colonna sono gli elementi fondamentali di una tabella pivot. Un campo posizionato nell'area righe appare verticalmente a sinistra della pivot, mentre un campo posizionato nell'area colonne appare orizzontalmente nella parte superiore. Questo articolo mostra come aggiungere campi di base a queste aree a livello di codice e come controllare i subtotali visualizzati tra i gruppi di campi utilizzando il metodo `PivotField.SetSubtotals`.

## **Aggiungere un Campo all'Area Righe o Colonne**

Il metodo `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.

- `Row` — campi posizionati verticalmente a sinistra
- `Column` — campi posizionati orizzontalmente nella parte superiore
- `Data` — campi i cui valori sono aggregati
- `Page` — campi usati come filtri del report

Dopo che i campi sono stati aggiunti, è possibile accedervi tramite le proprietà `PivotTable.RowFields` e `PivotTable.ColumnFields`. Ogni proprietà restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `RowFields` è il campo riga più esterno, e gli indici successivi rappresentano campi nidificati al suo interno. La stessa convenzione di indicizzazione si applica a `ColumnFields`.

L'ordine di nidificazione dei campi è importante. Aggiungere prima `Category` all'area righe e poi `Item` produce una pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertendo l'ordine si inverte la gerarchia.

## **Subtotali dei Campi Pivot**

Il metodo `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva/disattiva un singolo tipo di subtotale in modo indipendente. Passare `shown = true` visualizza il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata riguarda un solo tipo, chiamando il metodo più volte con valori diversi di `subtotalType` si costruisce un sottoinsieme personalizzato di subtotali.

L'enum `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.

- `Automatic` — Aspose.Cells sceglie la selezione predefinita (tipicamente `Sum` per i campi numerici)
- `None` — elimina ogni riga di subtotale
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando ci sono due o più campi pivot nell'area righe (o nell'area colonne). Un singolo campo non ha nulla di significativo tra cui calcolare un subtotale, quindi le chiamate a `SetSubtotals` non hanno alcun effetto visibile in tal caso. Questo articolo quindi posiziona due campi riga (`Category` esterno, `Item` interno) in ogni esempio, in modo che il confine del subtotale tra ogni gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali Automatici (Predefiniti)**

Quando non si chiama affatto `SetSubtotals`, Aspose.Cells applica la selezione `Automatic` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sul campo riga esterno `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **Scenario 2 — Eliminare Tutti i Subtotali (None)**

Chiamare `SetSubtotals(PivotFieldSubtotalType.None, true)` rimuove ogni riga di subtotale dalla pivot, lasciando solo le righe dei campi e il totale generale in basso. Questo è utile quando si desiderano i dati raggruppati grezzi senza righe di riepilogo.

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
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
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

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **Scenario 3 — Sottoinsieme di Subtotali Personalizzato (Sum + Average)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `SetSubtotals` opera indipendentemente su un tipo, quindi chiamando il metodo due volte — una con `Sum` e una con `Average` — si produce un sottoinsieme personalizzato di due righe di subtotale per ogni gruppo `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **Riepilogo**

I tre scenari precedenti condividono lo stesso dataset e la stessa struttura di tabella pivot. L'unica differenza tra loro è la chiamata a `SetSubtotals` applicata al campo riga esterno `Category`. Ricorda la regola dei due campi: un singolo campo in un'area non ha nulla tra cui calcolare un subtotale, quindi posiziona sempre almeno due campi nell'area righe o colonne quando desideri che `SetSubtotals` abbia un effetto visibile.

## **Articoli Correlati**

- [Campi Pagina nelle Tabelle Pivot](/cells/it/net/add-page-field-in-pivot-table/)
- [Aggiornamento delle Tabelle Pivot in Aspose.Cells for .NET](/cells/it/net/refresh-pivot-table/)
- [Applicazione degli Stili alle Tabelle Pivot](/cells/it/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
