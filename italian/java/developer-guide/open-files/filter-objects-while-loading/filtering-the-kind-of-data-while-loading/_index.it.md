---
title: Filtraggio del tipo di dati durante il caricamento della cartella di lavoro dal file modello
type: docs
weight: 680
url: /it/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 A volte, si desidera specificare quale tipo di dati deve essere caricato durante la creazione della cartella di lavoro da un file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per il tuo scopo speciale, specialmente durante l'utilizzo[API di LightCells](/cells/it/java/using-lightcells-api/) . Si prega di utilizzare il[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) proprietà a tale scopo.

{{% /alert %}} 
## **Filtraggio del tipo di dati durante il caricamento della cartella di lavoro da un file modello**
Il codice di esempio seguente carica solo oggetti shape durante il caricamento della cartella di lavoro da[file modello](5472556.xlsx)che puoi scaricare dal link indicato.

Lo screenshot seguente mostra il[file modello](5472556.xlsx) contenuti e spiega anche che i dati in colore rosso e sfondo giallo non verranno caricati perché il[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)è stata impostata la proprietà[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![cose da fare:immagine_alt_testo](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il[uscita PDF](5472554.pdf) che puoi scaricare dal link indicato. Qui puoi vedere, i dati in colore rosso e sfondo giallo non sono presenti ma tutte le forme sono presenti.

![cose da fare:immagine_alt_testo](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
