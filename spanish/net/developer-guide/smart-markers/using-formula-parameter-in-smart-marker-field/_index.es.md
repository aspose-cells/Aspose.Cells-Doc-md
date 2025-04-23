---
title: Uso del parámetro de fórmula en el campo de Marcador Inteligente
type: docs
weight: 40
url: /es/net/using-formula-parameter-in-smart-marker-field/
---


## **Escenarios de uso posibles**
A veces, se quiere incrustar una fórmula en el campo smart marker. Este artículo describe cómo utilizar el parámetro *Fórmula* para incrustar una fórmula en el campo Smart Marker.
## **Usar parámetro de fórmula en campo de Marcador Inteligente**
El siguiente código de ejemplo incrusta la fórmula en el campo smart marker llamado TestFormula y el nombre de su fuente de datos es MyDataSource, por lo que el campo completo con el parámetro de fórmula se ve así &=MyDataSource.TestFormula(fórmula) y después de la ejecución del código, el [archivo de Excel de salida final](46465047.xlsx) tendrá fórmulas en las celdas desde A1 hasta A5.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingFormulaParameterInSmartMarkerField.cs" >}}
{{< app/cells/assistant language="csharp" >}}
