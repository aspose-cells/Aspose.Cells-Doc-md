---
title: Aplicar subtotal y cambiar dirección de resumen de contorno de filas debajo del detalle
type: docs
weight: 100
url: /es/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Aprende cómo aplicar un subtotal y cambiar la dirección de las filas de resumen del esquema debajo del detalle utilizando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Aplicar subtotal, Agregar subtotal, cambiar la dirección de las filas de resumen del esquema debajo del detalle, cambiar la dirección de las columnas de resumen del esquema a la derecha del detalle, Crear un subtotal y cambiar la dirección de las filas de resumen del esquema debajo del detalle
---

{{% alert color="primary" %}}

Este artículo explicará cómo aplicar un subtotal a los datos y cambiar la dirección de las filas de resumen de contorno debajo del detalle.

Puede aplicar un subtotal a los datos usando el método [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool). Toma los siguientes parámetros.

- **ca** - El rango en el que aplicar el subtotal
- **group_by** - El campo por el cual agrupar, como un desplazamiento entero basado en cero
- **function** - La función de subtotal.
- **total_list** - Un array de desplazamientos de campo basados en cero, indicando los campos a los cuales se agregan los subtotales.
- **replace** - Indica si reemplazar los subtotales actuales
- **page_breaks** - Indica si agregar salto de página entre grupos
- **summary_below_data** - Indica si agregar el resumen debajo de los datos.

Además, puede controlar la dirección de las **filas de resumen de contorno debajo del detalle** como se muestra en la siguiente captura de pantalla utilizando la propiedad Worksheet.Outline.SummaryRowBelow. Puede abrir esta configuración en Microsoft Excel usando **Datos > Contorno > Configuración**

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Imágenes de los archivos de origen y salida**

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación, que contiene algunos datos en las columnas A y B.

![todo:image_alt_text](2.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de ejemplo. Como se puede ver, se ha aplicado un subtotal al rango A2:B11 y la dirección del contorno es resumen de filas debajo del detalle.

![todo:image_alt_text](3.png)

## **Código Python para aplicar subtotal y cambiar la dirección de las filas de resumen del esquema**

Aquí está el código de ejemplo para lograr el resultado mostrado anteriormente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
