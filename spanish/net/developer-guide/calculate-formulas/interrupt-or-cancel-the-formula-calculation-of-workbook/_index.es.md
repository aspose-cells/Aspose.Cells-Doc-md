---
title: Interrumpir o cancelar el cálculo de fórmulas del libro de trabajo
type: docs
weight: 50
url: /es/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Posibles escenarios de uso**

Aspose.Cells proporciona un mecanismo para interrumpir o cancelar el cálculo de fórmulas del libro de trabajo utilizando el[**ResumenCálculoMonitor.Interrupción()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)método. Esto es útil cuando el cálculo de la fórmula del libro de trabajo lleva demasiado tiempo y desea cancelar su procesamiento.

## **Interrumpir o cancelar el cálculo de fórmulas del libro de trabajo**

El siguiente código de ejemplo implementa el[**AntesCalcular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)método de[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) clase. Dentro de este método, encuentra el nombre de la celda usando parámetros de índice de fila y columna. Si el nombre de la celda es B8, interrumpe el proceso de cálculo llamando al[**ResumenCálculoMonitor.Interrupción()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)método. Una vez, la clase concreta de[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)se implementa la clase, su instancia se asigna a[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)propiedad. Finalmente,[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)se llama de paso[**Opciones de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) como parámetro. Por favor vea el[ejemplo de archivo de Excel](51740731.xlsx)utilizado dentro del código, así como la salida de la consola del código que se proporciona a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
