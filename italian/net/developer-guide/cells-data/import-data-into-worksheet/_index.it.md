---
title: Importa i dati nel foglio di lavoro
type: docs
weight: 170
url: /it/net/import-data-into-worksheet/
description: Scopri come importare i dati nel foglio di lavoro tramite Aspose.Cells for .NET API.
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

Questo articolo illustra alcune tecniche di importazione dei dati a cui gli sviluppatori hanno accesso tramite il numero Aspose.Cells.

{{% /alert %}}

##  **Come importare i dati nel foglio di lavoro**

Quando apri un file Excel con Aspose.Cells, tutti i dati nel file vengono importati automaticamente. Aspose.Cells può importare dati anche da altre fonti dati.

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La raccolta fornisce metodi utili per importare dati da diverse origini dati. In questo articolo viene spiegato come utilizzare questi metodi.

##  **Come importare dati in Excel con l'interfaccia ICellsDataTable**
 Strumento[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) per racchiudere le varie origini dati, quindi utilizzare[Cells.ImportaDati()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) per importare i dati nel foglio di lavoro Excel.
###  **Codice d'esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

L'implementazione di*CustomerDataSource*, *Customer* e *CustomerList* le classi sono riportate di seguito

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **Come importare dati in Excel da un array**

 Per importare dati in un foglio di calcolo da un array, chiamare il file[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione. Esistono molte versioni sovraccaricate di[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)metodo ma un tipico sovraccarico accetta i seguenti parametri:

- *Array**, l'oggetto array da cui stai importando il contenuto.
- *Numero riga**, il numero di riga della prima cella in cui verranno importati i dati.
- *Numero colonna**, il numero di colonna della prima cella in cui verranno importati i dati.
- *È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **Come importare dati in Excel da ArrayList**

 Per importare dati da un file*Lista di array* ai fogli di lavoro, chiamare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)metodo. Il metodo ImportArray accetta i seguenti parametri:

-  *Elenco di array**, rappresenta il file*Lista di array*oggetto che stai importando.
- *Numero riga**, rappresenta il numero di riga della prima cella in cui verranno importati i dati.
- *Numero colonna**, rappresenta il numero di colonna della prima cella in cui verranno importati i dati.
- *È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **Come importare dati in Excel da oggetti personalizzati**

 Per importare dati da una raccolta di oggetti in un foglio di lavoro, utilizzare[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fornire un elenco di colonne/proprietà al metodo per visualizzare l'elenco di oggetti desiderato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **Come importare dati in Excel da oggetti personalizzati nell'area unita**

Per importare dati da una raccolta di oggetti in un foglio di lavoro contenente celle unite, utilizzare[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) proprietà. Se il modello Excel ha celle unite, imposta il valore di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)proprietà su true. Passa il[**ImportaOpzioniTabella**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) object insieme all'elenco di colonne/proprietà del metodo per visualizzare l'elenco di oggetti desiderato. Nell'esempio di codice seguente viene illustrato l'utilizzo di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) proprietà per importare dati da oggetti personalizzati in celle unite. Per favore vedere l'allegato[fonte Excel](90112033.xlsx) file e il[produrre Excel](90112034.xlsx) file per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **Come importare dati in Excel da DataTable**

Per importare dati da un *DataTable*, chiamare il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) metodo. Esistono molte versioni sovraccaricate di[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)metodo ma un tipico sovraccarico accetta i seguenti parametri:

-  *Tabella dati**, il*Tabella dati* oggetto da cui stai importando il contenuto.
-  *Viene visualizzato il nome del campo**, specifica se i nomi dei file*Tabella dati*le colonne devono essere importate nel foglio di lavoro come prima riga oppure no.
- *Cella iniziale**, rappresenta il nome della cella iniziale (ad esempio "A1") da cui importare il contenuto della *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **Come importare dati in Excel da un oggetto dinamico come origine dati**

Aspose.Cells fornisce funzionalità per lavorare con oggetti dinamici come origine dati. Aiuta nell'utilizzo dell'origine dati in cui le proprietà vengono aggiunte dinamicamente agli oggetti. Una volta aggiunte le proprietà all'oggetto, Aspose.Cells considera la prima voce come modello e gestisce il resto di conseguenza. Ciò significa che se qualche proprietà dinamica viene aggiunta solo al primo elemento e non ad altri oggetti, Aspose.Cells considera che tutti gli elementi della raccolta dovrebbero essere uguali.

