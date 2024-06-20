---
title: Usar la función AbstractCalculationEngine
type: docs
weight: 20
url: /es/cpp/using-abstractcalculationengine-feature/
---

## Las características aún están en desarrollo, así que manténgase atento.


## **Introducción**
Este artículo proporciona una comprensión de cómo utilizar la función [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) para implementar funciones personalizadas con las API de Aspose.Cells.

<!--

La interfaz AbstractCalculationEngine le permite agregar funciones de cálculo de fórmulas personalizadas para extender el motor de cálculo principal de Aspose.Cells a fin de cumplir con ciertos requisitos. Esta característica es útil para definir funciones personalizadas (definidas por el usuario) en un archivo de plantilla o en un código donde la función personalizada puede implementarse y evaluarse utilizando las API de Aspose.Cells como cualquier otra función predeterminada de Microsoft Excel.
## **Usar la función AbstractCalculationEngine**
El siguiente código de muestra implementa la interfaz AbstractCalculationEngine que evalúa y devuelve los valores de las dos funciones personalizadas, es decir, MySampleFunc() y YourSampleFunc(). Estas funciones personalizadas están dentro de las celdas A1 y A2 respectivamente. Luego, llama al método Workbook.CalculateFormula(const CalculationOptions& options) para invocar la implementación de la función AbstractCalculationEngine.Calculate(CalculationData& data). Luego, imprime los valores de A1 y A2 en la consola. Consulte la Salida de la consola del código de muestra a continuación para obtener más ayuda.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **Salida de la consola**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
