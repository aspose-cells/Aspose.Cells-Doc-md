---
title: Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions att ha prioritet
type: docs
weight: 30
url: /sv/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Möjliga användningsscenarier**

 När du ställer in**DefaultFont** egendom av**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** och**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, kan du förvänta dig att spara till PDF eller bild skulle ställa in det standardteckensnittet till all text i en arbetsbok som har ett saknat (ej installerat) teckensnitt.

 I allmänhet, när du sparar till PDF eller bild, kommer Aspose.Cells först att försöka ställa in Workbooks standardteckensnitt (dvs. Workbook.DefaultStyle.Font). Om arbetsbokens standardteckensnitt fortfarande inte kan visa/rendera text korrekt, kommer Aspose.Cells att försöka rendera med teckensnitt som nämns mot DefaultFont-attributet i**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

För att klara dina förväntningar har vi en boolesk egenskap som heter "**CheckWorkbookDefaultFont** " i**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Du kan ställa in den på**falsk**för att inaktivera att försöka arbetsbokens standardteckensnitt eller låta**DefaultFont** sätter sig in**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** att ha prioritet.

## **Ställ in egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

 Följande exempelkod öppnar en Excel-fil. A1-cellen (i det första kalkylbladet) har en text inställd på "Christmas Time Font text". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi sätter***DefaultFont*** attribut av**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** till "Times New Roman". Vi ställer också in**CheckWorkbookDefaultFont** boolesk egendom till**"falsk"** vilket säkerställer att texten i A1-cellen renderas med typsnittet "Times New Roman" och inte bör använda standardteckensnittet i arbetsboken ("Calibri" i det här fallet). Koden återger det första kalkylbladet till PNG- och TIFF-bildformat. Den renderas äntligen till ett PDF-filformat.

{{% alert color="primary" %}}

 Standardvärdet för***CheckWorkbookDefaultFont*** attribut är**Sann**.

{{% /alert %}}

 Detta är skärmdumpen av[mallfil](49446913.xlsx) används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är den utgående PNG-bilden efter att ha ställt in**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**egendom till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Se utgången[TIFF](48496672.tiff) bild efter att ha ställt in**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**egendom till "Times New Roman".

Se utgången[PDF](48496673.pdf)fil efter att ha ställt in**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**egendom till "Times New Roman".

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
