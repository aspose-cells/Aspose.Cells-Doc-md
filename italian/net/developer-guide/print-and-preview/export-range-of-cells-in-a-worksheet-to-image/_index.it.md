---
title: Esporta intervallo di Cells in un foglio di lavoro in immagine
type: docs
weight: 60
url: /it/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Possibili scenari di utilizzo**

È possibile creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells. Tuttavia, a volte è necessario esportare solo un intervallo di celle in un foglio di lavoro in un'immagine. Questo articolo spiega come raggiungere questo obiettivo.

## **Esporta intervallo di Cells in un foglio di lavoro in immagine**

 Per acquisire un'immagine di un intervallo, impostare l'area di stampa sull'intervallo desiderato, quindi impostare tutti i margini su 0. Impostare anche[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) a**VERO** . Il codice seguente acquisisce un'immagine dell'intervallo D8:G16. Di seguito è riportato uno screenshot del[esempio di file Excel](47153160.xlsx) utilizzato nel codice. Puoi provare il codice con qualsiasi file Excel.

## **Screenshot del file Excel di esempio e della sua immagine esportata**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

L'esecuzione del codice crea solo un'immagine dell'intervallo D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
