---
title: Copiar Datos de Rango con Estilo
type: docs
weight: 340
url: /es/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Copiar Solo Datos del Rango](/cells/es/java/copy-range-data-only/) explica cómo copiar los datos de un rango de celdas a otro rango. Aspose.Cells también puede copiar un rango completo con formato. Este artículo explica cómo.

{{% /alert %}} 
## **Copiar datos de rango con estilo**
Aspose.Cells proporciona una variedad de clases y métodos para trabajar con rangos, por ejemplo, [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-), etc.

Este ejemplo:

1. Crea un libro de trabajo.
1. Rellena un número de celdas en la primera hoja de cálculo con datos.
1. Crea un rango.
1. Crea un objeto de estilo con atributos de formato específicos.
1. Aplica el estilo al rango de datos.
1. Crea un segundo rango de celdas.
1. Copia datos con el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

{{< app/cells/assistant language="java" >}}
