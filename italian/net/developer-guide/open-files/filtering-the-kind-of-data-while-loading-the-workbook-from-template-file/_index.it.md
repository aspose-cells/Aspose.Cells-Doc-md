---
title: Filtraggio del tipo di dati durante il caricamento della cartella di lavoro dal file modello
type: docs
weight: 400
url: /it/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 volte, si desidera specificare quale tipo di dati deve essere caricato durante la creazione della cartella di lavoro dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per il tuo scopo speciale, specialmente durante l'utilizzo[API di LightCells](/cells/it/net/using-lightcells-api/) . Si prega di utilizzare il[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) proprietà a tale scopo.

{{% /alert %}}

Il codice di esempio seguente carica solo oggetti shape durante il caricamento della cartella di lavoro da[file modello](5115552.xlsx) che puoi scaricare dal link indicato. Lo screenshot seguente mostra il[file modello](5115552.xlsx) contenuti e spiega anche che i dati in colore rosso e sfondo giallo non verranno caricati perché[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)è stata impostata la proprietà[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![cose da fare:immagine_alt_testo](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il[uscita PDF](5115555.pdf) che puoi scaricare dal link indicato. Qui puoi vedere, i dati in colore rosso e sfondo giallo non sono presenti ma tutte le forme sono presenti.

![cose da fare:immagine_alt_testo](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
