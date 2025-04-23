---
title: Pdf
type: docs
weight: 220
url: /de/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung eines Excel-Arbeitsblatts in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

## **Konvertierung der Excel-Arbeitsmappe in PDF**

PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{% alert color="primary" %}}

Aspose.Cells for .NET schreibt die Informationen zu API und Versionsnummer direkt in Ausgabedokumente. Zum Beispiel füllt Aspose.Cells for .NET beim Rendern eines Dokuments in PDF das Feld **PDF-Produzent** mit dem Wert, z. B. 'Aspose.Cells v23.2',.

Bitte beachten Sie, dass Sie diese Informationen im Ausgabedokument mit Hilfe der [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)-Eigenschaft ändern können.

{{% /alert %}}

### **Direkte Konvertierung**

Aspose.Cells for .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderen Software. Speichern Sie einfach eine Excel-Datei als PDF unter Verwendung der [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse und der Methode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index). Die Methode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) stellt das Enumerationsglied [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) bereit, das die nativen Excel-Dateien in das PDF-Format konvertiert.

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

Instantiieren Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwendung von Formatierungen, Setzen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) auf der Tabellenkalkulation mithilfe der APIs von Aspose.Cells durch.
Wenn der Tabellenkalkulationscode komplett ist, rufen Sie die Methode [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) auf, um die Tabellenkalkulation zu speichern.

Das Dateiformat sollte PDF sein. Wählen Sie *Pdf* (einen vordefinierten Wert) aus der [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) Aufzählung aus, um das endgültige PDF-Dokument zu erzeugen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Erweiterte Konvertierung**

Sie können auch die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) verwenden, um verschiedene Eigenschaften für die Konvertierung festzulegen. Das Festlegen verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) ermöglicht die Steuerung der Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die Ausgabe-PDF. 

Die wichtigste Eigenschaft ist [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance), mit der Sie das Niveau der Konformität der PDF-Standards festlegen können. Derzeit können Sie in den Formaten PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u speichern. Beachten Sie, dass bei PDF/A das Ausgabedateiformat größer ist als bei einer regulären PDF-Datei.

#### **Speichern der Arbeitsmappe als PDF/A-kompatible Dateien**

Der unten bereitgestellte Codeausschnitt zeigt, wie die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) verwendet wird, um Excel-Dateien im PDF/A-konformen PDF-Format zu speichern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass die Eigenschaft [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) mit der Veröffentlichung von Aspose.Cells for .NET 5.3.0 hinzugefügt wurde.

{{% /alert %}}

#### **Legen Sie die Erstellungszeit des PDF fest**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) können Sie die PDF-Erstellungszeit abrufen oder festlegen. Der folgende Code zeigt die Verwendung der Eigenschaft [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) zum Festlegen der Erstellungszeit der PDF-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Option ContentCopyForAccessibility festlegen**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) können Sie die PDF-[**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)-Option abrufen oder festlegen, um den Inhaltszugriff im konvertierten PDF zu steuern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Benutzerdefinierte Eigenschaften in PDF exportieren**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in die PDF exportieren. Der [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)-Enumerator dient dazu, den Exportweg der Eigenschaften anzugeben. Diese Eigenschaften können im Adobe Acrobat Reader eingesehen werden, indem Sie auf Datei und dann auf Eigenschaften klicken, wie im folgenden Bild gezeigt. Die Vorlagendatei "sourceWithCustProps.xlsx" kann [hier](sourceWithCustProps.xlsx) heruntergeladen werden, um sie zu testen, und die Ausgabe-PDF-Datei "outSourceWithCustProps" steht [hier](outSourceWithCustProps.pdf) für die Analyse zur Verfügung.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

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

Wenn Ihre Tabellenkalkulation Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor der Umwandlung der Tabellenkalkulation in das PDF-Format aufzurufen. Dadurch werden die von den Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben.

{{% /alert %}}

## **Erweiterte Themen**
- [PDF-Lesezeichen hinzufügen](/cells/de/net/add-pdf-bookmarks/)
- [PDF-Lesezeichen mit benannten Zielen hinzufügen](/cells/de/net/add-pdf-bookmarks-with-named-destinations/)
- [Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll](/cells/de/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändern Sie die Schriftart nur für bestimmte Unicode-Zeichen beim Speichern als PDF](/cells/de/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Steuerung des Ladens externer Ressourcen in MS Excel-Arbeitsmappe beim Rendern in PDF](/cells/de/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Konvertieren Sie XLSX-Datei in PDF-Format](/cells/de/net/convert-xlsx-file-to-pdf-format/)
- [Excel-Datei in das PDF-Format konvertieren, das mit PDFA-1a kompatibel ist](/cells/de/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie XLS-Datei mit Bildern oder Diagrammen in PDF](/cells/de/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie PdfBookmarkEntry für Diagrammblatt](/cells/de/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattsäulen auf eine einzige PDF-Seite an](/cells/de/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Holen Sie sich DrawObject und Bound beim Rendern in PDF mit der DrawObjectEventHandler-Klasse](/cells/de/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Holen Sie sich Warnungen für Schriftartenersatz beim Rendern von Excel-Dateien](/cells/de/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorieren Sie Fehler beim Rendern von Excel in PDF](/cells/de/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten - Excel zu PDF-Konvertierung](/cells/de/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare drucken beim Speichern als PDF](/cells/de/net/print-comments-while-saving-to-pdf/)
- [Office-Add-Ins beim Konvertieren von Excel in PDF anzeigen](/cells/de/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Eine PDF-Seite pro Excel-Arbeitsblatt rendern - Excel in PDF konvertieren](/cells/de/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern von Unicode-Zusatzzeichen im Ausgabe-PDF durch Aspose.Cells](/cells/de/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Neu abgetastete Bilder - Excel zu PDF-Konvertierung](/cells/de/net/resampling-added-images-excel-to-pdf-conversion/)
- [Jedes Arbeitsblatt in eine separate PDF-Datei speichern](/cells/de/net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel als PDF mit Standard- oder Minimalgröße speichern](/cells/de/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Bestimmte Arbeitsblätter als PDF speichern](/cells/de/net/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/net/secure-pdf-documents/)
- [Angeben, wie Zeilenumbruch im Ausgabe-PDF und Bild erfolgen soll](/cells/de/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
