---
title: Importare i dati nel foglio di lavoro
type: docs
weight: 170
url: /it/net/import-data-into-worksheet/
description: Imparare come importare i dati nel foglio di lavoro tramite l API Aspose.Cells for .NET.
keywords: C# Importa dati nel foglio di lavoro, importa dati in Excel con l interfaccia ICellsDataTable, importa dati da Array, importa dati da ArrayList, importa dati da Oggetti Personalizzati, importa dati da Oggetti Personalizzati in un area unita, importa dati da DataTable, importa dati da un oggetto dinamico come origine dati, importa dati da DataColumn, importa dati da DataView, importa dati da DataGrid, importa dati da GridView, importa dati formattati in HTML, importa dati da JSON.
---

{{% alert color="primary" %}}

Questo articolo discute alcune tecniche di importazione dati a cui i programmatori hanno accesso attraverso Aspose.Cells.

{{% /alert %}}

## **Come importare dati nel foglio di lavoro**

Quando si apre un file Excel con Aspose.Cells, tutti i dati nel file vengono automaticamente importati. Aspose.Cells può anche importare dati da altre fonti di dati.

Aspose.Cells fornisce una classe che rappresenta un file Microsoft Excel. Tale classe contiene una collezione che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe. La classe fornisce una collezione che fornisce metodi utili per importare dati da diverse fonti di dati. Questo articolo spiega come utilizzare questi metodi.

## **Come importare dati in Excel con l'interfaccia ICellsDataTable**
Implementare [ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) per incapsulare varie fonti dati, quindi utilizzare [Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) per importare i dati nel foglio di lavoro di Excel.
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

Di seguito è riportata l'implementazione delle classi *CustomerDataSource*, *Customer* e *CustomerList*

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Come importare dati in Excel da Array**

Per importare dati in un foglio di calcolo da un array, chiamare il metodo [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ci sono molte versioni sovraccaricate del metodo [**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) ma tipicamente una versione sovraccaricata richiede i seguenti parametri:

- **Array**, l'oggetto array da cui si sta importando il contenuto.
- **Numero di riga**, il numero di riga della prima cella in cui saranno importati i dati.
- **Numero di colonna**, il numero di colonna della prima cella in cui saranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Come importare dati in Excel da ArrayList**

Per importare dati da un *ArrayList* nei fogli di lavoro, chiamare il metodo [**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo ImportArray richiede i seguenti parametri:

- **Array list**, rappresenta l'oggetto *ArrayList* che si sta importando.
- **Numero di riga**, rappresenta il numero di riga della prima cella in cui saranno importati i dati.
- **Numero di colonna**, rappresenta il numero di colonna della prima cella in cui saranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Come importare i dati in Excel da oggetti personalizzati**

Per importare i dati da una raccolta di oggetti in un foglio di lavoro, utilizzare [**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fornire un elenco di colonne/proprietà al metodo per visualizzare l'elenco desiderato di oggetti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Come importare i dati in Excel da oggetti personalizzati e verificare l'area unita**

Per importare i dati da una raccolta di oggetti in un foglio di lavoro contenente celle unite, utilizzare la proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells). Se il modello di Excel ha celle unite, impostare il valore della proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) su true. Passare l'oggetto [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) insieme all'elenco di colonne/proprietà al metodo per visualizzare l'elenco desiderato di oggetti. Il seguente esempio di codice dimostra l'uso della proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) per importare i dati da oggetti personalizzati in celle unite. Si prega di consultare il file di Excel [origine](90112033.xlsx) e il file di Excel [output](90112034.xlsx) per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Come importare i dati in Excel da un DataTable**

