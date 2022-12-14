---
title: Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo
type: docs
weight: 650
url: /es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---
{{% alert color="primary" %}} 

 Este artículo explica cómo puede calcular directamente sus funciones personalizadas sin escribirlas primero en una hoja de trabajo. Por favor use el[Worksheet.calculateFormula (fórmula de cadena, Opciones de cálculo opta)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula\(java.lang.String,%20com.aspose.cells.CalculationOptions\)) método para este propósito.

{{% /alert %}} 
## **Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo**
Consulte el siguiente código de ejemplo que ilustra el uso de este método. Hemos utilizado una función personalizada llamada*MiEmpresa.FunciónPersonalizada()*calculamos su valor como "Aspose.Cells". por nosotros mismos y luego este valor se concatena automáticamente con el valor de la celda A1 que es "Bienvenido a" por el motor de cálculo y el valor final calculado regresa como "Bienvenido a Aspose.Cells". Como puede ver en un código, no hemos escrito nuestra función personalizada en ninguna parte de una hoja de trabajo y se calcula directamente mediante nuestra propia lógica personalizada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementDirectCalculationOfCustomFunction-ImplementDirectCalculationOfCustomFunction.java" >}}
## **Salida de consola**
A continuación se muestra la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}
## **Artículo relacionado**
{{% alert color="primary" %}} 

- [Implementar el motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells](/cells/es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
