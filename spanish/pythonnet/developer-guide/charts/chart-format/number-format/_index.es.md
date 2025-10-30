---
title: Establecer el código de formato de valores de la serie del gráfico
description: Aprende cómo establecer el código de formato de valores de las series de gráficos en Aspose.Cells para Python via .NET. Nuestra guía te ayudará a entender cómo formatear los datos de tus series de gráficos usando el código de formato apropiado, permitiéndote presentar tus datos con precisión y profesionalismo.
keywords: Aspose.Cells para Python via .NET, series de gráficos, código de formato de valores, formateo, presentación de datos, precisión, profesionalismo.
linktitle: Formato de número
type: docs
weight: 100
url: /es/python-net/set-the-values-format-code-of-chart-series/
---

## **Escenarios de uso posibles**
Puedes establecer el código de formato de valores de las series de gráficos usando la propiedad [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code). Esta propiedad no solo es útil para las series basadas en el rango dentro de la hoja de cálculo, sino que también funciona bien para las series creadas con un arreglo de valores.

## **Establecer el código de formato de valores de la serie del gráfico**
El siguiente código de ejemplo agrega una serie en un gráfico vacío que no tenía series antes. Añade la serie usando un arreglo de valores. Una vez que añade la serie, la formatea con el código $#,##0 usando la propiedad [Series.values_format_code] y el número 10000 se convierte en $10,000. La captura muestra el efecto del código en el [archivo Excel de ejemplo](51740712.xlsx) y el [archivo Excel de salida](51740713.xlsx) tras la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
{{< app/cells/assistant language="python-net" >}}
