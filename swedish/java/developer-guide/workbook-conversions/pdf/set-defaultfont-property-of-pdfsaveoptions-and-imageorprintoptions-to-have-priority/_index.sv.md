---
title: Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions att ha prioritet
type: docs
weight: 30
url: /sv/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Möjliga användningsscenarier**

 När du ställer in**DefaultFont** egendom av[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) och[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) , kan du förvänta dig att spara till PDF eller bild skulle ställa in det**DefaultFont** till all text i arbetsboken som saknar (ej installerat) teckensnitt.

 I allmänhet, när du sparar till PDF eller bild, kommer Aspose.Cells först att försöka ställa in arbetsbokens standardteckensnitt (dvs.[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Om arbetsbokens standardteckensnitt fortfarande inte kan visa/rendera text korrekt, kommer Aspose.Cells att försöka rendera med teckensnitt som nämns mot**DefaultFont** attribut i[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

För att klara dina förväntningar har vi en boolesk egenskap som heter "**CheckWorkbookDefaultFont** " i[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Du kan ställa in den på false för att inaktivera att försöka arbetsbokens standardteckensnitt eller låta**DefaultFont** sätter sig in[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) att ha prioritet.

## **Ställ in egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempelkod öppnar en Excel-fil. A1-cellen (i det första kalkylbladet) har en text inställd på "Christmas Time Font text". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi sätter**DefaultFont**attribut av[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)till "Times New Roman". Vi ställer också in**CheckWorkbookDefaultFont**boolesk egenskap till "**falsk**" som säkerställer att texten i A1-cellen renderas med typsnittet "Times New Roman" och inte bör använda standardteckensnittet i arbetsboken ("Calibri" i det här fallet). Koden återger det första kalkylbladet till bildformaten PNG och TIFF. Den renderas äntligen till filformatet PDF.

{{% alert color="primary" %}}

 Standardvärdet för***CheckWorkbookDefaultFont*** attribut är**Sann**.

{{% /alert %}}

Detta är skärmdumpen av[mallfil](49446914.xlsx)används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är utgångsbilden PNG efter att ha ställt in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)egendom till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utgången[TIFF](out1_imageTIFF.tiff)bild efter att ha ställt in[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)egendom till "Times New Roman".

Se utgången[PDF](out1_pdf.pdf)fil efter att ha ställt in[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)egendom till "Times New Roman".

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
