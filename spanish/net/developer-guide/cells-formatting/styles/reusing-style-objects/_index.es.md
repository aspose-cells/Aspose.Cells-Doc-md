---
title: Reutilización de objetos de estilo
type: docs
weight: 3000
url: /es/net/reusing-style-objects/
---
{{% alert color="primary" %}}

La reutilización de objetos de estilo puede ahorrar memoria y hacer que un programa sea más rápido.

{{% /alert %}}

Para aplicar algún formato a una gran variedad de celdas en una hoja de trabajo:

1. Cree un objeto de estilo.
1. Especifique los atributos.
1. Aplique el estilo a las celdas del rango.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Porque el[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) El enfoque usa mucha menos memoria y es eficiente, la antigua propiedad Cell.Style que consumía mucha memoria innecesaria, se eliminó con el lanzamiento de Aspose.Cells 7.1.0.

{{% /alert %}}
