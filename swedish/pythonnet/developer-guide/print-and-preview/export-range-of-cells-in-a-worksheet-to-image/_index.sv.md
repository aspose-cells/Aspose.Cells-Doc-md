---
title: Exportera område av celler i en arbetsbok till bild
type: docs
weight: 60
url: /sv/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Möjliga användningsscenario**

Du kan skapa en bild av ett arbetsblad med Aspose.Cells för Python via .NET. Men ibland vill du bara exportera ett område av celler i ett arbetsblad till en bild. Denna artikel förklarar hur du gör detta.

## **Exportera område av celler i en arbetsbok till bild**

För att ta en bild av ett område, ange utskriftsområdet till det önskade området och ställ sedan in alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) till **true**. Följande kod tar en bild av området D8:G16. Nedan finns en skärmbild av den [exempelfil i Excel](47153160.xlsx) som används i koden. Du kan prova koden med vilken Excel-fil som helst.

## **Skärmbild av exempelfil i Excel och dess exporterade bild**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Genom att köra koden skapas en bild av området D8:G16 endast.

**![todo:image_alt_text](Output-Image.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
