---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via Java with three different approaches.
linktitle: Trasporre un intervallo
url: /it/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, trasporre intervallo, ruotare dati, funzione TRANSPOSE, formula matrice dinamica, formula matrice, TRANSPOSE di Excel, Righe in Colonne
type: docs
weight: 80
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo in-place `Range.transpose()` e funziona su ogni versione di Excel, mentre il secondo utilizza `Cell.setDynamicArrayFormula()` per scrivere una moderna formula di matrice dinamica `=TRANSPOSE(...)` che viene distribuita automaticamente in Excel 365 o Excel 2021. Il terzo approccio utilizza `Cell.setArrayFormula()` per scrivere una classica formula di matrice Ctrl+Shift+Enter (CSE), compatibile con le versioni meno recenti di Excel. Questo articolo illustra ciascun approccio con istruzioni passo-passo ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo efficacemente i dati lungo la diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). La stessa idea può essere applicata a livello di codice a un intervallo di celle, il che risulta utile in molti scenari aziendali e di reportistica.
Gli scenari più comuni in cui la trasposizione è utile includono i seguenti.
- Riorientare i report di vendita trimestrali o annuali in cui i trimestri normalmente attraversano la pagina e le regioni scendono lungo la pagina, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale scenda lungo la pagina anziché attraversarla.
- Riformattare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o di reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'articolo presenta quindi tre modi diversi per trasporre questi dati utilizzando Aspose.Cells for Python via Java, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasporre un intervallo sul posto (Range.transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non dipende dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo dell'output trasposto finale e non si desidera mantenere la formula `TRANSPOSE` originale nella cartella di lavoro.

### **API utilizzata**
`Range.transpose()` è un metodo di istanza della classe `com.aspose.cells.Range`. La sua chiamata capovolge l'intervallo sul posto scambiandone righe e colonne, quindi ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` chiamando `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.getWorksheets().get(0)`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.getCells()`.
4. Creare l'intervallo di origine che copre **A1:D5** chiamando `cells.createRange("A1:D5")`.
5. Chiamare `source.transpose()` per ruotare l'intervallo sul posto, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
Dopo la trasposizione lo stesso intervallo di ancoraggio contiene i dati ruotati. La prima riga diventa (vuoto, **Europe**, **Asia**, **North America**) e la prima colonna diventa (vuoto, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Ogni colonna originale delle vendite diventa una riga nell'intervallo trasposto.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Approccio 2 — Trasporre con una formula di matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera mantenere la formula `=TRANSPOSE(A1:D5)` come formula attiva nella cartella di lavoro di output, in modo che il risultato venga aggiornato automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive**, dove le matrici dinamiche e l'operatore di spill sono supportati.

### **API utilizzata**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` è un metodo di `com.aspose.cells.Cell` che imposta la formula della cella come **formula di matrice dinamica**. Excel valuta la formula una sola volta e distribuisce automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `True`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine utilizzando `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Posizionare la formula di matrice dinamica sulla cella **A6**, appena sotto l'intervallo di origine, chiamando `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)`.
4. L'argomento `None` passa `FormulaParseOptions` predefinite e il terzo argomento `True` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla in modo che i valori distribuiti vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel distribuisce automaticamente il risultato nella regione **A6:D10**, un blocco di 5 righe per 4 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni meno recenti di Excel non distribuiranno correttamente le formule di matrice dinamica.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# codice portato qui
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Approccio 3 — Trasporre con una formula di matrice classica (CSE)**
Utilizzare questo approccio quando si desidera conservare una formula `TRANSPOSE` nella cartella di lavoro, ma il file Excel di destinazione potrebbe essere aperto in **versioni meno recenti di Excel (pre-2021, comprese 2019, 2016, 2013 e così via)**, dove la distribuzione delle matrici dinamiche non è supportata. La classica formula di matrice CSE (Ctrl+Shift+Enter) è l'alternativa compatibile con le versioni legacy che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` è un metodo di `com.aspose.cells.Cell` che assegna una **formula di matrice classica (CSE)** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marcatore di formula di matrice multi-cella in modo che Excel valuti la formula come una singola espressione di matrice che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine allo stesso modo degli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Chiamare `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** è l'ancoraggio della formula di matrice e la matrice valutata si estende per 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'origine A1:D5. Excel scrive un singolo marcatore di formula di matrice nell'intervallo risultante, in modo che le versioni meno recenti di Excel la valutino correttamente.

{{% alert color="primary" %}}
Le formule di matrice CSE sono il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra le versioni di Excel.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Carica la cartella di lavoro sorgente con LoadOptions xlsx
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Accedi al primo foglio di lavoro e alla sua raccolta Cells
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Imposta la formula di matrice CSE classica sulla cella A6.
# La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
# in una matrice di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
# e il terzo argomento (5) è il numero di colonne della matrice risultante.
# Aspose.Cells scrive il marcatore della formula di matrice CSE in modo che Excel la valuti come
# una singola formula di matrice multi-cella, compatibile con le versioni precedenti di Excel
# (2019, 2016, 2013, ecc.) che non supportano la distribuzione dinamica delle matrici.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Salva la cartella di lavoro in modo che il marcatore della formula di matrice venga mantenuto
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula di origine conservata? | Intervallo di output |
|----------|--------------|---------------|--------------------------|--------------|
| Approccio 1 — Trasposizione sul posto | `Range.transpose()` | Tutte le versioni di Excel | No (solo valori) | Stesso intervallo di ancoraggio, 5×4 |
| Approccio 2 — Formula di matrice dinamica | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Sì (distribuzione dinamica) | Distribuito dall'ancoraggio |
| Approccio 3 — Formula di matrice classica (CSE) | `Cell.setArrayFormula` | Tutte le versioni di Excel | Sì (formula di matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare **Approccio 1** quando si ha bisogno di una trasformazione rapida e compatibile tra le versioni e si desidera solo che i valori trasposti vengano scritti nel file. Utilizzare **Approccio 2** quando l'uso di Excel moderno è garantito e si desidera che la formula rimanga attiva e si aggiorni se l'origine cambia. Utilizzare **Approccio 3** quando si necessita della massima compatibilità con una formula conservata in tutte le versioni di Excel, comprese le versioni meno recenti che non supportano le matrici dinamiche.

## **Articoli correlati**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via Java](/cells/it/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/python-java/inserting-an-image-into-a-cell/)
- [Divisione di file Excel in più file](/cells/it/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}