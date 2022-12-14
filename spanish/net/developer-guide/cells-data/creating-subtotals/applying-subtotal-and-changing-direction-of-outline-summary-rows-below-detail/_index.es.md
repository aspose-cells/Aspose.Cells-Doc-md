---
title: Aplicar subtotal y cambiar la dirección de las filas de resumen del esquema debajo del detalle
type: docs
weight: 100
url: /es/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Este artículo explicará cómo aplicar el subtotal a los datos y cómo cambiar la dirección de las filas de resumen del esquema debajo del detalle.

 Puede aplicar Subtotal a los datos usando[**Hoja de trabajo.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) método. Toma los siguientes parámetros.

- **área de celda** - El rango para aplicar el subtotal en
- **Agrupar por** - El campo por el que agrupar, como un desplazamiento de entero basado en cero
- **Función** - La función de subtotal.
- **ListaTotal** - Una matriz de compensaciones de campo de base cero, que indica los campos a los que se agregan los subtotales.
- **Reemplazar** - Indica si reemplaza los subtotales actuales
- **Saltos de página** - Indica si agregar salto de página entre grupos
- **Resumen debajo de los datos** - Indica si se añade resumen debajo de los datos.

 Además, puede controlar la dirección del contorno**Filas de resumen debajo del detalle** como se muestra en la siguiente captura de pantalla usando la propiedad Worksheet.Outline.SummaryRowBelow. Puede abrir esta configuración en Microsoft Excel usando**Datos > Esquema > Configuración**

![todo:imagen_alternativa_texto](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Imágenes de archivos fuente y de salida.

La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:imagen_alternativa_texto](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La siguiente captura de pantalla muestra el archivo de salida de Excel generado por el código de muestra. Como puede ver, el subtotal se aplicó al rango A2:B11 y la dirección del contorno es filas de resumen debajo del detalle.

![todo:imagen_alternativa_texto](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## C# código para aplicar el subtotal y cambiar la dirección de las filas de resumen del esquema

Aquí está el código de muestra para lograr el resultado como se muestra arriba.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
