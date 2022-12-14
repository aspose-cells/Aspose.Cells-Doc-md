---
title: Insertar una imagen basada en la referencia Cell
type: docs
weight: 90
url: /es/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

A veces tiene una imagen vacía y necesita mostrar datos o contenidos en la imagen estableciendo una referencia de celda en la barra de fórmulas. Aspose.Cells admite esta función (Microsoft Excel 2010).

{{% /alert %}}

## Insertar una imagen basada en la referencia Cell

Aspose.Cells admite la visualización del contenido de una celda de la hoja de trabajo en forma de imagen. Puede vincular la imagen a la celda que contiene los datos que desea mostrar. Dado que la celda o el rango de celdas está vinculado al objeto gráfico, los cambios en los datos aparecen automáticamente en el objeto gráfico. Agregue una imagen a la hoja de trabajo llamando al[**añade una foto**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) método de la[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objeto). Especifique el rango de celdas usando el[**establecerFórmula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) metodo de la[**Imagen**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objeto.

A continuación se muestra una captura de pantalla del archivo que genera el siguiente código.

**Insertar una imagen basada en la referencia de celda**

![todo:imagen_alternativa_texto](insert-a-picture-based-on-cell-reference_1.png)

## Código de muestra

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
