---
title: Exportera intervallet Cells i ett kalkylblad till bild
type: docs
weight: 60
url: /sv/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Möjliga användningsscenarier**

Du kan skapa en bild av ett kalkylblad med Aspose.Cells. Men ibland behöver du bara exportera ett cellintervall i ett kalkylblad till en bild. Den här artikeln förklarar hur du uppnår detta.

## **Exportera intervallet Cells i ett kalkylblad till bild**

 För att ta en bild av ett område, ställ in utskriftsområdet till önskat område och ställ sedan in alla marginaler till 0. Ställ även in[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) till**Sann** . Följande kod tar en bild av området D8:G16. Nedan är en skärmdump av[exempel på Excel-fil](47153160.xlsx) används i koden. Du kan prova koden med valfri Excel-fil.

## **Skärmdump av exempel på Excel-fil och dess exporterade bild**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Genom att köra koden skapas endast en bild av området D8:G16.

**![todo:image_alt_text](Output-Image.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
