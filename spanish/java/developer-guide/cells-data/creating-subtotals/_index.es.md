---
title: Creación de subtotales
type: docs
weight: 50
url: /es/java/creating-subtotals/
---
{{% alert color="primary" %}}

Puede crear automáticamente subtotales para cualquier valor repetido en una hoja de cálculo. Aspose.Cells proporciona características de API que lo ayudan a agregar subtotales a las hojas de cálculo mediante programación.

{{% /alert %}}

## **Usando Microsoft Excel**

Para crear subtotales en Microsoft Excel:

1. Cree una lista de datos simple en la primera hoja de trabajo del libro de trabajo (como se muestra en la figura a continuación) y guarde el archivo como Book1.xls.
1. Seleccione cualquier celda dentro de su lista.
1.  Desde el**Datos** menú, seleccione**subtotales**.
 Se muestra el cuadro de diálogo Subtotales. Defina qué función utilizar y dónde colocar los subtotales.

   **Seleccionar un rango de datos para agregar subtotales**

![todo:imagen_alternativa_texto](creating-subtotals_1.png)

**El cuadro de diálogo Subtotal** 

![todo:imagen_alternativa_texto](creating-subtotals_2.png)

## **Usando Aspose.Cells API**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. Él[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de trabajo y otros objetos. Cada hoja de trabajo consta de un[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Para crear subtotales en una hoja de trabajo, use el[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)método subtotal de la clase. Proporcione valores apropiados para los parámetros del método para obtener el resultado que desea.

El siguiente ejemplo muestra cómo crear subtotales en la primera hoja de trabajo del archivo de plantilla (Book1.xls) usando Aspose.Cells API.

Cuando se ejecuta el código, se crea una hoja de cálculo con subtotales.

**Aplicar subtotales** 

![todo:imagen_alternativa_texto](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
