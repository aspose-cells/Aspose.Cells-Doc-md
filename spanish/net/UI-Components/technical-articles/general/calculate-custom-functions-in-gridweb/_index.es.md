---
title: Calcular funciones personalizadas en GridWeb
type: docs
weight: 90
url: /es/net/calculate-custom-functions-in-gridweb/
---
## **Posibles escenarios de uso**
Aspose.Cells.GridWeb admite el cálculo de funciones personalizadas con la propiedad GridWeb.CustomCalculationEngine. Esta propiedad toma la instancia de la interfaz GridAbstractCalculationEngine. Implemente la interfaz GridAbstractCalculationEngine y calcule sus funciones personalizadas con su propia lógica.
## **Calcular funciones personalizadas en GridWeb**
El siguiente código de ejemplo agrega una función personalizada denominada MYTESTFUNC() en la celda B3. Luego calculamos el valor de esta función implementando la interfaz GridAbstractCalculationEngine. Calculamos MYTESTFUNC() de tal manera que multiplique su parámetro por 2 y devuelva el resultado. Entonces, si su parámetro es 9, devolverá 2*9 = 18.
### **Código de muestra**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
