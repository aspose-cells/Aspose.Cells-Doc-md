---
title: Pdf
type: docs
weight: 220
url: /de/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer Excel-Arbeitsmappe in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

## **Konvertieren der Excel-Arbeitsmappe in PDF**

PDF-Dateien werden häufig zum Austausch von Dokumenten zwischen Organisationen, Regierungssektoren und Einzelpersonen verwendet. Es ist ein Standarddokumentformat und Softwareentwickler werden oft gebeten, einen Weg zu finden, Microsoft-Excel-Dateien in PDF-Dokumente umzuwandeln.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und behält eine hohe visuelle Wiedergabetreue bei der Konvertierung bei.

{{% alert color="primary" %}}

 Aspose.Cells for .NET schreibt die Informationen über API und die Versionsnummer direkt in Ausgabedokumente. Beispielsweise wird beim Rendern von Dokument an PDF Aspose.Cells for .NET ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF Hersteller**Feld mit Wert, zB 'Aspose.Cells v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for .NET nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Direkte Konvertierung**

 Aspose.Cells for .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei unter PDF mit der**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Klasse'**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode. Das**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode bietet die**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Enumerationsmember, der die nativen Excel-Dateien in das PDF-Format konvertiert.

Führen Sie die folgenden Schritte aus, um die Excel-Tabellen direkt in das Format PDF zu konvertieren:

