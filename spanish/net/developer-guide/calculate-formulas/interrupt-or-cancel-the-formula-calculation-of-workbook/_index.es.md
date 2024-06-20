---
title: Interrumpir o Cancelar el Cálculo de Fórmulas de una Hoja de Cálculo
description: Este artículo presenta cómo usar la librería Aspose.Cells para interrumpir o cancelar el cálculo de fórmulas en libros de trabajo en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para interrumpir o cancelar el cálculo de fórmulas y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, libros de trabajo, cálculos de fórmulas, interrupciones, cancelaciones
type: docs
weight: 50
url: /es/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona un mecanismo para interrumpir o cancelar el cálculo de fórmulas de un libro de trabajo usando el método [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Esto es útil cuando el cálculo de fórmulas de un libro de trabajo lleva demasiado tiempo y deseas cancelar su procesamiento.

## **Interrumpir o cancelar el cálculo de fórmulas de una hoja de cálculo**

El siguiente código de muestra implementa el método [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). Dentro de este método, encuentra el nombre de la celda usando parámetros de índice de fila y columna. Si el nombre de la celda es B8, interrumpe el proceso de cálculo llamando al método [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Una vez que se implementa la clase concreta de la clase [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor), su instancia se asigna a la propiedad [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor). Finalmente, se llama a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) pasando [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) como parámetro. Consulta también el [archivo de Excel de muestra](51740731.xlsx) utilizado dentro del código, así como la salida de consola del código proporcionado a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
