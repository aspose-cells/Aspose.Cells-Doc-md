---
title: Calcular funciones personalizadas en GridWeb
type: docs
weight: 90
url: /es/net/aspose-cells-gridweb/calculate-custom-functions-in-gridweb/
keywords: GridWeb,custom functions,custom,function
description: Este artículo presenta las características de las funciones personalizadas en GridWeb.
---


## **Escenarios de uso posibles**
Aspose.Cells.GridWeb admite el cálculo de funciones personalizadas con la propiedad GridWeb.CustomCalculationEngine. Esta propiedad toma la instancia de la interfaz GridAbstractCalculationEngine. Por favor implementa la interfaz GridAbstractCalculationEngine e calcula tus funciones customizadas con tu propia lógica.
## **Calcular funciones personalizadas en GridWeb**
El siguiente código de muestra agrega una función personalizada llamada MYTESTFUNC() en la celda B3. Luego calculamos el valor de esta función implementando la interfaz GridAbstractCalculationEngine. Calculamos MYTESTFUNC() de tal manera que multiplicamos su parámetro por 2 y devolvemos el resultado. Así que si su parámetro es 9, devolverá 2*9 = 18.
### **Código de muestra**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-CalculateCustomFunction.aspx-CalculateCustomFunction.cs" >}}
