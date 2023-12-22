---
title: Implementar un motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells
type: docs
weight: 590
url: /es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las Microsoft fórmulas de Excel. A pesar de esto, también le permite ampliar el motor de cálculo predeterminado, lo que le proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta característica.

- [Opciones de cálculo.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [ResumenCálculoMotor](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Datos de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Implementar motor de cálculo personalizado**
El siguiente código implementa el motor de cálculo personalizado. Implementa la interfaz[ResumenCálculoMotor](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) que tiene un solo método[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Este método se aplica a todas sus fórmulas. Dentro de este método, capturamos el**TODAY** función y agregar un día a la fecha del sistema. Entonces, si la fecha actual es 27/07/2023, el motor personalizado calculará HOY() como 28/07/2023.

###  **Muestra de programación**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Resultado**

Verifique la salida de la consola del código de muestra anterior, el valor (fecha y hora) de A1 con motor personalizado debe ser un día posterior al resultado sin motor personalizado.

###  **Artículo relacionado**
{{% alert color="primary" %}} 

- [Cálculo directo de una función personalizada sin escribirla en una hoja de trabajo](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
