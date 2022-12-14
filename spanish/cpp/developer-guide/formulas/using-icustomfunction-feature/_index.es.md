---
title: Uso de la función ICustomFunction
type: docs
weight: 20
url: /es/cpp/using-icustomfunction-feature/
---
## **Introducción**
Este artículo proporciona información sobre cómo usar la función ICustomFunction para implementar funciones personalizadas con las API Aspose.Cells.

La interfaz ICustomFunction le permite agregar funciones de cálculo de fórmulas personalizadas para ampliar el motor de cálculo central Aspose.Cells para cumplir con ciertos requisitos. Esta característica es útil para definir funciones personalizadas (definidas por el usuario) en un archivo de plantilla o en un código donde la función personalizada se puede implementar y evaluar utilizando las API Aspose.Cells como cualquier otra función de Excel predeterminada Microsoft.
## **Uso de la función ICustomFunction**
El siguiente código de ejemplo implementa la interfaz ICustomFunction que evalúa y devuelve los valores de las dos funciones personalizadas, es decir, MySampleFunc() y YourSampleFunc(). Estas funciones personalizadas están dentro de las celdas A1 y A2 respectivamente. Luego llama al método IWorkbook.CalculateFormula(false, ICustomFunction) para invocar la implementación del método ICustomFunction.CalculateCustomFunction(). Luego, imprime los valores de A1 y A2 en la consola, que en realidad son los valores devueltos por ICustomFunction.CalculateCustomFunction(). Consulte el resultado de la consola del código de muestra a continuación para obtener más ayuda.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Salida de consola**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
