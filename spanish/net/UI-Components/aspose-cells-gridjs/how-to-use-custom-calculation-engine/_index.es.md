---
title: Trabajar con motor de cálculo personalizado para GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: Este artículo describe cómo utilizar el motor de cálculo personalizado para la biblioteca Aspose.Cells.GridJs.
aliases:
  - /net/aspose-cells-gridjs/customcalculation/
  - /net/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells.GridJs tiene un poderoso motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te proporciona mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine) que tiene un método [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). Este método se llama contra todas tus fórmulas. Dentro de este método, capturamos la fórmula **MYTESTFUNC** y la multiplicamos por 2 para su primer valor de parámetro.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

