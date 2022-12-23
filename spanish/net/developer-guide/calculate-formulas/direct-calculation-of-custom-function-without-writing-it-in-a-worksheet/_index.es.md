---
title: Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo
type: docs
weight: 90
url: /es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
## **Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo**

 Este tema explica cómo puede calcular directamente sus funciones personalizadas sin escribirlas primero en una hoja de trabajo. Por favor use el[**Worksheet.CalculateFormula (fórmula de cadena, Opciones de cálculo opta)**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)método para este propósito.

Consulte el siguiente código de ejemplo que ilustra el uso de este método. Hemos utilizado una función personalizada llamada MyCompany.CustomFunction() y calculamos su valor como "Aspose.Cells". por nosotros mismos y luego este valor se concatena automáticamente con el valor de la celda A1 que es "Bienvenido a" por el motor de cálculo y el valor final calculado regresa como "Bienvenido a Aspose.Cells". Como puede ver en un código que tenemos no está escrita nuestra función personalizada en ninguna parte de una hoja de trabajo y se calcula directamente mediante nuestra propia lógica personalizada.

### **Ejemplo de programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.cs" >}}

### **Salida de consola**

A continuación se muestra la salida de la consola del código de ejemplo anterior.

{{< highlight "java" >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Artículo relacionado**

{{% alert color="primary" %}}

[Implementar el motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells](/cells/es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
