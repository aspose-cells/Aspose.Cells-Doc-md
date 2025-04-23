---
title: Estableciendo fórmula para rango con nombre
type: docs
weight: 20
url: /es/python-net/setting-formula-for-named-range/
---

## **Estableciendo fórmula para rango con nombre**
Al igual que la aplicación Excel, las API de Aspose.Cells para Python via .NET ofrecen la capacidad de especificar una fórmula para un rango con nombre mientras usas su propiedad [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to). Este feature puede tener muchos escenarios de usabilidad, algunos de los cuales se detallan a continuación.
### **Estableciendo una fórmula simple para rango con nombre**
Una fórmula simple podría ser una referencia a otra celda en la misma (o diferente) hoja de cálculo. El siguiente ejemplo crea un rango con nombre en una nueva hoja de cálculo y establece su referencia a otra celda.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Estableciendo una fórmula compleja para rango con nombre**
Una fórmula compleja podría ser cualquier cosa, como un rango dinámico o una fórmula que abarca múltiples celdas en diferentes hojas de cálculo. El siguiente ejemplo crea un rango dinámico utilizando la función INDEX para obtener el valor de una lista según su ubicación.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Aquí hay otro ejemplo que utiliza un rango con nombre para sumar valores de 2 celdas en diferentes hojas de cálculo.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
