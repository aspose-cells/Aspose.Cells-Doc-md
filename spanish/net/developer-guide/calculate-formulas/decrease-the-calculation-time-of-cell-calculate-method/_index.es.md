---
title: Reducir el tiempo de cálculo del método Cell.Calculate
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para reducir el tiempo de cálculo de los métodos de cálculo de celdas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar los métodos proporcionados por Aspose.Cells para optimizar el método de cálculo de celdas y mejorar su rendimiento. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, métodos de cálculo de celdas, optimización, rendimiento, reducción del tiempo de cálculo
type: docs
weight: 100
url: /es/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Escenarios de uso posibles**

Normalmente, recomendamos a los usuarios llamar al método [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) una vez y luego obtener los valores calculados de las celdas individuales. Pero a veces, los usuarios no desean calcular todo el libro. Solo desean calcular una celda. Aspose.Cells proporciona la propiedad [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive), que se puede establecer en **false** y disminuirá significativamente el tiempo de cálculo de la celda individual. Cuando la propiedad recursiva se establece en **true**, entonces todos los dependientes de las celdas se recalculan en cada llamada. Pero cuando la propiedad recursiva es **false**, las celdas dependientes se calculan solo una vez y no se vuelven a calcular en llamadas subsiguientes.

## **Reducir el tiempo de cálculo del método Cell.Calculate()**

El siguiente código de ejemplo ilustra el uso de la propiedad [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive). Por favor, ejecute este código con el archivo de Excel de ejemplo proporcionado y verifique su salida en la consola. Descubrirá que configurar la propiedad recursiva en **false** ha reducido significativamente el tiempo de cálculo. También lea los comentarios para comprender mejor esta propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Salida de la consola**

Esta es la salida en la consola del código de ejemplo anterior cuando se ejecuta con el archivo de Excel de ejemplo proporcionado en nuestra máquina. Tenga en cuenta que su salida puede ser diferente, pero el tiempo transcurrido después de establecer la propiedad recursiva en **false** siempre será menor que al establecerla en **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
