---
title: Exportera diagram till SVG med viewBox-attribut
type: docs
weight: 280
url: /sv/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportera diagram till SVG med viewBox-attribut genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Export Chart to SVG with viewBox attribute, Export Chart to SVG with viewBox attribute in Python via NET, Python Convert Chart to SVG with viewBox attribute.
---
{{% alert color="primary" %}}

 Som standard, när diagrammet exporteras till SVG-formatet,**viewBox** attribut ingår inte i dess XML. Däremot tillhandahåller Aspose.Cells for Python via .NET[**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) egenskap som när den är inställd på**Sann** exporterar diagrammet till SVG med viewBox-attribut.

{{% /alert %}}

##  Exportera diagram till SVG med viewBox-attribut

Följande exempelkod exporterar diagrammet till formatet SVG med attributet viewBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

 Om du öppnar diagrammets SVG i anteckningsblocket hittar du**viewBox** attribut liknande detta.

{{< highlight "java" >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
