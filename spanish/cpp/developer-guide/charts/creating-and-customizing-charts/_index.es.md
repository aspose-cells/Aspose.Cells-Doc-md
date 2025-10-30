---
title: Creación y personalización de gráficos
type: docs
weight: 10
url: /es/cpp/creating-and-customizing-charts/
---

## **Escenarios de uso posibles**

Un gráfico es una representación visual de la información. Aspose.Cells permite a los desarrolladores visualizar información en gráficos al igual que lo hace Microsoft Excel. Presentar información en gráficos siempre es útil para los tomadores de decisiones para tomar decisiones rápidas y oportunas. Es más fácil ver rápidamente comparaciones, patrones y tendencias en los datos con gráficos que con números brutos. La creación de gráficos en tiempo de ejecución, basados en los datos de una hoja de cálculo, es una de las características útiles de Aspose.Cells. Aspose.Cells admite la creación de gráficos tanto estándar como personalizados. A continuación, mostraremos algunos ejemplos con archivos de muestra sobre cómo crear algunos tipos comunes de gráficos de MS-Excel utilizando la API de Aspose.Cells.

## **Gráfico de pirámide**

Cuando se ejecuta el código de ejemplo, se agrega un gráfico de pirámide a la hoja de cálculo. Por favor, consulte el [archivo de Excel de salida](66519068.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Gráfico de líneas**

En el ejemplo anterior, simplemente cambiando el [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) a **`ChartType::Line`** se crea un gráfico de líneas. Se proporciona el código fuente completo a continuación. Cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de cálculo. Por favor, consulte el [archivo de Excel de salida](66519069.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Gráfico de burbujas**

Para crear un gráfico de burbujas, el [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) debe establecerse en **`ChartType_Bubble`** y se deben establecer algunas propiedades adicionales como [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) y [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) según corresponda. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de cálculo. Por favor, consulte el [archivo de Excel de salida](66519070.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Creación de gráficos personalizados**

Hasta ahora, al discutir los gráficos, hemos visto gráficos estándar que tienen sus propias configuraciones de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y se crea el gráfico con su configuración de formato predeterminada. Pero las API de Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato. Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico está compuesto por una serie de datos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos.

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo. Por favor, consulte el [archivo de Excel de salida](66519071.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
