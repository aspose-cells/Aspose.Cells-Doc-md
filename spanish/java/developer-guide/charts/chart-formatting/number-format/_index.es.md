---
title: Establecer el código de formato de valores de la serie de gráficos
description: Aprenda a configurar el código de formato de valores de la serie de gráficos en Aspose.Cells for Java. Nuestra guía lo ayudará a comprender cómo formatear los datos de la serie de gráficos utilizando el código de formato apropiado, lo que le permitirá presentar sus datos de manera precisa y profesional.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Formato numérico
type: docs
weight: 100
url: /es/java/set-the-values-format-code-of-chart-series/
---
##  **Posibles escenarios de uso**
Puede configurar el código de formato de valores de la serie de gráficos utilizando el[Serie.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) método. Este método no sólo es útil para las series que se basan en el rango dentro de la hoja de trabajo, sino que también funciona bien para las series creadas con una matriz de valores.
##  **Establecer el código de formato de valores de la serie de gráficos**
 El siguiente código de muestra agrega una serie en el gráfico vacío que no tenía series antes. Agrega la serie usando la matriz de valores. Una vez agrega la serie, la formatea con el código $#,##0 usando el[Serie.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)método y el número 10000 se convierte en $10,000. La captura de pantalla muestra el efecto del código en el[archivo de Excel de muestra](51740712.xlsx) y[archivo de salida de Excel](51740713.xlsx) después de la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
