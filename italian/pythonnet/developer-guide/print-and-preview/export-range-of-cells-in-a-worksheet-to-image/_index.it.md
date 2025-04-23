---
title: Esporta un intervallo di celle in un foglio di lavoro in un immagine
type: docs
weight: 60
url: /it/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Possibili Scenari di Utilizzo**

Puoi creare un’immagine di un foglio di lavoro usando Aspose.Cells per Python via .NET. Tuttavia, a volte è necessario esportare solo un intervallo di celle in un’immagine. Questo articolo spiega come farlo.

## **Esportare un intervallo di celle in un foglio di lavoro in un'immagine**

Per prendere un'immagine di un intervallo, impostare l'area di stampa sull'intervallo desiderato e quindi impostare tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) su **true**. Il seguente codice prende un'immagine dell'intervallo D8:G16. Di seguito è riportata un'istantanea del [file di Excel di esempio](47153160.xlsx) usato nel codice. Puoi provare il codice con qualsiasi file di Excel.

## **Screenshot del file di Excel di esempio e la sua immagine esportata**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Eseguendo il codice viene creata un'immagine dell'intervallo D8:G16 soltanto.

**![todo:image_alt_text](Output-Image.png)**

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

