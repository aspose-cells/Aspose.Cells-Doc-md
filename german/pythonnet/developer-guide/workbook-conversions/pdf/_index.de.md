---
title: Pdf
type: docs
weight: 220
url: /de/python-net/convert-excel-to-pdf/
description: Erfahren Sie, wie Sie Excel mit Aspose.Cells for Python via .NET API in PDF konvertieren.
keywords: Python converT Excel to PDF, ConverT Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET unterstützt die Konvertierung einer Excel-Arbeitsmappe in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

##  **Konvertieren einer Excel-Arbeitsmappe in PDF**

PDF-Dateien werden häufig zum Austausch von Dokumenten zwischen Organisationen, Behörden und Einzelpersonen verwendet. Es handelt sich um ein Standarddokumentformat und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft-Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells for Python via .NET unterstützt die Konvertierung von Excel-Dateien in PDF und sorgt für eine hohe visuelle Wiedergabetreue bei der Konvertierung.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET schreibt die Informationen zu API und der Versionsnummer direkt in Ausgabedokumente. Wenn beispielsweise das Dokument in PDF gerendert wird, wird Aspose.Cells for Python via .NET ausgefüllt**PDF Produzent** Feld mit Wert, z. B. „Aspose.Cells for Python via .NET v23.2“.

 Bitte beachten Sie, dass Sie diese Informationen in den Ausgabedokumenten ändern können**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)** Eigentum.

{{% /alert %}}

