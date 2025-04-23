---
title: PDF mit Node.js via C++
linktitle: Pdf
type: docs
weight: 220
url: /de/nodejs-cpp/convert-excel-to-pdf/
description: Erfahren Sie, wie Sie Excel Arbeitsmappen mithilfe von Aspose.Cells for Node.js via C++ in PDF umwandeln. 
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt die Konvertierung eines Excel-Arbeitsblatts in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.
{{% /alert %}}

## **Konvertierung der Excel-Arbeitsmappe in PDF**

PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ schreibt direkt die Informationen über API und Versionsnummer in die Ausgabedokumente. Zum Beispiel füllt es beim Rendern des Dokuments in PDF das Feld **PDF Producer** mit einem Wert, z.B. 'Aspose.Cells v23.2'.

Bitte beachten Sie, dass Sie diese Informationen im Ausgabedokument mit Hilfe der [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--)-Eigenschaft ändern können.
{{% /alert %}}

### **Direkte Konvertierung**

Aspose.Cells for Node.js via C++ unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei als PDF mit der Methode [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse. Die [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)-Methode bietet das [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)-Aufzählungsmitglied, das die nativen Excel-Dateien in PDF-Format umwandelt.

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

Instantiieren Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwendung von Formatierungen, Setzen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) auf der Tabellenkalkulation mithilfe der APIs von Aspose.Cells durch.
1. Sobald der Code für die Tabelle fertig ist, rufen Sie die Methode [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) der [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse auf, um die Tabelle zu speichern.

Das Dateiformat sollte PDF sein. Wählen Sie *Pdf* (einen vordefinierten Wert) aus der [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) Aufzählung aus, um das endgültige PDF-Dokument zu erzeugen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Erweiterte Konvertierung**

Sie können auch die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) verwenden, um verschiedene Eigenschaften für die Konvertierung festzulegen. Das Festlegen verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) ermöglicht die Steuerung der Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die Ausgabe-PDF. 

Die wichtigste Eigenschaft ist [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), mit der Sie das Niveau der Konformität der PDF-Standards festlegen können. Derzeit können Sie in den Formaten PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u speichern. Beachten Sie, dass bei PDF/A das Ausgabedateiformat größer ist als bei einer regulären PDF-Datei.

#### **Speichern der Arbeitsmappe als PDF/A-kompatible Dateien**

Der unten bereitgestellte Codeausschnitt zeigt, wie die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) verwendet wird, um Excel-Dateien im PDF/A-konformen PDF-Format zu speichern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Bitte beachten Sie, dass die Eigenschaft [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) mit der Version Aspose.Cells for Node.js via C++ 5.3.0 hinzugefügt wurde.
{{% /alert %}}

#### **Legen Sie die Erstellungszeit des PDF fest**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) können Sie die PDF-Erstellungszeit abrufen oder festlegen. Der folgende Code zeigt die Verwendung der Eigenschaft [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) zum Festlegen der Erstellungszeit der PDF-Datei.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Option ContentCopyForAccessibility festlegen**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) können Sie die PDF-[**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--)-Option abrufen oder festlegen, um den Inhaltszugriff im konvertierten PDF zu steuern.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Benutzerdefinierte Eigenschaften in PDF exportieren**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in die PDF exportieren. Der [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/)-Enumerator dient dazu, den Exportweg der Eigenschaften anzugeben. Diese Eigenschaften können im Adobe Acrobat Reader eingesehen werden, indem Sie auf Datei und dann auf Eigenschaften klicken, wie im folgenden Bild gezeigt. Die Vorlagendatei "sourceWithCustProps.xlsx" kann [hier](sourceWithCustProps.xlsx) heruntergeladen werden, um sie zu testen, und die Ausgabe-PDF-Datei "outSourceWithCustProps" steht [hier](outSourceWithCustProps.pdf) für die Analyse zur Verfügung.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Konvertierungseigenschaften**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Excel-zu-PDF-Konvertierung von Aspose.Cells hat immer noch ein paar Einschränkungen. MapChart wird beim Konvertieren in das PDF-Format nicht unterstützt. Außerdem werden einige Zeichenobjekte nicht gut unterstützt.

