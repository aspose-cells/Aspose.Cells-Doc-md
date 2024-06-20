---
title: Bild
type: docs
weight: 300
url: /de/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erklärt, wie man ein Arbeitsblatt in verschiedene Formate konvertiert.

{{% /alert %}}

## Arbeitsmappe in TIFF konvertieren

Eine Excel-Datei kann mehrere Tabellenblätter mit mehreren Seiten enthalten. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) ermöglicht es Ihnen, Excel in TIFF mit mehreren Seiten zu konvertieren. Außerdem können Sie mehrere Optionen für TIFF steuern, wie [Komprimierung](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Farbtiefe](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Auflösung ([Horizontale Auflösung](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Vertikale Auflösung](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

Der folgende Code zeigt, wie Excel in TIFF mit mehreren Seiten konvertiert wird. Die [Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) und das generierte TIFF-Bild (workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz angehängt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Arbeitsblatt in Bild konvertieren**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion zu verwenden, müssen Sie den [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) Namespace in Ihr Programm oder Projekt importieren. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, wie zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) und andere.

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) repräsentiert ein Arbeitsblatt, das als Bilder gerendert werden soll. Sie hat eine überladene Methode, [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), die ein Arbeitsblatt mit verschiedenen Attributen oder Optionen in eine Bilddatei konvertieren kann. Sie gibt ein System.Drawing.Bitmap-Objekt zurück, und Sie können eine Bilddatei auf der Festplatte oder im Stream speichern. Verschiedene Bildformate werden unterstützt, wie zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

Zum jetzigen Zeitpunkt unterstützt die API zur Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.

{{% /alert %}}

## **Arbeitsblatt in SVG konvertieren**

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Seit Version 7.1.0 kann Aspose.Cells for .NET Arbeitsblätter in SVG-Bilder konvertieren. Im folgenden Code-Ausschnitt wird gezeigt, wie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Erweiterte Themen**
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/net/convert-an-excel-chart-to-image/)
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/net/converting-chart-to-image-in-svg-format/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/net/export-chart-to-svg-with-viewbox-attribute/)
- [Konvertierungsvorgang von Excel nach TIFF verfolgen](/cells/de/net/track-conversion-progress-of-excel-to-tiff/)
