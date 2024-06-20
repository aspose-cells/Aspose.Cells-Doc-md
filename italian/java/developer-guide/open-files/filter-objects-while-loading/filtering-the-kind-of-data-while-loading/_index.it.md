---
title: Filtrare il tipo di dati durante il caricamento della cartella di lavoro dal file di modello
type: docs
weight: 680
url: /it/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

A volte si desidera specificare quale tipo di dati dovrebbe essere caricato durante la creazione del foglio di lavoro da un file di modello. Filtrare i dati caricati può migliorare le prestazioni per uno scopo speciale, specialmente quando si utilizzano [API LightCells](/cells/it/java/using-lightcells-api/). Si prega di utilizzare la proprietà [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) a tale scopo.

{{% /alert %}} 
## **Filtrare il tipo di dati durante il caricamento del foglio di lavoro dal file del modello**
Il codice di esempio seguente carica solo gli oggetti di forma durante il caricamento del foglio di lavoro dal [file del modello](5472556.xlsx) che è possibile scaricare dal link fornito.

La seguente schermata mostra il contenuto del [file del modello](5472556.xlsx) e spiega anche che i dati in colore rosso e sfondo giallo non verranno caricati perché la proprietà [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) è stata impostata su [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

La seguente schermata mostra il [file PDF di output](5472554.pdf) che è possibile scaricare dal link fornito. Qui è possibile vedere che i dati in colore rosso e sfondo giallo non sono presenti, ma tutte le forme ci sono.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
