---
title: Image
type: docs
weight: 300
url: /de/python-net/convert-excel-to-image/
description: Konvertieren Sie das Diagramm in Image, indem Sie Aspose.Cells for Python via .NET API verwenden.
keywords: Python Convert Chart to Image, Export Chart to Image in Python via NET, Python Save Chart to Image.
---
{{% alert color="primary" %}}

Mit Aspose.Cells for Python via .NET können Sie ein Arbeitsblatt aus der Arbeitsmappe exportieren und in verschiedene Formate konvertieren. In diesem Artikel wird erläutert, wie Sie ein Arbeitsblatt in verschiedene Formate konvertieren.

{{% /alert %}}

##  Konvertieren der Arbeitsmappe in TIFF

 Eine Excel-Datei kann mehrere Blätter mit mehreren Seiten enthalten.[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) ermöglicht Ihnen die Konvertierung von Excel in TIFF mit mehreren Seiten. Außerdem können Sie mehrere Optionen für TIFF steuern, z[Kompression](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), [Farbtiefe](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_color_depth/), Auflösung([Horizontale Auflösung](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Vertikale Auflösung](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

 Der folgende Codeausschnitt zeigt, wie man Excel mit mehreren Seiten in TIFF konvertiert. Der[Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) Und[generiertes TIFF-Bild](workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz beigefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

##  **Konvertieren des Arbeitsblatts in Image**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Ein Arbeitsblatt kann beispielsweise Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Beispielsweise müssen Sie möglicherweise ein Bild eines Arbeitsblatts in einer Anwendung oder Webseite verwenden. Möglicherweise möchten Sie ein Bild in ein Word-Dokument Microsoft, eine Datei PDF, eine Präsentation PowerPoint oder einen anderen Dokumenttyp einfügen. Einfach ausgedrückt: Sie möchten, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es woanders verwenden können.

Aspose.Cells for Python via .NET unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion nutzen zu können, müssen Sie die importieren**[aspose.cells.rendering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/)**Namensraum für Ihr Programm oder Projekt. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel *[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**, *[ImageOrPrintOptions](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/)**, *[WorkbookRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/)**, und andere.

 Der**[SheetRender](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)**Die Klasse stellt ein Arbeitsblatt dar, das als Bilder gerendert werden soll. Es hat eine überladene Methode, *[vorstellen](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)**, das ein Arbeitsblatt in Bilddateien mit unterschiedlichen Attributen oder Optionen konvertieren kann. Es gibt ein System.Drawing.Bitmap-Objekt zurück und Sie können eine Bilddatei auf der Festplatte oder im Stream speichern. Es werden mehrere Bildformate unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

Derzeit unterstützt die Version API zum Konvertieren von Arbeitsblättern in Bilder keine 3D-Blasendiagramme.

{{% /alert %}}

##  **Konvertieren des Arbeitsblatts in SVG**

SVG steht für Scalable Vector Graphics. SVG ist eine auf XML-Standards basierende Spezifikation für zweidimensionale Vektorgrafiken. Es handelt sich um einen offenen Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

Aspose.Cells for Python via .NET konnte seit Version 7.1.0 Arbeitsblätter in das Bild SVG konvertieren. Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

##  **Vorabthemen**
- [Konvertieren Sie ein Excel-Diagramm in Image](/cells/de/python-net/convert-an-excel-chart-to-image/)
- [Konvertieren des Diagramms in Image im SVG-Format](/cells/de/python-net/converting-chart-to-image-in-svg-format/)
- [Diagramm nach SVG mit viewBox-Attribut exportieren](/cells/de/python-net/export-chart-to-svg-with-viewbox-attribute/)
