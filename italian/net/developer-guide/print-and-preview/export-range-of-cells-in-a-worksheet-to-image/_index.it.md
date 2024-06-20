---
title: Esporta un intervallo di celle in un foglio di lavoro in un immagine
type: docs
weight: 60
url: /it/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Possibili Scenari di Utilizzo**

È possibile creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells. Tuttavia, talvolta è necessario esportare solo un intervallo di celle in un foglio di lavoro in un'immagine. Questo articolo spiega come raggiungere questo obiettivo.

## **Esportare un intervallo di celle in un foglio di lavoro in un'immagine**

Per prendere un'immagine di un intervallo, impostare l'area di stampa sull'intervallo desiderato e quindi impostare tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) su **true**. Il seguente codice prende un'immagine dell'intervallo D8:G16. Di seguito è riportata un'istantanea del [file di Excel di esempio](47153160.xlsx) usato nel codice. Puoi provare il codice con qualsiasi file di Excel.

## **Screenshot del file di Excel di esempio e la sua immagine esportata**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Eseguendo il codice viene creata un'immagine dell'intervallo D8:G16 soltanto.

**![todo:image_alt_text](Output-Image.png)**

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
