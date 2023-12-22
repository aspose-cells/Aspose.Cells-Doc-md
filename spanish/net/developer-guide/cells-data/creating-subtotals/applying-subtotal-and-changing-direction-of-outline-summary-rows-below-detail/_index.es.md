---
title: Aplicar subtotal y cambiar la dirección de las filas de resumen del esquema debajo de los detalles
type: docs
weight: 100
url: /es/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aprenda cómo aplicar el subtotal y cambiar la dirección del resumen del esquema Filas debajo de Detalle usando Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

Este artículo explicará cómo aplicar el subtotal a los datos y cómo cambiar la dirección de las filas de resumen del esquema debajo de Detalle.

 Puede aplicar el subtotal a los datos usando[**Hoja de trabajo.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) método. Toma los siguientes parámetros.

- **Área de celda** - El rango para aplicar el subtotal en
- **Agrupar por** - El campo por el que agrupar, como un desplazamiento de entero de base cero.
- **Función** - La función subtotal.
- **ListaTotal** Una matriz de compensaciones de campo de base cero, que indica los campos a los que se agregan los subtotales.
- **Reemplazar** - Indica si se reemplazan los subtotales actuales.
- **Saltos de página** - Indica si agregar salto de página entre grupos.
- **ResumenA continuaciónDatos** - Indica si agregar resumen debajo de los datos.

 Además, puedes controlar la dirección del contorno.**Filas de resumen debajo del detalle** como se muestra en la siguiente captura de pantalla usando la propiedad Worksheet.Outline.SummaryRowBelow. Puede abrir esta configuración en Microsoft Excel usando**Datos > Esquema > Configuración**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Imágenes de archivos fuente y de salida.

La siguiente captura de pantalla muestra el archivo Excel fuente utilizado en el código de muestra a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La siguiente captura de pantalla muestra el archivo Excel de salida generado por el código de muestra. Como puede ver, el subtotal se aplicó al rango A2:B11 y la dirección del esquema son las filas de resumen debajo de los detalles.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Código C# para aplicar el subtotal y cambiar la dirección de las filas del resumen del esquema

Aquí está el código de muestra para lograr el resultado que se muestra arriba.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
