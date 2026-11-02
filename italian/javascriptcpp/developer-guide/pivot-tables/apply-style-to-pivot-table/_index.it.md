---
title: Applicare stili alle tabelle pivot in Aspose.Cells for JavaScript via C++
linktitle: Applicare stili alle tabelle pivot
description: Scoprire come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for JavaScript via C++, inclusi i formati automatici XLS tradizionali, gli stili moderni con nome introdotti in Excel 2007+, gli stili personalizzati delle tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells for JavaScript via C++, stile di tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'applicazione sia dei formati automatici tradizionali per le tabelle pivot (destinati ai file `.xls`), sia degli stili moderni con nome o personalizzati per le tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da utilizzare dipende dal formato in cui viene salvata la cartella di lavoro, non da quello da cui è stata caricata.
{{% /alert %}}

## **Introduzione**
Aspose.Cells espone due API parallele per gli stili delle tabelle pivot. La scelta tra esse dipende dal formato in cui viene salvata la cartella di lavoro, non da quello da cui viene letta. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`; in tal caso, viene applicata l'API moderna anziché quella tradizionale.
- `pivotTable.pivotTableStyleType` seleziona uno degli stili predefiniti con nome (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi stili sono di sola lettura.
- `pivotTable.pivotTableStyleName` seleziona uno stile personalizzato definito tramite `workbook.worksheets.tableStyles.addPivotTableStyle(...)`. Gli stili personalizzati sono necessari per modificare colori, bordi o caratteri oltre a quelli offerti dagli stili predefiniti.
Inoltre, `pivotTable.formatAll(style)` è una scorciatoia che applica un singolo oggetto `style` a ogni cella della tabella pivot, sovrascrivendo le impostazioni definite tramite una delle due API precedenti, basate sul nome dello stile. È utile quando è necessario un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare un formato automatico predefinito a una tabella pivot in XLS tradizionale**
`pivotTable.autoFormatType` accetta un valore dell'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili comprendono `Report1`–`Report10`, `Classic` e `Table1`–`Table10`.
Nell'esempio seguente viene caricata una nuova cartella di lavoro, vengono inseriti i dati di esempio Fruit/Year/Amount, viene aggiunta una tabella pivot, viene applicato `PivotTableAutoFormatType.Report5` e il risultato viene salvato come `.xls`.

{{% alert color="primary" %}}
**Perché non è disponibile uno stile per i campi colonna?** I formati automatici della serie Report (`Report1`–`Report10`, `Table1`–`Table10`) sono stati progettati nella versione classica di Excel per **tabelle pivot a singola dimensione** con soli campi riga e valori e non prevedono stili predefiniti per le intestazioni dei campi colonna. Se la tabella pivot richiede campi colonna, utilizzare invece gli stili predefiniti moderni dell'API `PivotTableStyleType` descritti in [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), progettati per la disposizione bidimensionale adottata dalle versioni moderne di Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 1: applica un formato automatico predefinito XLS legacy
            // API in uso: PivotTable.AutoFormatType
            // Formato file di destinazione: .xls (legacy)
            // Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Crea una nuova cartella di lavoro
            const workbook = new Workbook();
            // Ottieni il primo foglio di lavoro
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Popola i dati di origine con la riga di intestazione (Fruit, Year, Amount)
            // e 9 righe di dati che coprono grape, blueberry, kiwi e cherry nel 2020 e nel 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Aggiungi una tabella pivot nella cella di destinazione E3, usando l'intervallo di origine A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Assegna i campi: Fruit -> Righe, Amount -> Dati
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Applica il formato automatico predefinito "Report5" per XLS legacy
            // Nota: questa proprietà è significativa solo quando si salva come .xls.
            // Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
            // e utilizzawhatever specifica PivotTableStyleType / PivotTableStyleName.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Salva la cartella di lavoro nel formato legacy .xls
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Applicare uno stile predefinito moderno con nome alla tabella pivot**
`pivotTable.pivotTableStyleType` seleziona uno degli stili predefiniti con nome introdotti da Excel 2007 per le tabelle pivot. L'enumerazione `PivotTableStyleType` espone tre famiglie di temi: gli stili chiari, da `PivotTableStyleLight1` a `PivotTableStyleLight28`, gli stili medi, da `PivotTableStyleMedium1` a `PivotTableStyleMedium28`, e gli stili scuri, da `PivotTableStyleDark1` a `PivotTableStyleDark28`. Definisce inoltre `None` e `Custom`. I membri con numerazione più elevata di ciascuna famiglia corrispondono agli stili aggiunti in Excel 2017.
Questi stili predefiniti sono di sola lettura. Quando occorre modificare colori, bordi o caratteri oltre a quanto offerto da uno stile predefinito, è necessario definire uno stile personalizzato per la tabella pivot, come mostrato in [Scenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**Perché utilizzare gli stili predefiniti moderni anziché i formati automatici della serie Report?** I valori `Report1`–`Report10` e `Table1`–`Table10` di `PivotTableAutoFormatType` sono anteriori all'introduzione dei campi colonna nelle tabelle pivot e, pertanto, non includono stili per le intestazioni dei campi colonna; Excel visualizza quindi tali intestazioni senza formattazione. Gli stili predefiniti `PivotTableStyleType` sono stati progettati per la disposizione bidimensionale adottata dalle versioni moderne di Excel e applicano la formattazione sia alle intestazioni dei campi di riga sia a quelle dei campi di colonna.
{{% /alert %}}

Questo scenario riutilizza il set di dati Fruit/Year/Amount dello Scenario 1, aggiunge `Year` all'area delle colonne accanto al campo di riga `Fruit` tramite `PivotFieldType.Column`, applica lo stile predefinito del tema scuro `PivotTableStyleDark1` tramite `pivotTable.pivotTableStyleType` e salva il risultato come `.xlsx`, il formato per il quale `PivotTableStyleType` è applicabile.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 2: applica uno stile predefinito moderno di Excel 2007+ utilizzando PivotTableStyleType.
            // Formato file di destinazione: .xlsx. L'enumerazione PivotTableStyleType si trova nel namespace Aspose.Cells
            // (non in Aspose.Cells.Pivot), motivo per cui non sono necessarie ulteriori dichiarazioni using.
            // Riferimento GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Riga di intestazione: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 righe di dati di Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Aggiunge una tabella pivot in E3, utilizzando A1:C10 come origine
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Assegna i campi pivot: Fruit -> area righe, Year -> area colonne, Amount -> area dati
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Applica uno stile pivot predefinito moderno di Excel 2007+.
            // PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
            // viene ignorato da Excel per questi formati. PivotTableStyleDark1 appartiene alla famiglia
            // dei temi scuri (PivotTableStyleDark1..PivotTableStyleDark28) e la stessa enumerazione espone anche
            // i temi chiari/scuri più recenti di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Salva nel formato moderno .xlsx, per il quale PivotTableStyleType è significativo.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **Definire e applicare uno stile personalizzato alla tabella pivot**
Gli stili predefiniti non possono essere modificati. Quando occorre sovrascrivere colori, bordi o caratteri, è necessario definire uno stile personalizzato per la tabella pivot. Il flusso di lavoro è composto da tre passaggi:
1. Aggiungere uno stile personalizzato alla raccolta `tableStyles` della cartella di lavoro tramite `workbook.worksheets.tableStyles.addPivotTableStyle(name)`. Il metodo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi, ad esempio `WholeTable` o `GrandTotalRow`, tramite `tableStyle.tableStyleElements.add(tableStyleElementType)`, quindi assegnare uno `style` a ogni elemento tramite `tableStyleElement.setElementStyle(style)`.
3. Applicare lo stile personalizzato alla tabella pivot impostando `pivotTable.pivotTableStyleName` sul nome dello stile. Non utilizzare `pivotTable.pivotTableStyleType` in questo caso, poiché questa proprietà seleziona gli stili predefiniti.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` e `pivotTable.pivotTableStyleType` non sono intercambiabili. Utilizzare `pivotTable.pivotTableStyleType` per gli stili predefiniti e `pivotTable.pivotTableStyleName` per gli stili personalizzati definiti tramite `addPivotTableStyle`. L'impostazione di entrambe non causa problemi, ma viene visualizzato soltanto lo stile corrispondente al tipo di stile utilizzato.
I valori disponibili di `TableStyleElementType` includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` e `PageFieldValues`.
Nell'esempio seguente viene definito uno stile personalizzato per la tabella pivot con un bordo nero sottile su `WholeTable` e un carattere rosso in grassetto su `GrandTotalRow`; lo stile viene quindi applicato tramite `pivotTable.pivotTableStyleName` e il risultato viene salvato come `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Popola i dati di origine: intestazione + 9 righe di dati (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Aggiungi una tabella pivot con origine da A1:C10, ancorata in E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Passaggio 1: registra un nuovo stile personalizzato per la tabella pivot e acquisisci il relativo indice
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Passaggio 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Passaggio 3: aggiungi un elemento GrandTotalRow e applica un carattere rosso grassetto
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Passaggio 4: applica lo stile personalizzato in base al nome (NON tramite PivotTableStyleType, che è per preset predefiniti)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Applicare uno stile a ogni cella della tabella pivot con formatAll**
`pivotTable.formatAll(style)` è una scorciatoia che applica un singolo oggetto `style` a ogni cella della tabella pivot, inclusi l'area dei dati, le intestazioni di riga e colonna e i totali. Le impostazioni applicate in precedenza tramite `pivotTable.pivotTableStyleType` o `pivotTable.pivotTableStyleName` sono sovrascritte.

{{% alert color="primary" %}}
`formatAll` sovrascrive sia `pivotTable.pivotTableStyleType` sia `pivotTable.pivotTableStyleName`. Utilizzarlo soltanto quando è necessario un aspetto uniforme e indipendente dal tema per l'intera tabella pivot.
Nell'esempio seguente viene creato uno `style` con riempimento giallo uniforme, carattere blu scuro in grassetto e bordi neri sottili su tutti i lati; lo stile viene quindi applicato con `formatAll` e il risultato viene salvato come `.xlsx`.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 4: applica un singolo Style a ogni cella della tabella pivot utilizzando FormatAll
            // API in uso: PivotTable.FormatAll(Style)
            // Formato di destinazione: .xlsx
            // Riferimento GitHub: consultare il repository Aspose.Cells-for-.NET — esempi di stilizzazione delle tabelle pivot
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Popola i dati di origine: riga di intestazione (riga 1) + 9 righe di dati (righe 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Aggiungi la tabella pivot: intervallo di origine A1:C10, cella di destinazione E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Assegna i campi della tabella pivot: Fruit -> area Righe, Year -> area Colonne, Amount -> area Dati
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Crea uno Style che verrà applicato forzatamente a ogni cella della tabella pivot
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Applica FormatAll: impone questo singolo stile a ogni cella della tabella pivot,
            // sovrascrivendo eventuali PivotTableStyleType / PivotTableStyleName impostati in precedenza
            pivotTable.formatAll(style);
            // Salva il workbook nel formato moderno .xlsx
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Quale API di stile conviene usare?**
La scelta dell'API di stile dipende dal formato in cui viene salvato il file. Consultare la tabella seguente come riferimento rapido.
| Formato del file di destinazione | API da usare | Note |
|---|---|---|
| `.xls` (tradizionale) | `pivotTable.autoFormatType` | Valori dell'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad esempio `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). La proprietà viene ignorata quando si salva in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `pivotTable.pivotTableStyleType` | Valori dell'enumerazione `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, inclusi gli stili aggiunti in Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Utilizzare quando gli stili predefiniti non sono sufficienti. Configurare lo stile tramite `tableStyleElement.setElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `pivotTable.formatAll(style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |
In caso di dubbio, salvare come `.xlsx` e utilizzare `pivotTable.pivotTableStyleType` per i temi predefiniti oppure `pivotTable.pivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="javascript-cpp" >}}