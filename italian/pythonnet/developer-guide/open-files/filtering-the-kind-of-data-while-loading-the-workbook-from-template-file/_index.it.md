---
title: Filtrare il tipo di dati durante il caricamento della cartella di lavoro dal file di modello
type: docs
weight: 400
url: /it/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

A volte, si desidera specificare quale tipo di dati devono essere caricati quando si costruisce il workbook dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per scopi specifici. Usa la proprietà [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) a questo scopo.

{{% /alert %}}

Il codice di esempio seguente carica solo gli oggetti di forma durante il caricamento della cartella di lavoro dal [file di modello](5115552.xlsx) che è possibile scaricare dal link fornito. Lo screenshot seguente mostra i contenuti del [file di modello](5115552.xlsx) e spiega anche che i dati di colore rosso e sfondo giallo non saranno caricati perché la proprietà [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) è stata impostata su [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il [PDF di output](5115555.pdf) che è possibile scaricare dal link fornito. Qui si può vedere che i dati di colore rosso e sfondo giallo non sono presenti ma ci sono tutte le forme.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
