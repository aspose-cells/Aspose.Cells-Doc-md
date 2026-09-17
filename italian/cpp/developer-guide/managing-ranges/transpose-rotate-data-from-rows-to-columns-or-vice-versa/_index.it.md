---
title: Trasporre un intervallo
linktitle: Trasporre un intervallo
description: Questo articolo spiega come trasporre o ruotare i dati da righe a colonne o viceversa nei file Excel utilizzando Aspose.Cells for C++ con tre diversi approcci.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, trasporre intervallo, ruotare dati, funzione TRANSPOSE, formula array dinamica, formula matrice, TRANSPOSE di Excel, Righe in Colonne
type: docs
weight: 80
url: /it/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ supporta la trasposizione (rotazione) dei dati in modo che le righe diventino colonne e le colonne diventino righe in tre modi diversi. Il primo approccio utilizza il metodo in-place `Range.Transpose()` e funziona su ogni versione di Excel, mentre il secondo utilizza `Cell.SetDynamicArrayFormula()` per scrivere una moderna formula `=TRANSPOSE(...)` come array dinamico che si espande automaticamente in Excel 365 o Excel 2021. Il terzo approccio utilizza `Cell.SetArrayFormula()` per scrivere una classica formula matrice Ctrl+Shift+Enter (CSE) compatibile con le versioni precedenti di Excel. Questo articolo illustra ciascun approccio con istruzioni passo-passo ed esempi di codice completi.
{{% /alert %}}

## **Introduzione**
Trasporre un intervallo significa ruotarlo in modo che ciò che era una riga diventi una colonna e ciò che era una colonna diventi una riga, riflettendo efficacemente i dati lungo la diagonale principale. In Microsoft Excel, la funzione del foglio di lavoro `TRANSPOSE` esegue questa operazione, e il riferimento concettuale è documentato all'indirizzo [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). Questo concetto può essere applicato a livello di programmazione a un intervallo di celle, il che è utile in molti scenari aziendali e di reportistica.
- Riorientare report di vendita trimestrali o annuali in cui i trimestri normalmente si estendono orizzontalmente e le regioni verticalmente, o viceversa.
- Scambiare l'orientamento degli assi nelle dashboard o nei grafici in modo che una serie temporale scenda lungo la pagina invece di estendersi orizzontalmente.
- Rimodellare i dati importati da sistemi esterni in modo che corrispondano al layout previsto dai modelli di analisi o reportistica a valle.
Per rendere concreto il resto dell'articolo, ogni esempio utilizza la seguente piccola tabella di vendite per regione e per trimestre. Nella cartella di lavoro di esempio questa tabella occupa l'intervallo **A1:D5**, con **A1** lasciato vuoto come angolo in alto a sinistra, **B1:D1** che contiene le intestazioni delle regioni e **A2:A5** che contiene le intestazioni dei trimestri.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
L'articolo presenta quindi tre diversi modi per trasporre questi dati utilizzando Aspose.Cells for C++, ciascuno adatto a una diversa versione di Excel e a un diverso caso d'uso.

## **Approccio 1 — Trasporre un intervallo in place (Range.Transpose)**
Utilizzare questo approccio ogni volta che si desidera trasporre i dati senza coinvolgere la funzione del foglio di lavoro `TRANSPOSE`. Funziona su **ogni versione di Excel** e non dipende dagli array dinamici, il che lo rende l'opzione più sicura e compatibile tra le versioni. È ideale quando si ha bisogno solo del risultato trasposto finale e non si desidera mantenere la formula `TRANSPOSE` originale nella cartella di lavoro.

### **API utilizzata**
`Range.Transpose()` è un metodo di istanza della classe `Aspose.Cells.Range`. Chiamandolo, l'intervallo viene capovolto in place scambiando righe e colonne, quindi ciò che era una riga diventa una colonna e ciò che era una colonna diventa una riga. Il metodo modifica direttamente le celle sottostanti senza scrivere alcuna formula.

### **Passaggi**
1. Aprire la cartella di lavoro di origine con `LoadOptions` impostato sul formato `.xlsx` creando un `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Recuperare il primo foglio di lavoro dalla cartella di lavoro utilizzando `workbook.GetWorksheets().Get(0)`.
3. Accedere alla raccolta di celle del foglio di lavoro tramite `worksheet.GetCells()`.
4. Creare l'intervallo di origine che copre **A1:D5** chiamando `cells.CreateRange(u"A1:D5")`.
5. Chiamare `source.Transpose()` per ruotare l'intervallo in place, scambiando righe e colonne.
6. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approccio 2 — Trasporre con una formula di array dinamico (Excel 365 / 2021)**
Utilizzare questo approccio quando si desidera preservare la formula `=TRANSPOSE(A1:D5)` come formula attiva nella cartella di lavoro di output, in modo che il risultato si aggiorni automaticamente se i dati di origine cambiano, e il file Excel di destinazione verrà aperto in **Excel 365 / Excel 2021 o versioni successive** dove gli array dinamici e l'operatore di spill sono supportati.

### **API utilizzata**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` è un metodo di `Aspose.Cells.Cell` che imposta la formula della cella come una **formula di array dinamico**. Excel valuta la formula una volta ed espande automaticamente il risultato nelle celle circostanti. Il terzo parametro, quando impostato su `true`, indica ad Aspose.Cells di calcolare anche i valori risultanti al momento della scrittura.

