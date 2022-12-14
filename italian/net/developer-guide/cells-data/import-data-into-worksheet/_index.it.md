---
title: Importa i dati nel foglio di lavoro
type: docs
weight: 170
url: /it/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

Questo articolo discute alcune tecniche di importazione dei dati a cui gli sviluppatori hanno accesso tramite Aspose.Cells.

{{% /alert %}}

## **Importa i dati nel foglio di lavoro**

Quando apri un file Excel con Aspose.Cells, tutti i dati nel file vengono importati automaticamente. Aspose.Cells può anche importare dati da altre fonti di dati.

Aspose.Cells fornisce a[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fornisce metodi utili per importare dati da diverse origini dati. Questo articolo spiega come utilizzare questi metodi.

## **Importazione dati int Excel con interfaccia ICellsDataTable**
 Strumento[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable) per eseguire il wrapping delle varie origini dati, quindi utilizzare[Cells.ImportaDati()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata) per importare i dati nel foglio di lavoro di Excel.
### **Codice di esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

L'implementazione di*CustomerDataSource*, *Cliente*, e*Elenco clienti* classi è riportato di seguito

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **Importazione dall'array**

 Per importare i dati in un foglio di calcolo da un array, chiama il metodo[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Esistono molte versioni sovraccaricate di[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)metodo ma un sovraccarico tipico accetta i seguenti parametri:

- **Vettore**, l'oggetto array da cui stai importando il contenuto.
- **Numero di riga**il numero di riga della prima cella in cui verranno importati i dati.
- **Numero di colonna**, il numero di colonna della prima cella in cui verranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **Importazione da ArrayList**

 Per importare i dati da un file*Lista di array* ai fogli di lavoro, chiamare il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) della collezione[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)metodo. Il metodo ImportArray accetta i seguenti parametri:

- **Lista di array** , rappresenta il*Lista di array*oggetto che stai importando.
- **Numero di riga**, rappresenta il numero di riga della prima cella in cui verranno importati i dati.
- **Numero di colonna**, rappresenta il numero di colonna della prima cella in cui verranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **Importazione da oggetti personalizzati**

 Per importare dati da una raccolta di oggetti in un foglio di lavoro, utilizzare[**Importa oggetti personalizzati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index). Fornire un elenco di colonne/proprietà al metodo per visualizzare l'elenco di oggetti desiderato.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **Importazione da oggetti personalizzati nell'area unita**

Per importare dati da una raccolta di oggetti in un foglio di lavoro contenente celle unite, utilizzare[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) proprietà. Se il modello di Excel ha celle unite, impostare il valore di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)proprietà su true. Passa il[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) oggetto insieme all'elenco di colonne/proprietà al metodo per visualizzare l'elenco di oggetti desiderato. L'esempio di codice seguente illustra l'utilizzo di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells) proprietà per importare i dati dagli oggetti personalizzati alle celle unite. Per favore vedere l'allegato[fonte Excel](90112033.xlsx) file e il[uscita Excel](90112034.xlsx) file per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **Importazione da DataTable**

 Per importare dati da a*Tabella dati* , chiama il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) della collezione[**Importa tabella dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index) metodo. Esistono molte versioni sovraccaricate di[**Importa tabella dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)metodo ma un sovraccarico tipico accetta i seguenti parametri:

- **Tabella dati** , il*Tabella dati* oggetto da cui stai importando il contenuto.
- **Viene visualizzato il nome del campo** , specifica se i nomi di*Tabella dati*le colonne devono essere importate nel foglio di lavoro come prima riga o meno.
- **Inizio cella** rappresenta il nome della cella iniziale (ad esempio "A1") da cui importare il contenuto della*Tabella dati*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Importazione da oggetto dinamico come origine dati**

Aspose.Cells fornisce funzionalità per lavorare con oggetti dinamici come origine dati. Aiuta a utilizzare l'origine dati in cui le proprietà vengono aggiunte dinamicamente agli oggetti. Una volta aggiunte le proprietà all'oggetto, Aspose.Cells considera la prima voce come modello e gestisce il resto di conseguenza. Significa che se una proprietà dinamica viene aggiunta solo a un primo elemento e non ad altri oggetti, Aspose.Cells considera che tutti gli elementi nella raccolta dovrebbero essere uguali.

