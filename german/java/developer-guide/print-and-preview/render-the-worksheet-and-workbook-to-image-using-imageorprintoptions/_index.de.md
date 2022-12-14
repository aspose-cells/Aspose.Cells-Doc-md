---
title: Rendern Sie das Arbeitsblatt und die Arbeitsmappe mithilfe von ImageOrPrintOptions in ein Bild
type: docs
weight: 220
url: /de/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Dieses Dokument soll ein detailliertes Verständnis dafür vermitteln, wie Sie ein Arbeitsblatt oder eine Arbeitsmappe in eine Bilddatei konvertieren und verschiedene Bild- und Druckoptionen für das Bild anwenden, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

## **Überblick**

Manchmal müssen Sie Ihre Arbeitsblätter möglicherweise als bildliche Darstellung präsentieren. Sie müssen die Arbeitsblattbilder in Ihren Anwendungen oder Webseiten präsentieren. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Einstellung verschiedener Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und andere Bild- und Druckoptionen.

Die API bietet mehrere wertvolle Klassen, zum Beispiel,[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

 Das[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) Die Klasse übernimmt die Aufgabe, Bilder für das Arbeitsblatt zu rendern, während die[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)macht dasselbe für eine Arbeitsmappe. Beide oben genannten Klassen haben mehrere überladene Versionen der*vorstellen*Methode, die ein Arbeitsblatt oder eine Arbeitsmappe direkt in Bilddatei(en) konvertieren kann, die mit Ihren gewünschten Attributen oder Optionen angegeben sind. Sie können die Bilddatei auf der Festplatte/im Stream speichern. Es werden mehrere Bildformate unterstützt, zB BMP, PNG, GIFF, JPEG, TIFF, EMF und so weiter.

### **Arbeitsblatt in Bild umwandeln**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Konvertierungsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert das erste und zweite Arbeitsblatt in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Oder Sie können durch die Arbeitsmappe blättern und jedes darin enthaltene Arbeitsblatt in ein separates Bild rendern:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Arbeitsmappe in Bild konvertieren:**

 Um die komplette Arbeitsmappe in das Bildformat zu rendern, können Sie entweder den obigen Ansatz verwenden oder einfach die verwenden[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) Klasse, die eine Instanz von akzeptiert[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sowie das Objekt von[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

 Das[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) Klasse kann die Arbeitsmappe nur im TIFF-Format speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## In Verbindung stehende Artikel

- [Konvertieren von Arbeitsblättern in verschiedene Bildformate](/cells/de/java/converting-worksheet-to-different-image-formats/)
- [Diagramm mit viewBox-Attribut nach SVG exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertieren von Arbeitsblatt in Bild und Arbeitsblatt in Bild für Seite](/cells/de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
