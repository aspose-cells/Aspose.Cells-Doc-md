---
title: Konvertera Excel till Pdf, Bild och andra format med Golang via C++
linktitle: Arbetsbokskonverteringar
type: docs
weight: 65
url: /sv/go-cpp/convert-workbook-to-different-formats/
description: Konvertera Excel filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML och mer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering mellan många format. Teknisk sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.

{{% /alert %}}

## **Konvertera Excel Arbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, myndigheter och individer. Det är ett standarddokumentformat, och programvaruutvecklare ombeds ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Konvertera Excel-arbetsbok till JPG**
Aspose.Cells stöder konvertering av Excel-filer till JPG.
Exemplet nedan visar hur man sparar en arbetsbok som JPG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Konvertera Excel-arbetsbok till bild**
Aspose.Cells stöder konvertering av Excel-filer till bilder.
Exemplet nedan visar hur man sparar en arbetsbok som bilder.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Konvertera Excel-arbetsbok till XPS**

XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och det visuella utseendet för varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.

 markup-språket för XPS är en delmängd av XAML, vilket gör att det kan innehålla vektorgrafik-element i dokumenten, med XAML för att markera Windows Presentation Foundation (WPF) primitives. De använda elementen beskrivs i termer av vägar och andra geometriska primitiva.

En XPS-fil är faktiskt ett Unicode ZIP-arkiv som använder Open Packaging Conventions, och innehåller filer som utgör dokumentet. Dessa inkluderar en XML-markupfil för varje sida, text, inbäddade typsnitt, rasterbilder, 2D vektorgrafik samt digitala rättighetsstyrningsinformation. Innehållet i en XPS-fil kan enkelt granskas genom att öppna den i ett program som stöder ZIP-filer.

Från Aspose.Cells 6.0.0, stöds konvertering från Microsoft Excel till XPS.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Konvertera Excel till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells stöder konvertering av Excel-filer till Ods, Sxc och Fods filer. Exemplet nedan visar hur du konverterar [mall](book1.xlsx) till Ods, Sxc och Fods filer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Konvertera Excel arbetsbok till MHTML-filer**

MHTML kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljuddokument med mera) till en enda fil. De används för e-postmeddelanden med filändelsen .mht.

Aspose.Cells stödjer att läsa och skriva MHTML-filer.

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Konvertera Excelfil till HTML**

Aspose.Cells API stöder export av kalkylblad till HTML-format. För detta använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) för att ge flexibilitet att kontrollera flera aspekter av utdata-HTML:en.

Kodexemplet nedan visar hur du sparar en arbetsbok som en HTML-fil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Inställning av bildpreferenser för HTML**

Från version 8.0.2 har Aspose.Cells exponerat [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) för klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) vilket möjliggör för utvecklare att specificera bildpreferenser vid sparande av kalkylblad till HTML-format.

Nedanför finns detaljer om några av bildinställningarna som kan tillämpas:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): Specificerar bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i utdata-HTML.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): Anger bildkvaliteten mellan 0 till 100 när [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) anges som Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): Hämta eller sätta kompressionstyp för bilder när [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) är specificerat som Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): Anger om bakgrunden för en bild ska vara transparent när ImageFormat anges som Png.

Koden nedan visar hur man använder [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) för att ange olika preferenser.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Konvertera Excel-arbetsbok till Markdown**

Aspose.Cells API stöder export av kalkblad till Markdown-format. För att exportera det aktiva kalkbladet till Markdown, skicka [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till Markdown.

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till Markdown med hjälp av [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration-medlem. Se den genererade [Markdown-utdatafilen](md_sample.txt) som referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Konvertera Excel-arbetsbok till JSON**

Aspose.Cells stödjer konvertering av en arbetsbok till JSON (JavaScript Object Notation).

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till JSON med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration-medlem. Se koden för att konvertera [källfilen](Book1.xlsx) till den [utgångs-JSON filen](Book1.Json) som genererats av koden som referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Konvertera Excel till XML**
Aspose.Cells stöder konvertering av en arbetsbok till Excel 2003 Spreadsheet XML och vanliga XML-data.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Konvertera Excel-arbetsbok till TIFF**
Aspose.Cells stöder konvertering av en arbetsbok till TIFF-fil.

Kodsnutten nedan visar hur man konverterar Excel till TIFF:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Konvertera Excel-arbetsbok till DOCX**

Aspose.Cells API stöder konvertering av kalkblad till DOCX-format. För att exportera arbetsboken till DOCX, skicka [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till DOCX.

Följande kodexempel visar hur man exporterar det aktiva kalkbladet till DOCX med hjälp av [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration-medlem. Se den genererade [DOCX-utdatafilen](Book1.docx) som referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Konvertera Excel-arbetsbok till PPTX**

Aspose.Cells API stöder konvertering av kalkblad till PPTX-format. För att exportera arbetsboken till PPTX, skicka [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metod. Du kan också använda [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) klass för att specificera ytterligare inställningar för export av kalkblad till PPTX.

Följande kodexempel demonstrerar export av aktivt kalkylblad till PPTX med hjälp av [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumerationsmedlem. Se den [utgångs-PPTX-fil](Book1.pptx) som genererats av koden för referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Konvertera Excel-arbetsbok till EPUB**

Aspose.Cells API stöder konvertering av kalkylblad till EPUB-format. För att exportera arbetsboken till EPUB, skicka [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden. Du kan också använda [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-klassen för att specificera ytterligare inställningar för export av kalkylbladet till EPUB.

Följande kodexempel demonstrerar export av aktivt kalkylblad till EPUB med hjälp av [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumerationsmedlem.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Konvertera Excel-arbetsbok till AZW3**

Aspose.Cells API stöder konvertering av kalkylblad till AZW3-format. För att exportera arbetsboken till AZW3, skicka [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-metoden. Du kan också använda [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-klassen för att specificera ytterligare inställningar för export av kalkylblad till AZW3.

Följande kodexempel demonstrerar export av aktivt kalkylblad till AZW3 med hjälp av [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumerationsmedlem.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Fortsatta ämnen**
- [Konvertera revidering av XLSB till XLSM](/cells/sv/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/sv/cpp/convert-excel-to-html/)
- [Bild](/cells/sv/cpp/convert-excel-to-image/)
- [Json](/cells/sv/cpp/convert-workbook-to-json/)
- [Konvertera Excelarbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice calc).](/cells/sv/cpp/convert-excel-to-ods/)
- [Pdf](/cells/sv/cpp/convert-excel-workbook-to-pdf/)
- [Konvertera Excel till CSV, TSV och Txt](/cells/sv/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Spåra Dokumentkonverteringsframsteg](/cells/sv/cpp/track-document-conversion-progress/)
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/cpp/convert-csv-tsv-and-txt-to-excel/)
