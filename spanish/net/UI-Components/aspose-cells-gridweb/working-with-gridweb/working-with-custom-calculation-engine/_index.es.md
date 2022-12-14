---
title: Trabajar con un motor de cálculo personalizado
type: docs
weight: 70
url: /es/net/working-with-custom-calculation-engine/
---
## **Implementar motor de cálculo personalizado**

Aspose.Cells.Gridweb tiene un potente motor de cálculo que puede calcular casi todas las fórmulas Microsoft de Excel. A pesar de ello, también te permite ampliar el motor de cálculo predeterminado lo que te proporciona mayor potencia y flexibilidad.

Las siguientes propiedades y clases se utilizan para implementar esta característica.

 
- **[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

El código siguiente implementa el motor de cálculo personalizado. Implementa la interfaz**[GridAbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** que tiene un**[Calcular (datos de GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** método. Este método se llama contra todas sus fórmulas. Dentro de este método, capturamos el**MIFUNCIÓN DE PRUEBA** fórmula y multiplique por 2 el valor de su primer parámetro.

### **Ejemplo de programación**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

