---
title: Diagramm nach SVG mit viewBox-Attribut exportieren
type: docs
weight: 280
url: /de/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportieren Sie das Diagramm nach SVG mit dem ViewBox-Attribut, indem Sie Aspose.Cells for Python via .NET API verwenden.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 Wenn das Diagramm in das Format SVG exportiert wird, wird standardmäßig das**viewBox** Das Attribut ist nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells for Python via .NET[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) Eigenschaft, die bei Festlegung auf**WAHR** Exportiert das Diagramm nach SVG mit dem ViewBox-Attribut.

{{% /alert %}}

##  Diagramm nach SVG mit viewBox-Attribut exportieren

Der folgende Beispielcode exportiert das Diagramm in das Format SVG mit dem viewBox-Attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Wenn Sie die SVG des Diagramms im Editor öffnen, finden Sie die**viewBox** Attribut ähnlich diesem.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
