---
title: Bild
type: docs
weight: 300
url: /de/python-net/convert-excel-to-image/
description: Konvertieren Sie das Diagramm in ein Bild mithilfe von Aspose.Cells for Python via .NET API.
keywords: Python Konvertieren Sie das Diagramm in ein Bild, exportieren Sie das Diagramm in ein Bild in Python via NET, speichern Sie das Diagramm in ein Bild.
---


{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erläutert, wie Sie ein Arbeitsblatt in verschiedene Formate konvertieren.

{{% /alert %}}

## Arbeitsmappe in TIFF konvertieren

Eine Excel-Datei kann mehrere Blätter mit mehreren Seiten enthalten. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) ermöglicht es Ihnen, Excel in TIFF mit mehreren Seiten zu konvertieren. Außerdem können Sie mehrere Optionen für TIFF kontrollieren, wie [Komprimierung](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Farbtiefe](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Auflösung ([Horizontale Auflösung](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Vertikale Auflösung](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

Der folgende Code zeigt, wie Excel in TIFF mit mehreren Seiten konvertiert wird. Die [Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) und das generierte TIFF-Bild (workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz angehängt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Arbeitsblatt in Bild konvertieren**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells für Python via .NET unterstützt die Umwandlung von Excel-Arbeitsblättern in Bilder. Um dieses Feature zu verwenden, müssen Sie den Namespace [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) in Ihr Programm oder Projekt importieren. Es verfügt über mehrere wertvolle Klassen für das Rendering und Drucken, wie zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/) und andere.

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) repräsentiert ein Arbeitsblatt, das als Bilder gerendert werden soll. Sie hat eine überladene Methode, [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), die ein Arbeitsblatt mit verschiedenen Attributen oder Optionen in eine Bilddatei konvertieren kann. Sie gibt ein System.Drawing.Bitmap-Objekt zurück, und Sie können eine Bilddatei auf der Festplatte oder im Stream speichern. Verschiedene Bildformate werden unterstützt, wie zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Zum jetzigen Zeitpunkt unterstützt die API zur Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.

{{% /alert %}}

## **Arbeitsblatt in SVG konvertieren**

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Aspose.Cells for Python via .NET kann Arbeitsblätter seit Version 7.1.0 in SVG-Bildern konvertieren. Im folgenden Codeausschnitt wird gezeigt, wie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Erweiterte Themen**
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/python-net/convert-an-excel-chart-to-image/)
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/python-net/converting-chart-to-image-in-svg-format/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/python-net/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="python-net" >}}
