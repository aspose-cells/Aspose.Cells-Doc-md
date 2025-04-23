---
title: Rendi sequenza di pagine usando le proprietà PageIndex e PageCount di ImageOrPrintOptions
type: docs
weight: 110
url: /it/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Possibili Scenari di Utilizzo**

Puoi rendere una sequenza di pagine del tuo file Excel in immagini utilizzando Aspose.Cells per Python via .NET con le proprietà [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) e [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Queste proprietà sono utili quando ci sono molte pagine, ad esempio migliaia, nel tuo foglio di lavoro, ma vuoi renderne solo alcune. Questo non solo risparmia tempo di elaborazione, ma anche consumo di memoria nel processo di rendering.

## **Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**

Il seguente codice di esempio carica il [file Excel di esempio](55541781.xlsx) e rende solo le pagine 4, 5, 6 e 7 utilizzando le proprietà [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) e [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count). Ecco le pagine renderizzate generate dal codice.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
