---
title: Reduzca el tiempo de cálculo de Cell. Método de cálculo
type: docs
weight: 100
url: /es/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Posibles escenarios de uso**

Normalmente, recomendamos a los usuarios que llamen[**Libro de trabajo. Calcular fórmula ()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)método una vez y luego obtenga los valores calculados de las celdas individuales. Pero a veces, los usuarios no quieren calcular todo el libro de trabajo. Solo quieren calcular una sola celda. Aspose.Cells proporciona[**CalculationOptions.Recursivo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propiedad que puede establecer en**falso** y disminuirá significativamente el tiempo de cálculo de la celda individual. Porque cuando la propiedad recursiva se establece en**verdadero** , luego todos los dependientes de las celdas se vuelven a calcular en cada llamada. Pero cuando la propiedad recursiva es**falso**, las celdas dependientes se calculan solo una vez y no se vuelven a calcular en llamadas posteriores.

## **Reduzca el tiempo de cálculo del método Cell.Calculate()**

 El siguiente código de ejemplo ilustra el uso de[**CalculationOptions.Recursivo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propiedad. Por favor, ejecute este código con el dado[ejemplo de archivo de Excel](5113710.xlsx) y verifique su salida de consola. Encontrará que establecer la propiedad recursiva en**falso**ha disminuido significativamente el tiempo de cálculo. Lea también los comentarios para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Salida de consola**

 Esta es la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[ejemplo de archivo de Excel](5113710.xlsx) en nuestra máquina. Tenga en cuenta que su salida puede diferir, pero el tiempo transcurrido después de establecer la propiedad recursiva en**falso** siempre será menor que establecerlo en**verdadero**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
