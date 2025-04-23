---
title: Establecer el código de formato de valores de la serie del gráfico
description: Aprenda a establecer el código de formato de valores de la serie del gráfico en Aspose.Cells for .NET. Nuestra guía le ayudará a comprender cómo formatear los datos de la serie de su gráfico utilizando el código de formato apropiado, lo que le permitirá presentar sus datos de manera precisa y profesional.
keywords: Aspose.Cells for .NET, serie de gráficos, código de formato de valores, formato, presentación de datos, precisión, profesionalismo.
linktitle: Formato de número
type: docs
weight: 100
url: /es/net/set-the-values-format-code-of-chart-series/
---

## **Escenarios de uso posibles**
Puede establecer el código de formato de valores de la serie de gráficos utilizando la propiedad [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). Esta propiedad no solo es útil para la serie que se basa en el rango dentro de la hoja de cálculo, sino que también funciona bien para la serie creada con un array de valores.
## **Establecer el código de formato de valores de la serie del gráfico**
El siguiente código de ejemplo agrega una serie en el gráfico vacío que no tiene series antes. Agrega la serie usando el array de valores. Una vez que agrega la serie, la formatea con el código $#,##0 utilizando la propiedad [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) y el número 10000 se convierte en $10,000. La captura de pantalla muestra el efecto del código en el [archivo de Excel de ejemplo](51740712.xlsx) y el [archivo de Excel de salida](51740713.xlsx) después de la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
{{< app/cells/assistant language="csharp" >}}
