---
title: Arbeitsblatt und Arbeitsmappe zu Bild mithilfe von ImageOrPrintOptions rendern
type: docs
weight: 220
url: /de/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Dieses Dokument soll ein detailliertes Verständnis dafür vermitteln, wie man ein Arbeitsblatt oder eine Arbeitsmappe in eine Bilddatei konvertiert und verschiedene Bild- und Druckoptionen für das Bild anwendet, z.B. Auflösung, TIFF-Komprimierung, Bildformat und Seitengüte.

{{% /alert %}}

## **Übersicht**

Manchmal müssen Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Möglicherweise müssen Sie die Arbeitsblattbilder in Ihre Anwendungen oder Webseiten einfügen. Sie müssen möglicherweise die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach ein Arbeitsblatt als Bild gerendert haben, um es anderswo verwenden zu können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen unterschiedlicher Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und weitere Bild- und Druckoptionen.

Die API bietet mehrere wertvolle Klassen, z.B. [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

Die [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-Klasse kümmert sich um das Rendern von Bildern für das Arbeitsblatt, während die [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)-Klasse dasselbe für eine Arbeitsmappe tut. Beide genannten Klassen haben mehrere überladene Versionen der *toImage*-Methode, die ein Arbeitsblatt oder eine Arbeitsmappe direkt in Bild-Datei(en) umwandeln können, die mit den gewünschten Attributen oder Optionen spezifiziert sind. Sie können die Bilddatei auf dem Datenträger/Stream speichern. Es gibt verschiedene Bildformate, die unterstützt werden, z.B. BMP, PNG, GIFF, JPEG, TIFF, EMF, usw.

### **Arbeitsblatt in Bild konvertieren**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Konversionsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert die ersten und zweiten Arbeitsblätter in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Oder Sie können durch die Arbeitsmappe navigieren und jedes Arbeitsblatt in ein separates Bild renden:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Arbeitsmappe in Bild konvertieren:**

Um die vollständige Arbeitsmappe ins Bildformat zu rendern, können Sie entweder den obigen Ansatz verwenden oder einfach die [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)-Klasse verwenden, die eine Instanz von [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) sowie das Objekt von [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) akzeptiert.

Sie können die gesamte Arbeitsmappe in ein einzelnes TIFF-Bild mit mehreren Bildern oder Seiten speichern:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Verwandte Artikel

- [Arbeitsblatt in verschiedene Bildformate konvertieren](/cells/de/java/converting-worksheet-to-different-image-formats/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
