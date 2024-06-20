---
title: Personalización de gráficos
type: docs
weight: 15
url: /es/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Creando gráficos**

Es posible agregar una variedad de gráficos a hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. Este tema discute los objetos de gráficos de Aspose.Cells.

### **Simplemente creando un gráfico**

Es simple crear un gráfico con Aspose.Cells con los siguientes códigos de ejemplo:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Cosas que debes saber para crear un gráfico**

Antes de crear gráficos es importante comprender algunos conceptos básicos que son útiles al crear gráficos con Aspose.Cells.

#### **Objetos de gráficos**

Aspose.Cells proporciona un conjunto especial de clases utilizadas para crear todo tipo de gráficos. Estas clases se usan para crear **objetos de gráficos**, que actúan como bloques de construcción del gráfico. A continuación se enumeran los objetos de gráficos:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), eje de un gráfico.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un solo gráfico de Excel.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), el área del gráfico en la hoja de cálculo.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabla de datos del gráfico.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), el objeto marco en un gráfico.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un solo punto en una serie de un gráfico.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una colección que contiene todos los puntos en una serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), una colección de [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objetos.
- DataLabels, etiquetas de datos para el [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) especificado, [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), formato de relleno para una forma.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), el piso de un gráfico 3D.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la leyenda del gráfico.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la línea del gráfico.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), una colección de [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objetos.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), representa una sola serie de datos en un gráfico.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), las etiquetas de marcas de graduación asociadas con marcas de graduación en un eje de gráfico.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), el título de un gráfico o eje.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una línea de tendencia en un gráfico.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una colección de todos los objetos de línea de tendencia para la serie de datos especificada.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), las paredes de un gráfico 3D.

#### **Usar objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus clases respectivas y proporcionan propiedades y métodos específicos para realizar tareas específicas. Use objetos de gráficos para crear gráficos.

Agregue cualquier tipo de gráfico a una hoja de cálculo utilizando la colección [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection). Cada elemento en la colección [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) representa un objeto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart). Un objeto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) engloba todos los Objetos de Gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo utilizar algunos objetos de gráficos básicos para crear un gráfico simple.

### **Creando un Gráfico Simple**

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración llamada [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Los tipos de gráfico predefinidos son:

|**Tipos de Gráficos**|**Descripción**|
| :- | :- |
|Column|Representa el Gráfico de Columnas Agrupadas|
|ColumnStacked|Representa Gráfico de Columnas Apiladas|
|Column100PercentStacked|Representa Gráfico de Columnas Apiladas al 100%|
|Column3DClustered|Representa Gráfico de Columnas Agrupadas en 3D|
|Column3DStacked|Representa Gráfico de Columnas Apiladas en 3D|
|Column3D100PercentStacked|Representa Gráfico de Columnas Apiladas al 100% en 3D|
|Column3D|Representa Gráfico de Columnas en 3D|
|Bar|Representa Gráfico de Barras Agrupadas|
|BarStacked|Representa Gráfico de Barras Apiladas|
|Bar100PercentStacked|Representa Gráfico de Barras Apiladas al 100%|
|Bar3DClustered|Representa Gráfico de Barras Agrupadas en 3D|
|Bar3DStacked|Representa Gráfico de Barras Apiladas en 3D|
|Bar3D100PercentStacked|Representa Gráfico de Barras Apiladas al 100% en 3D|
|Line|Representa Gráfico de Líneas|
|LineStacked|Representa Gráfico de Líneas Apiladas|
|Line100PercentStacked|Representa Gráfico de Líneas Apiladas al 100%|
|LineWithDataMarkers|Representa Gráfico de Líneas con marcadores de datos|
|LineStackedWithDataMarkers|Representa Gráfico de Líneas Apiladas con marcadores de datos|
|Line100PercentStackedWithDataMarkers|Representa Gráfico de Líneas Apiladas al 100% con marcadores de datos|
|Line3D|Representa Gráfico de Líneas en 3D|
|Pie|Representa Gráfico Circular|
|Pie3D|Representa Gráfico Circular en 3D|
|PiePie|Representa Gráfico de Pastel de Pastel|
|PieExploded|Representa Gráfico de Pastel Explodido|
|Pie3DExploded|Representa Gráfico de Pastel Explodido en 3D|
|PieBar|Representa Gráfico de Barras de Pastel|
|Scatter|Representa el gráfico de dispersión|
|ScatterConnectedByCurvesWithDataMarker|Representa el gráfico de dispersión conectado por curvas, con marcadores de datos|
|ScatterConnectedByCurvesWithoutDataMarker|Representa el gráfico de dispersión conectado por curvas, sin marcadores de datos|
|ScatterConnectedByLinesWithDataMarker|Representa el gráfico de dispersión conectado por líneas, con marcadores de datos|
|ScatterConnectedByLinesWithoutDataMarker|Representa el gráfico de dispersión conectado por líneas, sin marcadores de datos|
|Area|Representa un gráfico de área|
|AreaStacked|Representa un gráfico de área apilada|
|Area100PercentStacked|Representa un gráfico de área apilada al 100%|
|Area3D|Representa un gráfico de área 3D|
|Area3DStacked|Representa un gráfico de área 3D apilada|
|Area3D100PercentStacked|Representa un gráfico de área 3D apilada al 100%|
|Doughnut|Representa un gráfico de rosquilla|
|DoughnutExploded|Representa un gráfico de rosquilla explosionada|
|Radar|Representa un gráfico de radar|
|RadarWithDataMarkers|Representa un gráfico de radar con marcadores de datos|
|RadarFilled|Representa un gráfico radar relleno|
|Surface3D|Representa un gráfico de superficie 3D|
|SurfaceWireframe3D|Representa un gráfico de superficie en 3D con alambre de contorno|
|SurfaceContour|Representa un gráfico de contorno|
|SurfaceContourWireframe|Representa un gráfico de contorno con estructura de alambre|
|Bubble|Representa un gráfico de burbujas|
|Bubble3D|Representa Gráfico de Burbujas 3D|
|Cylinder|Representa Gráfico de Cilindro|
|CylinderStacked|Representa Gráfico de Cilindro Apilado|
|Cylinder100PercentStacked|Representa Gráfico de Cilindro Apilado al 100%|
|CylindricalBar|Representa el gráfico de barras cilíndricas.
|CylindricalBarStacked|Representa el gráfico de barras cilíndricas apiladas.
|CylindricalBar100PercentStacked|Representa el gráfico de barras cilíndricas apiladas al 100%.
|CylindricalColumn3D|Representa el gráfico de columnas cilíndricas en 3D.
|Cone|Representa Gráfico de Cono|
|ConeStacked|Representa Gráfico de Cono Apilado|
|Cone100PercentStacked|Representa Gráfico de Cono Apilado al 100%|
|ConicalBar|Representa Gráfico de Barras Cónicas|
|ConicalBarStacked|Representa Gráfico de Barras Cónicas Apiladas|
|ConicalBar100PercentStacked|Representa Gráfico de Barras Cónicas Apiladas al 100%|
|ConicalColumn3D|Representa Gráfico de Columnas Cónicas 3D|
|Pyramid|Representa Gráfico de Pirámide|
|PyramidStacked|Representa Gráfico de Pirámide Apilada|
|Pyramid100PercentStacked|Representa Gráfico de Pirámide Apilada al 100%|
|PyramidBar|Representa el gráfico de barras piramidales.
|PyramidBarStacked|Representa Gráfico de Barras de Pirámide Apiladas|
|PyramidBar100PercentStacked|Representa un gráfico de barras de pirámide apilada al 100%|
|PyramidColumn3D|Representa un gráfico de columnas de pirámide 3D|
Para crear un gráfico usando Aspose.Cells:

1. Agregue algunos datos a las celdas de la hoja de cálculo con el método [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) del objeto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).
   Esto se utilizará como fuente de datos para el gráfico.
