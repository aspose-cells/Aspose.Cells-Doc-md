---
title: Trasporre un intervallo
description: Questo articolo spiega come trasporre o ruotare i dati da righe a colonne o viceversa nei file Excel utilizzando Aspose.Cells for .NET con tre diversi approcci.
linktitle: Trasporre un intervallo
url: /it/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, trasporre intervallo, ruotare dati, funzione trasponi, formula matrice dinamica, formula matrice, TRANSPOSE di Excel, Righe in Colonne
type: docs
weight: 80
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo in-place `Range.Transpose()` e funziona su ogni versione di Excel, mentre il secondo utilizza `Cell.SetDynamicArrayFormula()` per scrivere una moderna formula di matrice dinamica `=TRANSPOSE(...)` che si espande automaticamente su Excel 365 o Excel 2021. Il terzo approccio utilizza `Cell.SetArrayFormula()` per scrivere una classica formula di matrice CSE (Ctrl+Maiusc+Invio) compatibile con le versioni meno recenti di Excel. Questo articolo illustra ogni approccio con istruzioni dettagliate ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo di fatto i dati lungo la diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione, e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Questo concetto può essere applicato programmaticamente a un intervallo di celle, il che è utile in molti scenari aziendali e di reportistica.
- Riorientare i report di vendita trimestrali o annuali in cui i trimestri normalmente sono disposti orizzontalmente nella pagina e le regioni verticalmente, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale scenda lungo la pagina invece di attraversarla.
- Riformulare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nel foglio di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Regione            | Europa     | Asia       | Nord America |
|--------------------|------------|------------|--------------|
| Trim 1             | 21704714   | 8774099    | 12094215     |
| Trim 2             | 17987034   | 12214447   | 10873099     |
| Trim 3             | 19485029   | 14356879   | 15689543     |
| Trim 4             | 22567894   | 15763492   | 17456723     |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for .NET, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasporre un intervallo sul posto (Range.Transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza ricorrere alla funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non ha dipendenze dalle matrici dinamiche, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo del risultato finale trasposto e non si desidera mantenere la formula `TRANSPOSE` originale nel foglio di lavoro.

### **API utilizzata**
`Range.Transpose()` è un metodo di istanza della classe `Aspose.Cells.Range`. Richiamandolo, l'intervallo viene ribaltato sul posto scambiando le sue righe e colonne, così che ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` richiamando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.Worksheets[0]`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.Cells`.
4. Creare l'intervallo di origine che copre **A1:D5** richiamando `cells.CreateRange("A1:D5")`.
5. Richiamare `source.Transpose()` per ruotare l'intervallo sul posto, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.
Dopo la trasposizione, questo intervallo di ancoraggio contiene i dati ruotati. La prima riga è (vuoto, **Europa**, **Asia**, **Nord America**) e la prima colonna è (vuoto, **Trim 1**, **Trim 2**, **Trim 3**, **Trim 4**). Ogni colonna originale di vendite diventa una riga nell'intervallo trasposto.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Approccio 2 — Trasposizione con una formula di matrice dinamica (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera preservare la formula `=TRANSPOSE(A1:D5)` come formula viva nella cartella di lavoro di output, così che il risultato si aggiorni automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive** dove le matrici dinamiche e l'operatore di espansione sono supportati.

### **API utilizzata**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` è un metodo di `Aspose.Cells.Cell` che imposta la formula della cella come **formula di matrice dinamica**. Excel valuta la formula una volta ed espande automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine utilizzando `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Inserire la formula di matrice dinamica nella cella **A6**, appena sotto l'intervallo di origine, richiamando `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. L'argomento `new FormulaParseOptions()` utilizza le impostazioni predefinite di `FormulaParseOptions`, e il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come una matrice dinamica e di valutarla in modo che i valori espansi vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel espande automaticamente il risultato nella regione **A6:E9**, un blocco di 4 righe per 5 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni meno recenti di Excel non espanderanno correttamente le formule di matrice dinamica.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Approccio 3 — Trasposizione con una classica formula di matrice (CSE)**
Utilizzare questo approccio quando si desidera preservare una formula `TRANSPOSE` nella cartella di lavoro ma il file Excel di destinazione potrebbe essere aperto in **versioni meno recenti di Excel (precedenti al 2021, inclusi 2019, 2016, 2013 e così via)** dove l'espansione delle matrici dinamiche non è supportata. La classica formula di matrice CSE (Ctrl+Maiusc+Invio) è l'alternativa legacy compatibile che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` è un metodo di `Aspose.Cells.Cell` che assegna una **formula di matrice classica (CSE)** alla cella di ancoraggio e dichiara le dimensioni della matrice risultante. Aspose.Cells scrive il marker di formula di matrice multi-cella in modo che Excel valuti la formula come un'unica espressione di matrice che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine come descritto negli approcci precedenti.
2. Recuperare il primo foglio di lavoro e accedere alla sua raccolta `Cells`.
3. Richiamare `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe della matrice di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.
La cella **A6** è l'ancoraggio della formula di matrice e la matrice valutata si estende su 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'intervallo di origine A1:D5. Excel scrive un singolo marker di formula di matrice attraverso l'intervallo risultante in modo che le versioni meno recenti di Excel lo valutino correttamente.

{{% alert color="primary" %}}
Le formule di matrice CSE sono il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra tutte le versioni di Excel.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Carica la cartella di lavoro sorgente con LoadOptions xlsx
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Accedi al primo foglio di lavoro e alla sua raccolta Cells
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Imposta la formula di matrice CSE classica sulla cella A6.
// La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
// in una matrice di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
// e il terzo argomento (5) è il numero di colonne della matrice risultante.
// Aspose.Cells scrive il marcatore della formula di matrice CSE in modo che Excel la valuti come
// una singola formula di matrice multi-cella, compatibile con le versioni precedenti di Excel
// (2019, 2016, 2013, ecc.) che non supportano lo spill dinamico delle matrici.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Salva la cartella di lavoro in modo che il marcatore della formula di matrice venga mantenuto
workbook.Save("output.xlsx");
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula di origine preservata? | Intervallo di output |
|-----------|--------------|-------------------|-------------------------------|----------------------|
| Approccio 1 — Trasposizione in-place | `Range.Transpose()` | Tutte le versioni di Excel | No (solo valori) | Intervallo di ancoraggio iniziale, 5×4 |
| Approccio 2 — Formula di matrice dinamica | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Sì (espansione dinamica) | Espanso dall'ancoraggio |
| Approccio 3 — Formula di matrice classica (CSE) | `Cell.SetArrayFormula` | Tutte le versioni di Excel | Sì (formula di matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare **Approccio 1** quando serve una trasformazione rapida e compatibile tra le versioni e si ha bisogno solo dei valori trasposti scritti nel file. Utilizzare **Approccio 2** quando Excel moderno è garantito e si desidera che la formula rimanga viva e si aggiorni se l'origine cambia. Utilizzare **Approccio 3** quando serve la massima compatibilità con una formula preservata in ogni versione di Excel, comprese le versioni meno recenti che non supportano le matrici dinamiche.

{{< app/cells/assistant language="csharp" >}}