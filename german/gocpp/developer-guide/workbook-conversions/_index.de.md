---
title: Konvertieren Sie Excel in PDF, Bild und andere Formate mit Golang über C++
linktitle: Arbeitsmappen Konvertierungen
type: docs
weight: 65
url: /de/go-cpp/convert-workbook-to-different-formats/
description: Konvertieren Sie Excel Dateien in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML und mehr mit Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.

{{% /alert %}}

## **Excel-Arbeitsmappe in PDF konvertieren**

PDF-Dateien werden häufig verwendet, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es ist ein standardisiertes Dokumentformat und Softwareentwickler werden oft gefragt, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente umzuwandeln.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Excel-Arbeitsmappe in JPG konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in JPG.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als JPG speichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Excel-Arbeitsmappe in Bild konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Bilder.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als Bilder speichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Excel-Arbeitsmappe in XPS konvertieren**

Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, Darstellung, Verarbeitung und zum Drucken von Dokumenten definiert.

Das Markup-Sprachenformat für XPS ist ein Teilmenge von XAML, was es ermöglicht, Vektorgrafikelemente in Dokumenten zu integrieren, indem XAML verwendet wird, um die Windows Presentation Foundation (WPF) Primitive zu kennzeichnen. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitive beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Diese umfassen eine XML-Markup-Datei für jede Seite, Text, eingebettete Schriftarten, Rasterbilder, 2D-Vektorgrafiken sowie Digital Rights Management-Informationen. Der Inhalt einer XPS-Datei kann einfach durch Öffnen in einer Anwendung geprüft werden, die ZIP-Dateien unterstützt.

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel in XPS unterstützt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Excel in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Ods, Sxc und Fods Dateien. Das unten stehende Codebeispiel zeigt, wie die [Vorlage](book1.xlsx) in Ods, Sxc und Fods Dateien konvertiert wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**

MHTML kombiniert normales HTML mit externen Ressourcen (das heißt, Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Excel-Arbeitsmappe in HTML konvertieren**

Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

Das folgende Beispiel zeigt, wie man eine Arbeitsmappe als HTML-Datei speichert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Bildvoreinstellungen für HTML einstellen**

Ab Version 8.0.2 hat Aspose.Cells die [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) für die [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) Klasse öffentlich gemacht, um Entwicklern die Angabe von Bildeinstellungen beim Speichern von Tabellen in HTML-Format zu ermöglichen.

Im Folgenden sind einige Bild-Einstellungen aufgeführt, die angewendet werden können:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): Gibt den Bildtyp an. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): Gibt die Qualität des Bildes zwischen 0 und 100 an, wenn [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) als Jpeg angegeben ist.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): Holt oder setzt den Komprimierungstyp für die Bilder, wenn [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) als Tiff angegeben ist.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.

Der unten stehende Code demonstriert, wie man [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) verwendet, um verschiedene Präferenzen festzulegen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Excel-Arbeitsmappe in Markdown konvertieren**

Das Aspose.Cells API unterstützt den Export von Tabellen in das Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, übergeben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach Markdown festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration-Mitglied in Markdown exportiert werden kann. Bitte beachten Sie die [Ausgabedatei im Markdown-Format](md_sample.txt), die durch den Code erzeugt wurde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Excel-Arbeitsmappe in JSON konvertieren**

Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt in JSON mit [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration-Mitglied exportiert werden kann. Bitte sehen Sie den Code, um die [Quelle-Datei](Book1.xlsx) in die [Ausgabe-JSON-Datei](Book1.Json) zu konvertieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Excel in XML umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in das Excel 2003 Spreadsheet XML- und das Plain-XML-Format.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Excel-Arbeitsmappe in TIFF umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine TIFF-Datei.

Der unten stehende Codeausschnitt zeigt, wie Excel in TIFF umgewandelt wird:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Excel-Arbeitsmappe in DOCX umwandeln**

Das Aspose.Cells API bietet Unterstützung für die Konvertierung von Tabellen in das DOCX-Format. Um die Arbeitsmappe in DOCX zu exportieren, übergeben Sie [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach DOCX festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration-Mitglied in DOCX exportiert werden kann. Bitte beachten Sie die [Ausgabedatei im DOCX-Format](Book1.docx), die vom Code erzeugt wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Excel-Arbeitsmappe in PPTX umwandeln**

Das Aspose.Cells API unterstützt die Konvertierung von Tabellen in das PPTX-Format. Um die Arbeitsmappe in PPTX zu exportieren, übergeben Sie [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) Methode. Sie können auch die [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach PPTX festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration Mitglied in PPTX exportiert wird. Bitte sehen Sie sich die [Ausgabedatei PPTX](Book1.pptx) an, die vom Code generiert wurde, zur Referenz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Excel-Arbeitsmappe in EPUB konvertieren**

Die Aspose.Cells API unterstützt die Konvertierung von Tabellen in das EPUB-Format. Um die Arbeitsmappe in EPUB zu exportieren, übergeben Sie [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweites Parameter an die [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export der Tabelle in EPUB festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration Mitglied in EPUB exportiert wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Excel-Arbeitsmappe nach AZW3 konvertieren**

Die Aspose.Cells API unterstützt die Konvertierung von Tabellen in das AZW3-Format. Um die Arbeitsmappe in AZW3 zu exportieren, übergeben Sie [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweites Parameter an die [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export der Tabelle in AZW3 festzulegen.

Das folgende Codebeispiel zeigt, wie die aktive Tabelle mit [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) Enumeration Mitglied in AZW3 exportiert wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Erweiterte Themen**
- [Konvertieren der Überarbeitung von XLSB zu XLSM](/cells/de/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/de/cpp/convert-excel-to-html/)
- [Bild](/cells/de/cpp/convert-excel-to-image/)
- [Json](/cells/de/cpp/convert-workbook-to-json/)
- [Excel-Arbeitsmappe in Ods, Sxc und Fods (OpenOffice / LibreOffice calc) konvertieren.](/cells/de/cpp/convert-excel-to-ods/)
- [Pdf](/cells/de/cpp/convert-excel-workbook-to-pdf/)
- [Excel in CSV, TSV und Txt konvertieren](/cells/de/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/cpp/track-document-conversion-progress/)
- [CSV, TSV und TXT in Excel konvertieren](/cells/de/cpp/convert-csv-tsv-and-txt-to-excel/)
