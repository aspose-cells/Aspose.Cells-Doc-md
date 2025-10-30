---
title: Filtrare il tipo di dati durante il caricamento del file di lavoro dal file modello con Golang via C++
linktitle: Filtrare i dati durante il caricamento del workbook
type: docs
weight: 400
url: /it/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Impara come filtrare tipi di dati specifici durante il caricamento di un file di lavoro da un modello usando Aspose.Cells con Golang via C++.
---

{{% alert color="primary" %}}

A volte, si vuole specificare quale tipo di dati deve essere caricato quando si costruisce il workbook dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per uno scopo particolare, specialmente quando si usano le API [LightCells](/cells/it/cpp/using-lightcells-api/). Si prega di utilizzare la proprietà [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) a questo scopo.

{{% /alert %}}

Il codice di esempio seguente carica solo gli oggetti di forma durante il caricamento della cartella di lavoro dal [file di modello](5115552.xlsx) che è possibile scaricare dal link fornito. Lo screenshot seguente mostra i contenuti del [file di modello](5115552.xlsx) e spiega anche che i dati di colore rosso e sfondo giallo non saranno caricati perché la proprietà [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) è stata impostata su [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il [PDF di output](5115555.pdf) che è possibile scaricare dal link fornito. Qui si può vedere che i dati di colore rosso e sfondo giallo non sono presenti ma ci sono tutte le forme.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
