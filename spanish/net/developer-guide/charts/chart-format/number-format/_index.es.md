---
title: Establecer el código de formato de valores de la serie de gráficos
linktitle: Formato numérico
type: docs
weight: 100
url: /es/net/set-the-values-format-code-of-chart-series/
---
## **Posibles escenarios de uso**
Puede establecer el código de formato de valores de la serie de gráficos usando el[Serie.ValoresFormatoCódigo](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propiedad. Esta propiedad no solo es útil para la serie que se basa en el rango dentro de la hoja de cálculo, sino que también funciona bien para la serie creada con una matriz de valores.
## **Establecer el código de formato de valores de la serie de gráficos**
El siguiente código de ejemplo agrega una serie en el gráfico vacío que no tiene ninguna serie antes. Agrega la serie usando la matriz de valores. Una vez agrega la serie, la formatea con el código $#,##0 usando el[Serie.ValoresFormatoCódigo](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)propiedad y el número 10000 se convierte en $10,000. La captura de pantalla muestra el efecto del código en el[ejemplo de archivo de Excel](51740712.xlsx) y[archivo de salida de Excel](51740713.xlsx) después de la ejecución.

![todo:imagen_alternativa_texto](set-the-values-format-code-of-chart-series_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