###  **Direkte Konvertierung**

 Aspose.Cells for Python via .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei unter PDF mit**[Arbeitsmappe](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**Klasse'**[speichern](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** Methode. Der**[speichern](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** Methode bietet die**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**Aufzählungsmitglied, das die nativen Excel-Dateien in das Format PDF konvertiert.

Führen Sie die folgenden Schritte aus, um die Excel-Tabellen direkt in das Format PDF zu konvertieren:

1.  Instanziieren Sie ein Objekt von**[Arbeitsmappe](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**Klasse durch Aufrufen ihres leeren Konstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie mithilfe der APIs Aspose.Cells for Python via .NET beliebige Arbeiten (Eingabe von Daten, Anwenden von Formatierungen, Festlegen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) in der Tabelle aus.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie auf**[Arbeitsmappe](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**Klasse'**[speichern](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**Methode zum Speichern der Tabelle.

 Das Dateiformat sollte PDF sein, also wählen Sie es aus*PDF* (ein vordefinierter Wert) aus dem**[Speicherformat](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**Aufzählung, um das endgültige Dokument PDF zu generieren.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

###  **Erweiterte Konvertierung**

 Sie können sich auch für die Verwendung entscheiden**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften des**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** Mit der Klasse können Sie die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe PDF steuern. Die wichtigste Eigenschaft ist**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**Dadurch können Sie die Excel-Dateien in PDF/A-kompatiblen PDF-Dateien speichern.

####  **Speichern der Arbeitsmappe in PDF/A-kompatiblen Dateien**

 Das unten bereitgestellte Code-Snippet zeigt die Verwendung von**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**Klasse zum Speichern von Excel-Dateien im PDF/A-kompatiblen PDF-Format.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**Die Eigenschaft wurde mit der Veröffentlichung von Aspose.Cells for Python via .NET for .NET 5.3.0 hinzugefügt.

{{% /alert %}}

####  **Legen Sie die Erstellungszeit PDF fest**

 Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**Klasse können Sie die Erstellungszeit PDF abrufen oder festlegen. Der folgende Code demonstriert die Verwendung von**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)** Eigenschaft, um den Erstellungszeitpunkt der Datei PDF festzulegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

####  **Legen Sie die Option „ContentCopyForAccessibility“ fest**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** Klasse können Sie die PDF erhalten oder festlegen**[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** Option zur Steuerung des Inhaltszugriffs in der konvertierten PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

####  **Benutzerdefinierte Eigenschaften nach PDF exportieren**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** Klasse können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe nach PDF exportieren.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**Es wird ein Enumerator bereitgestellt, um anzugeben, wie Eigenschaften exportiert werden. Diese Eigenschaften können in Adobe Acrobat Reader angezeigt werden, indem Sie auf „Datei“ und dann auf die Option „Eigenschaften“ klicken, wie in der folgenden Abbildung dargestellt. Die Vorlagendatei „sourceWithCustProps.xlsx“ kann heruntergeladen werden[Hier](sourceWithCustProps.xlsx) Zum Testen und Ausgeben steht die Datei „outSourceWithCustProps“ PDF zur Verfügung[Hier](outSourceWithCustProps.pdf) zur Analyse.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

###  **Konvertierungsattribute**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Konvertierung von Aspose.Cell von Excel in PDF weist noch einige Einschränkungen auf. MapChart wird bei der Konvertierung in das Format PDF nicht unterstützt. Außerdem werden einige Zeichenobjekte nicht gut unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Export nach PDF mit Aspose.Cells for Python via .NET vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabellenattribute ab, identifiziert jedoch die Funktionen, die für die Konvertierung nicht oder teilweise unterstützt werden an PDF.

|**Dokumentelement**|**Attribut**|**Unterstützt**|**Anmerkungen**|
| :- | :- | :- | :- |
|Ausrichtung| |Ja| |
|Hintergrundeinstellungen| |Ja| |
|Grenze|Farbe|Ja| |
|Grenze|Linienstil|Ja| |
|Grenze|Linienbreite|Ja| |
|Cell Daten| |Ja| |
|Kommentare| |Ja| |
|Bedingte Formatierung| |Ja| |
|Dokumenteigenschaften| |Ja| |
|Zeichnungsobjekte| |Teilweise|Schatten- und 3D-Effekte für Zeichenobjekte werden nicht gut unterstützt; WordArt und SmartArt werden teilweise unterstützt.|
|Schriftart|Größe|Ja| |
|Schriftart|Farbe|Ja| |
|Schriftart|Stil|Ja| |
|Schriftart|Unterstreichen|Ja| |
|Schriftart|Auswirkungen|Ja||
|Bilder| |Ja| |
|Hyperlink| |Ja| |
|Diagramme| |Teilweise|MapChart wird nicht unterstützt.|
|Zusammengelegt Cells| |Ja| |
|Seitenumbruch| |Ja| |
|Seiteneinrichtung|Kopfzeile Fußzeile|Ja| |
|Seiteneinrichtung|Ränder|Ja| |
|Seiteneinrichtung|Seitenausrichtung|Ja| |
|Seiteneinrichtung|Seitengröße|Ja| |
|Seiteneinrichtung|Druckbereich|Ja| |
|Seiteneinrichtung|Titel drucken|Ja| |
|Seiteneinrichtung|Skalierung|Ja| |
|Zeilenhöhe/Spaltenbreite| |Ja| |
|RTL-Sprache (von rechts nach links).| |Ja| |

{{% alert color="primary" %}}

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)-Methode kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}

##  **Vorabthemen**
- [Fügen Sie PDF Lesezeichen hinzu](/cells/de/python-net/add-pdf-bookmarks/)
- [Fügen Sie PDF-Lesezeichen mit benannten Zielen hinzu](/cells/de/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Vermeiden Sie leere Seiten in der Ausgabe PDF, wenn nichts zum Drucken vorhanden ist](/cells/de/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Konvertieren Sie die Datei XLSX in das Format PDF](/cells/de/python-net/convert-xlsx-file-to-pdf-format/)
- [Konvertieren Sie eine Excel-Datei in das mit PDFA-1a kompatible Format PDF](/cells/de/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie die Datei XLS mit Bildern oder Diagrammen in PDF](/cells/de/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie einen PDFBookmarkEntry für das Diagrammblatt](/cells/de/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattspalten auf eine einzelne Seite PDF an](/cells/de/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorieren Sie Fehler beim Rendern von Excel auf PDF](/cells/de/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten – Excel auf PDF Konvertierung](/cells/de/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare beim Speichern unter PDF ausdrucken](/cells/de/python-net/print-comments-while-saving-to-pdf/)
- [Rendern Sie Office-Add-Ins, während Sie Excel in PDF konvertieren](/cells/de/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt – Konvertierung von Excel in PDF](/cells/de/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern Sie Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells](/cells/de/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling hinzugefügter Bilder – Konvertierung von Excel in PDF](/cells/de/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei](/cells/de/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Speichern Sie Excel unter PDF mit Standard- oder Mindestgröße](/cells/de/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Speichern Sie die angegebenen Arbeitsblätter unter PDF](/cells/de/python-net/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/python-net/secure-pdf-documents/)
- [Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll](/cells/de/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
