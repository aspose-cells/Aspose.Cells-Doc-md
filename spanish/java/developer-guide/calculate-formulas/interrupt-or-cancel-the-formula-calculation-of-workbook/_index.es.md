---
title: Interrumpir o Cancelar el Cálculo de Fórmulas de una Hoja de Cálculo
type: docs
weight: 30
url: /es/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona un mecanismo para interrumpir o cancelar el cálculo de fórmulas del libro de trabajo mediante el método interrupt() de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Esto es útil cuando el cálculo de fórmulas del libro de trabajo está tardando demasiado tiempo y deseas cancelar su procesamiento.

## **Interrumpir o cancelar el cálculo de fórmulas de una hoja de cálculo**

El siguiente código de ejemplo implementa el método [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Dentro de este método, encuentra el nombre de la celda utilizando los parámetros de índice de fila y columna. Si el nombre de la celda es B8, interrumpe el proceso de cálculo llamando al método AbstractCalculationMonitor.interrupt(). Una vez que se implementa la clase concreta de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor), se asigna su instancia a la propiedad [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor). Finalmente, se llama a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) pasando [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) como parámetro. Consulta el [archivo de Excel de ejemplo](51740744.xlsx) utilizado en el código, así como la salida de consola del código que se muestra a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Salida de la consola**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
