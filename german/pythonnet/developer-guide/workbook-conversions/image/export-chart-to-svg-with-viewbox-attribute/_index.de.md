---
title: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 280
url: /de/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportieren Sie das Diagramm in SVG mit Attribut viewBox unter Verwendung von Aspose.Cells für Python via .NET API.
keywords: Python Exportieren Sie das Diagramm in SVG mit dem Attribut viewBox, Exportieren Sie das Diagramm in SVG mit dem Attribut viewBox in Python via NET, Konvertieren Sie das Diagramm in SVG mit dem Attribut viewBox.
---

{{% alert color="primary" %}}

Standardmäßig wird beim Export des Diagramms in das SVG-Format das **viewBox**-Attribut nicht in seinem XML enthalten. Aspose.Cells für Python via .NET bietet jedoch die [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/)-Eigenschaft, die beim Setzen auf **true** das Diagramm in SVG mit dem Attribut viewBox exportiert.

{{% /alert %}}

## Diagramm als SVG mit viewBox-Attribut Exportieren

Der folgende Beispielcode exportiert das Diagramm im SVG-Format mit dem viewBox-Attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
