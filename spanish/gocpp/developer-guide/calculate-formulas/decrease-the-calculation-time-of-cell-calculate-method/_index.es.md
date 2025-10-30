---
title: Reducir el tiempo de cálculo del método Cell.Calculate con Golang mediante C++
linktitle: Reducir el tiempo de cálculo de Cell.Calculate
description: Este artículo presenta cómo usar la biblioteca Aspose.Cells para reducir el tiempo de cálculo de los métodos de cálculo de celdas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar los métodos proporcionados por Aspose.Cells para optimizar el método de cálculo de celdas y mejorar su rendimiento. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, métodos de cálculo de celdas, optimización, rendimiento, reducción del tiempo de cálculo
type: docs
weight: 100
url: /es/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Escenarios de uso posibles**

Normalmente, recomendamos a los usuarios llamar al método [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) una vez y luego obtener los valores calculados de las celdas individuales. Pero a veces, los usuarios no quieren calcular todo el libro. Solo desean calcular una sola celda. Aspose.Cells proporciona la propiedad [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) que puedes establecer en **false** y eso reducirá significativamente el tiempo de cálculo de las celdas individuales. Porque cuando la propiedad recursiva está en **true**, todos los dependientes de las celdas se vuelven a calcular en cada llamada. Pero cuando la propiedad recursiva está en **false**, las celdas dependientes se Calculan solo una vez y no se vuelven a calcular en llamadas posteriores.

## **Reducir el tiempo de cálculo del método Cell.Calculate()**

El siguiente código de ejemplo ilustra el uso de la propiedad [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). Ejecuta este código con el [archivo de Excel de muestra](5113710.xlsx) y verifica su salida en consola. Verás que establecer la propiedad recursiva en **false** ha reducido significativamente el tiempo de cálculo. También lee los comentarios para una mejor comprensión de esta propiedad.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **Salida de la consola**

Esta es la salida de consola del código de ejemplo anterior cuando se ejecuta con el [archivo de Excel de muestra](5113710.xlsx) en nuestra máquina. Ten en cuenta que tu salida puede variar, pero el tiempo transcurrido después de establecer la propiedad recursiva en **false** siempre será menor que al establecerla en **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
