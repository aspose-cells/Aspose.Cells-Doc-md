---
title: Interrumpir o cancelar el cálculo de la fórmula del libro de trabajo
description: Este artículo presenta cómo utilizar la biblioteca Aspose.Cells para interrumpir o cancelar cálculos de fórmulas de libros en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para interrumpir o cancelar el cálculo de la fórmula y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /es/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **Posibles escenarios de uso**

Aspose.Cells proporciona un mecanismo para interrumpir o cancelar el cálculo de la fórmula del libro de trabajo utilizando el[**ResumenCalculaciónMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)método. Esto es útil cuando el cálculo de la fórmula del libro de trabajo lleva demasiado tiempo y desea cancelar su procesamiento.

##  **Interrumpir o cancelar el cálculo de la fórmula del libro de trabajo**

El siguiente código de muestra implementa el[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)método de[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) clase. Dentro de este método, encuentra el nombre de la celda utilizando parámetros de índice de fila y columna. Si el nombre de la celda es B8, interrumpe el proceso de cálculo llamando al[**ResumenCalculaciónMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)método. Una vez, la clase concreta de[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)Se implementa la clase, su instancia se asigna a[**Opciones de cálculo.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)propiedad. Finalmente,[**Libro de trabajo.CalcularFórmula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)se llama pasando[**Opciones de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) como parámetro. Por favor vea el[archivo de Excel de muestra](51740731.xlsx) se utiliza dentro del código, así como en la salida de la consola del código que se proporciona a continuación como referencia.

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **Salida de consola**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
