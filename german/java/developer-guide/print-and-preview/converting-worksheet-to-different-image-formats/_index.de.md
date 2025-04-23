---
title: Konvertieren von Arbeitsblättern in verschiedene Bildformate
type: docs
weight: 30
url: /de/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erklärt, wie man ein Arbeitsblatt in verschiedene Formate konvertiert.

{{% /alert %}}

## **Arbeitsblatt in Bild konvertieren**

Manchmal ist es nützlich, ein Bild eines Arbeitsblatts zu speichern. Bilder können online geteilt, in andere Dokumente eingefügt (Beispielsweise in Berichte in Microsoft Word oder in PowerPoint-Präsentationen).

Aspose.Cells bietet die Bildexportfunktion durch die Klasse [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Diese Klasse repräsentiert die Arbeitsmappe, die als Bild gerendert wird. Die Klasse [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) bietet die Methode [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-) zur Umwandlung einer Arbeitsmappe in eine Bilddatei. BMP, PNG, JPEG, TIFF und EMF-Formate werden unterstützt.

{{% alert color="primary" %}}

Aspose.Cells for Java unterstützt auch die Konvertierung in das TIFF-Format. Um ein Arbeitsblatt in ein TIFF-Bild umzuwandeln, fügen Sie die JAI-Bibliothek Ihrem Klassenpfad hinzu.

{{% /alert %}} {{% alert color="primary" %}}

Zurzeit unterstützt die API für die Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.

{{% /alert %}}

Der folgende Code zeigt, wie man ein Arbeitsblatt in einer Microsoft Excel-Datei in eine PNG-Datei konvertiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Arbeitsblatt in SVG konvertieren**

SVG steht für **skalierbare Vektorgrafiken**. SVG ist eine Spezifikation, die auf XML-Standards für zweidimensionale Vektorgrafiken basiert. Es ist ein offener Standard, der seit 1999 von der World Wide Web Consortium (W3C) entwickelt wurde.

Seit der Veröffentlichung von v7.1.0 kann **Aspose.Cells for Java** Arbeitsblätter in SVG-Bilder konvertieren.

Um diese Funktion zu verwenden, müssen Sie den Namespace com.aspose.cells in Ihr Programm oder Projekt importieren. Es gibt mehrere wertvolle Klassen zum Rendern und Drucken, wie z.B. [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender) und andere.

Die Klasse [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) gibt an, dass die Arbeitsmappe im SVG-Format gespeichert wird.

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) benötigt das Objekt von [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) als Parameter, das das Speicherformat auf das SVG-Format einstellt.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Rendern Sie das aktive Arbeitsblatt in einer Arbeitsmappe**

Ein einfacher Weg, das aktive Arbeitsblatt in einer Arbeitsmappe zu konvertieren, besteht darin, den Index des aktiven Blatts festzulegen und dann die Arbeitsmappe als SVG zu speichern. Dadurch wird das aktive Arbeitsblatt in SVG gerendert. Der folgende Beispielcode zeigt diese Funktion:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Verwandte Artikel

- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Arbeitsblatt in Bild und Arbeitsblatt in Bild nach Seite konvertieren](/cells/de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
