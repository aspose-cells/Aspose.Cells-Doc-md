---
title: Implementar un Motor de Cálculo Personalizado para extender el Motor de Cálculo Predeterminado de Aspose.Cells
type: docs
weight: 590
url: /es/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te brinda mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Implementar Motor de Cálculo Personalizado**
El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine), que tiene solo un método [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Este método se llama para todas tus fórmulas. Dentro de este método, capturamos la función **TODAY** y añadimos un día a la fecha del sistema. Por lo tanto, si la fecha actual es 27/07/2023, el motor personalizado calculará TODAY() como 28/07/2023.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Resultado**

Por favor revisa la salida de consola del código de muestra anterior, el valor (fecha y hora) de A1 con el motor personalizado debería ser un día después del resultado sin el motor personalizado.

### **Artículo Relacionado**
{{% alert color="primary" %}} 

- [Cálculo directo de una función personalizada sin escribirla en una hoja de cálculo](/cells/es/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
