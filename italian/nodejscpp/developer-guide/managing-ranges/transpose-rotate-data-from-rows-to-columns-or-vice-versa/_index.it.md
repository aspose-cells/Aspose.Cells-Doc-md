---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: Trasporre un intervallo
url: /it/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, libreria Node.js via C++, foglio di calcolo, trasporre un intervallo, ruotare i dati, funzione Trasponi, formula matrice dinamica, formula matrice, TRANSPOSE di Excel, Righe in Colonne
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo `range.transpose()` sul posto e funziona su ogni versione di Excel, mentre il secondo utilizza `cell.setDynamicArrayFormula()` per scrivere una moderna formula matrice dinamica `=TRANSPOSE(...)` che si espande automaticamente in Excel 365 o Excel 2021. Il terzo approccio utilizza `cell.setArrayFormula()` per scrivere una classica formula matrice di tipo Ctrl+Shift+Enter (CSE) compatibile con le versioni più vecchie di Excel. Questo articolo illustra ciascun approccio con istruzioni passo-passo ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo di fatto i dati rispetto alla diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione, e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La stessa idea può essere applicata a livello di codice a un intervallo di celle, il che è utile in molti scenari aziendali e di reportistica.
Gli scenari comuni in cui la trasposizione risulta utile includono i seguenti.
- Riorientare report di vendita trimestrali o annuali in cui i trimestri normalmente si sviluppano orizzontalmente sulla pagina e le regioni verticalmente, o viceversa.
- Scambiare l'orientamento degli assi in dashboard o grafici in modo che una serie temporale scenda lungo la pagina invece di attraversarla.
- Riformulare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o di reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for Node.js via C++, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasporre un intervallo sul posto (range.transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non ha dipendenze dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo dell'output trasposto finale e non si desidera mantenere la formula `TRANSPOSE` originale nella cartella di lavoro.

### **API utilizzata**
`range.transpose()` è un metodo di istanza sulla classe `Aspose.Cells.Range`. Richiamandolo, l'intervallo viene capovolto sul posto scambiando le righe e le colonne, quindi ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` richiamando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.getWorksheets().get(0)`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.getCells()`.
4. Creare l'intervallo di origine che copre **A1:D5** richiamando `cells.createRange("A1:D5")`.
5. Richiamare `source.transpose()` per ruotare l'intervallo sul posto, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
Dopo la trasposizione, lo stesso intervallo di ancoraggio contiene i dati ruotati. La prima riga è (vuoto, **Europe**, **Asia**, **North America**) e la prima colonna è (vuoto, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Ogni colonna di vendite originale diventa una riga nell'intervallo trasposto.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approccio 2 — Trasporre con una formula matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera conservare la formula `=TRANSPOSE(A1:D5)` come formula attiva nella cartella di lavoro di output, in modo che il risultato si aggiorni automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive** dove sono supportate le matrici dinamiche e l'operatore di spill.

### **API utilizzata**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` è un metodo su `Aspose.Cells.Cell` che imposta la formula della cella come **formula matrice dinamica**. Excel valuta la formula una sola volta ed espande automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando è impostato su `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine utilizzando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Inserire la formula matrice dinamica nella cella **A6**, appena sotto l'intervallo di origine, richiamando `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L'argomento `null` passa le `FormulaParseOptions` predefinite, e il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla in modo che i valori espansi vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel espande automaticamente il risultato nella regione **A6:D10**, un blocco di 5 righe per 4 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni più vecchie di Excel non espanderanno correttamente le formule matrice dinamiche.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approccio 3 — Trasporre con una formula matrice classica (CSE)**
Utilizzare questo approccio quando si desidera conservare una formula `TRANSPOSE` nella cartella di lavoro ma il file Excel di destinazione potrebbe essere aperto in **versioni più vecchie di Excel (pre-2021, inclusi 2019, 2016, 2013 e così via)** dove l'espansione delle matrici dinamiche non è supportata. La classica formula matrice CSE (Ctrl+Shift+Enter) è l'alternativa compatibile con le versioni legacy che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` è un metodo su `Aspose.Cells.Cell` che assegna una **formula matrice classica (CSE)** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marcatore di formula matrice multi-cella in modo che Excel valuti la formula come una singola espressione matriciale che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine nello stesso modo degli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Richiamare `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** è l'ancoraggio della formula matrice e la matrice valutata si estende su 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'origine A1:D5. Excel scrive un singolo marcatore di formula matrice attraverso l'intervallo risultante in modo che le versioni più vecchie di Excel la valutino correttamente.

{{% alert color="primary" %}}
Le formule matrice CSE rappresentano il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra le versioni di Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Carica la cartella di lavoro sorgente con LoadOptions xlsx
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Accedi al primo foglio di lavoro e alla sua raccolta Cells
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Imposta la formula array CSE classica sulla cella A6.
// La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
// in un array di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
// e il terzo argomento (5) è il numero di colonne dell'array risultante.
// Aspose.Cells scrive il marcatore di formula array CSE in modo che Excel la valuti come
// una singola formula array multi-cella, compatibile con le versioni precedenti di Excel
// (2019, 2016, 2013, ecc.) che non supportano lo spilling dinamico dell'array.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Salva la cartella di lavoro in modo che il marcatore della formula array venga mantenuto
workbook.save("output.xlsx");
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula di origine conservata? | Intervallo di output |
|----------|--------------|---------------|--------------------------|--------------|
| Approccio 1 — Trasposizione sul posto | `range.transpose()` | Tutte le versioni di Excel | No (solo valori) | Stesso intervallo di ancoraggio, 5×4 |
| Approccio 2 — Formula matrice dinamica | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sì (si espande dinamicamente) | Espanso dall'ancoraggio |
| Approccio 3 — Formula matrice classica (CSE) | `cell.setArrayFormula` | Tutte le versioni di Excel | Sì (formula matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare l'**Approccio 1** quando si ha bisogno di una trasformazione rapida e compatibile tra le versioni e si desidera solo che i valori trasposti vengano scritti nel file. Utilizzare l'**Approccio 2** quando è garantito l'utilizzo di Excel moderno e si desidera che la formula rimanga attiva e si aggiorni se l'origine cambia. Utilizzare l'**Approccio 3** quando si ha bisogno della massima compatibilità con una formula conservata attraverso ogni versione di Excel, comprese le versioni più vecchie che non supportano le matrici dinamiche.

## **Articoli correlati**
- [Rendering di SmartMarker come matrice a cella singola](/cells/it/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Divisione di file Excel in più file](/cells/it/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}