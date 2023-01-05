---
title: Interrumpir o cancelar el cálculo de fórmulas del libro de trabajo
type: docs
weight: 30
url: /es/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Posibles escenarios de uso**

Aspose.Cells proporciona un mecanismo para interrumpir o cancelar el cálculo de la fórmula del libro utilizando el método interrupt() del[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) clase. Esto es útil cuando el cálculo de la fórmula del libro de trabajo lleva demasiado tiempo y desea cancelar su procesamiento.

## **Interrumpir o cancelar el cálculo de fórmulas del libro de trabajo**

El siguiente código de ejemplo implementa el[**antes de Calcular ()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) método de la[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)clase. Dentro de este método, encuentra el nombre de la celda usando parámetros de índice de fila y columna. Si el nombre de la celda es B8, interrumpe el proceso de cálculo llamando al método AbstractCalculationMonitor.interrupt(). Una vez, la clase concreta de[**ResumenCálculoMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)se implementa la clase, su instancia se asigna a[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)propiedad. Finalmente,[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) se llama pasando[**Opciones de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)como parámetro. Por favor vea el[ejemplo de archivo de Excel](51740744.xlsx)utilizado dentro del código, así como la salida de la consola del código que se proporciona a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
