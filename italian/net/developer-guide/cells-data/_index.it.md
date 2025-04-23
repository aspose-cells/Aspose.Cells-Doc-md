---
title: Gestire i dati dei file di Excel
linktitle: Dati delle celle
type: docs
weight: 110
url: /it/net/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file di Excel con la libreria Aspose.Cells.
keywords: Aspose.Cells C# Gestisci i dati del file Excel, aggiungi dati al file Excel, ottieni dati dal file Excel, Come migliorare l efficienza dell aggiunta di dati, gestisci i dati delle celle, aggiorna i dati delle celle, ottieni i dati delle celle, inserisci i dati delle celle
---

{{% alert color="primary" %}}

In [Accesso alle celle di un foglio di lavoro](/celle/it/net/accesso-alle-celle-di-un-foglio-di-lavoro/), abbiamo discusso dei metodi di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di quei metodi per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

## **Come aggiungere dati alle celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ogni elemento della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)

Aspose.Cells permette agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Aspose.Cells fornisce versioni sovraccaricate del metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) che consentono agli sviluppatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate del metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index), è possibile aggiungere valori booleani, stringhe, doppie, interi o valori data/ora, ecc. alla cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

## **Come migliorare l'efficienza**

Se si utilizza il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) per inserire una grande quantità di dati in un foglio di lavoro, è consigliabile aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

## **Come recuperare i dati dalle celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) fornisce diverse proprietà che consentono agli sviluppatori di recuperare i valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): restituisce il valore di stringa della cella.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): restituisce il valore decimale della cella.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): restituisce il valore booleano della cella.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): restituisce il valore data/ora della cella.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): restituisce il valore in virgola mobile della cella.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) o [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue) generano un'eccezione.

Il tipo di dati contenuti in una cella può anche essere verificato utilizzando la proprietà [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Infatti, la proprietà [**Type**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) della classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) si basa sull'enumerazione [**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype), i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|IsBool| Specifica che il valore della cella è booleano.
|IsDateTime| Specifica che il valore della cella è data/ora.
|IsNull| Rappresenta una cella vuota.
|IsNumeric| Specifica che il valore della cella è numerico.
|IsString| Specifica che il valore della cella è una stringa.
|IsUnknown| Specifica che il valore della cella è sconosciuto.

È anche possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontare con il tipo di dati presente in ogni cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Durante il lavoro sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi tipi di dati possono includere valori booleani, interi, in virgola mobile, testo o data/ora. Con Aspose.Cells, è possibile ottenere i valori appropriati dalle celle in base ai loro tipi di dati.

{{% /alert %}}

## **Argomenti avanzati**
- [Accesso alle celle di un foglio di lavoro](/cells/it/net/accessing-cells-of-a-worksheet/)
- [Converti Dati Numerici Testuali in Numero](/cells/it/net/convert-text-numeric-data-to-number/)
- [Creare i Subtotali](/cells/it/net/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/net/data-filtering/)
- [Ordinamento dati](/cells/it/net/sort-data-of-excel/)
- [Convalida Dati](/cells/it/net/data-validation/)
- [Esporta dati dalla scheda di lavoro](/cells/it/net/export-data-from-worksheet/)
- [Trova o cerca dati](/cells/it/net/find-or-search-data/)
- [Ottieni il valore stringa della cella con e senza formattazione](/cells/it/net/get-cell-string-value-with-and-without-formatting/)
- [Aggiunta di testo ricco in formato HTML all'interno della cella](/cells/it/net/adding-html-rich-text-inside-the-cell/)
- [Inserimento di collegamenti ipertestuali in Excel o OpenOffice](/cells/it/net/insert-hyperlinks-to-excel/)
- [Importazione di dati nella scheda di lavoro](/cells/it/net/import-data-into-worksheet/)
- [Come e dove utilizzare gli enumeratori](/cells/it/net/how-and-where-to-use-enumerators/)
- [Misurare la larghezza e l'altezza del valore della cella in unità di pixel](/cells/it/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lettura dei valori della cella in più thread contemporaneamente](/cells/it/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversione tra nome della cella e indice riga/colonna](/cells/it/net/names-and-indices/)
- [Popolare prima i dati per riga e poi per colonna](/cells/it/net/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedere e aggiornare le porzioni di testo arricchito della cella](/cells/it/net/access-and-update-the-portions-of-rich-text-of-cell/)



{{< app/cells/assistant language="csharp" >}}
