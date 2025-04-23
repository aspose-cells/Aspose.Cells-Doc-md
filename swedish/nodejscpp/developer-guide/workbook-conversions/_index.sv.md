---  
title: Konvertera Excel till Pdf, bild och andra format  
linktitle: Arbetsbokskonverteringar  
type: docs  
weight: 65  
url: /sv/nodejs-cpp/convert-workbook-to-different-formats/  
description: Konvertera Excel filer till Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML och mer med Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells stödjer konvertering mellan många format. Tekniskt sett innebär konvertering att ladda en arbetsbok i ett filformat och spara den i ett annat.  
{{% /alert %}}  

## **Konvertera Excel Arbetsbok till PDF**  
PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.  

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **Konvertera Excel-arbetsbok till JPG**  
Aspose.Cells stöder konvertering av Excel-filer till JPG. Exemplet nedan visar hur man sparar en arbetsbok som JPG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **Konvertera Excel-arbetsbok till bild**  
Aspose.Cells stöder konvertering av Excel-filer till bilder. Exemplet nedan visar hur man sparar en arbetsbok som bilder.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **Konvertera Excel-arbetsbok till XPS**  
XPS-dokumentformatet består av strukturerad XML-markering som definierar layouten för ett dokument och det visuella utseendet för varje sida, tillsammans med renderingsregler för distribution, arkivering, rendering, bearbetning och utskrift av dokument.  

Märkspråket för XPS är en delmängd av XAML vilket gör att det kan inkludera vektorgrafikelement i dokumenten, använda XAML för att märka upp Windows Presentation Foundation (WPF)-primitiverna. De använda elementen beskrivs i termer av banor och andra geometriska primitiver.  

En XPS-fil är faktiskt en unicode ZIP-arkiv med hjälp av Open Packaging Conventions, som innehåller filerna som utgör dokumentet. Dessa inkluderar en XML-markering för varje sida, text, inbäddade teckensnitt, rasterbilder, 2D-vektorgrafik samt information om digital rättighetsförvaltning. Innehållet i en XPS-fil kan undersökas genom att helt enkelt öppna den i en applikation som stöder ZIP-filer.  

Från Aspose.Cells 6.0.0, stöds konvertering från Microsoft Excel till XPS.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **Konvertera Excel till Ods, Sxc och Fods (OpenOffice / LibreOffice Calc)**  
Aspose.Cells stöder konvertering av Excel-filer till Ods, Sxc och Fods. Exemplet nedan visar hur man konverterar mallen (book1.xlsx) till Ods, Sxc och Fods-fil.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **Konvertera Excel arbetsbok till MHTML-filer**  
MHTML kombinerar vanlig HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, som bilder, animationer, ljuddokument med mera) till en enda fil. De används för e-postmeddelanden med filändelsen .mht.  

Aspose.Cells stödjer att läsa och skriva MHTML-filer.  

Kodexemplet nedan visar hur man sparar en arbetsbok som en MHTML-fil.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **Konvertera Excelfil till HTML**  
Aspose.Cells API stöder export av kalkylblad till HTML-format. För detta använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) för att ge flexibilitet att kontrollera flera aspekter av utdata-HTML:en.  

Kodexemplet nedan visar hur du sparar en arbetsbok som en HTML-fil.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **Inställning av bildpreferenser för HTML**  
Från version 8.0.2 har Aspose.Cells exponerat [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) för klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) vilket möjliggör för utvecklare att specificera bildpreferenser vid sparande av kalkylblad till HTML-format.  

Nedan finns detaljer om några av de bildinställningar som kan tillämpas,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Specificerar bildtypen. Observera att alla former, inklusive diagram, renderas som bilder i utdata-HTML.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Anger bildkvaliteten mellan 0 och 100 när [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) är specificerat som Jpeg.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Hämtar eller anger den vertikala upplösningen för bilden i punkter per tum.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Hämtar eller anger den horisontella upplösningen för bilden i punkter per tum.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): Hämta eller sätta kompressionstyp för bilder när [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) är specificerat som Tiff.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Anger om bakgrunden för en bild ska vara transparent när ImageFormat anges som Png.  

## **Konvertera Excel-arbetsbok till Markdown**  
Aspose.Cells API ger stöd för att exportera kalkylblad till Markdown-format. För att exportera det aktiva kalkylbladet till Markdown, skicka [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter till [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-metoden. Du kan även använda [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) klassen för att specificera ytterligare inställningar för export av kalkylblad till Markdown.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Markdown med hjälp av [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem. Se den genererade [utdata Markdown-filen](md_sample.txt) för referens.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **Konvertera Excel-arbetsbok till JSON**  
Aspose.Cells stöder konvertering av en arbetsbok till JSON (JavaScript Object Notation) fil.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till Json med hjälp av [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem. Se koden för att konvertera [källfilen](Book1.xlsx) till [utdata Json-fil](Book1.Json) för referens.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **Konvertera Excel till XML**  
Aspose.Cells stöder konvertering av en arbetsbok till Excel 2003 Spreadsheet XML och vanliga XML-data.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **Konvertera Excel-arbetsbok till TIFF**  
Aspose.Cells stöder konvertering av en arbetsbok till TIFF-fil.  

Kodsnutten nedan visar hur man konverterar Excel till TIFF:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **Konvertera Excel-arbetsbok till DOCX**  
Aspose.Cells API ger stöd för konvertering av kalkylblad till DOCX-format. För att exportera arbetsboken till DOCX, skicka [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter till [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-metoden. Du kan även använda [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) klassen för att specificera ytterligare inställningar för export till DOCX.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till DOCX med hjälp av [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem. Se den genererade [output DOCX-filen](Book1.docx) för referens.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **Konvertera Excel-arbetsbok till PPTX**  
Aspose.Cells API ger stöd för konvertering av kalkylblad till PPTX-format. För att exportera arbetsboken till PPTX, skicka [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter till [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-metoden. Du kan även använda [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) klassen för att specificera ytterligare inställningar för export till PPTX.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till PPTX med hjälp av [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem. Se den genererade [utdata PPTX-filen](Book1.pptx) för referens.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **Konvertera Excel-arbetsbok till EPUB**  
Aspose.Cells API ger stöd för konvertering av kalkylblad till EPUB-format. För att exportera arbetsboken till EPUB, skicka [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter till [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-metoden. Du kan även använda [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) klassen för att specificera ytterligare inställningar för export till Epub.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till EPUB med hjälp av [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **Konvertera Excel-arbetsbok till AZW3**  
Aspose.Cells API ger stöd för konvertering av kalkylblad till AZW3-format. För att exportera arbetsboken till AZW3, skicka [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) som andra parameter till [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-metoden. Du kan även använda [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) klassen för att specificera ytterligare inställningar för export till AZW3.  

Följande kodexempel visar hur man exporterar det aktiva kalkylbladet till AZW3 med hjälp av [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) enum-medlem.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **Fortsatta ämnen**  
- [Konvertera revidering av XLSB till XLSM](/cells/sv/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/sv/nodejs-cpp/convert-excel-to-html/)  
- [Bild](/cells/sv/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/sv/nodejs-cpp/convert-workbook-to-json/)  
- [Konvertera Excel-arbetsbok till Ods, Sxc och Fods (OpenOffice / LibreOffice calc).](/cells/sv/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/sv/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Konvertera Excel till CSV, TSV och Txt](/cells/sv/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Spåra Dokumentkonverteringsframsteg](/cells/sv/nodejs-cpp/track-document-conversion-progress/)  
- [Konvertera CSV, TSV och TXT till Excel](/cells/sv/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