Die nachfolgende Tabelle listet alle Funktionen auf, die beim Exportieren nach PDF mit Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht abschließend und deckt nicht alle Tabellenattributen ab, identifiziert jedoch die Funktionen, die nicht unterstützt oder teilweise unterstützt werden, wenn sie in PDF konvertiert werden.

|**Dokumentenelement**|**Attribut**|**Unterstützt**|**Anmerkungen**|
| :- | :- | :- | :- |
|Ausrichtung| |Ja| |
|Hintergrund-Einstellungen| |Ja| |
|Rahmen|Farbe|Ja| |
|Rahmen|Linienart|Ja| |
|Rahmen|Linienbreite|Ja| |
|Zellendaten| |Ja| |
|Kommentare| |Ja| |
|Bedingte Formatierung| |Ja| |
|Dokumenteigenschaften| |Ja| |
|Zeichenobjekte| |Teilweise|Schatten und 3-D-Effekte für Zeichenobjekte werden nicht gut unterstützt; WordArt und SmartArt werden teilweise unterstützt.|
|Schriftart|Größe|Ja| |
|Schriftart|Farbe|Ja| |
|Schriftart|Stil|Ja| |
|Schriftart|Unterstrichen|Ja| |
|Schriftart|Effekte|Ja||
|Bilder| |Ja| |
|Hyperlink| |Ja| |
|Diagramme| |Teilweise|Karten Diagramme werden nicht unterstützt.|
|Zellen zusammenführen| |Ja| |
|Seitenumbruch| |Ja| |
|Seiteneinrichtung|Kopfzeile/Fußzeile|Ja| |
|Seiteneinrichtung|Ränder|Ja| |
|Seiteneinrichtung|Seitenorientierung|Ja| |
|Seiteneinrichtung|Seitengröße|Ja| |
|Seiteneinrichtung|Druckbereich|Ja| |
|Seiteneinrichtung|Drucktitel|Ja| |
|Seiteneinrichtung|Skalierung|Ja| |
|Zeilenhöhe/Spaltenbreite| |Ja| |
|RTL (Rechts nach Links) Sprache| |Ja| |

{{% alert color="primary" %}}
Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.
{{% /alert %}}

## **Erweiterte Themen**
- [PDF-Lesezeichen mit benannten Zielen hinzufügen](/cells/de/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll](/cells/de/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändern Sie die Schriftart nur für bestimmte Unicode-Zeichen beim Speichern als PDF](/cells/de/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Konvertieren Sie XLSX-Datei in PDF-Format](/cells/de/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Excel-Datei in das PDF-Format konvertieren, das mit PDFA-1a kompatibel ist](/cells/de/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie XLS-Datei mit Bildern oder Diagrammen in PDF](/cells/de/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie PdfBookmarkEntry für Diagrammblatt](/cells/de/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattsäulen auf eine einzige PDF-Seite an](/cells/de/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der DrawObjectEventHandler-Klasse](/cells/de/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Holen Sie sich Warnungen für Schriftartenersatz beim Rendern von Excel-Dateien](/cells/de/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorieren Sie Fehler beim Rendern von Excel in PDF](/cells/de/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten - Excel zu PDF-Konvertierung](/cells/de/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare drucken beim Speichern als PDF](/cells/de/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen](/cells/de/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Eine PDF-Seite pro Excel-Arbeitsblatt rendern - Excel in PDF konvertieren](/cells/de/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern von Unicode-Zusatzzeichen im Ausgabe-PDF durch Aspose.Cells](/cells/de/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Neu abgetastete Bilder - Excel zu PDF-Konvertierung](/cells/de/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Jedes Arbeitsblatt in eine separate PDF-Datei speichern](/cells/de/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Excel als PDF mit Standard- oder Minimalgröße speichern](/cells/de/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Bestimmte Arbeitsblätter als PDF speichern](/cells/de/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/nodejs-cpp/secure-pdf-documents/)
- [Angeben, wie Zeilenumbruch im Ausgabe-PDF und Bild erfolgen soll](/cells/de/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
