﻿---
title: Actualizar valores de formas vinculadas
type: docs
weight: 3000
url: /es/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

 veces, tiene una forma vinculada en su archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells si desea guardar su libro de trabajo en formato XLS o XLSX. Sin embargo, si desea guardar su libro de trabajo en formato PDF o HTML, deberá llamar[**Hoja de trabajo.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

 La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado en el código de ejemplo a continuación. tiene un enlace**Foto 1** vinculado a la celda A1. Cambiaremos el valor de la celda A1 con Aspose.Cells y luego llamaremos[**Hoja de trabajo.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) método para actualizar el valor de**Foto 1** y guardarlo en formato PDF.

![todo:imagen_alternativa_texto](refresh-values-of-linked-shapes_1.png)

Puedes descargar el[archivo fuente de Excel](5472956.xlsx) y el[salida PDF](5472955.pdf) de los enlaces dados.

### Java código para actualizar los valores de las formas vinculadas

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
