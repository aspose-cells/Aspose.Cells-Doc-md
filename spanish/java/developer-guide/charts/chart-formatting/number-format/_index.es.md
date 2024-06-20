---
title: Establecer el código de formato de valores de la serie del gráfico
description: Aprenda a establecer el código de formato de valores de la serie del gráfico en Aspose.Cells for Java. Nuestra guía le ayudará a entender cómo formatear los datos de la serie del gráfico utilizando el código de formato apropiado, lo que le permitirá presentar sus datos de manera precisa y profesional.
keywords: Aspose.Cells for Java, serie del gráfico, código de formato de valores, formateo, presentación de datos, precisión, profesionalismo.
linktitle: Formato de número
type: docs
weight: 100
url: /es/java/set-the-values-format-code-of-chart-series/
---

## **Escenarios de uso posibles**
Puede establecer el código de formato de valores de la serie del gráfico utilizando el método [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-). Este método no solo es útil para la serie que se basa en el rango dentro de la hoja de cálculo, sino que también funciona bien para la serie creada con un conjunto de valores.
## **Establecer el código de formato de valores de la serie del gráfico**
El siguiente código de muestra agrega una serie en el gráfico vacío que no tiene una serie antes. Agrega la serie usando el conjunto de valores. Una vez que agrega la serie, la formatea con el código $#,##0 utilizando el método [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) y el número 10000 se convierte en $10,000. La captura de pantalla muestra el efecto del código en el [archivo de Excel de muestra](51740712.xlsx) y en el [archivo de Excel de salida](51740713.xlsx) después de la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
