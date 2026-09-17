---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Java, with three different approaches.
linktitle: Trasponi Intervallo
url: /it/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, libreria Java, foglio di calcolo, trasposizione intervallo, ruotare dati, funzione di trasposizione, formula matrice dinamica, formula matrice, TRANSPOSE di Excel, Da Righe a Colonne
type: docs
weight: 80
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe, in tre modi diversi. Il primo approccio utilizza il metodo sul posto `Range.transpose()` e funziona su ogni versione di Excel, mentre il secondo utilizza `Cell.setDynamicArrayFormula()` per scrivere una moderna formula a matrice dinamica `=TRANSPOSE(...)` che si espande automaticamente in Excel 365 o Excel 2021. Il terzo approccio utilizza `Cell.setArrayFormula()` per scrivere una classica formula matrice CSE (Ctrl+Shift+Enter) compatibile con le versioni più datate di Excel. Questo articolo illustra ciascun approccio con istruzioni dettagliate ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo di fatto i dati lungo la diagonale principale. In Microsoft Excel la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La stessa idea può essere applicata a livello di programmazione a un intervallo di celle, il che risulta utile in molti scenari aziendali e di reportistica.
Tra gli scenari comuni in cui la trasposizione è utile vi sono i seguenti.
- Riorientare i report di vendita trimestrali o annuali in cui i trimestri normalmente sono disposti orizzontalmente e le regioni verticalmente, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale scorra verticalmente anziché orizzontalmente.
- Riformattare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for Java, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasposizione dell'intervallo sul posto (Range.transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non dipende dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando serve solo il risultato trasposto finale e non è necessario mantenere la formula `TRANSPOSE` originale nella cartella di lavoro.

### **API utilizzata**
`Range.transpose()` è un metodo di istanza della classe `com.aspose.cells.Range`. La sua chiamata inverte l'intervallo sul posto scambiando le sue righe e le sue colonne, quindi ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` chiamando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro usando `workbook.getWorksheets().get(0)`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.getCells()`.
4. Creare l'intervallo di origine che copre **A1:D5** chiamando `cells.createRange("A1:D5")`.
5. Chiamare `source.transpose()` per ruotare l'intervallo sul posto, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
Dopo la trasposizione, lo stesso intervallo di ancoraggio contiene i dati ruotati. La prima riga è (vuoto, **Europe**, **Asia**, **North America**) e la prima colonna è (vuoto, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Ogni colonna originale di vendite diventa una riga nell'intervallo trasposto.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Approccio 2 — Trasposizione con una formula a matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera mantenere la formula `=TRANSPOSE(A1:D5)` come formula attiva nella cartella di lavoro di output, così che il risultato si aggiorni automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive**, dove le matrici dinamiche e l'operatore di espansione sono supportati.

### **API utilizzata**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` è un metodo di `com.aspose.cells.Cell` che imposta la formula della cella come **formula a matrice dinamica**. Excel valuta la formula una sola volta ed espande automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine utilizzando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Inserire la formula a matrice dinamica nella cella **A6**, appena sotto l'intervallo di origine, chiamando `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. L'argomento `null` passa le `FormulaParseOptions` predefinite, mentre il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla così che i valori espansi vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel espande automaticamente il risultato nell'area **A6:D10**, un blocco di 5 righe per 4 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo in Excel 365 / 2021 o versioni successive**. Le versioni più datate di Excel non espandono correttamente le formule a matrice dinamica.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Approccio 3 — Trasposizione con una formula matrice classica (CSE)**
Utilizzare questo approccio quando si desidera mantenere una formula `TRANSPOSE` nella cartella di lavoro, ma il file Excel di destinazione potrebbe essere aperto in **versioni più datate di Excel (precedenti al 2021, tra cui 2019, 2016, 2013 e così via)** dove l'espansione delle matrici dinamiche non è supportata. La formula matrice CSE classica (Ctrl+Shift+Enter) è l'alternativa compatibile con le versioni legacy che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` è un metodo di `com.aspose.cells.Cell` che assegna una **formula matrice (CSE) classica** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marker di formula matrice multi-cella in modo che Excel valuti la formula come un'unica espressione di matrice che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine nello stesso modo degli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Chiamare `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** è l'ancoraggio della formula matrice e la matrice valutata si estende su 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'intervallo di origine A1:D5. Excel scrive un singolo marker di formula matrice attraverso l'intervallo risultante così che le versioni più datate di Excel la valutino correttamente.

{{% alert color="primary" %}}
Le formule matrice CSE rappresentano il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra tutte le versioni di Excel.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Carica la cartella di lavoro di origine con LoadOptions xlsx
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Accedi al primo foglio di lavoro e alla relativa raccolta Cells
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Imposta la formula di matrice CSE classica sulla cella A6.
// La formula =TRANSPOSE(A1:D5) ruota l'intervallo di origine di 5 righe x 4 colonne
// in una matrice di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
// e il terzo argomento (5) è il numero di colonne della matrice risultante.
// Aspose.Cells scrive il contrassegno della formula di matrice CSE, in modo che Excel la valuti come
// un'unica formula di matrice multicella, compatibile con le versioni precedenti di Excel
// (2019, 2016, 2013, ecc.) che non supportano il riversamento delle matrici dinamiche.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Salva la cartella di lavoro in modo che il contrassegno della formula di matrice venga conservato
workbook.save("output.xlsx");
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione Excel | Formula sorgente preservata? | Intervallo di output |
|----------|--------------|---------------|--------------------------|--------------|
| Approccio 1 — Trasposizione sul posto | `Range.transpose()` | Tutte le versioni di Excel | No (solo valori) | Stesso intervallo di ancoraggio, 5×4 |
| Approccio 2 — Formula a matrice dinamica | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sì (espansione dinamica) | Espanso dall'ancoraggio |
| Approccio 3 — Formula matrice classica (CSE) | `Cell.setArrayFormula` | Tutte le versioni di Excel | Sì (formula matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare l'**Approccio 1** quando si necessita di una trasformazione rapida e cross-version e si vogliono solo i valori trasposti scritti nel file. Utilizzare l'**Approccio 2** quando Excel moderno è garantito e si desidera che la formula rimanga attiva e si aggiorni se l'origine cambia. Utilizzare l'**Approccio 3** quando serve la massima compatibilità con una formula preservata attraverso ogni versione di Excel, comprese le release più datate che non supportano le matrici dinamiche.

## **Articoli correlati**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/it/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/java/inserting-an-image-into-a-cell/)
- [Divisione di file Excel in più file](/cells/it/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}