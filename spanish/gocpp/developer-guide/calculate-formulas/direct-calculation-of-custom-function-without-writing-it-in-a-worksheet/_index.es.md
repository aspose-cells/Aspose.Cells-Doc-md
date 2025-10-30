---
title: Cálculo directo de funciones personalizadas sin escribirlas en una hoja de cálculo con Golang mediante C++
linktitle: Cálculo directo de función personalizada
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para calcular directamente funciones personalizadas en Microsoft Excel sin escribir la función en una hoja de cálculo. Al cargar un archivo existente de Excel o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para calcular la función personalizada y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones personalizadas, cálculos directos, sin necesidad de escribir, hojas de cálculo
type: docs
weight: 90
url: /es/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Cálculo directo de función personalizada sin escribirla en una hoja de cálculo**

Este tema explica cómo puedes calcular directamente tus funciones personalizadas sin escribirlas primero en una hoja de cálculo. Por favor, usa el método [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/) para este propósito.

Consulta el siguiente código de ejemplo que ilustra el uso de este método. Hemos utilizado una función personalizada llamada MyCompany::CustomFunction() y calculamos su valor como "Aspose.Cells." y luego este valor se concatena automáticamente con el valor de la celda A1, que es "Bienvenido a " por el motor de cálculo, y el valor final calculado regresa como "Bienvenido a Aspose.Cells.". Como puedes ver en el código, no hemos escrito nuestra función personalizada en ninguna hoja de cálculo y se calcula directamente mediante nuestra lógica personalizada.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **Salida de la consola**

A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Implementar motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
