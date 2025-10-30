---
title: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 280
url: /sv/python-net/export-chart-to-svg-with-viewbox-attribute/
description: Exportera diagram till SVG med viewBox attribut genom att använda Aspose.Cells för Python via .NET API.
keywords: Python Exportera diagram till SVG med viewBox attribut, Exportera diagram till SVG med viewBox attribut i Python via NET, Python Konvertera diagram till SVG med viewBox attribut.
---

{{% alert color="primary" %}}

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i dess XML. Aspose.Cells för Python via .NET tillhandahåller dock [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) -egenskapen som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attribut.

{{% /alert %}}

## Exportera diagram till SVG med viewBox-attribut

Följande kodexempel exporterar diagrammet till SVG-format med viewBox-attributet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ExportChartToSvgWithViewBox.py" >}}

{{% alert color="primary" %}}

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
