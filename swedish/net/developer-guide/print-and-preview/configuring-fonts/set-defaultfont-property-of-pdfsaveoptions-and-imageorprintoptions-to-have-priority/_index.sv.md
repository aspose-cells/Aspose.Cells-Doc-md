---
title: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Möjliga användningsscenario**

När du ställer in **DefaultFont**-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) kan du förvänta dig att vid sparande till PDF eller bild kommer den inställda StandardFonten att gälla för all text i en arbetsbok som har en saknad (ej installerad) font.

Vanligtvis, när man sparar till PDF eller bild, kommer Aspose.Cells först försöka ställa in arbetsbokens standardfont (dvs. Workbook.DefaultStyle.Font). Om arbetsbokens standardfont fortfarande inte kan visa/rendera text korrekt, då kommer Aspose.Cells försöka rendera med den font som nämns mot DefaultFont-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

För att möta dina förväntningar har vi en boolesk egenskap som heter "**CheckWorkbookDefaultFont**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Du kan ställa in den till **false** för att inaktivera försöket att använda arbetsbokens standardfont eller låta inställningen för **DefaultFont** i [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) ha prioritet.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempelkod öppnar en Excel-fil. Cellen A1 (i den första kalkylbladet) har en text inställd på "Christmas Time Font text". Fontnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi ställer in ***DefaultFont***-attributet för [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) till "Times New Roman". Vi ställer också in **CheckWorkbookDefaultFont**-boolesk egenskap till **"false"** vilket säkerställer att texten i cell A1 renderas med fonten "Times New Roman" och inte använder arbetsbokens standardfont ("Calibri" i detta fall). Koden renderar det första kalkylbladet till PNG- och TIFF-bildformat. Den renderar slutligen till ett PDF-filformat.

{{% alert color="primary" %}}

Standardvärdet för ***CheckWorkbookDefaultFont*** attributet är **true**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446913.xlsx) som används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är den resulterande PNG-bilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utmatnings [TIFF](48496672.tiff)-bilden efter att ha ställt in [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) egenskapen till "Times New Roman".

Se utmatnings [PDF](48496673.pdf)-filen efter att ha ställt in [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) egenskapen till "Times New Roman".

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
