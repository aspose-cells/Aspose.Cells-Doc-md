---
title: Konvertieren von Arbeitsblättern in verschiedene Bildformate
type: docs
weight: 30
url: /de/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. In diesem Artikel wird erläutert, wie Sie ein Arbeitsblatt in andere Formate konvertieren.

{{% /alert %}}

## **Arbeitsblatt in Bild umwandeln**

Manchmal ist es nützlich, ein Bild eines Arbeitsblatts zu speichern. Bilder können online geteilt und in andere Dokumente eingefügt werden (z. B. in Microsoft Word verfasste Berichte oder PowerPoint Präsentationen).

Aspose.Cells bietet Bildexport über die**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** Klasse. Diese Klasse stellt das Arbeitsblatt dar, das in ein Bild gerendert wird. Das**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** Klasse bietet die**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**Methode zum Konvertieren eines Arbeitsblatts in eine Bilddatei. BMP-, PNG-, JPEG-, TIFF- und EMF-Formate werden unterstützt.

{{% alert color="primary" %}}

Aspose.Cells for Java unterstützt auch die Konvertierung in das TIFF-Format. Um ein Arbeitsblatt in ein TIFF-Bild zu konvertieren, fügen Sie Ihrem Klassenpfad die JAI-Bibliothek hinzu.

{{% /alert %}} {{% alert color="primary" %}}

Derzeit unterstützt das Konvertierungsarbeitsblatt in Bild API keine 3D-Blasendiagramme.

{{% /alert %}}

Der folgende Code zeigt, wie ein Arbeitsblatt in einer Microsoft-Excel-Datei in eine PNG-Datei konvertiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Arbeitsblatt in SVG konvertieren**

 SVG steht für**Skalierbare Vektorgrafiken**. SVG ist eine auf XML-Standards basierende Spezifikation für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

Seit der Veröffentlichung von v7.1.0,**Aspose.Cells for Java** kann Arbeitsblätter in SVG-Bilder umwandeln.

Um diese Funktion zu verwenden, müssen Sie den Namespace com.aspose.cells in Ihr Programm oder Projekt importieren. Es hat mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, und andere.

Das**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class gibt an, dass das Arbeitsblatt im SVG-Format gespeichert wird.

Das**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**Klasse übernimmt das Objekt von**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** als Parameter, der das Speicherformat auf das SVG-Format setzt.

Das folgende Code-Snippet zeigt, wie Sie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Aktives Arbeitsblatt in einer Arbeitsmappe rendern**

Eine einfache Möglichkeit, ein aktives Arbeitsblatt in eine Arbeitsmappe zu konvertieren, besteht darin, den aktiven Blattindex festzulegen und die Arbeitsmappe dann als SVG zu speichern. Das aktive Blatt wird in SVG gerendert. Der folgende Beispielcode demonstriert diese Funktion:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## In Verbindung stehende Artikel

- [Diagramm mit viewBox-Attribut nach SVG exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertieren von Arbeitsblatt in Bild und Arbeitsblatt in Bild für Seite](/cells/de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
