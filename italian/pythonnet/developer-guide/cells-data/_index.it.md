---
title: Gestire i dati dei file di Excel
linktitle: Dati delle celle
type: docs
weight: 110
url: /it/python-net/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file Excel con la libreria Aspose.Cells for Python via .NET.
keywords: Libreria Python Excel, Aspose.Cells for Python Gestisce dati del file Excel, Python aggiunge dati al file Excel, Python ottiene dati dal file Excel, Python Come migliorare l efficienza dell aggiunta di dati, Python gestisce dati delle celle, Python aggiorna dati delle celle, Python ottiene dati delle celle, Python inserisce dati delle celle.
---

{{% alert color="primary" %}}

In [Accesso alle celle di un foglio di lavoro](/cells/it/python-net/accessing-cells-of-a-worksheet/), abbiamo discusso degli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di quegli approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

## **Come aggiungere dati alle celle**

Aspose.Cells for Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells for Python via .NET consente ai programmatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Aspose.Cells for Python via .NET fornisce versioni sovraccaricate del metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) che consentono ai programmatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate del metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int), è possibile aggiungere valori booleani, stringhe, numeri in virgola mobile, interi o data/ora, ecc. alla cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-AddingDataToCells-1.py" >}}

## **Come migliorare l'efficienza**

Se si utilizza il metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#int) per inserire una grande quantità di dati in un foglio di lavoro, è consigliabile aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

## **Come recuperare i dati dalle celle**

Aspose.Cells for Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/). Ogni elemento nella collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) fornisce diverse proprietà che consentono agli sviluppatori di recuperare i valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [**string_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/string_value/): restituisce il valore di stringa della cella.
- [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/): restituisce il valore decimale della cella.
- [**bool_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/bool_value/): restituisce il valore booleano della cella.
- [**date_time_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/date_time_value/): restituisce il valore data/ora della cella.
- [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/): restituisce il valore in virgola mobile della cella.
- [**int_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/int_value/): restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [**double_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/double_value/) o [**float_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/float_value/) generano un'eccezione.

Il tipo di dati contenuti in una cella può anche essere verificato utilizzando la proprietà [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Infatti, la proprietà [**type**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/type/) della classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) si basa sull'enumerazione [**CellValueType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvaluetype), i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|IS_BOOL| Specifica che il valore della cella è Booleano.
|IS_DATE_TIME| Specifica che il valore della cella è data/ora.
|IS_NULL| Rappresenta una cella vuota.
|IS_NUMERIC| Specifica che il valore della cella è numerico.
|IS_STRING| Specifica che il valore della cella è una stringa.
|IS_ERROR| Specifica che il valore della cella è un valore di errore.
|IS_UNKNOWN| Specifica che il valore della cella è sconosciuto.

È anche possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontare con il tipo di dati presente in ogni cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-RetrievingDataFromCells-1.py" >}}

{{% alert color="primary" %}}

Mentre si lavora sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati alle celle. Questi tipi di dati possono includere valori booleani, interi, numeri in virgola mobile, testo o valori di data/ora. Con Aspose.Cells for Python via .NET, è possibile ottenere i valori appropriati dalle celle in base ai loro tipi di dati.

{{% /alert %}}

## **Argomenti avanzati**
- [Accesso alle celle di un foglio di lavoro](/cells/it/python-net/accessing-cells-of-a-worksheet/)
- [Converti Dati Numerici Testuali in Numero](/cells/it/python-net/convert-text-numeric-data-to-number/)
- [Creare i Subtotali](/cells/it/python-net/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/python-net/data-filtering/)
- [Ordinamento dati](/cells/it/python-net/sort-data-of-excel/)
- [Convalida Dati](/cells/it/python-net/data-validation/)
- [Ottieni il valore stringa della cella con e senza formattazione](/cells/it/python-net/get-cell-string-value-with-format-strategy/)
- [Aggiunta di testo ricco in formato HTML all'interno della cella](/cells/it/python-net/adding-html-rich-text-inside-the-cell/)
- [Trova o cerca dati](/cells/it/python-net/find-or-search-data/)
- [Inserimento di collegamenti ipertestuali in Excel o OpenOffice](/cells/it/python-net/insert-hyperlinks-to-excel/)
- [Misurare la larghezza e l'altezza del valore della cella in unità di pixel](/cells/it/python-net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Conversione tra nome della cella e indice riga/colonna](/cells/it/python-net/names-and-indices/)
- [Popolare prima i dati per riga e poi per colonna](/cells/it/python-net/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/python-net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedere e aggiornare le porzioni di testo arricchito della cella](/cells/it/python-net/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="python-net" >}}
