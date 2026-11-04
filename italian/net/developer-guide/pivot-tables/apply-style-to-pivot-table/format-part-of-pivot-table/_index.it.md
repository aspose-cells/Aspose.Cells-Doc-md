---
title: Formattare parte di una Tabella Pivot
description: Formattare parte di una tabella pivot in Aspose.Cells for .NET applicando stili alle regioni semantiche PivotArea o ai rettangoli CellArea tramite PivotTable.Format, con i formati memorizzati in PivotTable.PivotFormats e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, tabella pivot, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /it/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
`PivotTable.FormatAll` applica un unico stile all’intera tabella pivot ed è descritto nella pagina principale. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
Nella pratica, di solito è necessario evidenziare solo una parte della tabella pivot. Gli obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile di cella. Un formato di area pivot rimane collegato a una regione, ad esempio le etichette di un campo o i valori dei dati, e viene ricalcolato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l’intera famiglia di overload di `PivotTable.Format` in modo che siano disponibili entrambi i tipi di formattazione:
- `Format(PivotArea, Style)` collega uno stile a una regione semantica creata con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(CellArea, Style)` collega uno stile a un rettangolo del foglio di lavoro all’interno della tabella pivot.
- `Format(int row, int column, Style)` mira a una singola cella.
- `FormatAll(Style)` formatta l’intera tabella pivot.

## **Formattare un’area Pivot**
Il flusso di lavoro basato su area semantica è l’approccio consigliato quando un evidenziatore deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `new PivotArea(pivotTable)`. L’oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
2. Selezionare un campo tramite la sua posizione zero‑based su un determinato asse con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LabelOnly` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DataOnly` seleziona solo le celle dati del campo.
3. Selezionare un campo per nome con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle valore generate dagli elementi di quel campo.
4. Creare un `Style` con `Workbook.CreateStyle()`, configurarne il carattere, il colore di primo piano e il modello di sfondo solido, e passare lo stile a `PivotTable.Format(area, style)`.
5. Ogni chiamata all’overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.PivotFormats`.
6. I formati ancorati al campo vengono applicati quando i dati pivot vengono calcolati. Pertanto, chiamare `PivotTable.CalculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L’esempio seguente costruisce una piccola tabella pivot di vendite di frutta, applica uno stile alle etichette di riga `Fruit` con `PivotArea.Select` e `PivotTableSelectionType.LabelOnly`, applica uno stile alle celle valore prodotte dallo stesso campo di riga con `PivotArea.SelectField` e quindi ricalcola la tabella pivot affinché entrambi gli stili vengano visualizzati.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Formattare un’area di celle della Tabella Pivot**
Utilizzare `PivotTable.Format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché un’area pivot semantica.  
Un `CellArea` è descritto dalle proprietà `StartRow`, `StartColumn`, `EndRow` e `EndColumn`. I valori sono coordinate zero‑based del foglio di lavoro e le coordinate finali identificano l’ultima riga e colonna incluse nel rettangolo; pertanto l’area comprende le celle dalla posizione di inizio fino a quella di fine, inclusa.  
A differenza di un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessaria un’altra chiamata a `CalculateData()` perché lo stile diventi visibile.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L’esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo e di colore blu‑chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Come le aree Pivot e le aree di celle sono mappate**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile di cella del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, così una richiesta di formattazione viene tradotta in aree pivot al momento della registrazione.  
La relazione tra la `CellArea` fornita dall’utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Una `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta indipendentemente la formattazione delle etichette e quella dei dati.
- Un’area pivot può risolversi in diverse istanze `CellArea` disgiunte. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.GetCellAreas()` restituisce una collezione anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.Format` è registrata in `PivotTable.PivotFormats`. Ogni voce `PivotTableFormat` espone il `PivotArea` associato e lo `Style` applicato. L’overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre una `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone i flag `OnlyLabel` e `OnlyData`. L’esempio sottostante formatta un singolo rettangolo che copre sia etichette sia valori, ispeziona `PivotTable.PivotFormats` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come normali stili di cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `PivotTable.RefreshData`, ricalcolata con `CalculateData` o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e il suo stile viene riapplicato.
{{% /alert %}}

Utilizzare un `PivotArea` costruito con `Select` o `SelectField` quando un evidenziatore deve rimanere ancorato a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout attuale della tabella pivot. L’overload `Format(int row, int column, Style)` per singola cella mira a una cella individuale. Usare `FormatAll`, descritto nella pagina principale, quando l’intera tabella pivot deve essere riformattata in un’unica operazione.

## **Articoli correlati**
- [Applicare stile alla Tabella Pivot](/cells/it/net/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla Tabella Pivot](/cells/it/net/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella Tabella Pivot](/cells/it/net/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}