---
title: Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo
description: Este artículo introduce cómo usar la biblioteca Aspose.Cells para calcular directamente funciones personalizadas en Microsoft Excel sin escribir la función en una hoja de cálculo. Al cargar un archivo existente de Excel o crear un nuevo archivo de Excel, podemos usar los métodos proporcionados por Aspose.Cells para calcular la función personalizada y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones personalizadas, cálculos directos, sin necesidad de escribir, hojas de cálculo
type: docs
weight: 90
url: /es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo**

Este tema explica cómo puedes calcular directamente tus funciones personalizadas sin escribirlas primero en una hoja de cálculo. Por favor, utiliza el método [**Worksheet.CalculateFormula(string formula, CalculationOptions opts)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) para este propósito.

Por favor, consulta el siguiente código de muestra que ilustra el uso de este método. Hemos utilizado una función personalizada llamada MyCompany.CustomFunction() y calculamos su valor como "Aspose.Cells." por nosotros mismos y luego este valor se concatena automáticamente con el valor de la celda A1 que es "Bienvenido a " por el motor de cálculo y el valor calculado final retorna como "Bienvenido a Aspose.Cells.". Como se puede ver en un código, no hemos escrito nuestra función personalizada en ninguna hoja de cálculo y se calcula directamente por nuestra lógica personalizada.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Salida de la consola**

A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Implementar un Motor de Cálculo Personalizado para extender el Motor de Cálculo Predeterminado de Aspose.Cells](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
