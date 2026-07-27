---
title: Applicare stili alle tabelle pivot in Aspose.Cells per .NET
linktitle: Applicare stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Node.js via C++, coprendo autoformati legacy XLS, stili denominati moderni di Excel 2007+, stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Node.js via C++ stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports applying both legacy pivot autoformats (intended for `.xls` files) and modern named or custom pivot table styles (intended for `.xlsx`, `.xlsm`, and `.xlsb` files). The API you should call depends on the file format the workbook is saved to, not the format it was loaded from.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse dipende dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui è stata letta. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.

Per l'output legacy `.xls`, utilizzare la proprietà `PivotTable.AutoFormatType` insieme all'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Questa API corrisponde al selettore di formattazione automatica offerto dalla versione classica di Excel per le tabelle pivot.

Per l'output moderno `.xlsx`, `.xlsm` e `.xlsb`, sono disponibili due varianti dell'API di stile:

- `PivotTable.PivotTableStyleType` seleziona uno degli stili predefiniti denominati (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o caratteri oltre quanto offerto dai preset.

Inoltre, `PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione definita tramite una delle API basate sul nome dello stile sopra indicate. Questo è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare una formattazione automatica preimpostata XLS legacy**

`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili sono `Report1` fino a `Report10`, `Classic`, e `Table1` fino a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa proprietà e ricorre alle impostazioni `PivotTableStyleType` e `PivotTableStyleName`.

{{% /alert %}}

Il seguente esempio carica una nuova cartella di lavoro, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.Report5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}

**Perché nessun campo colonna?** Gli autoformati della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) erano progettati in Excel classico per **tabelle pivot monodimensionali** con soli campi riga e valori — non hanno uno stile integrato per le intestazioni dei campi colonna. Se la tua tabella pivot richiede campi colonna, usa i preset moderni `PivotTableStyleType` dello Scenario 2 qui sotto, progettati per il layout bidimensionale usato da Excel moderno.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// Scenario 1: Applica un formato automatico preimpostato XLS legacy
// API in uso: PivotTable.AutoFormatType
// Formato file di destinazione: .xls (legacy)
// Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Crea una nuova cartella di lavoro
const workbook = new AsposeCells.Workbook();

// Ottieni il primo foglio di lavoro
const sheet = workbook.getWorksheets().get(0);

// Popola i dati di origine con la riga di intestazione (Frutto, Anno, Importo)
// e 9 righe di dati che coprono uva, mirtillo, kiwi, ciliegia negli anni 2020 e 2021
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

// Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", usando l'intervallo di origine A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// Assegna i campi: Frutto -> Righe, Anno -> Colonne, Importo -> Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Applica il formato automatico preimpostato XLS legacy "Report5"
// Nota: questa proprietà è significativa solo quando si salva come .xls.
// Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// e utilizza qualsiasi PivotTableStyleType / PivotTableStyleName specifichi.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Salva la cartella di lavoro nel formato legacy .xls
workbook.save("output.xls");
```

## **Applicare uno stile di tabella pivot preimpostato denominato moderno**

`PivotTable.PivotTableStyleType` accetta un valore dall'enumerazione `Aspose.Cells.PivotTableStyleType`. L'enumerazione copre i temi chiari da `PivotTableStyleLight1` a `PivotTableStyleLight28` e i temi scuri da `PivotTableStyleDark1` a `PivotTableStyleDark28`. Gli stili aggiunti in Excel 2017 (la seconda ondata di temi chiari e scuri) sono raggiungibili tramite la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza della formattazione automatica legacy, lo stile qui selezionato viene reso fedelmente da Excel e sopravvive ai passaggi attraverso altri strumenti Office.

Il seguente esempio utilizza gli stessi dati Frutto/Anno/Importo, crea una tabella pivot identica, applica `PivotTableStyleDark1` e salva la cartella di lavoro come `.xlsx`.

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

// Aggiungi una tabella pivot in E3 denominata "Pivot1", con origine da A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Frutto -> area Righe, Anno -> area Colonne, Importo -> area Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Applica uno stile pivot preimpostato denominato moderno di Excel 2007+.
// PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
// viene ignorato da Excel per quei formati. PivotTableStyleDark1 appartiene alla famiglia
// del tema scuro (PivotTableStyleDark1..PivotTableStyleDark28), e la stessa enum espone anche i
// nuovi temi chiari/scuri di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// Salva come .xlsx moderno — questo è il formato per cui PivotTableStyleType è significativo.
workbook.save("output.xlsx");
```

## **Definire e applicare uno stile di tabella pivot personalizzato**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o caratteri, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro prevede tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Viene restituito l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.TableStyleElements.Add(TableStyleElementType)`, quindi assegnare un `Style` a ciascun elemento tramite `TableStyleElement.SetElementStyle(Style)`.
3. Applicare lo stile personalizzato alla tabella pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare `PivotTableStyleType` qui, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}

`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Utilizzare `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati definiti tramite `AddPivotTableStyle`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente alla sorgente prevista.

{{% /alert %}}

I valori disponibili di `TableStyleElementType` includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` e `PageFieldValues`.

Il seguente esempio definisce uno stile pivot personalizzato con un bordo nero sottile su `WholeTable` e un carattere rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e salva come `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Popola i dati di origine: riga intestazione + 9 righe di dati (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
```

## **Applicare un unico stile a ogni cella della tabella pivot con FormatAll**

`PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione precedente definita tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`FormatAll` sovrascrive sia `PivotTableStyleType` che `PivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.

{{% /alert %}}

Il seguente esempio crea uno `Style` con riempimento giallo solido, carattere blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `FormatAll` e salva come `.xlsx`.

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

// Assegna i campi pivot: Fruit -> area Righe, Year -> area Colonne, Amount -> area Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Crea uno Stile che verrà applicato a ogni cella della tabella pivot
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

// Salva la cartella di lavoro nel formato moderno .xlsx
workbook.save("output.xlsx");
```

## **Quale API di stile devo usare?**

La scelta dell'API di stile dipende dal formato di file in cui si sta salvando. Utilizzare la tabella seguente come riferimento rapido.

| Formato file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad es. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorato quando si salva in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.SetElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.FormatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile in tutta la tabella pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `PivotTableStyleType` per i temi predefiniti oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="javascript" >}}