1. Agregue un gráfico a la hoja de cálculo llamando al método [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int)) de la colección [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Especifique el tipo de gráfico con la enumeración [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).
   Por ejemplo, el ejemplo utiliza el valor [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) como tipo de gráfico.
1. Acceda al nuevo objeto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) de la colección [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) pasando su índice.
1. Utilice cualquiera de los objetos de gráficos encapsulados en el objeto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) para gestionar el gráfico.
   El ejemplo a continuación utiliza el objeto de gráficos [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) para especificar la fuente de datos del gráfico.

Cuando se agrega datos de origen al gráfico, la fuente de datos puede ser un rango de celdas (como "A1:C3"), o una secuencia de celdas no contiguas (como "A1, A3, A5"), o una secuencia de valores (como "1,2,3").

{{% alert color="primary" %}}

Cuando asigna un rango de celdas como fuente de datos, solo puede establecer el rango de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" es inválido.

{{% /alert %}}

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear distintos gráficos.

Cuando se ejecuta el código de ejemplo, se agrega un gráfico de pirámide a la hoja de cálculo como se muestra a continuación.

**Gráfico de pirámide con su fuente de datos**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Para crear un gráfico de burbujas, el [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) debe establecerse en [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE) y se deben establecer algunas propiedades adicionales como BubbleSizes, Values & XValues en consecuencia. Al ejecutar el código siguiente, se agrega un gráfico de burbujas a la hoja de cálculo como se muestra a continuación.

**Gráfico de burbujas con su fuente de datos**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Gráfico de líneas con marcadores de datos**

Para crear un gráfico de línea con marcador de datos, el [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) debe establecerse en [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) y se deben establecer algunas propiedades adicionales como área de fondo, marcadores de serie, valores y XValues en consecuencia. Al ejecutar el código siguiente, se agrega un gráfico de línea con marcador de datos a la hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos discutido sobre gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero Aspose.Cells también admite la creación de gráficos personalizados que permite a los desarrolladores crear gráficos con su propia configuración de formato.

### **Creación de gráficos personalizados**

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando la sencilla API de Aspose.Cells.

Un gráfico está compuesto por una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), mientras que el objeto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) sirve como una colección de objetos [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de utilizar diferentes tipos de gráficos para diferentes series de datos (recopilados en un objeto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)).

{{% alert color="primary" %}}

Actualmente Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de columnas apiladas, pero se admitirán más gráficos en futuras versiones. Para ver una lista completa de los gráficos estándar que admite Aspose.Cells, consulte el artículo [Tipos de gráficos](/cells/es/java/chart-types/).

{{% /alert %}}

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.

**Gráfico personalizado que combina gráficos de columnas y de líneas**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Ejemplo de programación**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Para ver una lista de tipos de gráficos admitidos, lea el artículo [Tipos de gráficos](/cells/es/java/chart-types/).

{{% /alert %}}

