---
title: Trabajar con motor de cálculo personalizado
type: docs
weight: 70
url: /es/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb,personalizado,cálculo,CalculationEngine,GridAbstractCalculationEngine
description: Este artículo describe cómo usar GridAbstractCalculationEngine para personalizar el proceso de cálculo en GridWeb.
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells.Gridweb tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también le permite extender el motor de cálculo predeterminado que le proporciona mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine) que tiene un método [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate). Este método se llama contra todas tus fórmulas. Dentro de este método, capturamos la fórmula **MYTESTFUNC** y la multiplicamos por 2 para su primer valor de parámetro.

### **Ejemplo de Programación**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

