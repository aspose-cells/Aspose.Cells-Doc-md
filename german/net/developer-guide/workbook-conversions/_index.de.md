---
title: Excel in Pdf, Bild und andere Formate konvertieren
linktitle: Arbeitsmappen Konvertierungen
type: docs
weight: 65
url: /de/net/convert-workbook-to-different-formats/
description: Konvertieren Sie Excel Dateien in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML und mehr.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung zwischen vielen Formaten. Technisch gesehen bedeutet Konvertierung, eine Arbeitsmappe in einem Dateiformat zu laden und in ein anderes zu speichern.

{{% /alert %}}

## **Excel-Arbeitsmappe in PDF konvertieren**

PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Excel-Arbeitsmappe in JPG konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in JPG.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als JPG speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Excel-Arbeitsmappe in Bild konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Bilder.
Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als Bilder speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Excel-Arbeitsmappe in XPS konvertieren**

Das XPS-Dokumentenformat besteht aus strukturierter XML-Auszeichnung, die das Layout eines Dokuments und das visuelle Erscheinungsbild jeder Seite sowie Rendering-Regeln zur Verteilung, Archivierung, Darstellung, Verarbeitung und zum Drucken von Dokumenten definiert.

Die Auszeichnungssprache für XPS ist ein Subset von XAML, das es ermöglicht, Vektorgrafikelemente in Dokumente zu integrieren, indem XAML die Windows Presentation Foundation (WPF)-Primitive markiert. Die verwendeten Elemente werden in Bezug auf Pfade und andere geometrische Primitiven beschrieben.

Eine XPS-Datei ist tatsächlich ein Unicode-ZIP-Archiv, das die Open Packaging Conventions verwendet und die Dateien enthält, aus denen das Dokument besteht. Dazu gehören eine XML-Auszeichnungsdatei für jede Seite, Text, eingebettete Schriften, Rasterbilder, 2D-Vektorgrafiken sowie die Informationen zum Digital Rights Management. Der Inhalt einer XPS-Datei kann einfach untersucht werden, indem sie in einer Anwendung geöffnet wird, die ZIP-Dateien unterstützt.

Ab Aspose.Cells 6.0.0 wird die Konvertierung von Microsoft Excel in XPS unterstützt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Excel in Ods, Sxc und Fods (OpenOffice / LibreOffice Calc) konvertieren**
Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in Ods-, Sxc- und Fods-Dateien. Das nachstehende Codebeispiel zeigt, wie man die [Vorlage](book1.xlsx) in Ods-, Sxc- und Fods-Dateien konvertiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**

MHTML kombiniert normales HTML mit externen Ressourcen (das heißt, Inhalt, der normalerweise verknüpft ist, wie Bilder, Animationen, Audio usw.) in einer Datei. Sie werden für E-Mails mit der Dateierweiterung .mht verwendet.

Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe als MHTML-Datei speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Excel-Arbeitsmappe in HTML konvertieren**

Die Aspose.Cells-API bietet Unterstützung für den Export von Tabellenkalkulationen im HTML-Format. Hierfür verwendet Aspose.Cells die Klasse [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), um die Flexibilität zu bieten, verschiedene Aspekte der Ausgabe-HTML zu steuern.

Das folgende Beispiel zeigt, wie man eine Arbeitsmappe als HTML-Datei speichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Bildvoreinstellungen für HTML einstellen**

Ab Windows 8.0.2 hat Aspose.Cells [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) für die Klasse [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) freigelegt, was es Entwicklern ermöglicht, Bildpräferenzen beim Speichern von Tabellenkalkulationen im HTML-Format anzugeben.

