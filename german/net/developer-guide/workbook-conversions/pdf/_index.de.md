---
title: Pdf
type: docs
weight: 220
url: /de/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer Excel-Arbeitsmappe in PDF. In diesem Beispiel sehen wir die vollständige Konvertierung einer Excel-Arbeitsmappe in PDF.

{{% /alert %}}

##  **Konvertieren einer Excel-Arbeitsmappe in PDF**

PDF-Dateien werden häufig zum Austausch von Dokumenten zwischen Organisationen, Behörden und Einzelpersonen verwendet. Es handelt sich um ein Standarddokumentformat und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft-Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und sorgt für eine hohe visuelle Wiedergabetreue bei der Konvertierung.

{{% alert color="primary" %}}

 Aspose.Cells for .NET schreibt die Informationen zu API und der Versionsnummer direkt in Ausgabedokumente. Wenn beispielsweise das Dokument in PDF gerendert wird, wird Aspose.Cells for .NET ausgefüllt**PDF Produzent** Feld mit Wert, z. B. „Aspose.Cells v23.2“.

 Bitte beachten Sie, dass Sie diese Informationen in den Ausgabedokumenten ändern können**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** Eigentum.

{{% /alert %}}

###  **Direkte Konvertierung**

 Aspose.Cells for .NET unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei unter PDF mit**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse'**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode. Der**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode bietet die**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Aufzählungsmitglied, das die nativen Excel-Dateien in das Format PDF konvertiert.

Führen Sie die folgenden Schritte aus, um die Excel-Tabellen direkt in das Format PDF zu konvertieren:

1.  Instanziieren Sie ein Objekt von**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse durch Aufrufen ihres leeren Konstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwenden von Formatierungen, Festlegen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) in der Tabelle mithilfe der APIs von Aspose.Cells aus.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie auf**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse'**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode zum Speichern der Tabelle.

 Das Dateiformat sollte PDF sein, also wählen Sie es aus*Pdf* (ein vordefinierter Wert) aus dem**[Speicherformat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Aufzählung, um das endgültige Dokument PDF zu generieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **Erweiterte Konvertierung**

 Sie können sich auch für die Verwendung entscheiden**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften des**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Mit der Klasse können Sie die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe PDF steuern. Die wichtigste Eigenschaft ist**[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Dadurch können Sie die Excel-Dateien in PDF/A-kompatiblen PDF-Dateien speichern.

####  **Speichern der Arbeitsmappe in PDF/A-kompatiblen Dateien**

 Das unten bereitgestellte Code-Snippet zeigt die Verwendung von**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Klasse zum Speichern von Excel-Dateien im PDF/A-kompatiblen PDF-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Bitte beachten Sie, dass**[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Die Eigenschaft wurde mit der Veröffentlichung von Aspose.Cells for .NET 5.3.0 hinzugefügt.

{{% /alert %}}

####  **Legen Sie die Erstellungszeit PDF fest**

 Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Klasse können Sie die Erstellungszeit PDF abrufen oder festlegen. Der folgende Code demonstriert die Verwendung von**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** Eigenschaft, um den Erstellungszeitpunkt der Datei PDF festzulegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **Legen Sie die Option „ContentCopyForAccessibility“ fest**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Klasse können Sie die PDF erhalten oder festlegen**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** Option zur Steuerung des Inhaltszugriffs in der konvertierten PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **Benutzerdefinierte Eigenschaften nach PDF exportieren**

Mit dem**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Klasse können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe nach PDF exportieren.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**Es wird ein Enumerator bereitgestellt, um anzugeben, wie Eigenschaften exportiert werden. Diese Eigenschaften können in Adobe Acrobat Reader angezeigt werden, indem Sie auf „Datei“ und dann auf die Option „Eigenschaften“ klicken, wie in der folgenden Abbildung dargestellt. Die Vorlagendatei „sourceWithCustProps.xlsx“ kann heruntergeladen werden[Hier](sourceWithCustProps.xlsx) Zum Testen und Ausgeben steht die Datei „outSourceWithCustProps“ PDF zur Verfügung[Hier](outSourceWithCustProps.pdf) zur Analyse.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **Konvertierungsattribute**

Wir arbeiten daran, die Konvertierungsfunktionen mit jeder neuen Version zu verbessern. Die Konvertierung von Aspose.Cell von Excel in PDF weist noch einige Einschränkungen auf. MapChart wird bei der Konvertierung in das Format PDF nicht unterstützt. Außerdem werden einige Zeichenobjekte nicht gut unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Export nach PDF unter Verwendung von Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabellenattribute ab, identifiziert jedoch die Funktionen, die für die Konvertierung in PDF nicht oder teilweise unterstützt werden .

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

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}

##  **Vorabthemen**
- [Fügen Sie PDF Lesezeichen hinzu](/cells/de/net/add-pdf-bookmarks/)
- [Fügen Sie PDF-Lesezeichen mit benannten Zielen hinzu](/cells/de/net/add-pdf-bookmarks-with-named-destinations/)
- [Vermeiden Sie leere Seiten in der Ausgabe PDF, wenn nichts zum Drucken vorhanden ist](/cells/de/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändern Sie die Schriftart beim Speichern nur für die spezifischen Unicode-Zeichen in PDF](/cells/de/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Steuern Sie das Laden externer Ressourcen in der MS Excel-Arbeitsmappe beim Rendern in PDF](/cells/de/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Konvertieren Sie die Datei XLSX in das Format PDF](/cells/de/net/convert-xlsx-file-to-pdf-format/)
- [Konvertieren Sie eine Excel-Datei in das mit PDFA-1a kompatible Format PDF](/cells/de/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertieren Sie die Datei XLS mit Bildern oder Diagrammen in PDF](/cells/de/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Erstellen Sie einen PDFBookmarkEntry für das Diagrammblatt](/cells/de/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Passen Sie alle Arbeitsblattspalten auf eine einzelne Seite PDF an](/cells/de/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Rufen Sie DrawObject und Bound ab, während Sie mit der DrawObjectEventHandler-Klasse auf PDF rendern](/cells/de/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Erhalten Sie Warnungen zur Schriftartersetzung beim Rendern einer Excel-Datei](/cells/de/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorieren Sie Fehler beim Rendern von Excel auf PDF](/cells/de/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Begrenzen Sie die Anzahl der generierten Seiten – Excel auf PDF Konvertierung](/cells/de/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Kommentare beim Speichern unter PDF ausdrucken](/cells/de/net/print-comments-while-saving-to-pdf/)
- [Rendern Sie Office-Add-Ins, während Sie Excel in PDF konvertieren](/cells/de/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt – Konvertierung von Excel in PDF](/cells/de/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendern Sie Unicode-Ergänzungszeichen in der Ausgabe PDF durch Aspose.Cells](/cells/de/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resampling hinzugefügter Bilder – Konvertierung von Excel in PDF](/cells/de/net/resampling-added-images-excel-to-pdf-conversion/)
- [Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei](/cells/de/net/save-each-worksheet-to-a-different-pdf-file/)
- [Speichern Sie Excel unter PDF mit Standard- oder Mindestgröße](/cells/de/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Speichern Sie die angegebenen Arbeitsblätter unter PDF](/cells/de/net/save-specified-worksheets-to-pdf/)
- [Sichere PDF-Dokumente](/cells/de/net/secure-pdf-documents/)
- [Geben Sie an, wie die Zeichenfolge in Ausgabe PDF und Bild gekreuzt werden soll](/cells/de/net/specify-how-to-cross-string-in-output-pdf-and-image/)
