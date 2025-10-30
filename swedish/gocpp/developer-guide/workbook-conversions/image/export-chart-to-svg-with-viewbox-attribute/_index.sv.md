---
title: Exportera diagram till SVG med viewBox atribut med C++
linktitle: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 280
url: /sv/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exportera ett diagram till SVG format med viewBox attribut med Aspose.Cells med Golang via C++.
---

{{% alert color="primary" %}}

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i dess XML. Men Aspose.Cells tillhandahåller [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/)-egenskapen som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attributen.

{{% /alert %}}

## Exportera diagram till SVG med viewBox-attribut

Följande kodexempel exporterar diagrammet till SVG-format med viewBox-attributet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
