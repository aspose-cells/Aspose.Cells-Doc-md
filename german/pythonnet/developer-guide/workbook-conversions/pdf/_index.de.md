---
title: Pdf
type: docs
weight: 220
url: /de/python-net/convert-excel-to-pdf/
description: Erfahren Sie, wie Sie Excel in PDF mit der Aspose.Cells for Python via .NET API konvertieren.
keywords: Python von Excel zu PDF konvertieren, Excel nach PDF konvertieren mit Python, Python speichert Excel nach PDF, Excel nach PDF in Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET unterstützt die Konvertierung einer Excel-Arbeitsmappe in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

## **Konvertierung der Excel-Arbeitsmappe in PDF**

PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells for Python via .NET unterstützt die Konvertierung von Excel-Dateien in PDF und bewahrt bei der Konvertierung eine hohe visuelle Treue.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET schreibt die Informationen zum API und zur Versionsnummer direkt in die Ausgabedokumente. Beispielsweise füllt Aspose.Cells for Python via .NET bei der Umsetzung von Dokumenten in PDF das Feld **PDF-Produzent** mit dem Wert 'Aspose.Cells for Python via .NET v23.2',.

Bitte beachten Sie, dass Sie diese Informationen im Ausgabedokument mit Hilfe der [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)-Eigenschaft ändern können.

{{% /alert %}}

### **Direkte Konvertierung**

Aspose.Cells für Python via .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei im PDF-Format unter Verwendung der Methode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Die Methode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) bietet das [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) Aufzählungsmitglied, das die nativen Excel-Dateien in das PDF-Format konvertiert.

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

Instantiieren Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingangsdaten, Formatierung anwenden, Formeln setzen, Bilder oder andere Zeichenobjekte einfügen usw.) auf der Tabellenkalkulation mit den APIs von Aspose.Cells für Python via .NET durch.
Wenn der Tabellenkalkulationscode komplett ist, rufen Sie die Methode [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf, um die Tabellenkalkulation zu speichern.

Das Dateiformat sollte PDF sein, wählen Sie also *PDF* (einen vordefinierten Wert) aus der [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) Aufzählung, um das endgültige PDF-Dokument zu generieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Erweiterte Konvertierung**

Sie können auch die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Durch das Festlegen verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) haben Sie Kontrolle über die Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für das Ausgabe-PDF. Die wichtigste Eigenschaft ist [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/), die es ermöglicht, die Excel-Dateien als PDF/A-konforme PDF-Dateien zu speichern.

#### **Speichern der Arbeitsmappe als PDF/A-kompatible Dateien**

Der unten bereitgestellte Codeausschnitt zeigt, wie die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) verwendet wird, um Excel-Dateien im PDF/A-konformen PDF-Format zu speichern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, die [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)-Eigenschaft wurde mit der Veröffentlichung von Aspose.Cells für Python via .NET für .NET 5.3.0 hinzugefügt.

{{% /alert %}}

#### **Legen Sie die Erstellungszeit des PDF fest**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) können Sie die PDF-Erstellungszeit abrufen oder festlegen. Der folgende Code zeigt die Verwendung der Eigenschaft [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) zum Festlegen der Erstellungszeit der PDF-Datei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Option ContentCopyForAccessibility festlegen**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) können Sie die PDF-[**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)-Option abrufen oder festlegen, um den Inhaltszugriff im konvertierten PDF zu steuern.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Benutzerdefinierte Eigenschaften in PDF exportieren**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in die PDF exportieren. Der [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)-Enumerator dient dazu, den Exportweg der Eigenschaften anzugeben. Diese Eigenschaften können im Adobe Acrobat Reader eingesehen werden, indem Sie auf Datei und dann auf Eigenschaften klicken, wie im folgenden Bild gezeigt. Die Vorlagendatei "sourceWithCustProps.xlsx" kann [hier](sourceWithCustProps.xlsx) heruntergeladen werden, um sie zu testen, und die Ausgabe-PDF-Datei "outSourceWithCustProps" steht [hier](outSourceWithCustProps.pdf) für die Analyse zur Verfügung.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Konvertierungseigenschaften**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Excel-zu-PDF-Konvertierung von Aspose.Cells hat immer noch ein paar Einschränkungen. MapChart wird beim Konvertieren in das PDF-Format nicht unterstützt. Außerdem werden einige Zeichenobjekte nicht gut unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Exportieren in PDF mit Aspose.Cells für Python via .NET vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabelleneigenschaften ab, identifiziert jedoch die Funktionen, die nicht unterstützt oder nur teilweise unterstützt werden, wenn sie in PDF konvertiert werden.

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

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch werden die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF dargestellt.

{{% /alert %}}

## **Erweiterte Themen**
- [PDF-Lesezeichen hinzufügen](/cells/de/python-net/add-pdf-bookmarks/)
- [PDF-Lesezeichen mit benannten Zielen hinzufügen](/cells/de/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll](/cells/de/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Konvertieren Sie XLSX-Datei in PDF-Format](/cells/de/python-net/convert-xlsx-file-to-pdf-format/)
- [Excel-Datei in das PDF-Format konvertieren, das mit PDFA-1a kompatibel ist](/cells/de/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie XLS-Datei mit Bildern oder Diagrammen in PDF](/cells/de/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie PdfBookmarkEntry für Diagrammblatt](/cells/de/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattsäulen auf eine einzige PDF-Seite an](/cells/de/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorieren Sie Fehler beim Rendern von Excel in PDF](/cells/de/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten - Excel zu PDF-Konvertierung](/cells/de/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare drucken beim Speichern als PDF](/cells/de/python-net/print-comments-while-saving-to-pdf/)
- [Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen](/cells/de/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Eine PDF-Seite pro Excel-Arbeitsblatt rendern - Excel in PDF konvertieren](/cells/de/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern von Unicode-Zusatzzeichen im Ausgabe-PDF durch Aspose.Cells](/cells/de/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Neu abgetastete Bilder - Excel zu PDF-Konvertierung](/cells/de/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Jedes Arbeitsblatt in eine separate PDF-Datei speichern](/cells/de/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel als PDF mit Standard- oder Minimalgröße speichern](/cells/de/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Bestimmte Arbeitsblätter als PDF speichern](/cells/de/python-net/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/python-net/secure-pdf-documents/)
- [Angeben, wie Zeilenumbruch im Ausgabe-PDF und Bild erfolgen soll](/cells/de/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
