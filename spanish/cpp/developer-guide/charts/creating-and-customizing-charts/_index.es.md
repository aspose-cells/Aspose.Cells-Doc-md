---
title: Crear y personalizar gráficos
type: docs
weight: 10
url: /es/cpp/creating-and-customizing-charts/
---
##  **Posibles escenarios de uso**

Un gráfico es una presentación visual de información. Aspose.Cells permite a los desarrolladores visualizar información en gráficos tal como lo hace Microsoft Excel. Presentar información en gráficos siempre es útil para que los tomadores de decisiones tomen decisiones rápidas y oportunas. Es más fácil ver rápidamente comparaciones, patrones y tendencias en los datos con gráficos en lugar de números sin procesar. La creación de gráficos en tiempo de ejecución, basados en los datos de una hoja de cálculo, es una de las funciones útiles de Aspose.Cells. Aspose.Cells admite la creación de gráficos estándar y personalizados. A continuación, mostraremos algunos ejemplos con archivos de muestra sobre cómo crear algunos tipos de gráficos comunes de MS-Excel usando Aspose.Cells API.

##  **Gráfico piramidal**

 Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519068.xlsx) del siguiente código de muestra.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Gráfico de linea**

En el ejemplo anterior, simplemente cambiando el[**Tipo de gráfico**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)a**`Tipo de gráfico::Línea`**crea un gráfico de líneas. La fuente completa se proporciona a continuación. cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519069.xlsx) del siguiente código de muestra.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Gráfico de burbujas**

Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) tiene que estar configurado en**`ChartType_Bubble`** y pocas propiedades extra como[**Establecer tamaños de burbujas**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**Establecer valoresX**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519070.xlsx) del siguiente código de muestra.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Crear gráficos personalizados**

Hasta ahora, cuando hemos analizado los gráficos, hemos analizado los gráficos estándar que tienen sus propias configuraciones de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero las API Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato. Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico se compone de una serie de datos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de utilizar diferentes tipos de gráficos para diferentes series de datos.

 El siguiente código de ejemplo demuestra cómo crear gráficos personalizados. En este ejemplo, usaremos un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519071.xlsx) del siguiente código de muestra.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
