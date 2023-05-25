---
title: Rendern Sie das Arbeitsblatt und die Arbeitsmappe mit ImageOrPrintOptions in ein Bild
type: docs
weight: 220
url: /de/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Dieses Dokument soll ein detailliertes Verständnis dafür vermitteln, wie man ein Arbeitsblatt oder eine Arbeitsmappe in eine Bilddatei konvertiert und verschiedene Bild- und Druckoptionen für das Bild anwendet, Optionen wie Auflösung, Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

##  **Überblick**

Manchmal kann es erforderlich sein, dass Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Sie müssen die Arbeitsblattbilder in Ihren Anwendungen oder Webseiten präsentieren. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten lediglich, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen verschiedener Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und andere Bild- und Druckoptionen.

Die API bietet mehrere wertvolle Klassen, zum Beispiel:[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), usw.

 Der[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) Die Klasse übernimmt die Aufgabe, Bilder für das Arbeitsblatt zu rendern, während die[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)macht dasselbe für eine Arbeitsmappe. Beide oben genannten Klassen verfügen über mehrere überladene Versionen von*vorstellen*Methode, die ein Arbeitsblatt oder eine Arbeitsmappe direkt in Bilddateien konvertieren kann, die mit den gewünschten Attributen oder Optionen angegeben sind. Sie können die Bilddatei auf der Festplatte/im Stream speichern. Es werden mehrere Bildformate unterstützt, z. B. BMP, PNG, GIFF, JPEG, TIFF, EMF usw.

###  **Arbeitsblatt in Bild konvertieren**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

##  **Konvertierungsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert das erste und zweite Arbeitsblatt in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Oder Sie können durch die Arbeitsmappe blättern und jedes darin enthaltene Arbeitsblatt in ein separates Bild rendern:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

##  **Arbeitsmappe in Bild konvertieren:**

 Um die komplette Arbeitsmappe in ein Bildformat zu rendern, können Sie entweder den oben genannten Ansatz verwenden oder einfach die verwenden[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) Klasse, die eine Instanz von akzeptiert[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sowie der Gegenstand von[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Sie können die gesamte Arbeitsmappe in einem einzigen TIFF-Bild mit mehreren Frames oder Seiten speichern:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

##  In Verbindung stehende Artikel

- [Arbeitsblatt in verschiedene Bildformate konvertieren](/cells/de/java/converting-worksheet-to-different-image-formats/)
- [Diagramm nach SVG mit viewBox-Attribut exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportieren Sie ein Arbeitsblatt oder Diagramm in ein Bild mit der gewünschten Breite und Höhe](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild seitenweise konvertieren](/cells/de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
