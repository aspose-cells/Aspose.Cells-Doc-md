---
title: Reducir el tiempo de cálculo del método Cell.Calculate
type: docs
weight: 860
url: /es/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Escenarios de uso posibles

Normalmente, recomendamos a los usuarios llamar al método [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) una vez y luego obtener los valores calculados de las celdas individuales. Pero a veces, los usuarios no quieren calcular todo el libro de trabajo. Solo quieren calcular una sola celda. Aspose.Cells proporciona la propiedad [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) la cual puedes establecer en **false** y disminuirá significativamente el tiempo de cálculo de la celda individual. Porque cuando la propiedad recursiva se establece en **true**, entonces todos los dependientes de las celdas se recalculan en cada llamada. Pero cuando la propiedad recursiva se establece en **false**, entonces las celdas dependientes se calculan una sola vez y no se vuelven a calcular en llamadas posteriores.
## **Reducir el tiempo de cálculo del método Cell.Calculate()**
El siguiente código de muestra ilustra el uso de la propiedad [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). Por favor, ejecuta este código con el [archivo de Excel de muestra](5472288.xlsx) dado y verifica su salida en la consola. Descubrirás que establecer la propiedad recursiva en **false** ha disminuido significativamente el tiempo de cálculo. Por favor, también lee los comentarios para una mejor comprensión de esta propiedad.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Salida de la consola**
Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](5472288.xlsx) en nuestra máquina. Por favor, ten en cuenta que tu salida puede ser diferente pero el tiempo transcurrido después de establecer la propiedad recursiva en **false** siempre será menor que si se estableciera en **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
