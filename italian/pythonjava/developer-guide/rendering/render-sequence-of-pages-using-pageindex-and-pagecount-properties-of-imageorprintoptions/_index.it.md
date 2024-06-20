---
title: Rendi sequenza di pagine usando le proprietà PageIndex e PageCount di ImageOrPrintOptions
type: docs
weight: 10
url: /it/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**
È possibile rendere una sequenza di pagine del file Excel in immagini utilizzando Aspose.Cells con le proprietà [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) e [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Queste proprietà sono utili quando ci sono ad esempio migliaia di pagine nel foglio di lavoro ma si desidera renderne solo alcune. Questo non solo risparmierà tempo di elaborazione ma ridurrà anche il consumo di memoria del processo di rendering.

Il seguente codice di esempio carica il file Excel di esempio e rende solo le pagine 4, 5, 6 e 7 utilizzando le proprietà [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) e [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount). Di seguito sono riportate le immagini delle pagine renderizzate generate dal codice di esempio.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
