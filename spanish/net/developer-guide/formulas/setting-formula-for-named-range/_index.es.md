---
title: Configuración de la fórmula para el rango con nombre
type: docs
weight: 20
url: /es/net/setting-formula-for-named-range/
---
## **Configuración de la fórmula para el rango con nombre**
 Al igual que la aplicación Excel, las API Aspose.Cells brindan la capacidad de especificar una fórmula para un rango con nombre mientras usa su[Se refiere a](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)propiedad. Podría haber numerosos escenarios de usabilidad para esta función, algunos de los cuales se detallan a continuación.
### **Establecer una fórmula simple para un rango con nombre**
Una fórmula simple podría ser una referencia a otra celda en la misma (o diferente) hoja de cálculo. El siguiente ejemplo crea un rango con nombre en una nueva hoja de cálculo y establece su referencia a otra celda.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Establecer una fórmula compleja para un rango con nombre**
Una fórmula compleja podría ser cualquier cosa, como un rango dinámico o una fórmula que abarque varias celdas en diferentes hojas de cálculo. El siguiente ejemplo crea un rango dinámico utilizando la función ÍNDICE para obtener el valor de una lista en función de su ubicación.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Aquí hay otro ejemplo que usa un rango con nombre para sumar valores de 2 celdas en diferentes hojas de cálculo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
