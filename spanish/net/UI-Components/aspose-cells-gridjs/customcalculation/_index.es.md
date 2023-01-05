---
title: Trabajar con un motor de cálculo personalizado para GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/customcalculation/
description: Este artículo describe cómo usar el motor de cálculo personalizado para la biblioteca Aspose.Cells.GridJs.
---
## **Implementar motor de cálculo personalizado**

Aspose.Cells.GridJs tiene un potente motor de cálculo que puede calcular casi todas las fórmulas Microsoft de Excel. A pesar de ello, también te permite ampliar el motor de cálculo predeterminado lo que te proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta función.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[Datos de cálculo de cuadrícula] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

El código siguiente implementa el motor de cálculo personalizado. Implementa la interfaz**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** que tiene un**[Calcular (datos de GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** método. Este método se llama contra todas sus fórmulas. Dentro de este método, capturamos el**MIFUNCIÓN DE PRUEBA** fórmula y multiplique por 2 el valor de su primer parámetro.

### **Ejemplo de programación**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
