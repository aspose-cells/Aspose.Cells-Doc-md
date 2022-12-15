---
title: Creación y personalización de gráficos
type: docs
weight: 10
url: /es/cpp/creating-and-customizing-charts/
---
## **Posibles escenarios de uso**

Un gráfico es una presentación visual de información. Aspose.Cells permite a los desarrolladores visualizar información en gráficos tal como lo hace Microsoft Excel. La presentación de información en gráficos siempre es útil para los tomadores de decisiones para tomar decisiones rápidas y oportunas. Es más fácil ver rápidamente comparaciones, patrones y tendencias en datos con gráficos en lugar de números sin procesar. La creación de gráficos en tiempo de ejecución, basados en los datos de una hoja de cálculo, es una de las funciones útiles de Aspose.Cells. Aspose.Cells admite la creación de gráficos estándar y personalizados. A continuación, mostraremos algunos ejemplos con archivos de muestra sobre cómo crear algunos tipos de gráficos comunes de MS-Excel usando Aspose.Cells API.

## **Gráfico piramidal**

 Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de cálculo. Por favor vea el[archivo de salida de Excel](66519068.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Gráfico de linea**

En el ejemplo anterior, simplemente cambiando el[**Tipo de gráfico**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)a[**ChartType_Line**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)crea un gráfico de líneas. La fuente completa se proporciona a continuación. cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de cálculo. Por favor vea el[archivo de salida de Excel](66519069.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Gráfico de burbujas**

Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) tiene que ser configurado para[**ChartType_Burbuja**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) y pocas propiedades extra como[**EstablecerTamañosDeBurbujas**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**EstablecerXValores**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) debe configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519070.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos discutido los gráficos, hemos visto gráficos estándar que tienen su propia configuración de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero las API Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con su propia configuración de formato. Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico se compone de una serie de datos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos.

 El siguiente código de ejemplo muestra cómo crear gráficos personalizados. En este ejemplo, vamos a utilizar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo. Por favor vea el[archivo de salida de Excel](66519071.xlsx) del siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
