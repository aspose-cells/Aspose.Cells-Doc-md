---
title: Konvertierung der Arbeitsmappe in verschiedene Formate
type: docs
weight: 20
url: /de/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch gesehen bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.

{{% /alert %}}

## **Excel in XPS umwandeln**

Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, zum Rendering, zur Verarbeitung und zum Drucken von Dokumenten definiert.

Die Auszeichnungssprache für XPS ist ein Teilmenge von XAML, die es ermöglicht, Vektorgrafikelemente in Dokumente zu integrieren, wobei XAML zur Markierung der Windows Presentation Foundation (WPF)-Primitive verwendet wird. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitive beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicoded-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, die das Dokument ausmachen. Dazu gehören eine XML-Auszeichnungsdatei für jede Seite, Text, eingebettete Schriftarten, Rasterbilder, 2D-Vektorgrafiken sowie die digitalen Rechtemanagement-Informationen. Der Inhalt einer XPS-Datei kann ganz einfach durch Öffnen in einer Anwendung, die ZIP-Dateien unterstützt, untersucht werden.

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel zu XPS unterstützt.

### **Konvertierung einzelner Arbeitsblätter in XPS**

Das folgende Beispiel zeigt, wie ein einzelnes Arbeitsblatt in einer Excel-Datei in XPS konvertiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Gesamtes Arbeitsblatt in XPS exportieren**

Das folgende Beispiel zeigt, wie das gesamte Arbeitsblatt in das XPS-Format konvertiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Schnelle Excel zu XPS Konvertierung**

Das folgende Beispiel zeigt einen einfachen Weg, um die Excel-Datei direkt in das XPS-Format zu konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Konvertierung von Excel in MHTML-Dateien**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML) kombiniert normales HTML mit externen Ressourcen; das heißt, Inhalte, die normalerweise wie Bilder, Animationen, Audio usw. verlinkt sind, in eine Datei ein. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

{{% /alert %}}

Die Umwandlung eines Tabellenkalkulationsblatts in MHTML ist wie unten gezeigt schnell und einfach.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Excel-Dateien in HTML konvertieren**

Die Aspose.Cells-APIs unterstützen den Export von Tabellenkalkulationen im HTML-Format. Zu diesem Zweck verwendet Aspose.Cells die Klasse [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions), mit der Entwickler mehrere Aspekte der Ausgabe-HTML steuern können.

Der folgende Code zeigt, wie die Klasse [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) verwendet wird, um Microsoft Excel-Dateien im HTML-Format ohne zusätzliche Parameter zu exportieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

Die gleichen Ergebnisse können erzielt werden, indem [**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML) an die Methode [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) übergeben wird.

{{% /alert %}}

### **Einstellen von Bildpräferenzen für HTML**

Ab Version 8.0.2 hat Aspose.Cells [**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) für die Klasse [**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions) freigelegt, wodurch Entwickler Bildpräferenzen beim Speichern von Tabellenkalkulationen im HTML-Format festlegen können.

Die anwendbaren Bildeinstellungen sind:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): Ruft den Bildtyp ab oder legt ihn fest. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): Ruft die Qualität der Bilder zwischen 0 und 100 ab oder legt sie fest, wenn ImageFormat als Jpeg festgelegt ist.
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt sie fest.
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt sie fest.
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): Ruft den Kompressionstyp für die Bilder ab oder legt ihn fest, wenn ImageFormat als Tiff festgelegt ist.
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png festgelegt ist.

Der unten stehende Code demonstriert, wie man [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions) verwendet, um verschiedene Präferenzen festzulegen.

