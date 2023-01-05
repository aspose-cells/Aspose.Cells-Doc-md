---
title: Eseguire il rendering della sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions
type: docs
weight: 10
url: /it/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---
## **Eseguire il rendering della sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**
È possibile eseguire il rendering di una sequenza di pagine del file Excel in immagini utilizzando Aspose.Cells con[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) e[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) proprietà. Queste proprietà sono utili quando ci sono così tante, ad esempio migliaia di pagine nel tuo foglio di lavoro, ma vuoi renderizzare solo alcune di esse. Ciò non solo salverà il tempo di elaborazione, ma salverà anche il consumo di memoria del processo di rendering.

Il seguente codice di esempio carica il file Excel di esempio ed esegue il rendering solo delle pagine 4, 5, 6 e 7 utilizzando il[ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex)e[ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) proprietà. Di seguito sono riportate le immagini delle pagine renderizzate generate dal codice di esempio.

|![cose da fare:immagine_alt_testo](outputImage-4.png)|![cose da fare:immagine_alt_testo](outputImage-5.png)|
|:- |:- |
|![cose da fare:immagine_alt_testo](outputImage-6.png)|![cose da fare:immagine_alt_testo](outputImage-7.png)|



## **Codice d'esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
