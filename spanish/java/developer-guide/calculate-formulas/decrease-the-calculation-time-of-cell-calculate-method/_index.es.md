---
title: Reduzca el tiempo de cálculo de Cell. Método de cálculo
type: docs
weight: 860
url: /es/java/decrease-the-calculation-time-of-cell-calculate-method/
---
Posibles escenarios de uso

 Normalmente, recomendamos a los usuarios que llamen[Libro de trabajo. Calcular fórmula ()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) una vez y luego obtenga los valores calculados de las celdas individuales. Pero a veces, los usuarios no quieren calcular todo el libro de trabajo. Solo quieren calcular una sola celda. Aspose.Cells proporciona[CalculationOptions.Recursivo](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) propiedad que puede establecer**falso**y disminuirá significativamente el tiempo de cálculo de la celda individual. Porque cuando la propiedad recursiva se establece en**verdadero**luego todos los dependientes de las celdas se vuelven a calcular en cada llamada. Pero cuando la propiedad recursiva se establece en**falso**, las celdas dependientes se calculan solo una vez y no se vuelven a calcular en llamadas posteriores.
## **Reduzca el tiempo de cálculo del método Cell.Calculate()**
 El siguiente código de ejemplo ilustra el uso de[CalculationOptions.Recursivo](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) propiedad. Por favor, ejecute este código con el dado[ejemplo de archivo de Excel](5472288.xlsx) y verifique su salida de consola. Encontrará que establecer la propiedad recursiva en**falso**ha disminuido significativamente el tiempo de cálculo. Lea también los comentarios para una mejor comprensión de esta propiedad.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Salida de consola**
 Esta es la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[ejemplo de archivo de Excel](5472288.xlsx) en nuestra máquina. Tenga en cuenta que su salida puede diferir, pero el tiempo transcurrido después de establecer la propiedad recursiva en**falso** siempre será menor que establecerlo en**verdadero**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
