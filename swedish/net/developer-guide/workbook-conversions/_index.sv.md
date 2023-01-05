---
title: Konvertera Excel till Pdf, bild och andra format
linktitle: Arbetsbokkonverteringar
type: docs
weight: 65
url: /sv/net/convert-workbook-to-different-formats/
description: Konvertera Excel-filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, PNG, 876163481, 48131, 8 XML, 48131, 8 mer, 48131, 48101, 8 XML, 48131, 48101, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131, 48131,4
---
{{% alert color="primary" %}}

Aspose.Cells stöder konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel-arbetsbok till PDF**

PDF-filer används ofta för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Konvertera Excel-arbetsbok till JPG**
Aspose.Cells stöder konvertering av Excel-filer till JPG.
Kodexemplet nedan visar hur man sparar en arbetsbok som JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Konvertera Excel-arbetsbok till bild**
Aspose.Cells stöder konvertering av Excel-filer till bilder.
Kodexemplet nedan visar hur man sparar en arbetsbok som bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Konvertera Excel Workbook till XPS**

Dokumentformatet XPS består av strukturerad XML-uppmärkning som definierar layouten för ett dokument och det visuella utseendet på varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

Markeringsspråket för XPS är en delmängd av XAML som gör att det kan inkorporera vektorgrafikelement i dokument, med XAML för att markera Windows Presentation Foundation (WPF) primitiver. Elementen som används beskrivs i termer av banor och andra geometriska primitiver.

En XPS-fil är i själva verket ett unicode ZIP-arkiv som använder Open Packaging Conventions, som innehåller filerna som utgör dokumentet. Dessa inkluderar en XML-uppmärkningsfil för varje sida, text, inbäddade typsnitt, rasterbilder, 2D-vektorgrafik samt information om hantering av digitala rättigheter. Innehållet i en XPS-fil kan granskas helt enkelt genom att öppna den i ett program som stöder ZIP-filer.

Konvertering från Aspose.Cells 6.0.0, Microsoft Excel till XPS stöds.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Konvertera Excel till Ods,Sxc och Fods (OpenOffice / LibreOffice Calc)**
 Aspose.Cells stöder konvertering av Excel-filer till Ods-, Sxc- och Fods-filer. Kodexemplet nedan visar hur man konverterar[tempalte](book1.xlsx) till Ods, Sxc och Fods fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Konvertera Excel-arbetsbok till MHTML-filer**

MHTML kombinerar normala HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljud och så vidare) till en fil. De används för e-postmeddelanden med filtillägget .mht.

Aspose.Cells stöder läsning och skrivning av MHTML filer.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Konvertera Excel Workbook till HTML**

 Aspose.Cells API ger stöd för export av kalkylblad till HTML-format. För detta ändamål använder Aspose.Cells**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**klass för att ge flexibiliteten att kontrollera flera aspekter av utdata HTML.

Kodexemplet nedan visar hur man sparar en arbetsbok som en HTML-fil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Ställa in bildinställningar för HTML**

 Från och med 8.0.2 har Aspose.Cells exponerats**[ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** för**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**klass, vilket gör att utvecklare kan ange bildpreferenser när de sparar kalkylblad i formatet HTML.

Nedan finns information om några av bildinställningarna som kan tillämpas,

- **[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: Anger bildtypen. Observera att alla former, inklusive diagram, återges som bilder i utgången HTML.
- **[SmoothingMode](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: Anger kantutjämning för linjer, kurvor och kanter på fyllda områden.
- **[TextRenderingHint](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: Anger kvaliteten på textåtergivningen.
- **[Kvalitet](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** : Anger kvaliteten på bilden mellan 0 och 100, när**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**anges som Jpeg.
- **[VerticalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: Hämtar eller ställer in bildens vertikala upplösning i punkter per tum.
- **[HorizontalResolution](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**Hämtar eller ställer in bildens horisontella upplösning i punkter per tum.
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : Hämtar eller ställer in komprimeringstypen för bilderna när**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**anges som Tiff.
- **[Transparent](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**: Indikerar om bakgrunden för en bild ska vara genomskinlig när ImageFormat anges som Png.

 Koden nedan visar hur man använder**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**för att ange olika preferenser.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API ger stöd för export av kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, godkänn**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** som den andra parametern för**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** metod. Du kan också använda**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)**klass för att ange ytterligare inställningar för export av kalkylblad till Markdown.

 Följande kodexempel visar export av aktivt kalkylblad till Markdown med hjälp av**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** uppräkningsmedlem. Vänligen se[output Markdown-fil](md_sample.txt)genereras av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells stöder konvertering av en arbetsbok till Json-fil (JavaScript Object Notation).

Följande kodexempel visar export av aktivt kalkylblad till Json med hjälp av[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningsmedlem. Se koden för att konvertera[källfilen](Book1.xlsx) till[output Json-fil](Book1.Json)genereras av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Konvertera Excel till XML**
Aspose.Cells stöder konvertering av en arbetsbok till Excel 2003-kalkylblads-XML och vanliga XML-data.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Konvertera Excel-arbetsbok till TIFF**
Aspose.Cells stöder konvertering av en arbetsbok till TIFF-fil.

Kodavsnittet nedan visar hur du konverterar Excel till TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Konvertera Excel-arbetsbok till DOCX**

Aspose.Cells API ger stöd för att konvertera kalkylblad till formatet DOCX. För att exportera arbetsboken till DOCX, godkänn[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) som den andra parametern för[**Arbetsbok.Spara**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metod. Du kan också använda[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) klass för att ange ytterligare inställningar för export av kalkylblad till DOCX.

 Följande kodexempel visar export av aktivt kalkylblad till DOCX genom att använda[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningsmedlem. Vänligen se[utgång DOCX fil](Book1.docx)genereras av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Konvertera Excel-arbetsbok till PPTX**

Aspose.Cells API ger stöd för att konvertera kalkylblad till formatet PPTX. För att exportera arbetsboken till PPTX, godkänn[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) som den andra parametern för[**Arbetsbok.Spara**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metod. Du kan också använda[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) klass för att ange ytterligare inställningar för export av kalkylblad till PPTX.

 Följande kodexempel visar export av aktivt kalkylblad till PPTX genom att använda[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) uppräkningsmedlem. Vänligen se[utgång PPTX fil](Book1.pptx)genereras av koden för referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Förhandsämnen**
- [Konvertera revision av XLSB till XLSM](/cells/sv/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/sv/net/convert-excel-to-html/)
- [Bild](/cells/sv/net/convert-excel-to-image/)
- [Json](/cells/sv/net/convert-workbook-to-json/)
- [Konvertera Excel-arbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice calc).](/cells/sv/net/convert-excel-to-ods/)
- [Pdf](/cells/sv/net/convert-excel-workbook-to-pdf/)
- [Konvertera Excel till CSV,TSV och Txt](/cells/sv/net/convert-excel-to-csv-tsv-and-txt/)
- [Spåra dokumentkonverteringsförlopp](/cells/sv/net/track-document-conversion-progress/)
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/net/convert-csv-tsv-and-txt-to-excel/)
