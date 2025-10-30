---
title: Gestire i dati dei file di Excel
linktitle: Dati delle celle
type: docs
weight: 110
url: /it/nodejs-cpp/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file Excel con la libreria Aspose.Cells per Node.js tramite C++.
keywords: Aspose.Cells Node.js tramite C++, Gestione dei dati del file Excel, aggiungere dati al file Excel, ottenere dati dal file Excel, Come Migliorare l’Efficienza dell’aggiunta di dati, gestire i dati delle celle, aggiornare i dati delle celle, ottenere i dati delle celle, inserire i dati nelle celle
---

{{% alert color="primary" %}}

In [Accesso alle Celle di un Foglio di Lavoro](/cells/it/nodejs-cpp/accessing-cells-of-a-worksheet/), abbiamo discusso gli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

## **Come aggiungere dati alle celle**

Aspose.Cells for Node.js via C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Aspose.Cells offre versioni sovrapposte del metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) che permettono di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovrapposte del metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-), è possibile aggiungere valori booleani, stringhe, double, interi o data/ora, ecc. alle celle.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-AddDataToCells.js" >}}


## **Come migliorare l'efficienza**

Se si utilizza il metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) per inserire una grande quantità di dati in un foglio di lavoro, si dovrebbe prima aggiungere i valori alle celle riga per riga e poi colonna per colonna. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

## **Come recuperare i dati dalle celle**

Aspose.Cells for Node.js via C++ fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che permette l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) fornisce diverse proprietà che permettono agli sviluppatori di recuperare valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [**getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--): restituisce il valore stringa della cella.
- [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--): restituisce il valore double della cella.
- [**getBoolValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getBoolValue--): restituisce il valore booleano della cella.
- [**getDateTimeValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDateTimeValue--): restituisce il valore data/ora della cella.
- [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--): restituisce il valore float della cella.
- [**getIntValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getIntValue--): restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [**getDoubleValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDoubleValue--) o [**getFloatValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFloatValue--) generano un'eccezione.

Il tipo di dati contenuti in una cella può essere verificato anche utilizzando il metodo [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). In realtà, il metodo [**getType()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getType--) della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) si basa sull'enumerazione [**CellValueType**](https://reference.aspose.com/cells/nodejs-cpp/cellvaluetype) i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|IsBool| Specifica che il valore della cella è booleano.
|IsDateTime| Specifica che il valore della cella è data/ora.
|IsNull| Rappresenta una cella vuota.
|IsNumeric| Specifica che il valore della cella è numerico.
|IsString| Specifica che il valore della cella è una stringa.
|IsUnknown| Specifica che il valore della cella è sconosciuto.

È anche possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontare con il tipo di dati presente in ogni cella.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-RetrieveDataFromCells.js" >}}


{{% alert color="primary" %}}

Durante il lavoro sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi tipi di dati possono includere valori booleani, interi, in virgola mobile, testo o dati data/ora. Con Aspose.Cells, puoi ottenere i valori appropriati dalle celle in base ai loro tipi di dati.

{{% /alert %}}

## **Argomenti avanzati**
- [Accesso alle celle di un foglio di lavoro](/cells/it/nodejs-cpp/accessing-cells-of-a-worksheet/)
- [Converti Dati Numerici Testuali in Numero](/cells/it/nodejs-cpp/convert-text-numeric-data-to-number/)
- [Creare i Subtotali](/cells/it/nodejs-cpp/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/nodejs-cpp/data-filtering/)
- [Ordinamento dati](/cells/it/nodejs-cpp/sort-data-of-excel/)
- [Convalida Dati](/cells/it/nodejs-cpp/data-validation/)
- [Trova o cerca dati](/cells/it/nodejs-cpp/find-or-search-data/)
- [Ottieni il valore stringa della cella con e senza formattazione](/cells/it/nodejs-cpp/get-cell-string-value-with-and-without-formatting/)
- [Aggiunta di testo ricco in formato HTML all'interno della cella](/cells/it/nodejs-cpp/adding-html-rich-text-inside-the-cell/)
- [Inserimento di collegamenti ipertestuali in Excel o OpenOffice](/cells/it/nodejs-cpp/insert-hyperlinks-to-excel/)
- [Come e dove utilizzare gli enumeratori](/cells/it/nodejs-cpp/how-and-where-to-use-enumerators/)
- [Misurare la larghezza e l'altezza del valore della cella in unità di pixel](/cells/it/nodejs-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lettura dei valori della cella in più thread contemporaneamente](/cells/it/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversione tra nome della cella e indice riga/colonna](/cells/it/nodejs-cpp/names-and-indices/)
- [Popolare prima i dati per riga e poi per colonna](/cells/it/nodejs-cpp/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedere e aggiornare le porzioni di testo arricchito della cella](/cells/it/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="nodejs-cpp" >}}
