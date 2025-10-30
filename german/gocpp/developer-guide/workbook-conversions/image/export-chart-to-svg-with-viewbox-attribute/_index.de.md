---
title: Exportieren Sie ein Diagramm mit viewBox Attribut in SVG mit C++
linktitle: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 280
url: /de/go-cpp/export-chart-to-svg-with-viewbox-attribute/
description: Ein Diagramm im SVG Format mit viewBox Attribut mithilfe von Aspose.Cells mit Golang über C++ exportieren.
---

{{% alert color="primary" %}}

Standardmäßig ist das **viewBox**-Attribut beim Export des Diagramms ins SVG-Format nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getsvgfittoviewport/) Eigenschaft, die beim Einstellen auf **true** das Diagramm ins SVG mit viewBox-Attribut exportiert.

{{% /alert %}}

## Diagramm als SVG mit viewBox-Attribut Exportieren

Der folgende Beispielcode exportiert das Diagramm im SVG-Format mit dem viewBox-Attribut.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportChartToSvgWithViewboxAttribute.go" >}}
{{% alert color="primary" %}}

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
