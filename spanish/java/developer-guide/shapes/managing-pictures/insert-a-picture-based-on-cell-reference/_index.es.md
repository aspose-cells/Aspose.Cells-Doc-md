---
title: Insertar una imagen basada en la referencia de celda
type: docs
weight: 90
url: /es/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A veces tienes una imagen vacía y necesitas mostrar datos o contenidos en la imagen configurando una referencia de celda en la Barra de Fórmulas. Aspose.Cells soporta esta característica (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en una referencia de celda

Aspose.Cells admite mostrar el contenido de una celda de la hoja de cálculo en una forma de imagen. Puede vincular la imagen a la celda que contiene los datos que desea mostrar. Dado que la celda o el rango de celdas están vinculados al objeto gráfico, los cambios en los datos aparecen automáticamente en el objeto gráfico. Agregue una imagen a la hoja de cálculo llamando al método [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream)) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Especifique el rango de celdas utilizando el método [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) del objeto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

A continuación se muestra una captura de pantalla del archivo que genera el código a continuación.

**Insertar una imagen basada en la referencia de la celda**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Código de Muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
