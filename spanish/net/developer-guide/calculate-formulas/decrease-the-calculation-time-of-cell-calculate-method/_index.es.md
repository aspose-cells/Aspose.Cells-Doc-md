---
title: Disminuya el tiempo de cálculo de Cell. Método de cálculo
description: Este artículo presenta cómo utilizar la biblioteca Aspose.Cells para reducir el tiempo de cálculo de los métodos de cálculo de celdas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar los métodos proporcionados por Aspose.Cells para optimizar el método de cálculo de la celda y mejorar su rendimiento. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /es/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **Posibles escenarios de uso**

Normalmente, recomendamos a los usuarios llamar[**Libro de trabajo.CalcularFórmula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)método una vez y luego obtenga los valores calculados de las celdas individuales. Pero a veces los usuarios no quieren calcular el libro completo. Sólo quieren calcular una sola celda. Aspose.Cells proporciona[**Opciones de cálculo.Recursivo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propiedad que puede establecer en**FALSO**y disminuirá significativamente el tiempo de cálculo de la celda individual. Porque cuando la propiedad recursiva se establece en *verdadero**, todos los dependientes de las celdas se recalculan en cada llamada. Pero cuando la propiedad recursiva es *falsa**, las celdas dependientes se calculan solo una vez y no se vuelven a calcular en llamadas posteriores.

##  **Disminuya el tiempo de cálculo del método Cell.Calculate()**

 El siguiente código de muestra ilustra el uso de[**Opciones de cálculo.Recursivo**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) propiedad. Por favor ejecute este código con el dado[archivo de excel de muestra](5113710.xlsx) y verifique la salida de su consola. Encontrará que establecer la propiedad recursiva en**FALSO**ha reducido significativamente el tiempo de cálculo. Lea también los comentarios para comprender mejor esta propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **Salida de consola**

 Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el comando dado[archivo de excel de muestra](5113710.xlsx) en nuestra máquina. Tenga en cuenta que su resultado puede diferir, pero el tiempo transcurrido después de configurar la propiedad recursiva en**FALSO**siempre será menor que establecerlo en *verdadero**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
