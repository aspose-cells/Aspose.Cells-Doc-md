---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via Java, with three different approaches.
linktitle: Trasporre un intervallo
url: /it/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, libreria Node.js via Java, foglio di calcolo, trasporre intervallo, ruotare dati, funzione TRASPONI, formula di matrice dinamica, formula matrice, TRASPONI di Excel, Righe in Colonne
type: docs
weight: 80
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo `Range.transpose()` sul posto e funziona su tutte le versioni di Excel, mentre il secondo utilizza `Cell.setDynamicArrayFormula()` per scrivere una moderna formula di matrice dinamica `=TRASPONI(...)` che si riversa automaticamente su Excel 365 o Excel 2021. Il terzo approccio utilizza `Cell.setArrayFormula()` per scrivere una classica formula matrice con Ctrl+Shift+Invio (CSE) compatibile con le versioni precedenti di Excel. Questo articolo illustra ciascun approccio con istruzioni passo-passo ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo effettivamente i dati rispetto alla diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRASPONI` esegue questa operazione e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La stessa idea può essere applicata programmaticamente a un intervallo di celle, il che è utile in molti scenari aziendali e di reportistica.
Gli scenari comuni in cui la trasposizione è utile includono i seguenti.
- Riorientare i report di vendita trimestrali o annuali in cui i trimestri normalmente si estendono orizzontalmente sulla pagina e le regioni verticalmente, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale si sviluppi verticalmente anziché orizzontalmente.
- Riorganizzare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o di reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente tabella di piccole vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for Node.js via Java, ciascuno adatto a una diversa versione di Excel e caso d'uso.

## **Approccio 1 — Trasporre un intervallo sul posto (Range.transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRASPONI`. Funziona su **tutte le versioni di Excel** e non ha dipendenza dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo del risultato trasposto finale e non si desidera mantenere la formula `TRASPONI` originale nella cartella di lavoro.

### **API utilizzata**
`Range.transpose()` è un metodo di istanza della classe `com.aspose.cells.Range`. Chiamandolo, l'intervallo viene capovolto sul posto scambiando le sue righe e colonne, così ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere una formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` chiamando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.getWorksheets().get(0)`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.getCells()`.
4. Creare l'intervallo di origine che copre **A1:D5** chiamando `cells.createRange("A1:D5")`.
5. Chiamare `source.transpose()` per ruotare l'intervallo sul posto, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
Dopo la trasposizione, lo stesso intervallo di ancoraggio contiene i dati ruotati. La prima riga legge (vuoto, **Europe**, **Asia**, **North America**) e la prima colonna legge (vuoto, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Ogni colonna originale di vendite diventa una riga nell'intervallo trasposto.

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approccio 2 — Trasporre con una formula di matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera preservare la formula `=TRASPONI(A1:D5)` come formula live nella cartella di lavoro di output, così il risultato si aggiorna automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o successivi** dove le matrici dinamiche e l'operatore di spill sono supportati.

### **API utilizzata**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` è un metodo di `com.aspose.cells.Cell` che imposta la formula della cella come **formula di matrice dinamica**. Excel valuta la formula una volta e riversa automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine utilizzando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Posizionare la formula di matrice dinamica sulla cella **A6**, appena sotto l'intervallo di origine, chiamando `cells.get("A6").setDynamicArrayFormula("=TRASPONI(A1:D5)", null, true)`.
4. L'argomento `null` passa i `FormulaParseOptions` predefiniti, e il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla in modo che i valori riversati vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRASPONI(A1:D5)` ed Excel riversa automaticamente il risultato nella regione **A6:D10**, un blocco di 5 righe per 4 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o successivi**. Le versioni precedenti di Excel non riverseranno correttamente le formule di matrice dinamica.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approccio 3 — Trasporre con una formula matrice classica (CSE)**
Utilizzare questo approccio quando si desidera preservare una formula `TRASPONI` nella cartella di lavoro, ma il file Excel di destinazione potrebbe essere aperto in **versioni precedenti di Excel (pre-2021, inclusi 2019, 2016, 2013 e così via)** dove il riversamento delle matrici dinamiche non è supportato. La classica formula matrice CSE (Ctrl+Shift+Invio) è l'alternativa legacy compatibile che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` è un metodo di `com.aspose.cells.Cell` che assegna una **formula matrice classica (CSE)** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marcatore di formula matrice multi-cella in modo che Excel valuti la formula come un'unica espressione di matrice che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine nello stesso modo degli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Chiamare `cells.get("A6").setArrayFormula("=TRASPONI(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** è l'ancoraggio della formula matrice e la matrice valutata si estende su 4 righe per 5 colonne partendo da A6, corrispondendo alle dimensioni trasposte dell'origine A1:D5. Excel scrive un singolo marcatore di formula matrice attraverso l'intervallo risultante in modo che le versioni precedenti di Excel lo valutino correttamente.

{{% alert color="primary" %}}
Le formule matrice CSE sono il modo classico di Excel per valutare un'espressione `TRASPONI` e questo approccio è universalmente compatibile tra tutte le versioni di Excel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Carica il workbook sorgente con le LoadOptions xlsx
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Accedi al primo foglio di lavoro e alla sua raccolta Cells
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Imposta la formula di matrice CSE classica sulla cella A6.
// La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
// in una matrice di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
// e il terzo argomento (5) è il numero di colonne della matrice risultante.
// Aspose.Cells scrive il marcatore della formula di matrice CSE in modo che Excel la valuti come
// una singola formula di matrice multi-cella, compatibile con le versioni precedenti di Excel
// (2019, 2016, 2013, ecc.) che non supportano lo spillover dinamico delle matrici.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Salva il workbook in modo che il marcatore della formula di matrice venga persistito
workbook.save("output.xlsx");
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula di origine preservata? | Intervallo di output |
|----------|--------------|---------------|--------------------------|--------------|
| Approccio 1 — Trasposizione sul posto | `Range.transpose()` | Tutte le versioni di Excel | No (solo valori) | Stesso intervallo di ancoraggio, 5×4 |
| Approccio 2 — Formula di matrice dinamica | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sì (si riversa dinamicamente) | Riversato dall'ancoraggio |
| Approccio 3 — Formula matrice classica (CSE) | `Cell.setArrayFormula` | Tutte le versioni di Excel | Sì (formula matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare l'**Approccio 1** quando è necessaria una trasformazione rapida e compatibile tra le versioni e si hanno bisogno solo dei valori trasposti scritti nel file. Utilizzare l'**Approccio 2** quando Excel moderno è garantito e si desidera che la formula rimanga live e si aggiorni se l'origine cambia. Utilizzare l'**Approccio 3** quando è necessaria la più ampia compatibilità con una formula preservata attraverso tutte le versioni di Excel, incluse le versioni meno recenti che non supportano le matrici dinamiche.

## **Articoli correlati**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/nodejs-java/inserting-an-image-into-a-cell/)
- [Divisione di file Excel in più file](/cells/it/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}