Per importare i dati da un *DataTable*, chiamare il metodo [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ci sono molte versioni sovraccaricate del metodo [**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) ma una tipica sovraccarica i seguenti parametri:

- **Tabella dati**, l'oggetto *DataTable* da cui si sta importando il contenuto.
- **Mostra il nome del campo**, specifica se i nomi delle colonne del *DataTable* dovrebbero essere importati nel foglio di lavoro come prima riga o meno.
- **Cella di inizio**, rappresenta il nome della cella di inizio (ad esempio "A1") da cui importare i contenuti del *DataTable*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Come importare i dati in Excel da un oggetto dinamico come origine dati**

Aspose.Cells fornisce funzionalità per lavorare con oggetti dinamici come origine dati. Aiuta nell'uso dell'origine dati in cui le proprietà vengono aggiunte in modo dinamico agli oggetti. Una volta che le proprietà vengono aggiunte all'oggetto, Aspose.Cells considera la prima voce come modello e gestisce il resto di conseguenza. Significa che se una proprietà dinamica viene aggiunta solo a un primo elemento e non agli altri oggetti, Aspose.Cells considera che tutte le voci nella raccolta devono essere uguali.

In questo esempio, viene utilizzato un modello di template che inizialmente contiene solo due variabili. Questo elenco viene convertito in elenco di oggetti dinamici. Quindi alcuni campi aggiuntivi vengono aggiunti e infine caricati nel foglio di lavoro. Il foglio di lavoro rileva solo quei valori che sono nel file XLSX template. Questo foglio di lavoro modello utilizza Smart Markers che contengono anche parametri. I parametri ti consentono di modificare come le informazioni sono disposte. I dettagli sui Smart Markers possono essere ottenuti dal seguente articolo:

[Utilizzo dei Smart Markers](/cells/it/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Come importare una DataColumn in Excel**

Un oggetto *DataTable* o *DataView* è composto da una o più colonne. Gli sviluppatori possono anche importare dati da qualsiasi colonna/colonne del *DataTable* o *DataView* chiamando il metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) accetta un parametro di tipo [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). La classe [**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) fornisce una proprietà [**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) che accetta un array di indici di colonne.

Il codice di esempio fornito di seguito dimostra l'uso di [**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) per importare colonne selettive.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Come importare un DataView in Excel**

Per importare i dati da un *DataView*, chiamare il metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ci sono molte versioni sovraccaricate del metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) ma quella per DataView prende i seguenti parametri:

- **DataView:** L'oggetto *DataView* da cui stai per importare il contenuto.
- **Prima riga:** il numero di riga della prima cella in cui i dati verranno importati.
- **Prima colonna:** il numero di colonna della prima cella in cui i dati verranno importati.
- **OpzioniImportaTabella:** Le opzioni di importazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Come importare DataGrid in Excel**

È possibile importare i dati da un *DataGrid* chiamando il metodo [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Ci sono molte versioni sovraccaricate del metodo [**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index), ma un sovraccarico tipico richiede i seguenti parametri:

- **Data grid**, l'oggetto *DataGrid* da cui si sta importando il contenuto.
- **Numero di riga**, il numero di riga della prima cella in cui i dati verranno importati.
- **Numero di colonna**, il numero di colonna della prima cella in cui i dati verranno importati.
- **Inserisci righe**, una proprietà booleana che indica se devono essere aggiunte righe aggiuntive al foglio di lavoro per adattare i dati o meno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Come importare GridView in Excel**

Per importare i dati da un controllo *GridView*, chiamare il metodo [**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells).

Aspose.Cells ci consente di rispettare valori formattati in HTML durante l'importazione dei dati nel foglio di calcolo. Quando il parsing HTML è abilitato durante l'importazione dei dati, Aspose.Cells converte l'HTML in formattazione di celle corrispondenti.

## **Come importare dati formattati in HTML in Excel**

Aspose.Cells fornisce una classe [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) che fornisce metodi molto utili per l'importazione di dati da fonti di dati esterne. Questo articolo mostra come analizzare il testo formattato in HTML durante l'importazione dei dati e convertire l'HTML in valori di celle formattati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Come importare i dati in Excel da JSON**

Aspose.Cells fornisce una classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) per l'elaborazione di JSON. La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) ha un metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) per l'importazione di dati JSON. Aspose.Cells fornisce anche una classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) che rappresenta le opzioni di layout JSON. Il metodo [**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) accetta [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) come parametro. La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) fornisce le seguenti proprietà:

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): Indica se l'array deve essere elaborato come una tabella o meno.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Ottiene o imposta un valore che indica se la stringa in JSON deve essere convertita in numerico o data.
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ottiene e imposta il formato del valore della data.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un array.
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica se il valore nullo deve essere ignorato o meno.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un oggetto.
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ottiene e imposta il formato del valore numerico.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ottiene e imposta lo stile del titolo.

Il codice di esempio riportato di seguito dimostra l'uso delle classi [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) e [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) per importare i dati JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Argomenti avanzati**
- [Specifica i campi di formula durante l'importazione dei dati nel foglio di lavoro.](/cells/it/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Sposta la prima riga in basso durante l'inserimento di righe tabella dati della tabella dati.](/cells/it/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
