---
title: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Möjliga användningsscenario**

När du ställer in **DefaultFont**-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) kan du förvänta dig att vid sparande till PDF eller bild kommer den inställda StandardFonten att gälla för all text i en arbetsbok som har en saknad (ej installerad) font.

Generellt, när du sparar till PDF eller bild, försöker Aspose.Cells för Python via .NET först att ställa in arbetsbokens standardteckensnitt (dvs. Workbook.DefaultStyle.Font). Om arbetsbokens standardteckensnitt fortfarande inte kan visa/rendera text ordentligt, försöker Aspose.Cells för Python via .NET att rendera med teckensnittet som nämns i DefaultFont-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

För att möta dina förväntningar har vi en Boolean-egenskap som heter "**check_workbook_default_font**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Du kan sätta den till **falskt** för att inaktivera att försöka med arbetsbokens standardteckensnitt eller låta "**default_font**"-inställningen i [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) ha prioritet.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempel öppnar en Excel-fil. Cell A1 (i det första bladet) har texten "Julens tid Fonttext". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi sätter ***default_font***-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) till "Times New Roman". Vi sätter också egenskapen **check_workbook_default_font** till **"falsk"**, vilket säkerställer att texten i A1 cellen renderas med "Times New Roman"-teckensnitt och inte använder standardteckensnittet för arbetsboken ("Calibri" i detta fall). Koden renderar det första bladet till PNG- och TIFF-bildformat. Den renderar också till en PDF-fil.

{{% alert color="primary" %}}

Standardvärdet för ***CheckWorkbookDefaultFont*** attributet är **true**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446913.xlsx) som används i exempelkoden.

![todo:image_alt_text](1.png)

Detta är den resulterande PNG-bilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) till "Times New Roman".

![todo:image_alt_text](2.png)

Se utmatnings [TIFF](48496672.tiff)-bilden efter att ha ställt in [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) egenskapen till "Times New Roman".

Se utmatnings [PDF](48496673.pdf)-filen efter att ha ställt in [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) egenskapen till "Times New Roman".

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
