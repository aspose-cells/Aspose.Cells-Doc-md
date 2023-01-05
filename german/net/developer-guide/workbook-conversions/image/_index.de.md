---
title: Bild
type: docs
weight: 300
url: /de/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. In diesem Artikel wird erläutert, wie Sie ein Arbeitsblatt in andere Formate konvertieren.

{{% /alert %}}

## Konvertieren der Arbeitsmappe in TIFF

 Eine Excel-Datei kann mehrere Blätter mit mehreren Seiten enthalten.[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) können Sie Excel in TIFF mit mehreren Seiten konvertieren. Außerdem können Sie mehrere Optionen für TIFF steuern, z[Kompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Farbtiefe](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Auflösung([Horizontale Auflösung](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Vertikale Auflösung](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 Das folgende Code-Snippet zeigt, wie Sie Excel in TIFF mit mehreren Seiten konvertieren. Das[Excel-Quelldatei](workbook-to-tiff-with-mulitiple-pages.xlsx) und[generiertes Bild TIFF](workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz beigefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Arbeitsblatt in Bild umwandeln**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Ein Arbeitsblatt kann beispielsweise Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Beispielsweise müssen Sie möglicherweise ein Bild eines Arbeitsblatts in einer Anwendung oder Webseite verwenden. Möglicherweise möchten Sie ein Bild in ein Microsoft-Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumenttyp einfügen. Einfach ausgedrückt, Sie möchten, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion nutzen zu können, müssen Sie die**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)** Namensraum zu Ihrem Programm oder Projekt. Es hat zum Beispiel mehrere wertvolle Klassen zum Rendern und Drucken**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, und andere.

 Das**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** Die Klasse stellt ein Arbeitsblatt dar, das als Bilder gerendert werden soll. Es hat eine überladene Methode,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**die ein Arbeitsblatt in Bilddatei(en) mit unterschiedlichen Attributen oder Optionen konvertieren kann. Es gibt ein System.Drawing.Bitmap-Objekt zurück und Sie können eine Bilddatei auf der Festplatte oder im Stream speichern. Mehrere Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Das folgende Code-Snippet zeigt, wie Sie ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Derzeit unterstützt die API zum Konvertieren von Arbeitsblättern in Bilder keine 3D-Blasendiagramme.

{{% /alert %}}

## **Konvertieren des Arbeitsblatts in SVG**

SVG steht für Scalable Vector Graphics. SVG ist eine auf XML-Standards basierende Spezifikation für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

Aspose.Cells for .NET kann seit Version 7.1.0 Arbeitsblätter in SVG-Bilder konvertieren. Das folgende Code-Snippet zeigt, wie Sie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Themen vorantreiben**
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/net/convert-an-excel-chart-to-image/)
- [Konvertieren des Diagramms in ein Bild im Format SVG](/cells/de/net/converting-chart-to-image-in-svg-format/)
- [Diagramm nach SVG mit viewBox-Attribut exportieren](/cells/de/net/export-chart-to-svg-with-viewbox-attribute/)
- [Verfolgen Sie den Konvertierungsfortschritt von Excel bis TIFF](/cells/de/net/track-conversion-progress-of-excel-to-tiff/)
