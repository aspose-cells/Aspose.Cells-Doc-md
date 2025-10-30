---
title: Creando Subtotales
type: docs
weight: 800
url: /es/python-net/creating-subtotals/
description: Aprenda cómo crear subtotales para cualquier valor que se repita en una hoja de cálculo mediante el uso de la API Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, Aplicar Subtotales, Establecer Subtotales, Agregar subtotales, Crear subtotales, Cómo agregar subtotales a una hoja de cálculo 
---

{{% alert color="primary" %}}

Puede crear automáticamente subtotales para cualquier valor que se repita en una hoja de cálculo. Aspose.Cells for Python via .NET proporciona funciones de API que le ayudan a agregar subtotales a las hojas de cálculo programáticamente.

{{% /alert %}}

## **Usar Microsoft Excel**

Para agregar subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de cálculo del libro (como se muestra en la figura siguiente) y guarde el archivo como Libro1.xls.
1. Seleccione cualquier celda dentro de su lista.
1. Desde el menú **Datos**, seleccione **Subtotales**. Se mostrará el cuadro de diálogo Subtotales. Defina qué función usar y dónde colocar los subtotales.

## **Usando la API Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección de [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo y otros objetos. Cada hoja de cálculo consta de una colección de [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Para agregar subtotales a una hoja de cálculo, utilice el método [**subtotal**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list) de la clase [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Proporcione valores de parámetro al método para especificar cómo se debe calcular y ubicar el subtotal.

En los ejemplos a continuación, hemos agregado subtotales a la primera hoja de cálculo del archivo de plantilla (Libro1.xls) utilizando la API Aspose.Cells for Python via .NET. Cuando se ejecuta el código, se crea una hoja de cálculo con subtotales.

Los fragmentos de código que siguen muestran cómo agregar subtotales a una hoja de cálculo con Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CreatingSubtotals-1.py" >}}

## **Temas avanzados**
- [Aplicar Subtotal y Cambiar la Dirección de las Filas de Resumen del Contorno por debajo del Detalle](/cells/es/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
{{< app/cells/assistant language="python-net" >}}
