---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati come «frutta» e «verdura», utilizzando DiscreteGroupItem e PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for .NET.
keywords: Aspose.Cells, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.Group, C#, tabella pivot di Excel
type: docs
weight: 90
url: /it/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico organizza gli elementi in base al tipo di dati, ad esempio le date in mesi e trimestri o i numeri in intervalli. Il raggruppamento discreto risolve il problema opposto, raccogliendo elementi specifici e non correlati in gruppi personalizzati, ad esempio i prodotti nei gruppi «frutta» e «verdura», i negozi nelle regioni e i conti nelle zone. Aspose.Cells for .NET offre il raggruppamento discreto tramite la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.DiscreteGroupItems`.
- Un `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che vi appartengono. Gli elementi possono essere identificati in due modi: tramite i rispettivi nomi (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) oppure tramite le rispettive posizioni contate da zero nei dati di origine (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Entrambe le modalità producono lo stesso risultato.
- Il raggruppamento discreto si applica a un campo nell'area delle righe o delle colonne di una tabella pivot, passando le opzioni a `PivotField.Group(PivotFieldGroupOptions)`.

## **Raggruppamento degli elementi dei campi pivot in base ai nomi degli elementi**
L'esempio seguente costruisce un piccolo elenco di vendite (prodotto, data e importo), crea una tabella pivot dall'elenco con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: «frutta» (uva, ciliegia) e «verdura» (carota, patata). Il risultato mostra una struttura a due livelli nell'area delle righe, con il nome del gruppo al livello esterno e gli elementi originali annidati al di sotto, consentendo di individuare le tendenze per ciascun gruppo personalizzato e per ciascun elemento.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

Dopo `CalculateData()`, l'area delle righe della tabella pivot mostra frutta (uva 50, ciliegia 80) e verdura (carota 60, patata 70), con un totale generale di 260, mentre le etichette delle colonne continuano a mostrare le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppamento degli elementi dei campi pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` li identifica tramite i relativi indici. Gli indici rappresentano le posizioni degli elementi contate da zero nell'ordine in cui compaiono nei dati di origine, non in ordine alfabetico. Nei dati di esempio precedenti, uva è l'elemento 0, carota l'elemento 1, patata l'elemento 2 e ciliegia l'elemento 3; pertanto, il gruppo frutta corrisponde a `{ 0, 3 }` e il gruppo verdura a `{ 1, 2 }`. Il risultato è identico all'esempio basato sui nomi.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a alcun gruppo personalizzato non vanno persi. Rimangono nella tabella pivot, allo stesso livello dei gruppi personalizzati, ciascuno come voce autonoma di un solo elemento. Nell'esempio precedente, definendo solo il gruppo «frutta», carota e patata rimangono nell'area delle righe come voci autonome accanto al gruppo «frutta».
- La proprietà `PivotFieldGroupOptions.NewPivotField` controlla la struttura del raggruppamento discreto. Il valore predefinito è `true`; con questo valore la proprietà aggiunge il campo raggruppato come nuovo campo di livello esterno accanto al campo originale, creando la struttura a due livelli mostrata in precedenza (il numero di elementi di `RowFields` aumenta a 2). L'impostazione della proprietà su `false` sostituisce il campo originale; l'area delle righe mostra quindi un singolo livello contenente solo i nomi dei gruppi e i relativi valori aggregati: frutta 130 (50 + 80) e verdura 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere combinati all'interno dello stesso array `DiscreteGroupItems`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppamento dei campi pivot nella tabella pivot](/cells/it/net/group-pivot-fields-in-the-pivot-table/)
- [Aggiunta di campi riga e colonna alla tabella pivot](/cells/it/net/pivot-table-add-row-and-column-fields/)
- [Filtro delle tabelle pivot per etichetta o valore](/cells/it/net/filter-by-label-or-value-of-pivot-table/)
- [Applicazione di uno stile alla tabella pivot](/cells/it/net/apply-style-to-pivot-table/)
- [Aggiornamento della tabella pivot](/cells/it/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}