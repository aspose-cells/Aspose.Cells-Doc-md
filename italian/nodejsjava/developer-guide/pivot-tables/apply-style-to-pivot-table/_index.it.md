---
title: Applicare stili alle tabelle pivot in Aspose.Cells per .NET
linktitle: Applicare stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Node.js via Java, trattando i formati automatici legacy XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Node.js via Java stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta l'applicazione sia dei formati automatici legacy per tabelle pivot (pensati per i file `.xls`) sia degli stili moderni denominati o personalizzati per tabelle pivot (pensati per i file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file con cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse è determinata dal formato di file con cui si salva la cartella di lavoro, non dal formato da cui la si legge. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.

Per l'output `.xls` legacy, utilizzare la proprietà `PivotTable.autoFormatType` insieme all'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Questa API corrisponde al selettore di formato automatico che il classico Excel offriva per le tabelle pivot.

Per l'output `.xlsx`, `.xlsm` e `.xlsb` moderno sono disponibili due varianti di API di stile:

- `PivotTable.pivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, compresi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.pivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Worksheets.getTableStyles().addPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o font oltre quanto offerto dai preset.

Inoltre, `PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi cosa impostata tramite una delle API basate sul nome dello stile sopra indicate. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare un formato automatico preset XLS legacy**

`PivotTable.autoFormatType` accetta un valore dall'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili sono `Report1` fino a `Report10`, `Classic`, e `Table1` fino a `Table10`.

{{% alert color="primary" %}}

`autoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa proprietà e ricorre alle impostazioni `pivotTableStyleType` e `pivotTableStyleName`.

{{% /alert %}}

L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.Report5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}

**Perché nessun campo colonna?** Gli autoformati della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) erano progettati in Excel classico per **tabelle pivot monodimensionali** con soli campi riga e valori — non hanno uno stile integrato per le intestazioni dei campi colonna. Se la tua tabella pivot richiede campi colonna, usa i preset moderni `PivotTableStyleType` dello Scenario 2 qui sotto, progettati per il layout bidimensionale usato da Excel moderno.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// Ottieni il primo foglio di lavoro
let sheet = workbook.getWorksheets().get(0);

// Popola i dati di origine con la riga di intestazione (Frutta, Anno, Quantità)
// e 9 righe di dati che coprono uva, mirtillo, kiwi, ciliegia nel 2020 e 2021
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

// Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", utilizzando l'intervallo di origine A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Assegna i campi: Frutta -> Righe, Anno -> Colonne, Quantità -> Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Applica il formato automatico predefinito legacy XLS "Report5"
// Nota: questa proprietà è significativa solo quando si salva come .xls.
// Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// e utilizza qualsiasi PivotTableStyleType / PivotTableStyleName specificato.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Salva la cartella di lavoro in formato legacy .xls
workbook.save("output.xls");
```

## **Applicare uno stile preset denominato moderno per tabelle pivot**

`PivotTable.pivotTableStyleType` accetta un valore dall'enumerazione `Aspose.Cells.PivotTableStyleType`. L'enumerazione copre i temi chiari da `PivotTableStyleLight1` a `PivotTableStyleLight28` e i temi scuri da `PivotTableStyleDark1` a `PivotTableStyleDark28`. Gli stili aggiunti in Excel 2017 (la seconda ondata di temi chiari e scuri) sono raggiungibili tramite la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza del formato automatico legacy, lo stile selezionato qui viene reso fedelmente da Excel e sopravvive ai round-trip attraverso altri strumenti Office.

L'esempio seguente utilizza gli stessi dati Frutto/Anno/Importo, crea una tabella pivot identica, applica `PivotTableStyleDark1` e salva la cartella di lavoro come `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 righe di dati di Frutto / Anno / Importo
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

// Aggiunge una tabella pivot in E3 denominata "Pivot1", con origine da A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Frutto -> area Righe, Anno -> area Colonne, Importo -> area Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Applica uno stile pivot preimpostato moderno di Excel 2007+.
// PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
// viene ignorato da Excel per questi formati. PivotTableStyleDark1 appartiene alla famiglia
// dei temi scuri (PivotTableStyleDark1..PivotTableStyleDark28), e lo stesso enum espone anche
// i temi più recenti chiari/scuri di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Salva come .xlsx moderno — questo è il formato per cui PivotTableStyleType è significativo.
workbook.save("output.xlsx");
```

## **Definire e applicare uno stile personalizzato per tabelle pivot**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o font, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro prevede tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Questo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.tableStyleElements.add(TableStyleElementType)`, quindi assegnare uno `Style` a ciascun elemento tramite `TableStyleElement.setElementStyle(Style)`.
3. Applicare lo stile personalizzato alla tabella pivot impostando `PivotTable.pivotTableStyleName` sul nome dello stile. Non utilizzare `pivotTableStyleType` qui, poiché quella proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}

`pivotTableStyleName` e `pivotTableStyleType` non sono intercambiabili. Utilizzare `pivotTableStyleType` per i preset predefiniti e `pivotTableStyleName` per gli stili personalizzati definiti tramite `addPivotTableStyle`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente alla sorgente prevista.

{{% /alert %}}

I valori di `TableStyleElementType` disponibili includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels`, e `PageFieldValues`.

L'esempio seguente definisce uno stile pivot personalizzato con un bordo nero sottile su `WholeTable` e un font rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `pivotTableStyleName` e salva come `.xlsx`.

```javascript
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

// Aggiungi una tabella pivot con origine da A1:C10, ancorata in E3, denominata "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Passaggio 1: registra un nuovo stile di tabella pivot personalizzato e cattura il suo indice
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Passaggio 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Passaggio 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Passaggio 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per gli stili predefiniti)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Applicare un unico stile a ogni cella della tabella pivot con FormatAll**

`PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, compresa l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi cosa fosse stata precedentemente impostata tramite `pivotTableStyleType` o `pivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`formatAll` sovrascrive sia `pivotTableStyleType` che `pivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.

{{% /alert %}}

L'esempio seguente crea uno `Style` con un riempimento solido giallo, un font blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `formatAll` e salva come `.xlsx`.

```javascript
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

// Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Fruit -> area Riga, Year -> area Colonna, Amount -> area Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Crea uno Stile che verrà applicato forzatamente su ogni cella della tabella pivot
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

// Applica FormatAll: forza questo singolo stile su ogni cella della tabella pivot,
// sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName precedentemente impostato
pivotTable.formatAll(style);

// Salva la cartella di lavoro nel formato .xlsx moderno
workbook.save("output.xlsx");
```

## **Quale API di stile dovrei usare?**

La scelta dell'API di stile dipende dal formato di file con cui si salva. Utilizzare la tabella seguente come riferimento rapido.

| Formato del file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.autoFormatType` | Valori da `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad es. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorato durante il salvataggio in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.pivotTableStyleType` | Valori da `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, comprese le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Da utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.setElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.formatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `pivotTableStyleType` per i temi predefiniti, oppure `pivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="nodejs-java" >}}