---
title: Actualizar valores de formas vinculadas
type: docs
weight: 3000
url: /es/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A veces, tiene una forma vinculada en su archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells si desea guardar su libro de trabajo en formato XLS o XLSX. Sin embargo, si desea guardar su libro de trabajo en formato PDF o HTML, entonces deberá llamar al método [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

La siguiente captura de pantalla muestra el archivo de Excel fuente utilizado en el código de muestra a continuación. Tiene una imagen vinculada **Picture 1** vinculada a la celda A1. Cambiaremos el valor de la celda A1 con Aspose.Cells y luego llamaremos al método [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) para actualizar el valor de **Picture 1** y guardarlo en formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Puede descargar el [archivo de Excel fuente](5472956.xlsx) y el [PDF de salida](5472955.pdf) desde los enlaces proporcionados.

### Código Java para actualizar los valores de formas vinculadas

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
