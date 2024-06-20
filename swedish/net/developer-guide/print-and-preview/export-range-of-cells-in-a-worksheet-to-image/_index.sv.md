---
title: Exportera område av celler i en arbetsbok till bild
type: docs
weight: 60
url: /sv/net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Möjliga användningsscenario**

Du kan skapa en bild av en arbetsbok med hjälp av Aspose.Cells. Ibland behöver du dock exportera endast ett område av celler i en arbetsbok till en bild. Den här artikeln förklarar hur du åstadkommer detta.

## **Exportera område av celler i en arbetsbok till bild**

För att ta en bild av ett område, ange utskriftsområdet till det önskade området och ställ sedan in alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) till **true**. Följande kod tar en bild av området D8:G16. Nedan finns en skärmbild av den [exempelfil i Excel](47153160.xlsx) som används i koden. Du kan prova koden med vilken Excel-fil som helst.

## **Skärmbild av exempelfil i Excel och dess exporterade bild**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Genom att köra koden skapas en bild av området D8:G16 endast.

**![todo:image_alt_text](Output-Image.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
