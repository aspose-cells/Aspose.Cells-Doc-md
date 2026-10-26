---
title: Applica stili alle tabelle pivot in Aspose.Cells for Node.js via C++
linktitle: Applica stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot usando Aspose.Cells for Node.js via C++, incluse le formattazioni automatiche XLS legacy, gli stili denominati moderni di Excel 2007+, gli stili personalizzati per tabelle pivot e la scorciatoia formatAll.
keywords: Aspose.Cells Node.js via C++ stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'applicazione sia delle formattazioni automatiche legacy per tabelle pivot (destinate ai file `.xls`) sia degli stili moderni denominati o personalizzati per tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.
{{% /alert %}}

## **Introduzione**
Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui la si legge. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.
- `PivotTable.PivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Workbook.Worksheets.TableStyles.addPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o font oltre quanto offerto dai preset.
Inoltre, `PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione effettuata tramite le due API basate sul nome di stile sopra descritte. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare una formattazione automatica preset XLS legacy**
`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili sono `Report1` fino a `Report10`, `Classic` e `Table1` fino a `Table10`.
L'esempio seguente carica una cartella di lavoro vuota, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.Report5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}
**Perché nessun campo colonna?** Le formattazioni automatiche della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) sono state progettate nel classico Excel per **tabelle pivot a dimensione singola** con solo campi riga e valori, senza stili predefiniti per le intestazioni dei campi colonna. Se la tabella pivot richiede campi colonna, utilizzare invece i preset moderni `PivotTableStyleType` dello [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), che sono progettati per il layout bidimensionale utilizzato da Excel moderno.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Add a pivot table at destination cell E3, using source range A1:C10
const pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **Applicare uno stile preset denominato moderno per tabelle pivot**
`PivotTable.pivotTableStyleType` seleziona uno degli stili predefiniti con nome che Excel 2007 ha introdotto per le tabelle pivot. L'enumerazione `PivotTableStyleType` espone tre famiglie di temi: la famiglia chiara da `PivotTableStyleLight1` a `PivotTableStyleLight28`, la famiglia media da `PivotTableStyleMedium1` a `PivotTableStyleMedium28` e la famiglia scura da `PivotTableStyleDark1` a `PivotTableStyleDark28`. Definisce inoltre `None` e `Custom`. I membri con numerazione più elevata di ciascuna famiglia sono gli stili aggiunti in Excel 2017.
Questi preset sono di sola lettura. Non appena è necessario modificare colori, bordi o caratteri oltre le opzioni offerte da un preset, occorre definire uno stile pivot personalizzato, come illustrato in [Scenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Perché usare i preset moderni anziché le formattazioni automatiche delle serie di report?** I valori `Report1` fino a `Report10` e `Table1` fino a `Table10` di `PivotTableAutoFormatType` sono anteriori all'introduzione dei campi di colonna delle tabelle pivot, quindi non prevedono alcuna formattazione per le intestazioni dei campi di colonna ed Excel visualizza queste intestazioni senza formattazione. I preset di `PivotTableStyleType` sono stati progettati per il layout bidimensionale utilizzato dalla versione moderna di Excel e applicano lo stesso stile alle intestazioni dei campi di riga e di colonna.
{{% /alert %}}

Questo scenario riutilizza il set di dati Fruit/Year/Amount dello Scenario 1, aggiunge `Year` all'area delle colonne accanto al campo di riga `Fruit` tramite `PivotFieldType.Column`, applica il preset del tema scuro `PivotTableStyleDark1` con `pivotTable.setPivotTableStyleType` e salva il risultato come `.xlsx` — il formato per cui `PivotTableStyleType` è significativo.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Definire e applicare uno stile personalizzato per tabelle pivot**
I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o font, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro prevede tre passaggi:
1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Workbook.Worksheets.TableStyles.addPivotTableStyle(string name)`. Viene restituito l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.TableStyleElements.Add(TableStyleElementType)`, quindi assegnare un `Style` a ciascun elemento tramite `TableStyleElement.SetElementStyle(Style)`.
3. Applicare lo stile personalizzato alla tabella pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare `PivotTableStyleType` qui, poiché questa proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}
`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Utilizzare `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati definiti tramite `addPivotTableStyle`. Impostare entrambi è innocuo, ma solo quello corrispondente alla fonte prevista viene visualizzato.
I valori disponibili di `TableStyleElementType` includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` e `PageFieldValues`.
L'esempio seguente definisce uno stile pivot personalizzato con un bordo nero sottile su `WholeTable` e un font rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e salva come `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Popola i dati di origine: riga di intestazione + 9 righe di dati (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// Aggiungi tabella pivot con origine da A1:C10, ancorata a E3, denominata
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Passaggio 1: registra un nuovo stile personalizzato di tabella pivot e memorizza il suo indice
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Passaggio 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);
// Passaggio 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Passaggio 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per i preset integrati)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Applicare un unico stile a ogni cella della tabella pivot con formatAll**
`PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione precedente effettuata tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}
`formatAll` sovrascrive sia `PivotTableStyleType` sia `PivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema nell'intera tabella pivot.
L'esempio seguente crea uno `Style` con riempimento giallo pieno, font blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `formatAll` e salva come `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Popola i dati di origine: riga di intestazione (riga 1) + 9 righe di dati (righe 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assegna i campi pivot: Fruit -> area Riga, Year -> area Colonna, Amount -> area Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Crea uno stile che verrà applicato forzatamente a ogni cella della tabella pivot
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
// Applica formatAll: forza questo singolo stile su ogni cella della tabella pivot,
// sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName impostato in precedenza
pivotTable.formatAll(style);
// Salva la cartella di lavoro nel formato .xlsx moderno
workbook.save("output.xlsx");
```

## **Quale API di stile dovrei usare?**
La scelta dell'API di stile dipende dal formato di file in cui si sta salvando. Utilizzare la tabella seguente come riferimento rapido.
| Formato file di destinazione | API da usare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad es. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorato quando si salva nei formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Da usare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.SetElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.formatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |
In caso di dubbio, salvare come `.xlsx` e utilizzare `PivotTableStyleType` per i temi predefiniti, oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="nodejs-cpp" >}}