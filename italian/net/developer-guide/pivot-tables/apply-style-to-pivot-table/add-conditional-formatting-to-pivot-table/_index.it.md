---
title: Aggiungere la formattazione condizionale a una Tabella Pivot
linktitle: Aggiungere la formattazione condizionale a una Tabella Pivot
description: Aggiungere la formattazione condizionale a una tabella pivot in Aspose.Cells for .NET - ancorare una regola all'intervallo dati con ApplyTo e un ambito PivotConditionFormatScopeType, oppure definire l'obiettivo con AddCellArea e PivotAreas, quindi collegare regole e stili tramite FormatConditions.AddCondition.
keywords: Aspose.Cells, tabella pivot, formattazione condizionale, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /it/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Gli stili descritti nella pagina padre e nella pagina sorella sono statici – un intervallo `PivotArea` o `CellArea` viene dipinto una volta e mantiene il suo stile indipendentemente dai valori. La formattazione condizionale è il corrispettivo basato su regole – evidenziare ogni importo superiore a 200, colorare la metà centrale per il cinquanta percento, o segnalare gli elementi con classifica più bassa – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale delle tabelle pivot risiede nella collezione `PivotTable.ConditionalFormats`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** La regione di destinazione è definita tramite `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, oppure tramite `AddCellArea(CellArea)` e la collezione `PivotAreas`, che nominano esplicitamente la regione.
- **Cosa testa la regola?** Uno o più condizioni sono aggiunte a `FormatConditions` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, e ogni condizione possiede il proprio `Style`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` o `FormatConditionCollection.AddArea(CellArea)` sull'oggetto `FormatConditions` di un formato condizionale pivot. Queste due overload sono ereditate dall'API di formattazione condizionale del foglio di lavoro ordinario e non funzionano per le tabelle pivot – l'area cella non viene mai convertita in un'area pivot, quindi la richiesta viene ignorata silenziosamente. Definisci sempre la regione sul `PivotConditionalFormat` stesso (`ApplyTo`, `AddCellArea` o `PivotAreas`) e aggiungi la regola con una delle overload `AddCondition`.
{{% /alert %}}

## **Applicare una regola con un ambito (modo UI di Excel)**
La prima modalità posiziona la regola come fa l'interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate del foglio di lavoro a base zero, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a che punto la regola deve estendersi da quella cella:
- `PivotConditionFormatScopeType.Data` – tutte le celle valore prodotte dalla tabella pivot, inclusi i totali generali.
- `PivotConditionFormatScopeType.Field` – le celle valore appartenenti al campo identificato dalla cella, escludendo i totali generali. La cella deve essere una cella di campo, ad esempio un'etichetta di campo di riga; fornire una cella valore genera un'eccezione.
- `PivotConditionFormatScopeType.Selection` – solo le celle valore all'intersezione selezionata dalla cella, tipicamente una singola cella valore.
L'esempio seguente crea una tabella pivot di vendite di frutta con l'angolo in alto a sinistra in E3, ancorando una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l'ambito `Data`, e evidenzia ogni importo superiore a 200 in bianco grassetto su rosso. Con i valori Apple 220, Banana 330, Cherry 200 e il totale generale 750, la regola colora F4, F5 e F7 – la regione risolta è l'intera colonna dei dati F4:F7, e solo le celle il cui valore soddisfa la regola si illuminano.

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
// Tabella pivot con l'angolo in alto a sinistra in E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Fissa il formato condizionale a F4 (riga 3, colonna 5) con l'ambito Dati
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Regola - evidenzia i valori superiori a 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

Ancorare la stessa regola sull'etichetta di campo riga E4 (riga 3, colonna 4) con l'ambito `Field` risulta in F4:F6 invece – la stessa colonna dei dati senza la riga del totale generale – perché l'ambito ora descrive il campo `Fruit` anziché l'intera area dei valori. L'ambito `Selection` ancorato a F4 risulta solo in F4.

## **Definire la regione manualmente**
Il secondo metodo evita il selettore di ambito e nomina la regione esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con AddCellArea**
`AddCellArea(CellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono a base zero del foglio di lavoro, e la regione è esattamente il rettangolo fornito – nessuna espansione alla colonna dei dati e nessuna logica di totale generale. Usalo quando le celle di interesse sono un rettangolo fisso noto del layout pivot corrente.

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
// Seleziona il rettangolo F4:F6 (le celle di valore senza il totale generale)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Regola - corsivo su giallo chiaro per importi tra 150 e 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **Una regione pivot semantica con PivotAreas**
`PivotAreas` è lo stesso modello di regione semantica usato dalla pagina sorella per gli stili statici. Costruisci un `PivotArea`, seleziona un campo o una regione con `Select` o `SelectField`, e aggiungilo con `PivotAreas.AddPivotArea(PivotArea)`. Una regione semantica rimane collegata al suo campo, così la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout cambia. L'overload `PivotAreas.Add(PivotArea)` compila ancora ma è contrassegnato come obsoleto – preferisci `AddPivotArea`.

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
// Allega la regola al campo dati Amount come area semantica
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Regola - testo grigio per importi inferiori a 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dove sono memorizzate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata a `ConditionalFormats.Add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file nell'esempio seguente mostra la stessa regola con il suo tipo, operatore e formula intatti, e `GetCellAreas()` restituisce le stesse regioni. Le voci che non hanno mai ricevuto una condizione vengono eliminate al salvataggio della cartella di lavoro, nello stesso modo in cui Excel elimina una formattazione condizionale priva di regola.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// Questo stampa:
// Formati condizionali: 1
// Formato 0: CellValue GreaterThan formula1==200
//     righe 4-7, colonne 6-6        (F4:F7, l'area dati risolta)
```

## **Articoli correlati**
- [Applicare stile a una Tabella Pivot](/cells/it/net/apply-style-to-pivot-table/)
- [Formattare parte di una Tabella Pivot](/cells/it/net/format-part-of-pivot-table/)
- [Mostrare o filtrare i primi 10 in una Tabella Pivot](/cells/it/net/top-10-show-or-filter-in-pivot-table/)
- [Filtrare le Tabelle Pivot per etichetta o valore](/cells/it/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}