### **Passaggi**
1. Caricare la cartella di lavoro di origine costruendo `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Recuperare il primo foglio di lavoro tramite `workbook.GetWorksheets().Get(0)` e accedere alla sua raccolta `Cells` tramite `worksheet.GetCells()`.
3. Inserire la formula di array dinamico nella cella **A6**, subito sotto l'intervallo di origine, chiamando `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. L'argomento `nullptr` passa i `FormulaParseOptions` predefiniti e il terzo argomento `true` indica ad Aspose.Cells di trattare la formula come array dinamico e di valutarla in modo che i valori espansi vengano scritti nella cartella di lavoro.
5. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.
La cella **A6** contiene la formula `=TRANSPOSE(A1:D5)` ed Excel espande automaticamente il risultato nella regione **A6:D10**, un blocco di 5 righe per 4 colonne pari ai dati trasposti.

{{% alert color="primary" %}}
Questo approccio funziona **solo su Excel 365 / 2021 o versioni successive**. Le versioni precedenti di Excel non espanderanno correttamente le formule di array dinamico.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approccio 3 — Trasporre con una formula matrice classica (CSE)**
Utilizzare questo approccio quando si desidera preservare una formula `TRANSPOSE` nella cartella di lavoro, ma il file Excel di destinazione potrebbe essere aperto in **versioni precedenti di Excel (pre-2021, incluse 2019, 2016, 2013 e così via)** dove l'espansione degli array dinamici non è supportata. La classica formula matrice CSE (Ctrl+Shift+Enter) è l'alternativa compatibile con le versioni legacy che tutte le versioni di Excel possono valutare.

### **API utilizzata**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` è un metodo di `Aspose.Cells.Cell` che assegna una **formula matrice (CSE) classica** alla cella di ancoraggio e dichiara le dimensioni dell'array risultante. Aspose.Cells scrive il marcatore di formula matrice multi-cella in modo che Excel valuti la formula come una singola espressione di array che riempie l'intervallo dichiarato.

### **Passaggi**
1. Caricare la cartella di lavoro di origine costruendo `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Recuperare il primo foglio di lavoro tramite `workbook.GetWorksheets().Get(0)` e accedere alla sua raccolta `Cells` tramite `worksheet.GetCells()`.
3. Chiamare `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. Il secondo argomento `4` è il numero di righe dell'array di destinazione e il terzo argomento `5` è il numero di colonne.
4. Salvare la cartella di lavoro con `workbook.Save(outputFile)`.
La cella **A6** è l'ancoraggio della formula matrice e l'array valutato si estende per 4 righe per 5 colonne a partire da A6, corrispondendo alle dimensioni trasposte dell'origine A1:D5. Excel scrive un singolo marcatore di formula matrice attraverso l'intervallo risultante in modo che le versioni precedenti di Excel lo valutino correttamente.

{{% alert color="primary" %}}
Le formule matrice CSE sono il modo classico di Excel per valutare un'espressione `TRANSPOSE` e questo approccio è universalmente compatibile tra tutte le versioni di Excel.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Carica la cartella di lavoro sorgente con LoadOptions xlsx
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Accedi al primo foglio di lavoro e alla sua collezione Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Imposta la classica formula in array CSE sulla cella A6.
    // La formula =TRANSPOSE(A1:D5) ruota l'intervallo sorgente di 5 righe x 4 colonne
    // in un array di 4 righe x 5 colonne. Il secondo argomento (4) è il numero di righe
    // e il terzo argomento (5) è il numero di colonne dell'array risultante.
    // Aspose.Cells scrive il marcatore di formula in array CSE così Excel la valuta come
    // una singola formula in array multi-cella, compatibile con le versioni meno recenti
    // di Excel (2019, 2016, 2013, ecc.) che non supportano lo spilling dinamico degli array.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Salva la cartella di lavoro così che il marcatore della formula in array venga persistito
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Confronto — Quando utilizzare ciascun approccio**
| Approccio | API / Metodo | Versione di Excel | Formula di origine preservata? | Intervallo di output |
|-----------|--------------|-------------------|-------------------------------|---------------------|
| Approccio 1 — Trasposizione in place | `Range.Transpose()` | Tutte le versioni di Excel | No (solo valori) | Intervallo di ancoraggio iniziale, 5×4 |
| Approccio 2 — Formula array dinamico | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Sì (si espande dinamicamente) | Espanso dall'ancoraggio |
| Approccio 3 — Formula matrice classica (CSE) | `Cell.SetArrayFormula` | Tutte le versioni di Excel | Sì (formula matrice multi-cella) | Dimensione esplicita, 4×5 |
Utilizzare l'**Approccio 1** quando serve una trasformazione rapida e compatibile tra versioni e si desidera solo che i valori trasposti vengano scritti nel file. Utilizzare l'**Approccio 2** quando Excel moderno è garantito e si vuole che la formula rimanga attiva e si aggiorni se l'origine cambia. Utilizzare l'**Approccio 3** quando serve la massima compatibilità con una formula preservata attraverso ogni versione di Excel, comprese le versioni precedenti che non supportano gli array dinamici.

## **Articoli correlati**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/it/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserimento di un'immagine in una cella](/cells/it/cpp/inserting-an-image-into-a-cell/)
- [Divisione di file Excel in più file](/cells/it/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}