|**Tabellenansicht vor dem Export**|**HTML-Ansicht nach dem Export**|
| :- | :- |
|![Tabellenansicht vor dem Export](converting-workbook-to-different-formats_1.png)|![HTML-Ansicht nach dem Export](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Umwandlung von Excel in PDF-Dateien**

PDF-Dokumente werden häufig als Standardformat zum Austausch von Dokumenten zwischen Organisationen, Regierungsstellen und Einzelpersonen verwendet. Softwareentwickler werden oft gebeten, eine Möglichkeit zu entwickeln, Microsoft Excel-Dateien einfach in PDF-Dokumente umzuwandeln. Aspose.Cells unterstützt diese Funktionen. In diesem Artikel wird gezeigt, wie.

### **Konvertierung von Excel nach PDF**

Die Umwandlung von Microsoft Excel in PDF wurde mit Aspose.Cells for Java 2.3.0 eingeführt. Ab diesem Release kann Aspose.Cells [Tabellenkalkulationen direkt in PDF umwandeln](#direct-conversion) (einschließlich [PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), ohne ein anderes Produkt. Um Tabellenkalkulationen mit älteren Versionen von Aspose.Cells umzuwandeln, [verwenden Sie Aspose.PDF für die Umwandlung](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cells konvertiert Tabellenkalkulationen mit hoher Genauigkeit und Treue in PDF. Es gibt jedoch einige [Einschränkungen](/cells/de/java/converting-workbook-to-different-formats/#conversion-attributes), die am Ende dieses Artikels aufgeführt sind.

{{% alert color="primary" %}}

Aspose.Cells for Java schreibt die Informationen über API und Versionsnummer direkt in Ausgabedokumente. Zum Beispiel füllt Aspose.Cells for Java beim Rendern des Dokuments in PDF das Feld **Anwendung** mit dem Wert 'Aspose.Cells' und das Feld **PDF-Produzent** mit einem Wert, z.B. 'Aspose.Cells for Java v17.9', aus.

Bitte beachten Sie, dass Sie Aspose.Cells for Java nicht anweisen können, diese Informationen aus den Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

#### **Direkte Konvertierung**

Speichern Sie eine Excel-Datei direkt als PDF mit der [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) Methode und geben Sie das [**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF) Schnittstellenmitglied an. Eine direkte Konvertierung wie diese ist die effizienteste Konvertierungsmethode. Sie verliert keine Daten oder Formate, sondern lässt das Ausgabepdf wie die Eingabe-Exceldatei aussehen.

Um Sicherheitsoptionen beim Speichern als PDF festzulegen, verwenden Sie [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Erweiterte Konvertierung**

Sie können auch die [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-Klasse verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Festlegen verschiedener Eigenschaften der [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-Klasse gibt Ihnen die Kontrolle über die Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die resultierende PDF-Datei. Die bemerkenswerteste Eigenschaft ist die [**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance), die es Ihnen ermöglicht, die Excel-Dateien als PDF/A-konforme PDF-Dateien zu speichern.

##### **Speichern von Excel-Tabellenkalkulationen als PDF/A-konforme Dateien**

Im folgenden bereitgestellten Codeausschnitt wird die Verwendung der [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-Klasse demonstriert, um die Excel-Dateien im PDF/A-konformen PDF-Format zu speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Umwandlung mit Aspose.Pdf: Aspose.Cells vor 2.3.0**

Für Aspose.Cells-Versionen vor Version 2.3.0 müssen Sie eine Komponente wie [Aspose.PDF für Java](/pdf/java/) verwenden, um Tabellenkalkulationen in PDF-Dateien umzuwandeln. Aspose.Cells und Aspose.PDF arbeiten zusammen, um eine Tabellenkalkulation über einen Zwischenschritt in PDF umzuwandeln.

Um Tabellenkalkulationen in PDF mit Aspose.Cells und Aspose.PDF umzuwandeln:

Instantiieren Sie ein Objekt der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), indem Sie ihren leeren Konstruktor aufrufen.
2. Führen Sie Ihre gewünschte Arbeit an der Tabellenkalkulation mit der Aspose.Cells API durch.
1. Rufen Sie die [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))-Methode auf, um die Tabelle zu speichern:
   4. Legen Sie das Dateiformat auf XML fest.
   5. Wählen Sie Aspose_Pdf (einen vordefinierten Wert) aus dem Interface-Mitglied FileFormatType. Dadurch wird die Save-Methode angewiesen, eine Tabellenkalkulation in der XML-Form zu generieren, die mit dem Aspose.PDF-Schema kompatibel ist, so dass Aspose.PDF für Java dann ein PDF-Dokument generieren kann.
1. Wenn die XML-Datei erstellt wurde, erstellen Sie ein Objekt der Klasse Pdf im Paket aspose.pdf.
1. Rufen Sie die Methode bindXML der Klasse Pdf auf und übergeben Sie den Namen der Ausgabedatei des XML.
1. Rufen Sie die Methode save der Klasse Pdf auf, um das PDF-Dokument zu generieren.

Die obigen Schritte werden unten in einem Beispiel implementiert.

{{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, die Methode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Dadurch werden die von der Formel abhängigen Werte neu berechnet, und die korrekten Werte werden im PDF gerendert.

{{% /alert %}}

#### **Konvertierungseigenschaften**

Wir arbeiten hart daran, die Konvertierung und andere Aspekte von Aspose.Cells mit jeder Veröffentlichung zu verbessern. Die Konvertierung von Excel nach PDF hat einige Einschränkungen. Einige im Tabellenblatt festgelegte Formatierungen können verloren gehen, und nicht alle Zeichenobjekte werden unterstützt.

Die Tabelle unten listet alle Funktionen auf, die beim Exportieren in PDF mit Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht abschließend und deckt nicht alle Tabellenkennzeichen ab. Sie kann auch Funktionen identifizieren, die möglicherweise nicht unterstützt werden oder nur teilweise für die Konvertierung unterstützt werden.

{{% alert color="primary" %}}

|**Dokumentenelement**|**Attribute**|**Vollständig unterstützt**|**Anmerkungen**|
| :- | :- | :- | :- |
|Ausrichtung| |Ja| |
|Drehung| |Teilweise|Unterstützt nur 90 und -90.|
|Hintergrund-Einstellungen| |Ja| |
|Rahmen|Farbe|Ja| |
|Rahmen|Linienart|Ja| |
|Rahmen|Linienbreite|Ja| |
|Zellendaten| |Ja| |
|Kommentare| |Nein| |
|Bedingte Formatierung| |Ja| |
|Dokumenteigenschaften| |Ja| |
|Zeichenobjekte| |Ja| |
|Schriftart|Größe|Ja| |
|Schriftart|Farbe|Ja| |
|Schriftart|Stil|Ja| |
|Schriftart|Unterstrichen|Ja| |
|Schriftart|Effekte|Teilweise|Nur der Durchstreicheffekt wird unterstützt|
|Bilder| |Ja| |
|Hyperlink| |Ja| |
|Diagramme| |Ja| |
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
{{% /alert %}}
