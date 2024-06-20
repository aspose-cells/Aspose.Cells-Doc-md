---
title: Creando Subtotales
type: docs
weight: 800
url: /es/net/creating-subtotals/
description: Aprende a crear subtotales para cualquier valor repetido en una hoja de cálculo utilizando la API Aspose.Cells for .NET.
keywords: Aplicar subtotales, Establecer subtotales, Agregar subtotales, Crear subtotales, Cómo agregar subtotales a una hoja de cálculo 
---

{{% alert color="primary" %}}

Puedes crear automáticamente subtotales para cualquier valor que se repita en una hoja de cálculo. Aspose.Cells proporciona funciones de API que te ayudan a agregar subtotales a las hojas de cálculo de forma programática.

{{% /alert %}}

## **Usar Microsoft Excel**

Para agregar subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de cálculo del libro (como se muestra en la figura siguiente) y guarde el archivo como Libro1.xls.
1. Seleccione cualquier celda dentro de su lista.
1. Desde el menú **Datos**, seleccione **Subtotales**. Se mostrará el cuadro de diálogo Subtotales. Defina qué función usar y dónde colocar los subtotales.

## **Usando la API de Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo y otros objetos. Cada hoja de cálculo consta de una colección de [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Para agregar subtotales a una hoja de cálculo, utilice el método [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Proporcione valores de parámetro al método para especificar cómo se debe calcular y ubicar el subtotal.

En los ejemplos a continuación, hemos agregado subtotales a la primera hoja de trabajo del archivo de plantilla (Libro1.xls) utilizando la API de Aspose.Cells. Cuando se ejecuta el código, se crea una hoja de trabajo con subtotales.

Los fragmentos de código que se muestran a continuación muestran cómo agregar subtotales a una hoja de trabajo con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-CreatingSubtotals-1.cs" >}}

## **Temas avanzados**
- [Aplicar Subtotal y Cambiar la Dirección de las Filas de Resumen del Contorno por debajo del Detalle](/cells/es/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
