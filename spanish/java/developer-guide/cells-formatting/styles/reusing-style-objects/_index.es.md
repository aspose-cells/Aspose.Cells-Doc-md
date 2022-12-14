---
title: Reutilización de objetos de estilo
type: docs
weight: 60
url: /es/java/reusing-style-objects/
---
{{% alert color="primary" %}}

La reutilización de objetos de estilo puede ahorrar memoria y hacer que el programa se ejecute más rápido.

{{% /alert %}}

Para aplicar algún formato a una gran variedad de celdas en una hoja de trabajo:

1. Cree un objeto de estilo.
1. Especifique los atributos.
1. Aplique el estilo a las celdas del rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

El mismo proceso que se discutió anteriormente también se podría lograr de la siguiente manera.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Porque el[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) y[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) utilizan mucha menos memoria y son eficientes, cuanto más antiguos*Cell.getStyle()* propiedad que consumía mucha memoria innecesaria, se eliminó con el lanzamiento de*Aspose.Cells 7.1.0*.

{{% /alert %}}
