---
title: Uso del parámetro de fórmula en el campo de Marcador Inteligente
type: docs
weight: 30
url: /es/java/using-formula-parameter-in-smart-marker-field/
---

## **Escenarios de uso posibles**
A veces, desea incrustar una fórmula en el campo de Marcador Inteligente. Este artículo describe cómo utilizar el parámetro de Fórmula para incrustar una fórmula en el campo de Marcador Inteligente.
## **Usar parámetro de fórmula en campo de Marcador Inteligente**
El siguiente código de ejemplo incrusta la fórmula en la variable de Marcador Inteligente llamada Test y su nombre de fuente de datos también es Test, por lo que el campo completo con el parámetro de fórmula se ve así **&=$Test(fórmula)** y después de la ejecución del código, el [archivo de Excel de salida final](47153156.xlsx) tendrá fórmulas en las celdas de A1 a A5.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-SmartMarkers-UsingFormulaParameterInSmartMarkerField.java" >}}
