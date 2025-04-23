---
title: Creando Subtotales
type: docs
weight: 800
url: /es/nodejs-cpp/creating-subtotals/
description: Aprende cómo crear subtotales para cualquier valor repetido en una hoja de cálculo utilizando la API Aspose.Cells for Node.js via C++.
keywords: Aplicar subtotales, Establecer subtotales, Agregar subtotales, Crear subtotales, Cómo agregar subtotales a una hoja de cálculo 
---

{{% alert color="primary" %}}

Puedes crear automáticamente subtotales para cualquier valor repetido en una hoja de cálculo. La API Aspose.Cells for Node.js via C++ proporciona funciones de API que te ayudan a agregar subtotales a las hojas de cálculo de manera programática.

{{% /alert %}}

## **Usar Microsoft Excel**

Para agregar subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de cálculo del libro (como se muestra en la figura siguiente) y guarde el archivo como Libro1.xls.
1. Seleccione cualquier celda dentro de su lista.
1. Desde el menú **Datos**, seleccione **Subtotales**. Se mostrará el cuadro de diálogo Subtotales. Defina qué función usar y dónde colocar los subtotales.

## **Usando la API Aspose.Cells for Node.js via C++**

La Aspose.Cells for Node.js via C++ proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo y otros objetos. Cada hoja de cálculo consta de una colección de [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Para agregar subtotales a una hoja de cálculo, utilice el método [**subtotal**](https://reference.aspose.com/cells/nodejs-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) de la clase [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Proporcione valores de parámetro al método para especificar cómo se debe calcular y ubicar el subtotal.

En los ejemplos a continuación, hemos añadido subtotales a la primera hoja del [archivo de plantilla](book1.xlsx) usando la API Aspose.Cells for Node.js via C++. Cuando se ejecuta el código, se crea una hoja de cálculo con subtotales.

Los fragmentos de código que siguen muestran cómo añadir subtotales a una hoja de cálculo con Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CreatingSubtotals-1.js" >}}

