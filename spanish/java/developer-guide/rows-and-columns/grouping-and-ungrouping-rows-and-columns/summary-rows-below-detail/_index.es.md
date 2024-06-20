---
title: Aplicar subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
type: docs
weight: 100
url: /es/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Este artículo explicará cómo aplicar un subtotal a los datos y cambiar la dirección de las filas de resumen de contorno debajo del detalle.

Puede aplicar un subtotal a los datos usando el método [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])). Toma los siguientes parámetros.

- **ÁreaCelda** - El rango en el que aplicar el subtotal
- **AgruparPor** - El campo por el que agrupar, como un desplazamiento entero basado en cero
- **Función** - La función de subtotal
- **ListaTotal** - Una matriz de desplazamientos de campo basados en cero, que indica los campos a los que se añaden los subtotales.
- **Reemplazar** - Indica si reemplazar los subtotales actuales
- **Saltos de página** - Indica si se debe agregar un salto de página entre grupos
- **ResumenDebajoDeDatos** - Indica si agregar resumen debajo de los datos.

También puede controlar la dirección de las filas de resumen **abajo del detalle** como se muestra en la siguiente captura de pantalla utilizando la propiedad [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow). Puede abrir esta configuración en Microsoft Excel utilizando **Datos > Esquema > Configuración**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Ejemplo

### Capturas de pantalla comparando archivos de origen y salida

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de muestra. Como puede ver, se ha aplicado un subtotal al rango **A2:B11** y la dirección del esquema es filas de resumen abajo del detalle.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Código Java para aplicar subtotal y cambiar la dirección de las filas de resumen abajo del detalle

Aquí está el código de ejemplo para lograr el resultado mostrado anteriormente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
