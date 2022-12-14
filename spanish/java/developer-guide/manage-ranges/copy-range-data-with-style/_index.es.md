---
title: Copiar datos de rango con estilo
type: docs
weight: 340
url: /es/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Copiar solo datos de rango](/cells/es/java/copy-range-data-only/) explicó cómo copiar los datos de un rango de celdas a otro rango. Aspose.Cells también puede copiar un rango completo con formato. Este artículo explica cómo.

{{% /alert %}} 
## **Copiar datos de rango con estilo**
Aspose.Cells proporciona una gama de clases y métodos para trabajar con rangos, por ejemplo,[crearRango()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [Bandera de estilo](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [aplicarEstilo()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), etc.

Este ejemplo:

1. Crea un libro de trabajo.
1. Llena un número de celdas en la primera hoja de cálculo con datos.
1. Crea un rango.
1. Crea un objeto de estilo con atributos de formato especificados.
1. Aplica el estilo al rango de datos.
1. Crea un segundo rango de celdas.
1. Copia datos con el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

