---
title: Konvertieren von Arbeitsmappen in verschiedene Formate
type: docs
weight: 20
url: /de/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch gesehen bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in einem anderen zu speichern.

{{% /alert %}}

## **Konvertieren von Excel in XPS**

Das XPS-Dokumentformat besteht aus strukturiertem XML-Markup, das das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite definiert, zusammen mit Wiedergaberegeln für das Verteilen, Archivieren, Wiedergeben, Verarbeiten und Drucken von Dokumenten.

Die Auszeichnungssprache für XPS ist eine Teilmenge von XAML, die es ermöglicht, Vektorgrafikelemente in Dokumente einzufügen, wobei XAML verwendet wird, um die Windows Presentation Foundation (WPF)-Grundelemente zu markieren. Die verwendeten Elemente werden in Form von Pfaden und anderen geometrischen Grundelementen beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Dazu gehören eine XML-Markup-Datei für jede Seite, Text, eingebettete Schriftarten, Rasterbilder, 2D-Vektorgrafiken sowie die Informationen zur digitalen Rechteverwaltung. Der Inhalt einer XPS-Datei kann einfach untersucht werden, indem Sie sie in einer Anwendung öffnen, die ZIP-Dateien unterstützt.

Ab Aspose.Cells 6.0.0 wird Microsoft Excel tp XPS-Konvertierung unterstützt.

### **Konvertieren eines einzelnen Arbeitsblatts in XPS**

Das folgende Beispiel zeigt, wie Sie ein einzelnes Arbeitsblatt in einer Excel-Datei in XPS konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **Ganze Arbeitsmappe nach XPS exportieren**

Das folgende Beispiel zeigt, wie die gesamte Arbeitsmappe in das XPS-Format konvertiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Schnelle Konvertierung von Excel in XPS**

Das folgende Beispiel zeigt eine einfache Möglichkeit, die Excel-Datei direkt in das XPS-Format zu konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Konvertieren von Excel in MHTML-Dateien**

