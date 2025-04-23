---
title: Rendi sequenza di pagine usando le proprietà PageIndex e PageCount di ImageOrPrintOptions
type: docs
weight: 110
url: /it/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Possibili Scenari di Utilizzo**

È possibile rendere una sequenza di pagine del file Excel in immagini utilizzando Aspose.Cells con le proprietà [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) e [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount). Queste proprietà sono utili quando ci sono ad esempio migliaia di pagine nel foglio di lavoro ma si desidera renderne solo alcune. Questo non solo risparmierà tempo di elaborazione ma risparmierà anche l'utilizzo della memoria del processo di rendering.

## **Rendere la sequenza di pagine utilizzando le proprietà PageIndex e PageCount di ImageOrPrintOptions**

Il seguente codice di esempio carica il [file Excel di esempio](55541781.xlsx) e rende solo le pagine 4, 5, 6 e 7 utilizzando le proprietà [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) e [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount). Ecco le pagine renderizzate generate dal codice.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
