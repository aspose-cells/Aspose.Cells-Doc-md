---
title: Applicazione degli stili alle tabelle pivot
linktitle: Applicazione degli stili
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for .NET, coprendo autoformati legacy XLS, stili denominati moderni di Excel 2007+, stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells .NET stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta l'applicazione sia degli autoformati legacy per tabelle pivot (destinati ai file `.xls`) sia degli stili moderni denominati o personalizzati per tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui la si legge. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.

Per l'output `.xls` legacy, utilizzare la proprietà `PivotTable.AutoFormatType` insieme all'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Questa API corrisponde al selettore di autoformato che la versione classica di Excel offriva per le tabelle pivot.

Per l'output `.xlsx`, `.xlsm` e `.xlsb` moderni, sono disponibili due varianti dell'API di stile:

- `PivotTable.PivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono in sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Gli stili personalizzati sono necessari quando si desidera modificare colori, bordi o caratteri oltre quanto offerto dai preset.

Inoltre, `PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della pivot, sovrascrivendo qualsiasi impostazione effettuata tramite entrambe le API di nome stile sopra descritte. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare un autoformato preset legacy XLS**

`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili sono `Report1` fino a `Report10`, `Classic` e `Table1` fino a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa proprietà e ricorre alle impostazioni `PivotTableStyleType` e `PivotTableStyleName`.

{{% /alert %}}

L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.Report5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}

**Perché nessun campo colonna?** Gli autoformati della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) erano progettati in Excel classico per **tabelle pivot monodimensionali** con soli campi riga e valori — non hanno uno stile integrato per le intestazioni dei campi colonna. Se la tua tabella pivot richiede campi colonna, usa i preset moderni `PivotTableStyleType` dello Scenario 2 qui sotto, progettati per il layout bidimensionale usato da Excel moderno.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 1: Applica un formato automatico preimpostato XLS legacy
// API in uso: PivotTable.AutoFormatType
// Formato file di destinazione: .xls (legacy)
// Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();

// Ottieni il primo foglio di lavoro
Worksheet sheet = workbook.Worksheets[0];

// Popola i dati di origine con una riga di intestazione (Fruit, Year, Amount)
// e 9 righe di dati che coprono grape, blueberry, kiwi, cherry negli anni 2020 e 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", usando l'intervallo di origine A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Assegna i campi: Fruit -> Righe, Year -> Colonne, Amount -> Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Applica il formato automatico preimpostato XLS legacy "Report5"
// Nota: questa proprietà è significativa solo quando si salva come .xls.
// Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// e utilizza ciò che specifica PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Salva la cartella di lavoro nel formato .xls legacy
workbook.Save("output.xls");
```

## **Applicare uno stile preset denominato moderno per tabelle pivot**

`PivotTable.PivotTableStyleType` accetta un valore dall'enumerazione `Aspose.Cells.PivotTableStyleType`. L'enumerazione copre i temi chiari `PivotTableStyleLight1` fino a `PivotTableStyleLight28` e i temi scuri `PivotTableStyleDark1` fino a `PivotTableStyleDark28`. Gli stili aggiunti in Excel 2017 (la seconda ondata di temi chiari e scuri) sono raggiungibili tramite la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza dell'autoformato legacy, lo stile qui selezionato viene reso fedelmente da Excel e sopravvive ai round-trip attraverso altri strumenti Office.

L'esempio seguente utilizza gli stessi dati Frutto/Anno/Importo, crea una tabella pivot identica, applica `PivotTableStyleDark1` e salva la cartella di lavoro come `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 2: Applica uno stile preimpostato denominato moderno di Excel 2007+ utilizzando PivotTableStyleType.
// Formato del file di destinazione: .xlsx. L'enum PivotTableStyleType si trova nel namespace Aspose.Cells
// (non in Aspose.Cells.Pivot) — ecco perché non abbiamo bisogno di alcuna using aggiuntiva per esso.
// Riferimento GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Riga di intestazione: Frutta / Anno / Importo
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 righe di dati di Frutta / Anno / Importo
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// Aggiungi una tabella pivot in E3 denominata "Pivot1", con origine da A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assegna i campi pivot: Frutta -> area Righe, Anno -> area Colonne, Importo -> area Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Applica uno stile pivot preimpostato denominato moderno di Excel 2007+.
// PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
// viene ignorato da Excel per questi formati. PivotTableStyleDark1 appartiene alla famiglia del tema scuro
// (PivotTableStyleDark1..PivotTableStyleDark28), e lo stesso enum espone anche i
// nuovi temi chiari/scuri di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Salva come .xlsx moderno — questo è il formato per cui PivotTableStyleType è significativo.
workbook.Save("output.xlsx");
```

## **Definire e applicare uno stile personalizzato per tabelle pivot**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o caratteri, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro si articola in tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Questo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.TableStyleElements.Add(TableStyleElementType)`, quindi assegnare un `Style` a ciascun elemento tramite `TableStyleElement.SetElementStyle(Style)`.
3. Applicare lo stile personalizzato alla pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare `PivotTableStyleType` qui, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}

`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Utilizzare `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati definiti tramite `AddPivotTableStyle`. Impostare entrambi è innocuo, ma solo quello corrispondente alla sorgente prevista viene reso.

{{% /alert %}}

I valori `TableStyleElementType` disponibili includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` e `PageFieldValues`.

L'esempio seguente definisce uno stile pivot personalizzato con un bordo nero sottile su `WholeTable` e un carattere rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e salva come `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Popola i dati di origine: riga intestazione + 9 righe di dati (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

// Aggiungi tabella pivot con origine da A1:C10, ancorata in E3, denominata "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Passo 1: registra un nuovo stile di tabella pivot personalizzato e cattura il suo indice
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Passo 2: aggiungi un elemento WholeTable e applica bordi sottili neri su tutti e quattro i lati
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);

// Passo 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Passo 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per preset integrati)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Applicare un unico stile a ogni cella della pivot con FormatAll**

`PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi cosa precedentemente impostata tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`FormatAll` sovrascrive sia `PivotTableStyleType` sia `PivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme, indipendente dal tema, in tutta la pivot.

{{% /alert %}}

L'esempio seguente crea un `Style` con riempimento solido giallo, un carattere blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `FormatAll` e salva come `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Scenario 4: Applica un singolo Stile a ogni cella della tabella pivot usando FormatAll
// API in uso: PivotTable.FormatAll(Style)
// Formato di destinazione: .xlsx
// Riferimento GitHub: vedi il repository Aspose.Cells-for-.NET — esempi di stile tabella pivot

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Popola i dati di origine: riga intestazione (riga 1) + 9 righe di dati (righe 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);

// Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Assegna i campi pivot: Fruit -> area Riga, Year -> area Colonna, Amount -> area Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Costruisci uno Stile che verrà applicato forzatamente su ogni cella della tabella pivot
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;

// Applica FormatAll: forza questo singolo stile su ogni cella della tabella pivot,
// sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName impostato in precedenza
pivotTable.FormatAll(style);

// Salva la cartella di lavoro nel formato moderno .xlsx
workbook.Save("output.xlsx");
```

## **Quale API di stile dovrei usare?**

La scelta dell'API di stile dipende dal formato di file in cui si sta salvando. Utilizzare la tabella seguente come riferimento rapido.

| Formato di file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad esempio `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorato quando si salva in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Da utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.SetElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.FormatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `PivotTableStyleType` per i temi predefiniti, oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="csharp" >}}