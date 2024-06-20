---
title: Estableciendo fórmula para rango con nombre
type: docs
weight: 20
url: /es/net/setting-formula-for-named-range/
---

## **Estableciendo fórmula para rango con nombre**
Al igual que la aplicación de Excel, las API de Aspose.Cells brindan la capacidad de especificar una fórmula para un rango con nombre al usar su propiedad [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto). Podría haber numerosos escenarios de usabilidad para esta característica, algunos de los cuales se detallan a continuación.
### **Estableciendo una fórmula simple para rango con nombre**
Una fórmula simple podría ser una referencia a otra celda en la misma (o diferente) hoja de cálculo. El siguiente ejemplo crea un rango con nombre en una nueva hoja de cálculo y establece su referencia a otra celda.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Estableciendo una fórmula compleja para rango con nombre**
Una fórmula compleja podría ser cualquier cosa, como un rango dinámico o una fórmula que abarca múltiples celdas en diferentes hojas de cálculo. El siguiente ejemplo crea un rango dinámico utilizando la función INDEX para obtener el valor de una lista según su ubicación.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Aquí hay otro ejemplo que utiliza un rango con nombre para sumar valores de 2 celdas en diferentes hojas de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