1.  Instanziieren Sie ein Objekt der**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse, indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf neu erstellen.
1. Führen Sie alle Arbeiten (Daten eingeben, Formatierung anwenden, Formeln festlegen, Bilder oder andere Zeichnungsobjekte einfügen usw.) in der Tabelle mithilfe von Aspose.Cells-APIs durch.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie die auf**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Klasse'**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode zum Speichern der Tabelle.

 Das Dateiformat sollte PDF sein, also wählen Sie es aus*Pdf* (ein vordefinierter Wert) aus der**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Enumeration, um das endgültige PDF-Dokument zu generieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Erweiterte Konvertierung**

 Sie können sich auch für die Verwendung entscheiden**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** -Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften der**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** -Klasse gibt Ihnen die Kontrolle über die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe PDF. Die wichtigste Eigenschaft ist**[Konformität](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Dadurch können Sie die Excel-Dateien in PDF/A-kompatible PDF-Dateien speichern.

#### **Speichern der Arbeitsmappe in PDF/A Kompilierte Dateien**

 Das unten bereitgestellte Code-Snippet zeigt, wie Sie die verwenden**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Klasse zum Speichern von Excel-Dateien im PDF/A-kompatiblen PDF-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Bitte beachten Sie, die**[Konformität](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Eigenschaft wurde mit der Veröffentlichung von Aspose.Cells for .NET 5.3.0 hinzugefügt.

{{% /alert %}}

#### **Stellen Sie die Erstellungszeit PDF ein**

 Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Klasse können Sie die Erstellungszeit PDF erhalten oder festlegen. Der folgende Code demonstriert die Verwendung von**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** -Eigenschaft, um die Erstellungszeit der Datei PDF festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Legen Sie die ContentCopyForAccessibility-Option fest**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Klasse, können Sie die PDF erhalten oder einstellen**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** Option zur Steuerung des Inhaltszugriffs in der konvertierten PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Exportieren Sie benutzerdefinierte Eigenschaften nach PDF**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Klasse können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in die Datei PDF exportieren.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**Enumerator wird bereitgestellt, um anzugeben, wie Eigenschaften exportiert werden. Diese Eigenschaften können in Adobe Acrobat Reader angezeigt werden, indem Sie auf Datei und dann auf die Option Eigenschaften klicken, wie in der folgenden Abbildung gezeigt. Die Vorlagendatei „sourceWithCustProps.xlsx“ kann heruntergeladen werden[Hier](sourceWithCustProps.xlsx) zum Testen und Ausgeben steht die PDF-Datei "outSourceWithCustProps" zur Verfügung[Hier](outSourceWithCustProps.pdf) zur Analyse.

![todo: Bild_alt_Text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Konvertierungsattribute**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Konvertierung von Aspose.Cell von Excel in PDF weist noch einige Einschränkungen auf. Beim Konvertieren in das PDF-Format gehen möglicherweise einige Tabellenformatierungen verloren. Außerdem werden einige Zeichnungsobjekte noch nicht unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Exportieren nach PDF mit Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabellenattribute ab, identifiziert jedoch die Funktionen, die für die Konvertierung nach PDF nicht oder teilweise unterstützt werden .

|**Dokumentelement**|**Attribut**|**Unterstützt**|**Anmerkungen**|
|:- |:- |:- |:- |
|Ausrichtung||Ja||
|Hintergrundeinstellungen||Ja||
|Grenze|Farbe|Ja||
|Grenze|Linienstil|Ja||
|Grenze|Linienbreite|Ja||
|Cell Daten||Ja||
|Bemerkungen||Ja||
|Bedingte Formatierung||Ja||
|Dokumenteigenschaften||Ja||
|Objekte zeichnen||Teilweise|Unterstützte Objekte: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Schriftart|Größe|Ja||
|Schriftart|Farbe|Ja||
|Schriftart|Stil|Ja||
|Schriftart|Unterstreichen|Ja||
|Schriftart|Auswirkungen|Teilweise|Es wird nur der Durchstreicheffekt unterstützt|
|Bilder||Ja||
|Hyperlinks||Ja||
|Diagramme||Teilweise||
|Zusammengeführt Cells||Ja||
|Seitenumbruch||Ja||
|Seiteneinrichtung|Kopfzeile Fußzeile|Ja||
|Seiteneinrichtung|Ränder|Ja||
|Seiteneinrichtung|Seitenausrichtung|Ja||
|Seiteneinrichtung|Seitengröße|Ja||
|Seiteneinrichtung|Druckbereich|Ja||
|Seiteneinrichtung|Titel drucken|Ja||
|Seiteneinrichtung|Skalierung|Ja||
|Zeilenhöhe/Spaltenbreite||Ja||
|RTL-Sprache (von rechts nach links).||Ja||

{{% alert color="primary" %}}

Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte in PDF wiedergegeben werden.

{{% /alert %}}

## **Themen vorantreiben**
- [PDF Lesezeichen hinzufügen](/cells/de/net/add-pdf-bookmarks/)
- [Fügen Sie PDF Lesezeichen mit benannten Zielen hinzu](/cells/de/net/add-pdf-bookmarks-with-named-destinations/)
- [Vermeiden Sie eine leere Seite in der Ausgabe PDF, wenn nichts zu drucken ist](/cells/de/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändern Sie die Schriftart nur für die spezifischen Unicode-Zeichen, während Sie auf PDF speichern](/cells/de/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Steuern Sie das Laden externer Ressourcen in der MS Excel-Arbeitsmappe, während Sie auf PDF rendern](/cells/de/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Konvertieren Sie eine XLS-Datei in das PDF-Format](/cells/de/net/convert-an-xls-file-to-pdf-format/)
- [Konvertieren Sie die Excel-Datei in das mit PDFA-1a kompatible PDF-Format](/cells/de/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie XLS-Datei mit Bildern oder Diagrammen in PDF](/cells/de/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [PdfBookmarkEntry für Diagrammblatt erstellen](/cells/de/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Alle Arbeitsblattspalten auf einer Seite PDF einpassen](/cells/de/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Holen Sie sich DrawObject und Bound beim Rendern auf PDF mithilfe der DrawObjectEventHandler-Klasse](/cells/de/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Erhalten Sie Warnungen für die Schriftartersetzung beim Rendern von Excel-Dateien](/cells/de/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Fehler beim Rendern von Excel auf PDF ignorieren](/cells/de/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Beschränken Sie die Anzahl der generierten Seiten – Excel auf PDF Konvertierung](/cells/de/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare beim Speichern unter PDF drucken](/cells/de/net/print-comments-while-saving-to-pdf/)
- [Rendern Sie Office-Add-Ins, während Sie Excel in PDF konvertieren](/cells/de/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt - Konvertierung von Excel in PDF](/cells/de/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendert Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells](/cells/de/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling hinzugefügter Bilder – Konvertierung von Excel in PDF](/cells/de/net/resampling-added-images-excel-to-pdf-conversion/)
- [Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei](/cells/de/net/save-each-worksheet-to-a-different-pdf-file/)
- [Speichern Sie Excel in PDF mit Standard- oder Mindestgröße](/cells/de/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [PDF Dokumente sichern](/cells/de/net/secure-pdf-documents/)
- [Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll](/cells/de/net/specify-how-to-cross-string-in-output-pdf-and-image/)
