---
title: Excel nach PDF mit C++ konvertieren
linktitle: Excel in PDF konvertieren
type: docs
weight: 220
url: /de/cpp/convert-excel-to-pdf/
description: Erfahren Sie, wie Sie Excel Arbeitsmappen mit Aspose.Cells und C++ in PDF umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsmappen in PDF. In diesem Beispiel sehen wir die vollständige Umwandlung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

## **Konvertierung der Excel-Arbeitsmappe in PDF**

PDF-Dateien werden häufig verwendet, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es ist ein standardisiertes Dokumentformat und Softwareentwickler werden oft gefragt, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente umzuwandeln.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{% alert color="primary" %}}

Aspose.Cells for C++ schreibt direkt die Informationen über API und Versionsnummer in Ausgabedokumente. Zum Beispiel füllt Aspose.Cells for C++ beim Rendern eines Dokuments in PDF das Feld **PDF Producer** mit einem Wert, z.B. 'Aspose.Cells v23.2'.

Bitte beachten Sie, dass Sie diese Angaben in Ausgabedokumenten mit der [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/)-Eigenschaft ändern können.

{{% /alert %}}

### **Direkte Konvertierung**

Aspose.Cells for C++ unterstützt die Konvertierung von Tabellen in PDF unabhängig von anderer Software. Speichern Sie eine Excel-Datei einfach mit der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse und der [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode als PDF. Die [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode bietet das [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)-Aufzählungsmitglied, das die nativen Excel-Dateien in PDF-Format umwandelt.

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

1. Erstellen eines Objekts der [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse durch Aufrufen ihres Standardkonstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie alle Arbeiten aus (Daten eingeben, Formatierungen anwenden, Formeln einstellen, Bilder oder andere Zeichenobjekte einfügen usw.) auf dem Arbeitsblatt mit den APIs von Aspose.Cells durch.
1. Wenn der Code für das Arbeitsblatt fertig ist, rufen Sie die [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode der Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) auf, um das Arbeitsblatt zu speichern.

Das Dateiformat sollte PDF sein, wählen Sie also *Pdf* (einen vordefinierten Wert) aus der [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)-Aufzählung, um das endgültige PDF-Dokument zu erstellen.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Erweiterte Konvertierung**

Sie können auch die [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Festlegen verschiedener Eigenschaften der [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse gibt Ihnen die Kontrolle über Druck-, Schrift-, Sicherheits- und Komprimierungseinstellungen für das Ausgabe-PDF.

Das wichtigste Property ist [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), mit dem Sie das Konformitätsniveau der PDF-Standards festlegen können. Derzeit können Sie auf PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u speichern. Beachten Sie, dass bei Verwendung des PDF/A-Formats die Ausgabedatei größer ist als eine reguläre PDF-Datei.

#### **Speichern der Arbeitsmappe als PDF/A-kompatible Dateien**

Der untenstehende Codeausschnitt zeigt, wie die [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse verwendet wird, um Excel-Dateien im PDF/A-konformen PDF-Format zu speichern.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Bitte beachten Sie, dass die Eigenschaft [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) mit der Version Aspose.Cells for C++ 5.3.0 hinzugefügt wurde.

{{% /alert %}}

#### **Legen Sie die Erstellungszeit des PDF fest**

Mit der [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse können Sie die Erstellungszeit des PDFs abrufen oder festlegen. Das folgende Beispiel demonstriert die Verwendung der [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/)-Eigenschaft, um die Erstellungszeit der PDF-Datei festzulegen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Option ContentCopyForAccessibility festlegen**

Mit der [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse können Sie die [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/)-Option des PDFs abrufen oder festlegen, um den Zugriff auf den Inhalt im konvertierten PDF zu steuern.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Benutzerdefinierte Eigenschaften in PDF exportieren**

Mit der [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)-Klasse können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in das PDF exportieren. Der [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/)-Enumerator wird bereitgestellt, um die Art der Exporte zu spezifizieren. Diese Eigenschaften sind in Adobe Acrobat Reader sichtbar, wenn Sie auf Datei klicken und dann Eigenschaften auswählen, wie im folgenden Bild gezeigt. Die Vorlage "sourceWithCustProps.xlsx" kann [hier](sourceWithCustProps.xlsx) zum Testen heruntergeladen werden, und die Ausgabedatei "outSourceWithCustProps" steht [hier](outSourceWithCustProps.pdf) zur Analyse bereit.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Konvertierungseigenschaften**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Excel-zu-PDF-Konvertierung von Aspose.Cells weist noch einige Einschränkungen auf. MapChart wird beim Konvertieren in PDF-Format nicht unterstützt. Außerdem sind einige Zeichenobjekte nicht gut unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Export in PDF mit Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabellenblattattribute ab, aber sie zeigt Funktionen, die nicht unterstützt werden oder nur teilweise unterstützt werden bei der Konvertierung in PDF.

| **Dokumentelement** | **Attribut** | **Unterstützt** | **Hinweise** |
| :- | :- | :- | :- |
| Ausrichtung |  | Ja |  |
| Hintergrund-Einstellungen |  | Ja |  |
| Rahmen | Farbe | Ja |  |
| Rahmen | Linienstil | Ja |  |
| Rahmen | Linienstärke | Ja |  |
| Zellendaten |  | Ja |  |
| Kommentare |  | Ja |  |
| Bedingte Formatierung |  | Ja |  |
| Dokumenteigenschaften |  | Ja |  |
| Zeichenobjekte |  | Teilweise | Schatten- und 3D-Effekte für Zeichenobjekte werden nicht gut unterstützt; WordArt und SmartArt werden teilweise unterstützt. |
| Schriftart | Größe | Ja |  |
| Schriftart | Farbe | Ja |  |
| Schriftart | Stil | Ja |  |
| Schriftart | Unterstreichung | Ja |  |
| Schriftart | Effekte | Ja |  |
| Bilder |  | Ja |  |
| Hyperlink |  | Ja |  |
| Diagramme |  | Teilweise | MapChart wird nicht unterstützt. |
| Zellen verbinden |  | Ja |  |
| Seitenumbruch |  | Ja |  |
| Seitenlayout | Kopf-/Fußzeile | Ja |  |
| Seitenlayout | Ränder | Ja |  |
| Seitenlayout | Seitenorientierung | Ja |  |
| Seiteneinrichtung | Seitengröße | Ja |  |
| Seiteneinrichtung | Druckbereich | Ja |  |
| Seiteneinrichtung | Drucktitel | Ja |  |
| Seiteneinrichtung | Skalierung | Ja |  |
| Zeilenhöhe/Spaltenbreite |  | Ja |  |
| RTL (Rechts nach Links) Sprache |  | Ja |  |

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) direkt vor dem Rendern der Tabelle in das PDF-Format aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}

## **Erweiterte Themen**
- [PDF-Lesezeichen mit benannten Zielen hinzufügen](/cells/de/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Ändern Sie die Schriftart nur für bestimmte Unicode-Zeichen beim Speichern als PDF](/cells/de/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Konvertieren Sie XLSX-Datei in PDF-Format](/cells/de/cpp/convert-xlsx-file-to-pdf-format/)
- [Excel-Datei in das PDF-Format konvertieren, das mit PDFA-1a kompatibel ist](/cells/de/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie XLS-Datei mit Bildern oder Diagrammen in PDF](/cells/de/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie PdfBookmarkEntry für Diagrammblatt](/cells/de/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattsäulen auf eine einzige PDF-Seite an](/cells/de/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der DrawObjectEventHandler-Klasse](/cells/de/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Holen Sie sich Warnungen für Schriftartenersatz beim Rendern von Excel-Dateien](/cells/de/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorieren Sie Fehler beim Rendern von Excel in PDF](/cells/de/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten - Excel zu PDF-Konvertierung](/cells/de/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare drucken beim Speichern als PDF](/cells/de/cpp/print-comments-while-saving-to-pdf/)
- [Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen](/cells/de/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Eine PDF-Seite pro Excel-Arbeitsblatt rendern - Excel in PDF konvertieren](/cells/de/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern von Unicode-Zusatzzeichen im Ausgabe-PDF durch Aspose.Cells](/cells/de/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Neu abgetastete Bilder - Excel zu PDF-Konvertierung](/cells/de/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Jedes Arbeitsblatt in eine separate PDF-Datei speichern](/cells/de/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Excel als PDF mit Standard- oder Minimalgröße speichern](/cells/de/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Bestimmte Arbeitsblätter als PDF speichern](/cells/de/cpp/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/cpp/secure-pdf-documents/)
- [Angeben, wie Zeilenumbruch im Ausgabe-PDF und Bild erfolgen soll](/cells/de/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="cpp" >}}
