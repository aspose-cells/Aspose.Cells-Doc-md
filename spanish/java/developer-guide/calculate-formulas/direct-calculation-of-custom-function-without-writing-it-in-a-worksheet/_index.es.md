---
title: Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo
type: docs
weight: 650
url: /es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

{{% alert color="primary" %}} 

Este artículo explica cómo puedes calcular directamente tus funciones personalizadas sin escribirlas primero en una hoja de cálculo. Utiliza el método [Worksheet.calculateFormula(string formula, CalculationOptions opts)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) para este propósito.

{{% /alert %}} 
## **Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo**
Por favor, consulta el siguiente código de ejemplo que ilustra el uso de este método. Hemos utilizado una función personalizada llamada *MyCompany.CustomFunction()* y calculamos su valor como "Aspose.Cells." por nosotros mismos y luego este valor se concatena automáticamente con el valor de la celda A1 que es "Bienvenido a " por el motor de cálculo, y el valor calculado final se devuelve como "Bienvenido a Aspose.Cells.". Como puedes ver en el código, no hemos escrito nuestra función personalizada en ninguna parte de una hoja de cálculo y se calcula directamente por nuestra propia lógica personalizada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Salida de la consola**
A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight java >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Artículo Relacionado**
{{% alert color="primary" %}} 

- [Implementar un motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
