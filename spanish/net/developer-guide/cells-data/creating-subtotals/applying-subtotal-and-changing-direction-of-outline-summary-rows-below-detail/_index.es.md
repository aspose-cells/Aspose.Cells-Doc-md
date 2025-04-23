---
title: Aplicar subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
type: docs
weight: 100
url: /es/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aprenda cómo aplicar subtotal y cambiar la dirección de resumen de contorno de filas debajo del detalle usando la API Aspose.Cells for .NET.
keywords: Aplicar subtotal, agregar subtotal, cambiar dirección del resumen de contorno de filas debajo del detalle, cambiar dirección del resumen de contorno de columnas a la derecha del detalle, crear subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
---

{{% alert color="primary" %}}

Este artículo explicará cómo aplicar un subtotal a los datos y cambiar la dirección de las filas de resumen de contorno debajo del detalle.

Puede aplicar un subtotal a los datos usando el método [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index). Toma los siguientes parámetros.

- **ÁreaCelda** - El rango en el que aplicar el subtotal
- **AgruparPor** - El campo por el que agrupar, como un desplazamiento entero basado en cero
- **Función** - La función de subtotal
- **ListaTotal** - Una matriz de desplazamientos de campo basados en cero, que indica los campos a los que se añaden los subtotales.
- **Reemplazar** - Indica si reemplazar los subtotales actuales
- **SaltosDePágina** - Indica si agregar salto de página entre grupos
- **ResumenDebajoDeDatos** - Indica si agregar resumen debajo de los datos.

Además, puede controlar la dirección de las **filas de resumen de contorno debajo del detalle** como se muestra en la siguiente captura de pantalla utilizando la propiedad Worksheet.Outline.SummaryRowBelow. Puede abrir esta configuración en Microsoft Excel usando **Datos > Contorno > Configuración**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Imágenes de los archivos de origen y salida

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de ejemplo. Como se puede ver, se ha aplicado un subtotal al rango A2:B11 y la dirección del contorno es resumen de filas debajo del detalle.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Código C# para aplicar subtotal y cambiar la dirección de las filas de resumen de contorno

Aquí está el código de ejemplo para lograr el resultado mostrado anteriormente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
