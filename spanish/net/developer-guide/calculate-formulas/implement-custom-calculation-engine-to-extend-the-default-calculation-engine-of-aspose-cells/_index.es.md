---
title: Implementar un Motor de Cálculo Personalizado para extender el Motor de Cálculo Predeterminado de Aspose.Cells
description: Este artículo describe cómo extender el motor de cálculo predeterminado mediante la implementación de un motor de cálculo personalizado utilizando la biblioteca Aspose.Cells. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar los métodos proporcionados por Aspose.Cells para implementar un motor de cálculo personalizado y obtener los resultados. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, Motor de Cálculo Personalizado, extiende el motor de cálculo predeterminado
type: docs
weight: 80
url: /es/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te brinda mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.

- [**CalculationOptions.CustomEngine**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/net/aspose.cells/calculationdata)

El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) que tiene un método [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate). Este método se llama para todas tus fórmulas. Dentro de este método, capturamos la función **TODAY** y añadimos un día a la fecha del sistema. Así que si la fecha actual es 27/07/2023, entonces el motor personalizado calculará TODAY() como 28/07/2023.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Resultado**

Por favor revisa la salida de consola del código de muestra anterior, el valor (fecha y hora) de A1 con el motor personalizado debería ser un día después del resultado sin el motor personalizado.

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Cálculo directo de función personalizada sin escribirla en una hoja de cálculo](/cells/es/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
