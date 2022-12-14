---
title: Implementar el motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells
type: docs
weight: 590
url: /es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Excel Microsoft. A pesar de ello, también te permite ampliar el motor de cálculo predeterminado lo que te proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta característica.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [ResumenCálculoMotor](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementar motor de cálculo personalizado**
El código siguiente implementa el motor de cálculo personalizado. Implementa la interfaz[ResumenCálculoMotor](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) que tiene un solo método[calcular (datos de datos de cálculo)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Este método se llama contra todas sus fórmulas. Dentro de este método, capturamos el**SUMA** fórmula y aumenta su valor en 30. Entonces, si el valor calculado Aspose.Cells es 20, nuestro motor personalizado lo convertirá en 50 al agregar 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Artículo relacionado**
{{% alert color="primary" %}} 

- [Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
