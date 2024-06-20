---
title: Konvertera Excel till Pdf, bild och andra format
linktitle: Arbetsbokskonverteringar
type: docs
weight: 65
url: /sv/net/convert-workbook-to-different-formats/
description: Konvertera Excel filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML och mer.
---

{{% alert color="primary" %}}

Aspose.Cells stödjer konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel Arbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Konvertera Excel-arbetsbok till JPG**
Aspose.Cells stöder konvertering av Excel-filer till JPG.
Exemplet nedan visar hur man sparar en arbetsbok som JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Konvertera Excel-arbetsbok till bild**
Aspose.Cells stöder konvertering av Excel-filer till bilder.
Exemplet nedan visar hur man sparar en arbetsbok som bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Konvertera Excel-arbetsbok till XPS**

XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och det visuella utseendet för varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

Märkspråket för XPS är en delmängd av XAML vilket gör att det kan inkludera vektorgrafikelement i dokumenten, använda XAML för att märka upp Windows Presentation Foundation (WPF)-primitiverna. De använda elementen beskrivs i termer av banor och andra geometriska primitiver.

En XPS-fil är faktiskt en unicode ZIP-arkiv med hjälp av Open Packaging Conventions, som innehåller filerna som utgör dokumentet. Dessa inkluderar en XML-markering för varje sida, text, inbäddade teckensnitt, rasterbilder, 2D-vektorgrafik samt information om digital rättighetsförvaltning. Innehållet i en XPS-fil kan undersökas genom att helt enkelt öppna den i en applikation som stöder ZIP-filer.

Från Aspose.Cells 6.0.0, stöds konvertering från Microsoft Excel till XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Konvertera Excel till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells stöder konvertering av Excel-filer till Ods, Sxc och Fods-filer. Kodexemplet nedan visar hur man konverterar mallen book1.xlsx till Ods, Sxc och Fods-filer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Konvertera Excel arbetsbok till MHTML-filer**

MHTML kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljuddokument med mera) till en enda fil. De används för e-postmeddelanden med filändelsen .mht.

Aspose.Cells stödjer att läsa och skriva MHTML-filer.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Konvertera Excelfil till HTML**

Aspose.Cells API:et ger stöd för att exportera kalkylblad till HTML-format. För detta ändamål använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) för att ge flexibilitet att kontrollera flera aspekter av det utgående HTML:et.

Kodexemplet nedan visar hur du sparar en arbetsbok som en HTML-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Inställning av bildpreferenser för HTML**

Från och med 8.0.2 har Aspose.Cells exponerat [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) för klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), vilket ger utvecklare möjlighet att ange bildpreferenser när de sparar kalkylblad till HTML-format.

Nedan finns detaljer om några av de bildinställningar som kan tillämpas,

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): Specificerar bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i utdata-HTML.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Specificerar antialiasing för linjer, kurvor och kanter på fyllda områden.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Specificerar kvaliteten på textrendering.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): Specificerar bildkvaliteten mellan 0 till 100 när [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) anges som Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Hämtar eller anger komprimeringstypen för bilderna när [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) anges som Tiff.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): Anger om bakgrunden för en bild ska vara transparent när ImageFormat anges som Png.

Koden nedan demonstrerar hur man använder [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) för att ange olika preferenser.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API:et ger stöd för att exportera kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, skicka [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) som andra parameter av [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)-metoden. Du kan också använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)-klassen för att specificera ytterligare inställningar för att exportera kalkylbladet till Markdown.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Markdown genom att använda [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)-uppräkningsmedlemmen. Se även [utdatan Markdown-fil](md_sample.txt) genererad av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells stöder konvertering av arbetsbok till Json (JavaScript Object Notation)-fil.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Json med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)-uppräkningsmedlemmen. Se även koden för att konvertera [källfilen](Book1.xlsx) till den [genererade Json-filen](Book1.Json) för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Konvertera Excel till XML**
Aspose.Cells stöder konvertering av en arbetsbok till Excel 2003 Spreadsheet XML och vanliga XML-data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Konvertera Excel-arbetsbok till TIFF**
Aspose.Cells stöder konvertering av en arbetsbok till TIFF-fil.

Kodsnutten nedan visar hur man konverterar Excel till TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Konvertera Excel-arbetsbok till DOCX**

Aspose.Cells API:et ger stöd för att konvertera kalkylblad till DOCX-format. För att exportera arbetsboken till DOCX, skicka [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) som andra parameter av [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)-metoden. Du kan också använda [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)-klassen för att specificera ytterligare inställningar för att exportera arbetsbladet till DOCX.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till DOCX genom att använda [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)-uppräkningsmedlemmen. Se även [utdatan DOCX-fil](Book1.docx) genererad av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Konvertera Excel-arbetsbok till PPTX**

Aspose.Cells API ger stöd för att konvertera kalkylblad till PPTX-format. För att exportera arbetsboken till PPTX, skicka [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) som det andra parametern av [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metoden. Du kan också använda [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) klassen för att ange ytterligare inställningar för att exportera kalkylblad till PPTX.

Följande kodexempel visar export av aktivt arbetsblad till PPTX med hjälp av medlemsuppräkningen [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Vänligen se [utdata PPTX-filen](Book1.pptx) genererad av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Fortsatta ämnen**
- [Konvertera revidering av XLSB till XLSM](/cells/sv/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/sv/net/convert-excel-to-html/)
- [Bild](/cells/sv/net/convert-excel-to-image/)
- [Json](/cells/sv/net/convert-workbook-to-json/)
- [Konvertera Excel-arbetsbok till Ods, Sxc och Fods (ÖppnaOffice / LibreOffice calc).](/cells/sv/net/convert-excel-to-ods/)
- [Pdf](/cells/sv/net/convert-excel-workbook-to-pdf/)
- [Konvertera Excel till CSV, TSV och Txt](/cells/sv/net/convert-excel-to-csv-tsv-and-txt/)
- [Spåra Dokumentkonverteringsframsteg](/cells/sv/net/track-document-conversion-progress/)
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/net/convert-csv-tsv-and-txt-to-excel/)
