---
title: Implementar el motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells
type: docs
weight: 80
url: /es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Implementar motor de cálculo personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Excel Microsoft. A pesar de ello, también te permite ampliar el motor de cálculo predeterminado lo que te proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta característica.

- **[Opciones de cálculo.Motor personalizado](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[Motor de cálculo abstracto] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Datos de cálculo](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

El código siguiente implementa el motor de cálculo personalizado. Implementa la interfaz**[Motor de cálculo abstracto] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** que tiene un**[Calcular (datos de CalculationData)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** método. Este método se llama contra todas sus fórmulas. Dentro de este método, capturamos el**Suma** fórmula y aumenta su valor en 30. Entonces, si el valor calculado Aspose.Cells es 20, nuestro motor personalizado lo convertirá en 50 al agregar 30.

### **Ejemplo de programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Artículo relacionado**

{{% alert color="primary" %}}

[Cálculo directo de la función personalizada sin escribirla en una hoja de trabajo](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