[MHTML](https://en.wikipedia.org/wiki/MHTML) kombiniert normales HTML mit externen Ressourcen; Das heißt, Inhalte, die normalerweise wie Bilder, Animationen, Audio usw. in einer Datei verknüpft sind. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

{{% /alert %}}

Das Konvertieren einer Tabellenkalkulation in MHTML ist ein schneller Vorgang, wie unten gezeigt.

Das folgende Codebeispiel zeigt, wie eine Arbeitsmappe als MHTML-Datei gespeichert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Konvertieren von Excel-Dateien in HTML**

 Die Aspose.Cells-APIs bieten Unterstützung für den Export von Tabellenkalkulationen in das HTML-Format. Dazu nutzt die Aspose.Cells die**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**-Klasse, mit der Entwickler mehrere Aspekte des Ausgabe-HTML steuern können.

Der folgende Code zeigt, wie man die verwendet**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**Klasse zum Exportieren von Microsoft Excel-Dateien in das HTML-Format, ohne zusätzliche Parameter anzugeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

 Sie können die gleichen Ergebnisse erzielen, wenn Sie die bestehen**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** zum**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** Methode.

{{% /alert %}}

### **Festlegen von Bildeinstellungen für HTML**

 Ab 8.0.2 hat Aspose.Cells ausgesetzt**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**für die**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**-Klasse, mit der Entwickler beim Speichern von Tabellenkalkulationen im HTML-Format Bildeinstellungen festlegen können.

Folgende Bildeinstellungen können angewendet werden:

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: Ruft den Bildtyp ab oder legt ihn fest. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- **[Qualität](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: Ruft die Qualität von Bildern zwischen 0 und 100 ab oder legt sie fest, wenn ImageFormat als JPEG angegeben ist.
- **[VerticalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt sie fest.
- **[HorizontalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt sie fest.
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: Ruft den Komprimierungstyp für die Bilder ab oder legt ihn fest, wenn ImageFormat als Tiff angegeben ist.
- **[Transparent](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.

 Der folgende Code demonstriert die Verwendung**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** verschiedene Vorlieben angeben.

|**Tabellenansicht vor dem Export**|**HTML-Ansicht nach dem Export**|
|:- |:- |
|![Tabellenansicht vor dem Export](converting-workbook-to-different-formats_1.png)|![HTML-Ansicht nach dem Export](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Konvertieren von Excel in PDF-Dateien**

PDF-Dokumente werden häufig als Standardformat für den Austausch von Dokumenten zwischen Organisationen, Regierungssektoren und Einzelpersonen verwendet. Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien einfach in PDF-Dokumente umzuwandeln. Aspose.Cells unterstützt diese Funktionen. Dieser Artikel zeigt, wie.

### **Konvertieren von Excel in PDF**

 Microsoft Excel-zu-PDF-Konvertierung wurde mit Aspose.Cells for Java 2.3.0 eingeführt. Ab dieser Version kann Aspose.Cells[Konvertieren Sie Tabellenkalkulationen direkt in PDF](#direct-conversion) (einschließlich[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), ohne ein anderes Produkt. Um Tabellenkalkulationen mit älteren Versionen von Aspose.Cells zu konvertieren,[Verwenden Sie Aspose.PDF für die Konvertierung](#conversion-with-asposepdf-asposecells-prior-to-230).

 Aspose.Cell konvertiert Tabellenkalkulationen mit einem hohen Grad an Genauigkeit und Wiedergabetreue in PDF. Es gibt jedoch einige[Einschränkungen](/cells/de/java/converting-workbook-to-different-formats/#conversion-attributes), aufgeführt am Ende dieses Artikels.

{{% alert color="primary" %}}

 Aspose.Cells for Java schreibt die Informationen über API und die Versionsnummer direkt in Ausgabedokumente. Beim Rendern von Document in PDF wird beispielsweise Aspose.Cells for Java ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF-Produzent** Feld mit einem Wert, zB 'Aspose.Cells for Java v17.9'.

Bitte beachten Sie, dass Sie Aspose.Cells for Java nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

#### **Direkte Konvertierung**

Speichern Sie eine Excel-Datei mithilfe von direkt als PDF**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** Methode und bieten die**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**Schnittstellenmitglied. Eine direkte Konvertierung wie diese ist die effizienteste Konvertierungsmethode. Es gehen keine Daten oder Formatierungen verloren, aber die Ausgabe-PDF sieht weiterhin wie die Excel-Eingabedatei aus.

 Verwenden Sie zum Festlegen von Sicherheitsoptionen beim Speichern im PDF-Format**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **Erweiterte Konvertierung**

Sie können sich auch für die Verwendung entscheiden**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** -Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften von**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**Klasse gibt Ihnen die Kontrolle über die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die resultierende PDF-Datei. Die bemerkenswerteste Eigenschaft ist die**[Konformität](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**mit dem Sie die Excel-Dateien in PDF/A-kompatible PDF-Dateien speichern können.

##### **Speichern von Excel-Tabellen in PDF/A-kompilierte Dateien**

Das unten bereitgestellte Code-Snippet demonstriert die Verwendung von**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** Klasse zum Speichern der Excel-Dateien im PDF/A-kompatiblen PDF-Format.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Konvertierung mit Aspose.Pdf: Aspose.Cells Vor 2.3.0**

 Für Aspose.Cells-Versionen vor Version 2.3.0 müssen Sie eine Komponente wie verwenden[Aspose.PDF for Java](/pdf/java/) um Tabellenkalkulationen in PDF-Dateien umzuwandeln. Aspose.Cells und Aspose.PDF arbeiten zusammen, um eine Tabelle über einen Zwischenschritt in PDF umzuwandeln.

So konvertieren Sie Tabellen mit Aspose.Cells und Aspose.PDF in PDF:

1.  Instanziieren Sie ein Objekt der**[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**Klasse, indem Sie ihren leeren Konstruktor aufrufen.
1. Erledigen Sie Ihre gewünschte Arbeit an der Tabelle mit Aspose.Cells API.
1. Ruf den**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**Methode zum Speichern der Tabelle:
1. Stellen Sie das Dateiformat auf XML ein.
 1. Wählen Sie Aspose_Pdf (ein vordefinierter Wert) aus der FileFormatType-Schnittstelle aus. Dies weist die save-Methode an, eine Kalkulationstabelle in XML-Form zu generieren, die mit dem Aspose.PDF-Schema kompatibel ist, sodass Aspose.PDF for Java dann ein PDF-Dokument generieren kann.
1. Wenn die XML-Datei erstellt wurde, erstellen Sie ein Objekt der Klasse Pdf im Paket aspose.pdf.
1. Rufen Sie die bindXML-Methode der Pdf-Klasse auf und übergeben Sie den Namen der XML-Ausgabedatei.
1. Rufen Sie die save-Methode der Pdf-Klasse auf, um das PDF-Dokument zu generieren.

Die obigen Schritte werden nachfolgend beispielhaft umgesetzt.

{{% alert color="primary" %}}

 Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** -Methode unmittelbar vor dem Rendern der Tabelle in das PDF-Format. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}

#### **Konvertierungsattribute**

Wir arbeiten hart daran, die Konvertierung und andere Aspekte von Aspose.Cells mit jeder Veröffentlichung zu verbessern. Die Konvertierung von Excel in PDF hat einige Einschränkungen. Einige in einer Tabelle angegebene Formateinstellungen gehen möglicherweise verloren, und nicht alle Zeichnungsobjekte werden unterstützt.

Die folgende Tabelle listet alle Funktionen auf, die beim Exportieren in PDF mit Aspose.Cells vollständig oder teilweise unterstützt werden. Diese Tabelle ist nicht endgültig und deckt nicht alle Tabellenattribute ab. Es kann auch diejenigen Funktionen identifizieren, die möglicherweise nicht oder teilweise für die Konvertierung unterstützt werden.

{{% alert color="primary" %}}

|**Dokumentelement**|**Attribut**|**Netz unterstützt**|**Anmerkungen**|
|:- |:- |:- |:- |
|Ausrichtung||Ja||
|Drehung||Teilweise|Unterstützt nur 90 und -90.|
|Hintergrundeinstellungen||Ja||
|Grenze|Farbe|Ja||
|Grenze|Linienstil|Ja||
|Grenze|Linienbreite|Ja||
|Cell Daten||Ja||
|Kommentare||Nein||
|Bedingte Formatierung||Ja||
|Dokumenteigenschaften||Ja||
|Objekte zeichnen||Ja||
|Schriftart|Größe|Ja||
|Schriftart|Farbe|Ja||
|Schriftart|Stil|Ja||
|Schriftart|Unterstreichen|Ja||
|Schriftart|Auswirkungen|Teilweise|Nur der Durchstreicheffekt wird unterstützt|
|Bilder||Ja||
|Hyperlinks||Ja||
|Diagramme||Ja||
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
{{% /alert %}}