In questo esempio viene utilizzato un modello modello che inizialmente contiene solo due variabili. Questo elenco viene convertito in elenco di oggetti dinamici. Quindi viene aggiunto un campo aggiuntivo e infine caricato nella cartella di lavoro. La cartella di lavoro seleziona solo i valori che si trovano nel file XLSX del modello. Questa cartella di lavoro modello utilizza marcatori intelligenti che contengono anche parametri. I parametri consentono di modificare la disposizione delle informazioni. I dettagli sugli Smart Marker possono essere ottenuti dal seguente articolo:

[Utilizzo di marcatori intelligenti](/cells/it/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **Importazione da DataColumn (.NET)**

UN*Tabella dati*o*Visualizzazione dati*oggetto è composto da una o più colonne. Gli sviluppatori possono anche importare dati da qualsiasi colonna/colonne del file*Tabella dati*o*Visualizzazione dati*chiamando il[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione. Il[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)Il metodo accetta un parametro di tipo[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions). Il[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions) la classe fornisce a[**Indici di colonna**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)proprietà che accetta un array di indici di colonne.

Il codice di esempio fornito di seguito dimostra l'uso di[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes) per importare colonne selettive.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **Importazione da DataView (.NET)**

 Per importare dati da a*Visualizzazione dati* , chiama il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) della collezione[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index) metodo. Esistono molte versioni sovraccaricate di[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)metodo ma quello per DataView accetta i seguenti parametri:

- **Visualizzazione dati:** Il*Visualizzazione dati*oggetto da cui stai per importare il contenuto.
- **Prima riga:**il numero di riga della prima cella in cui verranno importati i dati.
- **Prima colonna:**il numero di colonna della prima cella in cui verranno importati i dati.
- **Opzioni ImportTable:**Le opzioni di importazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **Importazione da DataGrid (.NET)**

 È possibile importare dati da a*DataGrid* chiamando il[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. Esistono molte versioni sovraccaricate di[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)metodo ma un sovraccarico tipico accetta i seguenti parametri:

- **Griglia dati** , il*DataGrid*oggetto da cui stai importando il contenuto.
- **Numero riga**il numero di riga della prima cella in cui verranno importati i dati.
- **Numero di colonna**, il numero di colonna della prima cella in cui verranno importati i dati.
- **Inserisci righe**, una proprietà booleana che indica se è necessario aggiungere righe aggiuntive al foglio di lavoro per adattare o meno i dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **Importazione da GridView**

 Per importare dati da a*Vista a griglia* controllo, chiamare il[**ImportaGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione.

Aspose.Cells ci consente di rispettare i valori in formato HTML durante l'importazione dei dati nel foglio di calcolo. Quando l'analisi HTML è abilitata durante l'importazione dei dati, Aspose.Cells converte l'HTML nella formattazione della cella corrispondente.

## **Importazione di dati in formato HTML**

 Aspose.Cells fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)classe che fornisce metodi molto utili per l'importazione di dati da origini dati esterne. Questo articolo mostra come analizzare il testo in formato HTML durante l'importazione dei dati e convertire l'HTML in valori di cella formattati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **Importazione di dati da JSON**

Aspose.Cells fornisce a[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) classe per l'elaborazione di JSON.[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) la classe ha un[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata) metodo per l'importazione di dati JSON. Aspose.Cells fornisce anche a[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classe che rappresenta le opzioni del layout JSON. Il[**Importa dati**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)metodo accetta[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)come parametro. Il[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)class fornisce le seguenti proprietà.

- [**ArrayComeTabella**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): indica che l'array deve essere elaborato come tabella o meno.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): Ottiene o imposta un valore che indica se la stringa in JSON deve essere convertita in numerico o data.
- [**Formato data**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat): Ottiene e imposta il formato del valore della data.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un array
- [**IgnoraNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull): Indica se il valore null deve essere ignorato o meno.
- [**IgnoraTitoloOggetto**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un oggetto.
- [**NumeroFormato**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): Ottiene e imposta il formato del valore numerico.
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle): Ottiene e imposta lo stile del titolo.

Il codice di esempio fornito di seguito illustra l'uso di[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) e[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) classi per importare dati JSON.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **Argomenti avanzati**
- [Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro](/cells/it/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Sposta la prima riga verso il basso quando inserisci le righe della tabella dati Cells](/cells/it/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
