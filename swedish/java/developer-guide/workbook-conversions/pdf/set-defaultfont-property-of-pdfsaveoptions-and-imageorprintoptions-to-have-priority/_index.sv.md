---
title: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Möjliga användningsscenario**

När man anger egenskapen **DefaultFont** för [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), kan man förvänta sig att sparande till PDF eller bild skulle sätta den **DefaultFont** för all text i arbetsboken som har en saknad (inte installerad) font.

I allmänhet kommer Aspose.Cells först att försöka att ange arbetsbokens standardfont (dvs. [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)). Om arbetsbokens standardfont fortfarande inte kan visa/rendera text korrekt, kommer Aspose.Cells att försöka rendera med den font som anges mot **DefaultFont** attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

För att klara av din förväntan har vi en Boolean-egenskap med namnet "**CheckWorkbookDefaultFont**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Du kan ställa in den till false för att inaktivera försöket att använda arbetsbokens standardfont eller låta inställningen av **DefaultFont** i [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) att prioriteras.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exemplarkod öppnar en Excelfil. Cellen A1  (i det första kalkylbladet) har en text som är inställd på "Christmas Time Font text". Fonten heter "Christmas Time Personal Use" som inte är installerad på maskinen. Vi sätter **DefaultFont** attributet för [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) till "Times New Roman". Vi ställer också in **CheckWorkbookDefaultFont** egenskapen till "**false**" vilket säkerställer att texten i cell A1 renderas med fonten "Times New Roman" och inte använder arbetsbokens standardfont ("Calibri" i detta fall). Koden renderar det första kalkylbladet till PNG- och TIFF-bildformat. Den renderar slutligen till PDF-filformatet.

{{% alert color="primary" %}}

Standardvärdet för ***CheckWorkbookDefaultFont*** attributet är **true**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446914.xlsx) som används i exemplkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är den resulterande PNG-bilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utdata [TIFF](out1_imageTIFF.tiff)-bilden efter att ha ställt in egenskapen [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) till "Times New Roman".

Se utdata [PDF](out1_pdf.pdf)-filen efter att ha ställt in egenskapen [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) till "Times New Roman".

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
