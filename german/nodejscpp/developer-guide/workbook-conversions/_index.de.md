---  
title: Excel in Pdf, Bild und andere Formate konvertieren  
linktitle: Arbeitsmappen Konvertierungen  
type: docs  
weight: 65  
url: /de/nodejs-cpp/convert-workbook-to-different-formats/  
description: Excel Dateien in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML und mehr konvertieren mit Node.js über C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch gesehen bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.  
{{% /alert %}}  

## **Excel-Arbeitsmappe in PDF konvertieren**  
PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.  

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.  

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

## **Excel-Arbeitsmappe in JPG konvertieren**  
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in JPG. Das untenstehende Codebeispiel zeigt, wie eine Arbeitsmappe als JPG gespeichert wird.  

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

## **Excel-Arbeitsmappe in Bild konvertieren**  
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in Bilder. Das untenstehende Codebeispiel zeigt, wie eine Arbeitsmappe als Bilder gespeichert wird.  

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

## **Excel-Arbeitsmappe in XPS konvertieren**  
Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, Darstellung, Verarbeitung und zum Drucken von Dokumenten definiert.  

Die Auszeichnungssprache für XPS ist ein Subset von XAML, das es ermöglicht, Vektorgrafikelemente in Dokumente zu integrieren, indem XAML die Windows Presentation Foundation (WPF)-Primitive markiert. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitiven beschrieben.  

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Dazu gehören eine XML-Auszeichnungsdatei für jede Seite, Text, eingebettete Schriften, Rasterbilder, 2D-Vektorgrafiken sowie die Informationen zum Digital Rights Management. Der Inhalt einer XPS-Datei kann einfach untersucht werden, indem sie in einer Anwendung geöffnet wird, die ZIP-Dateien unterstützt.  

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel in XPS unterstützt.  

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

## **Excel zu Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren**  
Aspose.Cells unterstützt das Konvertieren von Excel-Dateien in Ods, Sxc und Fods. Das untenstehende Codebeispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods konvertiert wird.  

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

## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**  
MHTML kombiniert normales HTML mit externen Ressourcen (das heißt, Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.  

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.  

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.  

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

## **Excel-Arbeitsmappe in HTML konvertieren**  
Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.  

Das folgende Beispiel zeigt, wie man eine Arbeitsmappe als HTML-Datei speichert.  

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

## **Bildvoreinstellungen für HTML einstellen**  
Ab Version 8.0.2 hat Aspose.Cells die [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) für die [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) Klasse öffentlich gemacht, um Entwicklern die Angabe von Bildeinstellungen beim Speichern von Tabellen in HTML-Format zu ermöglichen.  

Im Folgenden sind Details einiger Bildvoreinstellungen aufgelistet,  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/): Gibt den Bildtyp an. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--): Gibt die Qualität des Bildes zwischen 0 und 100 an, wenn [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) als Jpeg angegeben wird.  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/): Holt oder setzt den Komprimierungstyp für die Bilder, wenn [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) als Tiff angegeben ist.  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.  

## **Excel-Arbeitsmappe in Markdown konvertieren**  
Die Aspose.Cells-API bietet Unterstützung für den Export von Tabellenblättern in Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, übergeben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-Methode. Sie können auch die [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach Markdown festzulegen.  

Das folgende Codebeispiel zeigt das Exportieren des aktiven Arbeitsblatts nach Markdown unter Verwendung des [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds. Bitte sehen Sie sich die [Ausgabedatei im Markdown-Format](md_sample.txt) an, die vom Code generiert wurde.  

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

## **Excel-Arbeitsmappe in JSON konvertieren**  
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine Json-Datei (JavaScript Object Notation).  

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach Json unter Verwendung des [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe den Code, um die [Quell-Datei](Book1.xlsx) in die generierte [Ausgabe-Json-Datei](Book1.Json) zu konvertieren.  

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

## **Excel in XML umwandeln**  
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in das Excel 2003 Spreadsheet XML- und das Plain-XML-Format.  

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

## **Excel-Arbeitsmappe in TIFF umwandeln**  
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine TIFF-Datei.  

Der unten stehende Codeausschnitt zeigt, wie Excel in TIFF umgewandelt wird:  

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

## **Excel-Arbeitsmappe in DOCX umwandeln**  
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das DOCX-Format. Um die Arbeitsmappe nach DOCX zu exportieren, übergebe [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach DOCX festzulegen.  

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach DOCX unter Verwendung des [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe die [Ausgabedatei DOCX](Book1.docx), die vom Code generiert wurde.  

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

## **Excel-Arbeitsmappe in PPTX umwandeln**  
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das PPTX-Format. Um die Arbeitsmappe nach PPTX zu exportieren, übergebe [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach PPTX festzulegen.  

Das folgende Codebeispiel demonstriert das Exportieren des aktiven Arbeitsblatts nach PPTX unter Verwendung des [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds. Bitte siehe die [Ausgabedatei PPTX](Book1.pptx), die vom Code generiert wurde.  

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

## **Excel-Arbeitsmappe in EPUB konvertieren**  
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das EPUB-Format. Um die Arbeitsmappe nach EPUB zu exportieren, übergebe [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach EPUB festzulegen.  

Das folgende Code-Beispiel zeigt die Exportierung des aktiven Arbeitsblatts nach EPUB unter Verwendung des [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds.  

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

## **Excel-Arbeitsmappe nach AZW3 konvertieren**  
Die Aspose.Cells API unterstützt die Konvertierung von Tabellenkalkulationen in das AZW3-Format. Um die Arbeitsmappe nach AZW3 zu exportieren, übergebe [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) als zweiten Parameter der [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-)-Methode. Du kannst auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach AZW3 festzulegen.  

Das folgende Code-Beispiel zeigt die Exportierung des aktiven Arbeitsblatts nach AZW3 unter Verwendung des [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglieds.  

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

## **Erweiterte Themen**  
- [Konvertieren der Überarbeitung von XLSB zu XLSM](/cells/de/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/de/nodejs-cpp/convert-excel-to-html/)  
- [Bild](/cells/de/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/de/nodejs-cpp/convert-workbook-to-json/)  
- [Excel-Arbeitsmappe in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren.](/cells/de/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/de/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [Excel in CSV, TSV und Txt konvertieren](/cells/de/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/nodejs-cpp/track-document-conversion-progress/)  
- [CSV, TSV und TXT in Excel umwandeln](/cells/de/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

