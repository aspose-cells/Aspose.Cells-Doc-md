---
title: Gestire i dati dei file Excel
linktitle: Cells Dati
type: docs
weight: 110
url: /it/net/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file Excel con la libreria Aspose.Cells.
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

 In[Accesso allo Cells di un foglio di lavoro](/cells/it/net/accessing-cells-of-a-worksheet/), abbiamo discusso gli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di questi approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

##  **Come aggiungere dati a Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells consente agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il file[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metodo. Aspose.Cells fornisce versioni sovraccaricate di[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metodo che consente agli sviluppatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate di[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metodo, è possibile aggiungere alla cella un valore booleano, stringa, double, intero o data/ora, ecc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **Come migliorare l'efficienza**

 Se usi[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Per inserire una grande quantità di dati in un foglio di lavoro, è necessario aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle tue applicazioni.

##  **Come recuperare i dati da Cells**

 Aspose.Cells fornisce una lezione,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Ogni elemento in[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la raccolta rappresenta un oggetto del[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 IL[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)La classe fornisce diverse proprietà che consentono agli sviluppatori di recuperare valori dalle celle in base ai tipi di dati. Queste proprietà includono:

- [**Valore stringa**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): restituisce il valore stringa della cella.
- [**DoppioValore**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): restituisce il doppio valore della cella.
- [**BoolValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): restituisce il valore booleano della cella.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): restituisce il valore data/ora della cella.
- [**ValoreFloat**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): restituisce il valore float della cella.
- [**ValoreInt**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): restituisce il valore intero della cella.

 Quando un campo non è riempito, le celle con[**DoppioValore**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) O[**ValoreFloat**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)genera un'eccezione.

 Il tipo di dati contenuti in una cella può essere verificato anche utilizzando il comando[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe'[**Tipo**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) proprietà. In effetti, il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe'[**Tipo**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) la proprietà si basa su[**TipoValoreCella**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)enumerazione i cui valori predefiniti sono elencati di seguito:

|**Cell Tipi di valore**|**Descrizione**|
| :- | :- |
|IsBool|Specifica che il valore della cella è booleano.|
|IsDateTime|Specifica che il valore della cella è data/ora.|
|È zero|Rappresenta una cella vuota.|
|È numerico|Specifica che il valore della cella è numerico.|
|IsString|Specifica che il valore della cella è una stringa.|
|È sconosciuto|Specifica che il valore della cella è sconosciuto.|

È inoltre possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontarli con il Tipo di dati presenti in ciascuna cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Mentre lavorano sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi tipi di dati possono includere valori booleani, interi, a virgola mobile, testo o valori di data/ora. Con Aspose.Cells puoi ottenere i valori appropriati dalle celle in base al loro tipo di dati.

{{% /alert %}}

##  **Argomenti avanzati**
- [Accesso allo Cells di un foglio di lavoro](/cells/it/net/accessing-cells-of-a-worksheet/)
- [Converti dati numerici di testo in numeri](/cells/it/net/convert-text-numeric-data-to-number/)
- [Creazione di totali parziali](/cells/it/net/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/net/data-filtering/)
- [Ordinamento dei dati](/cells/it/net/sort-data-of-excel/)
- [Convalida dei dati](/cells/it/net/data-validation/)
- [Esporta dati dal foglio di lavoro](/cells/it/net/export-data-from-worksheet/)
- [Trova o cerca dati](/cells/it/net/find-or-search-data/)
- [Ottieni il valore stringa Cell con e senza formattazione](/cells/it/net/get-cell-string-value-with-and-without-formatting/)
- [Aggiunta di HTML Rich Text all'interno di Cell](/cells/it/net/adding-html-rich-text-inside-the-cell/)
- [Inserisci collegamenti ipertestuali in Excel o OpenOffice](/cells/it/net/insert-hyperlinks-to-excel/)
- [Importa i dati nel foglio di lavoro](/cells/it/net/import-data-into-worksheet/)
- [Come e dove utilizzare gli enumeratori](/cells/it/net/how-and-where-to-use-enumerators/)
- [Misura la larghezza e l'altezza del valore Cell in unità di pixel](/cells/it/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lettura dei valori Cell in più thread contemporaneamente](/cells/it/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversione tra il nome della cella e l'indice di riga/colonna](/cells/it/net/names-and-indices/)
- [Compilare i dati prima per riga e poi per colonna](/cells/it/net/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso delle virgolette singole del valore o intervallo Cell](/cells/it/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedi e aggiorna le parti del Rich Text di Cell](/cells/it/net/access-and-update-the-portions-of-rich-text-of-cell/)



