---
title: Implementar un motor de cálculo personalizado para ampliar el motor de cálculo predeterminado de Aspose.Cells con Golang mediante C++
linktitle: Implementar motor de cálculo personalizado
description: Este artículo describe cómo ampliar el motor de cálculo predeterminado implementando un motor de cálculo personalizado usando la biblioteca Aspose.Cells con Golang mediante C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para implementar un motor de cálculo personalizado y obtener los resultados. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, motor de cálculo personalizado, extiende el motor de cálculo predeterminado, C++
type: docs
weight: 80
url: /es/go-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te brinda mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/go-cpp/calculationdata/)

El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/) que tiene un método [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/calculate/). Este método se llama para todas tus fórmulas. Dentro de este método, capturamos la función **TODAY** y añadimos un día a la fecha del sistema. Así que si la fecha actual es 27/07/2023, entonces el motor personalizado calculará TODAY() como 28/07/2023.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomCalculationEngineToExtendTheDefaultCalculationEngineOfAsposeCells.go" >}}
### **Resultado**

Por favor revisa la salida de consola del código de muestra anterior, el valor (fecha y hora) de A1 con el motor personalizado debería ser un día después del resultado sin el motor personalizado.

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Cálculo directo de función personalizada sin escribirla en una hoja de cálculo](/cells/es/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
