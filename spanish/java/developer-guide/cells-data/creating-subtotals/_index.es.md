---
title: Creando Subtotales
type: docs
weight: 50
url: /es/java/creating-subtotals/
---

{{% alert color="primary" %}}

Puede crear automáticamente subtotales para cualquier valor repetido en una hoja de cálculo. Aspose.Cells proporciona funciones de API que le ayudan a agregar subtotales a las hojas de cálculo de forma programática.

{{% /alert %}}

## **Usar Microsoft Excel**

Para crear subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de cálculo del libro (como se muestra en la figura siguiente) y guarde el archivo como Libro1.xls.
1. Seleccione cualquier celda dentro de su lista.
1. Desde el menú **Datos**, seleccione **Subtotales**.
   Se muestra el cuadro de diálogo Subtotales. Defina qué función utilizar y dónde colocar los subtotales.

   **Seleccionar un rango de datos para agregar subtotales**

![todo:image_alt_text](creating-subtotals_1.png)

**El cuadro de diálogo Subtotal** 

![todo:image_alt_text](creating-subtotals_2.png)

## **Uso de la API de Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo y otros objetos. Cada hoja de cálculo consta de una colección de [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Para crear subtotales en una hoja de cálculo, utilice el método de subtotal de la clase [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Proporcione valores apropiados para los parámetros del método para obtener el resultado deseado.

El siguiente ejemplo muestra cómo crear subtotales en la primera hoja de cálculo del archivo de plantilla (Libro1.xls) utilizando Aspose.Cells API.

Cuando se ejecuta el código, se crea una hoja de cálculo con subtotales.

**Aplicando subtotales** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
{{< app/cells/assistant language="java" >}}
