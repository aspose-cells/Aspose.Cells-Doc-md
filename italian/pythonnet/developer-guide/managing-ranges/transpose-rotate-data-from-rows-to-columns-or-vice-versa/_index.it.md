---
title: Trasponi intervallo
linktitle: Trasponi intervallo
description: Questo articolo spiega come trasporre o ruotare i dati da righe a colonne o viceversa nei file Excel utilizzando Aspose.Cells for Python via .NET, con tre approcci diversi.
keywords: Aspose.Cells for Python via .NET, foglio di calcolo, trasponi intervallo, ruota dati, funzione TRANSPOSE, formula matrice dinamica, formula matrice, TRANSPOSE di Excel, Righe a Colonne
type: docs
weight: 80
url: /it/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo in-place `range.transpose()` e funziona su ogni versione di Excel, mentre il secondo utilizza `cell.set_dynamic_array_formula()` per scrivere una moderna formula di matrice dinamica `=TRANSPOSE(...)` che si espande automaticamente su Excel 365 o Excel 2021. Il terzo approccio utilizza `cell.set_array_formula()` per scrivere una classica formula matrice Ctrl+Shift+Enter (CSE) compatibile con le versioni precedenti di Excel. Questo articolo illustra ogni approccio con istruzioni dettagliate ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo effettivamente i dati lungo la diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione, e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Questo concetto può essere applicato a livello di programmazione a un intervallo di celle, il che è utile in molti scenari aziendali e di reportistica.
- Riorientare i report di vendita trimestrali o annuali in cui i trimestri normalmente si estendono in orizzontale e le regioni in verticale, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale scorra in verticale anziché in orizzontale.
- Riformattare i dati importati da sistemi esterni in modo che corrispondano al layout atteso dai modelli di analisi o di reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** contenente le intestazioni delle regioni e **A2:A5** contenente le intestazioni dei trimestri.
| Regione          | Europa     | Asia       | Nord America |
|------------------|------------|------------|--------------|
| Trim 1           | 21704714   | 8774099    | 12094215     |
| Trim 2           | 17987034   | 12214447   | 10873099     |
| Trim 3           | 19485029   | 14356879   | 15689543     |
| Trim 4           | 22567894   | 15763492   | 17456723     |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for Python via .NET, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasponi intervallo in place (range.transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non ha dipendenze dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo dell'output trasposto finale e non si desidera mantenere la formula `TRANSPOSE` originale nella cartella di lavoro.

### **API utilizzata**
`range.transpose()` è un metodo di istanza della classe `Aspose.Cells.Range`. Richiamandolo, l'intervallo viene invertito in place scambiando le sue righe e colonne, quindi ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere una formula.

### **Passaggi**
1. Aprire la cartella di lavoro sorgente con `LoadOptions` impostato sul formato `.xlsx` richiamando `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.worksheets[0]`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.cells`.
4. Creare l'intervallo sorgente che copre **A1:D5** richiamando `cells.create_range("A1:D5")`.
5. Richiamare `source.transpose()` per ruotare l'intervallo in place, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
Dopo la trasposizione, l'intervallo di ancoraggio iniziale contiene i dati ruotati. La prima riga recita (vuoto, **Europa**, **Asia**, **Nord America**) e la prima colonna recita (vuoto, **Trim 1**, **Trim 2**, **Trim 3**, **Trim 4**). Ogni colonna originale di vendite diventa una riga nell'intervallo trasposto.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Approccio 2 — Trasponi con una formula matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera conservare la formula `=TRANSPOSE(A1:D5)` come formula attiva nella cartella di lavoro di output, così che il risultato si aggiorni automaticamente se i dati sorgente cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive** dove le matrici dinamiche e l'operatore di espansione sono supportati.

### **API utilizzata**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` è un metodo di `Aspose.Cells.Cell` che imposta la formula della cella come **formula matrice dinamica**. Excel valuta la formula una volta ed espande automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `True`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro sorgente utilizzando `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `cells`.
3. Posizionare la formula matrice dinamica sulla cella **A6**, appena sotto l'intervallo sorgente, richiamando `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. L'argomento `None` passa `FormulaParseOptions` predefiniti, e il terzo argomento `True` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla in modo che i valori espansi vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel espande automaticamente il risultato nella regione **A6:D10**, un blocco di 5 righe per 4 colonne uguale ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni precedenti di Excel non espanderanno correttamente le formule matrice dinamiche.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Approccio 3 — Trasponi con una formula matrice classica (CSE)**
Utilizzare questo approccio quando si desidera conservare una formula `TRANSPOSE` nella cartella di lavoro ma il file Excel di destinazione potrebbe essere aperto in **versioni precedenti di Excel (pre-2021, inclusi 2019, 2016, 2013 e così via)** dove l'espansione delle matrici dinamiche non è supportata. La formula matrice classica CSE (Ctrl+Shift+Enter) è l'alternativa compatibile con le versioni legacy che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`cell.set_array_formula(array_formula, n_rows, n_columns)` è un metodo di `Aspose.Cells.Cell` che assegna una **formula matrice (CSE) classica** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marcatore di formula matrice multi-cella in modo che Excel valuti la formula come una singola espressione matriciale che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro sorgente come descritto negli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `cells`.
3. Richiamare `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.save(outputFile)`.
La cella **A6** è l'ancoraggio della formula matrice e la matrice valutata si estende su 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'intervallo sorgente A1:D5. Excel scrive un singolo marcatore di formula matrice attraverso l'intervallo risultante in modo che le versioni precedenti di Excel lo valutino correttamente.

{{% alert color="primary" %}}
Le formule matrice CSE rappresentano il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra tutte le versioni di Excel.
{{% /alert %}}

```python
import aspose.cells as ac
# Carica la cartella di lavoro sorgente con LoadOptions xlsx
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Accedi al primo foglio di lavoro e alla sua raccolta Cells
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Imposta la formula di matrice CSE classica sulla cella A6.
# La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
# in una matrice di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
# e il terzo argomento (5) è il numero di colonne della matrice risultante.
# Aspose.Cells scrive il marker della formula di matrice CSE in modo che Excel la valuti come
# una singola formula di matrice multi-cella, compatibile con le versioni più vecchie di Excel
# (2019, 2016, 2013, ecc.) che non supportano lo spilling dinamico delle matrici.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Salva la cartella di lavoro in modo che il marker della formula di matrice venga mantenuto
workbook.save("output.xlsx")
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula sorgente conservata? | Intervallo di output |
|-----------|--------------|-------------------|------------------------------|----------------------|
| Approccio 1 — Trasposizione in place | `range.transpose()` | Tutte le versioni di Excel | No (solo valori) | Intervallo di ancoraggio iniziale, 5×4 |
| Approccio 2 — Formula matrice dinamica | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Sì (si espande dinamicamente) | Espanso dall'ancoraggio |
| Approccio 3 — Formula matrice classica (CSE) | `cell.set_array_formula` | Tutte le versioni di Excel | Sì (formula matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare l'**Approccio 1** quando è necessaria una trasformazione rapida e compatibile tra le versioni e si ha bisogno solo dei valori trasposti scritti nel file. Utilizzare l'**Approccio 2** quando Excel moderno è garantito e si desidera che la formula rimanga attiva e si aggiorni se la sorgente cambia. Utilizzare l'**Approccio 3** quando è necessaria la massima compatibilità con una formula conservata in tutte le versioni di Excel, comprese le versioni precedenti che non supportano le matrici dinamiche.

## **Articoli correlati**
- [Rendering di matrice a cella singola SmartMarker | Aspose.Cells for Python via .NET](/cells/it/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/python-net/inserting-an-image-into-a-cell/)
- [Divisione dei file Excel in più file](/cells/it/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}