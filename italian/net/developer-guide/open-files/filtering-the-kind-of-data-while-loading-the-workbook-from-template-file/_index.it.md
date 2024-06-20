---
title: Filtrare il tipo di dati durante il caricamento della cartella di lavoro dal file di modello
type: docs
weight: 400
url: /it/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

A volte, si desidera specificare quale tipo di dati deve essere caricato durante la costruzione della cartella di lavoro dal file di modello. Il filtraggio dei dati caricati può migliorare le prestazioni per uno scopo specifico, specialmente quando si utilizzano [API LightCells](/cells/it/net/using-lightcells-api/). Si prega di utilizzare la proprietà [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) per questo scopo.

{{% /alert %}}

Il codice di esempio seguente carica solo gli oggetti di forma durante il caricamento della cartella di lavoro dal [file di modello](5115552.xlsx) che è possibile scaricare dal link fornito. Lo screenshot seguente mostra i contenuti del [file di modello](5115552.xlsx) e spiega anche che i dati di colore rosso e sfondo giallo non saranno caricati perché la proprietà [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) è stata impostata su [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il [PDF di output](5115555.pdf) che è possibile scaricare dal link fornito. Qui si può vedere che i dati di colore rosso e sfondo giallo non sono presenti ma ci sono tutte le forme.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
