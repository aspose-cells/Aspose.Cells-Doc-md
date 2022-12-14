---
title: Uso del parámetro Fórmula en el campo Marcador inteligente
type: docs
weight: 40
url: /es/net/using-formula-parameter-in-smart-marker-field/
---
## **Posibles escenarios de uso**
A veces, desea incrustar una fórmula en el campo del marcador inteligente. Este artículo describe cómo hacer uso de la*Fórmula*parámetro para incrustar la fórmula en el campo del marcador inteligente.
## **Uso del parámetro Fórmula en el campo Marcador inteligente**
 El siguiente código de muestra incrusta la fórmula en el campo de marcador inteligente llamado TestFormula y su nombre de fuente de datos es MyDataSource, por lo que el campo completo con el parámetro de fórmula se parece a &=MyDataSource.TestFormula(formula) y después de la ejecución del código, el[archivo de Excel de salida final](46465047.xlsx) tendrá fórmulas en celdas desde A1 hasta A5.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
