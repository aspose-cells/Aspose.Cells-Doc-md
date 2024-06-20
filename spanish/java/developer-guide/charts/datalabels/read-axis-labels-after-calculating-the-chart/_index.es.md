---
title: Leer etiquetas del eje después de calcular el gráfico
description: Aprenda cómo leer las etiquetas del eje en Aspose.Cells for Java después de calcular el gráfico. Nuestra guía le mostrará cómo acceder y recuperar las etiquetas del eje, incluyendo su formato y posición.
keywords: Aspose.Cells for Java, gráfico, etiquetas del eje, cálculo, lectura, acceso, recuperación, formato, posición.
type: docs
weight: 90
url: /es/java/read-axis-labels-after-calculating-the-chart/
---

## **Escenarios de uso posibles**

Puede leer las etiquetas del eje de su gráfico después de calcular sus valores utilizando el método [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--). Por favor, utilice el método [**Axis.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--) para este propósito que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Por favor, vea el siguiente código de muestra que carga el [archivo Excel de muestra](64716829.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Por favor, consulte la salida de la consola del código de muestra que se presenta a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

## **Salida de la consola**

{{< highlight java >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
