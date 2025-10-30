---
title: Konvertera Excel till Pdf, bild och andra format
linktitle: Arbetsbokskonverteringar
type: docs
weight: 65
url: /sv/python-net/convert-workbook-to-different-formats/
description: Konvertera Excel filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML med mera genom att använda Aspose.Cells för Python via .NET API.
keywords: Python konvertera Excel arbetsbok till PDF, Konvertera Excel arbetsbok till JPG i Python, Python konvertera Excel arbetsbok till bild, Konvertera Excel arbetsbok till XPS med hjälp av Python, Konvertera Excel till ODS, SXC och FODS via Python, Python konvertera Excel arbetsbok till HTML, Konvertera Excel arbetsbok till JSON i Python, Python konvertera Excel arbetsbok till DOCX, Konvertera Excel arbetsbok till TIFF eller MARKDOWN med Python.
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET stöder konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel Arbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells for Python via .NET stödjer konvertering av Excel-filer till PDF och bibehåller hög visuell trohet i konverteringen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **Konvertera Excel-arbetsbok till JPG**
Aspose.Cells för Python via .NET stödjer konvertering av Excel-filer till JPG.
Exemplet nedan visar hur man sparar en arbetsbok som JPG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **Konvertera Excel-arbetsbok till bild**
Aspose.Cells för Python via .NET stödjer konvertering av Excel-filer till bilder.
Exemplet nedan visar hur man sparar en arbetsbok som bilder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **Konvertera Excel-arbetsbok till XPS**

XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och det visuella utseendet för varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

Märkspråket för XPS är en delmängd av XAML vilket gör att det kan inkludera vektorgrafikelement i dokumenten, använda XAML för att märka upp Windows Presentation Foundation (WPF)-primitiverna. De använda elementen beskrivs i termer av banor och andra geometriska primitiver.

En XPS-fil är faktiskt en unicode ZIP-arkiv med hjälp av Open Packaging Conventions, som innehåller filerna som utgör dokumentet. Dessa inkluderar en XML-markering för varje sida, text, inbäddade teckensnitt, rasterbilder, 2D-vektorgrafik samt information om digital rättighetsförvaltning. Innehållet i en XPS-fil kan undersökas genom att helt enkelt öppna den i en applikation som stöder ZIP-filer.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **Konvertera Excel till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells för Python via .NET stöder konvertering av Excel-filer till Ods, Sxc och Fods-filer . Exemplet nedan visar hur man konverterar [mallen](book1.xlsx) till Ods, Sxc och Fods-fil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}


## **Konvertera Excel arbetsbok till MHTML-filer**

MHTML kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljuddokument med mera) till en enda fil. De används för e-postmeddelanden med filändelsen .mht.

Aspose.Cells för Python via .NET stöder läsning och skrivning av MHTML-filer.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **Konvertera Excelfil till HTML**

Aspose.Cells för Python via .NET API ger stöd för att exportera kalkylblad till HTML-format. För detta ändamål använder Aspose.Cells för Python via .NET [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/)-klassen för att ge flexibilitet att styra flera aspekter av utdata-HTML.

Kodexemplet nedan visar hur du sparar en arbetsbok som en HTML-fil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **Inställning av bildpreferenser för HTML**

Aspose.Cells för Python via .NET har exponerat [**image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) för klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions), vilket låter utvecklare specificera bildpreferenser vid sparande av kalkylblad till HTML-format.

Nedan finns detaljer om några av de bildinställningar som kan tillämpas,

- [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/): Specificerar bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i utdata-HTML.
- [**smoothing_mode**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/): Specificerar antialiasing för linjer, kurvor och kanter på fyllda områden.
- [**text_rendering_hint**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/): Specificerar kvaliteten på textrendering.
- [**quality**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/): Specificerar bildkvaliteten mellan 0 till 100 när [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) anges som Jpeg.
- [**vertical_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.
- [**horizontal_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.
- [**tiff_compression**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/): Hämtar eller anger komprimeringstypen för bilderna när [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) anges som Tiff.
- [**transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/): Anger om bakgrunden för en bild ska vara transparent när ImageFormat anges som Png.

Koden nedan demonstrerar hur man använder [**HtmlSaveOptions.image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) för att ange olika preferenser.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells för Python via .NET API ger stöd för att exportera kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, skicka [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) som det andra parametern till [**Workbook.Save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.saveformat)-metoden. Du kan även använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/markdownsaveoptions)-klassen för att specificera ytterligare inställningar för att exportera kalkylblad till Markdown.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Markdown genom att använda [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)-uppräkningsmedlemmen. Se även [utdatan Markdown-fil](md_sample.txt) genererad av koden för referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells for Python via .NET stödjer konvertering av en arbetsbok till Json (JavaScript Object Notation) fil.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Json med hjälp av [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)-uppräkningsmedlemmen. Se även koden för att konvertera [källfilen](Book1.xlsx) till den [genererade Json-filen](Book1.Json) för referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **Konvertera Excel till XML**
Aspose.Cells för Python via .NET Ger stöd för att konvertera en arbetsbok till Excel 2003 Spreadsheet XML och ren XML-data.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **Konvertera Excel-arbetsbok till TIFF**
Aspose.Cells för Python via .NET Ger stöd för att konvertera en arbetsbok till TIFF-fil.

Kodsnutten nedan visar hur man konverterar Excel till TIFF:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **Konvertera Excel-arbetsbok till DOCX**

Aspose.Cells för Python via .NET API ger stöd för att konvertera kalkylblad till DOCX-format. För att exportera arbetsboken till DOCX, skicka [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) som andra parameter till [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)-metoden. Du kan även använda [**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/)-klassen för att specificera ytterligare inställningar för att exportera kalkylblad till DOCX.

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till DOCX genom att använda [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)-uppräkningsmedlemmen. Se även [utdatan DOCX-fil](Book1.docx) genererad av koden för referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **Konvertera Excel-arbetsbok till PPTX**

Aspose.Cells för Python via .NET API ger stöd för att konvertera kalkylblad till PPTX-format. För att exportera arbetsboken till PPTX, skicka [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) som andra parameter till [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions)-metoden. Du kan även använda [**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions)-klassen för att specificera ytterligare inställningar för att exportera kalkylblad till PPTX.

Följande kodexempel visar export av aktivt arbetsblad till PPTX med hjälp av medlemsuppräkningen [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/). Vänligen se [utdata PPTX-filen](Book1.pptx) genererad av koden för referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **Fortsatta ämnen**
- [Json](/cells/sv/python-net/convert-workbook-to-json/)
- [Pdf](/cells/sv/python-net/convert-excel-to-pdf/)
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/python-net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="python-net" >}}