Im Folgenden sind Details einiger Bildvoreinstellungen aufgelistet,

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): Gibt den Bildtyp an. Bitte beachten Sie, dass alle Formen, einschließlich Diagramme, im Ausgabe-HTML als Bilder gerendert werden.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Gibt das Anti-Aliasing für Linien, Kurven und Kanten von gefüllten Bereichen an.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Gibt die Qualität der Textdarstellung an.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): Gibt die Qualität des Bildes zwischen 0 und 100 an, wenn [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) als Jpeg angegeben ist.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Ruft die vertikale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Ruft die horizontale Auflösung des Bildes in Punkten pro Zoll ab oder legt diese fest.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Ruft den Kompressionstyp für die Bilder ab oder legt diesen fest, wenn [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) als Tiff angegeben ist.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): Gibt an, ob der Hintergrund eines Bildes transparent sein soll, wenn ImageFormat als Png angegeben ist.

Der folgende Code demonstriert, wie [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) verwendet wird, um verschiedene Präferenzen anzugeben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Excel-Arbeitsmappe in Markdown konvertieren**

Die Aspose.Cells-API bietet Unterstützung für den Export von Tabellenkalkulationen im Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, geben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) als zweiten Parameter der Methode [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) weiter. Sie können auch die Klasse [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions) verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblattes in Markdown anzugeben.

Das folgende Codebeispiel demonstriert den Export des aktiven Arbeitsblatts in Markdown unter Verwendung des Enumerationselements [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Bitte beachten Sie die [Ausgabedatei im Markdown-Format](md_sample.txt), die vom Code generiert wurde, als Referenz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine Json(Javascript Object Notation)-Datei.

Das folgende Beispiel demonstriert, wie das aktive Arbeitsblatt in JSON exportiert wird, indem das [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) Enumerationsmitglied verwendet wird. Bitte sehen Sie den Code zur Konvertierung der [Quelldatei](Book1.xlsx) in die [erstellte JSON-Datei](Book1.Json) für Referenzzwecke an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Excel in XML umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in das Excel 2003 Spreadsheet XML- und das Plain-XML-Format.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Excel-Arbeitsmappe in TIFF umwandeln**
Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine TIFF-Datei.

Der unten stehende Codeausschnitt zeigt, wie Excel in TIFF umgewandelt wird:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Excel-Arbeitsmappe in DOCX umwandeln**

Die Aspose.Cells-API bietet Unterstützung für die Konvertierung von Tabellenkalkulationen in das DOCX-Format. Um die Arbeitsmappe in DOCX zu exportieren, geben Sie als zweiten Parameter der Methode [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) das [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) an. Sie können auch die [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in DOCX festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt in DOCX exportiert wird, indem das Element [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) verwendet wird. Sehen Sie sich die [Ausgabe-DOCX-Datei](Book1.docx) an, die vom Code generiert wurde, um sich zu orientieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Excel-Arbeitsmappe in PPTX umwandeln**

Die Aspose.Cells-API bietet Unterstützung für die Konvertierung von Tabellenkalkulationen in das PPTX-Format. Um die Arbeitsmappe in PPTX zu exportieren, geben Sie als zweiten Parameter der Methode [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) das [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) an. Sie können auch die [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in PPTX festzulegen.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt in PPTX exportiert wird, indem das Element [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) verwendet wird. Sehen Sie sich die [Ausgabe-PPTX-Datei](Book1.pptx) an, die vom Code generiert wurde, um sich zu orientieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Erweiterte Themen**
- [Konvertieren der Überarbeitung von XLSB zu XLSM](/cells/de/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/de/net/convert-excel-to-html/)
- [Bild](/cells/de/net/convert-excel-to-image/)
- [Json](/cells/de/net/convert-workbook-to-json/)
- [Excel-Arbeitsmappe in ODS, SXC und FODS (OpenOffice / LibreOffice calc) konvertieren](/cells/de/net/convert-excel-to-ods/)
- [Pdf](/cells/de/net/convert-excel-workbook-to-pdf/)
- [Excel in CSV, TSV und Text konvertieren](/cells/de/net/convert-excel-to-csv-tsv-and-txt/)
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/net/track-document-conversion-progress/)
- [CSV, TSV und TXT in Excel umwandeln](/cells/de/net/convert-csv-tsv-and-txt-to-excel/)