In questo esempio viene utilizzato un modello modello che inizialmente contiene solo due variabili. Questo elenco viene convertito in elenco di oggetti dinamici. Quindi vengono aggiunti alcuni campi aggiuntivi e infine caricati nella cartella di lavoro. La cartella di lavoro seleziona solo i valori presenti nel file modello XLSX. Questa cartella di lavoro modello utilizza gli indicatori intelligenti che contengono anche parametri. I parametri consentono di modificare la modalità di presentazione delle informazioni. I dettagli sugli Smart Marker possono essere ottenuti dal seguente articolo:

[Utilizzo degli indicatori intelligenti](/cells/it/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **Come importare dati in Excel da DataColumn (.NET)**

A *Tabella dati*O*DataView*l'oggetto è composto da una o più colonne. Gli sviluppatori possono anche importare dati da qualsiasi colonna/colonne del file*Tabella dati*O*DataView*chiamando il[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione. IL[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)Il metodo accetta un parametro di tipo[**ImportaOpzioniTabella**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). IL[**ImportaOpzioniTabella**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) la classe fornisce a[**Indici di colonna**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)proprietà che accetta una serie di indici di colonne.

Il codice di esempio fornito di seguito illustra l'utilizzo di[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)per importare colonne selettive.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **Come importare dati in Excel da DataView (.NET)**

 Per importare dati da un *DataView*, chiamare il file[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metodo. Esistono molte versioni sovraccaricate di[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)metodo ma quello per DataView accetta i seguenti parametri:

- **Visualizzazione dati:** IL*DataView*oggetto da cui stai per importare il contenuto.
- **Prima riga:**il numero di riga della prima cella in cui verranno importati i dati.
- **Prima colonna:**il numero di colonna della prima cella in cui verranno importati i dati.
- **Opzioni ImportTabella:**Le opzioni di importazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **Come importare dati in Excel da DataGrid (.NET)**

 È possibile importare dati da a*DataGrid* chiamando il[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione. Esistono molte versioni sovraccaricate di[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)metodo ma un tipico sovraccarico accetta i seguenti parametri:

-  *Griglia dati**, il*DataGrid*oggetto da cui stai importando il contenuto.
- *Numero riga**, il numero di riga della prima cella in cui verranno importati i dati.
- *Numero colonna**, il numero di colonna della prima cella in cui verranno importati i dati.
- *Inserisci righe**, una proprietà booleana che indica se è necessario aggiungere righe aggiuntive al foglio di lavoro per adattare i dati o meno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **Come importare dati in Excel da GridView**

 Per importare dati da a*Vista a griglia* controllo, chiama il[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione.

Aspose.Cells ci consente di rispettare i valori formattati HTML durante l'importazione dei dati nel foglio di calcolo. Quando l'analisi HTML è abilitata durante l'importazione dei dati, Aspose.Cells converte HTML nella formattazione della cella corrispondente.

##  **Come importare i dati formattati HTML in Excel**

 Aspose.Cells fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe che fornisce metodi molto utili per importare dati da origini dati esterne. Questo articolo mostra come analizzare il testo formattato HTML durante l'importazione di dati e convertire HTML in valori di cella formattati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **Come importare dati in Excel da JSON**

Aspose.Cells fornisce a[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classe per l'elaborazione JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la classe ha un[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) metodo per importare i dati JSON. Aspose.Cells fornisce anche a[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classe che rappresenta le opzioni del layout JSON. IL[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)metodo accetta[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)come parametro. IL[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)La classe fornisce le seguenti proprietà.

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): indica che l'array deve essere elaborato come tabella o meno.
- [**ConvertiNumeriCOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Ottiene o imposta un valore che indica se la stringa in JSON deve essere convertita in numerico o in data.
- [**Formato data**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ottiene e imposta il formato del valore della data.
- [**IgnoraArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un array
- [**Ignora Null**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica se il valore null deve essere ignorato o meno.
- [**Ignora TitoloOggetto**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un oggetto.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ottiene e imposta il formato del valore numerico.
- [**TitoloStile**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ottiene e imposta lo stile del titolo.

Il codice di esempio fornito di seguito dimostra l'utilizzo di[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) E[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)classi per importare i dati JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **Argomenti avanzati**
- [Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro](/cells/it/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Sposta la prima riga verso il basso quando inserisci le righe della tabella dati Cells](/cells/it/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
