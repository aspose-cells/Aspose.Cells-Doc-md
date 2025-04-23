---
title: Crear y gestionar gráficos
description: Aprende cómo usar Aspose.Cells para Python via .NET para crear gráficos en Microsoft Excel. Nuestra guía demostrará los diferentes tipos de gráficos que se pueden crear, así como cómo personalizar su apariencia y formato.
keywords: Aspose.Cells para Python via .NET, creación de gráficos, Microsoft Excel, tipos de gráficos, personalización, apariencia, formato.
linktitle: Gráficos
type: docs
weight: 130
url: /es/python-net/creating-charts/
description: Crear un gráfico en CSharp para archivos de Excel y ODS.
keywords: crear un gráfico, hacer un gráfico 
---

{{% alert color="primary" %}}

Es posible agregar una variedad de gráficos a las hojas de cálculo con Aspose.Cells para Python via .NET. Aspose.Cells para Python via .NET ofrece muchos objetos de gráficos flexibles. Este tema discute los objetos de gráficos de Aspose.Cells.

{{% /alert %}}

## **Creando gráficos**

### **Simplemente creando un gráfico**
Es sencillo crear un gráfico con Aspose.Cells para Python via .NET con los siguientes códigos de ejemplo:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateColumnChart-1.py" >}}

### **Cosas a saber para crear un gráfico**

Antes de crear gráficos, es importante entender algunos conceptos básicos que son útiles al crear gráficos usando Aspose.Cells para Python via .NET.

#### **Objetos de gráficos**

Aspose.Cells para Python via .NET proporciona un conjunto especial de clases en el espacio de nombres [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts) que se usan para crear los gráficos compatibles con Aspose.Cells para Python via .NET. Estas clases se usan para crear **objetos de gráficos**, que actúan como los bloques de construcción del gráfico. Los objetos de gráficos se enumeran a continuación:

- Series, una sola serie de datos en un gráfico.
- Eje, el eje de un gráfico.
- Gráfico, un solo gráfico de Excel.
- Área de gráfico, el área de gráfico en la hoja de cálculo.
- Tabla de datos del gráfico, una tabla de datos de gráfico.
- ChartFrame, el objeto de marco en un gráfico.
- ChartPoint, un solo punto en una serie en un gráfico.
- ChartPointCollection, una colección que contiene todos los puntos en una serie.
- Charts, una colección de objetos Chart.
- DataLabels, una colección de todos los objetos DataLabel para la serie especificada.
- FillFormat, formato de relleno para una forma.
- Floor, el suelo de un gráfico en 3D.
- Legend, la leyenda del gráfico.
- Line, la línea del gráfico.
- SeriesCollection, una colección de objetos Series.
- TickLabels, las etiquetas de marca de graduación asociadas con las marcas en un eje de un gráfico.
- Title, el título de un gráfico o eje.
- Trendline, una línea de tendencia en un gráfico.
- TrendlineCollection, una colección de todos los objetos Trendline para la serie de datos especificada.
- Walls, las paredes de un gráfico en 3D.

#### **Usar objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus clases respectivas y proporcionan propiedades y métodos específicos para realizar tareas específicas. Use objetos de gráficos para crear gráficos.

Agregue cualquier tipo de gráfico a una hoja de cálculo usando la colección [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts). Cada elemento en la colección [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts) representa un objeto [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart). Un objeto [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) engloba todos los demás objetos de gráficos requeridos para personalizar la apariencia del gráfico. La siguiente sección muestra cómo usar algunos objetos básicos de gráficos para crear un gráfico simple.

### **Crear gráfico usando Aspose.Cells para Python via .NET**

**Pasos:**

1. Agregue algunos datos a las celdas de la hoja de cálculo con el método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value) del objeto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Esto se utilizará como fuente de datos para el gráfico.
1. Agregue un gráfico a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection/add) de la colección [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection), encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).
1. Especifique el tipo de gráfico con la enumeración [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype).
   Por ejemplo, el ejemplo a continuación utiliza el valor [**ChartType.PYRAMID**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) como tipo de gráfico.
1. Acceda al nuevo objeto [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) de la colección [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection) pasando su índice.
1. Utilice cualquiera de los objetos de gráficos encapsulados en el objeto [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) para gestionar el gráfico.
   El ejemplo a continuación utiliza el objeto de gráficos [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) para especificar la fuente de datos del gráfico.

Cuando se agrega datos de origen al gráfico, la fuente de datos puede ser un rango de celdas (como "A1:C3"), o una secuencia de celdas no contiguas (como "A1, A3, A5"), o una secuencia de valores (como "1,2,3").

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear distintos gráficos.

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells para Python via .NET. Todos los gráficos estándar soportados por Aspose.Cells para Python via .NET están predefinidos en una enumeración llamada [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype).

Los tipos de gráficos predefinidos son:

|**Tipos de Gráficos**|**Descripción**|
| :- | :- |
|Column|Representa Gráfico de Columnas Agrupadas|
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
|Scatter|Representa Gráfico de Dispersión|
|ScatterConnectedByCurvesWithDataMarker|Representa un gráfico de dispersión conectado por curvas, con marcadores de datos|
|ScatterConnectedByCurvesWithoutDataMarker|Representa un gráfico de dispersión conectado por curvas, sin marcadores de datos|
|ScatterConnectedByLinesWithDataMarker|Representa un gráfico de dispersión conectado por líneas, con marcadores de datos|
|ScatterConnectedByLinesWithoutDataMarker|Representa un gráfico de dispersión conectado por líneas, sin marcadores de datos|
|Area|Representa un gráfico de área|
|AreaStacked|Representa un gráfico de área apilada|
|Area100PercentStacked|Representa un gráfico de área apilada al 100%|
|Area3D|Representa un gráfico de área 3D|
|Area3DStacked|Representa un gráfico de área 3D apilada|
|Area3D100PercentStacked|Representa un gráfico de área 3D apilada al 100%|
|Doughnut|Representa un gráfico de rosquilla|
|DoughnutExploded|Representa un gráfico de rosquilla explosionada|
|Radar|Representa un gráfico radar|
|RadarWithDataMarkers|Representa un gráfico radar con marcadores de datos|
|RadarFilled|Representa un gráfico radar relleno|
|Surface3D|Representa un gráfico de superficie 3D|
|SurfaceWireframe3D|Representa un gráfico de superficie 3D con estructura de alambre|
|SurfaceContour|Representa un gráfico de contorno|
|SurfaceContourWireframe|Representa un gráfico de contorno con estructura de alambre|
|Bubble|Representa un gráfico de burbujas|
|Bubble3D|Representa Gráfico de Burbujas 3D|
|Cylinder|Representa Gráfico de Cilindro|
|CylinderStacked|Representa Gráfico de Cilindro Apilado|
|Cylinder100PercentStacked|Representa Gráfico de Cilindro Apilado al 100%|
|CylindericalBar|Representa Gráfico de Barras Cilíndricas|
|CylindericalBarStacked|Representa Gráfico de Barras Cilíndricas Apiladas|
|CylindericalBar100PercentStacked|Representa Gráfico de Barras Cilíndricas Apiladas al 100%|
|CylindericalColumn3D|Representa Gráfico de Columnas Cilíndricas 3D|
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
|PyramidBar|Representa Gráfico de Barras de Pirámide|
|PyramidBarStacked|Representa Gráfico de Barras de Pirámide Apiladas|
|PyramidBar100PercentStacked|Representa un gráfico de barras de pirámide apilada al 100%|
|PyramidColumn3D|Representa un gráfico de columnas de pirámide 3D|
{{% alert color="primary" %}}

Cuando asignas un rango de celdas como fuente de datos, solo puedes establecer el rango de arriba a la izquierda hacia abajo a la derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" es inválido.

{{% /alert %}}

#### **Gráfico de pirámide**

Cuando se ejecuta el código de ejemplo, se agrega un gráfico de pirámide a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreatePyramidChart-1.py" >}}

#### **Gráfico de líneas**

En el ejemplo anterior, simplemente cambiando el [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) a *Línea* se crea un gráfico de líneas. La fuente completa se proporciona a continuación. Cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateLineChart-1.py" >}}

#### **Gráfico de burbujas**

Para crear un gráfico de burbujas, el [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) debe configurarse en [**ChartType.BUBBLE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) y algunas propiedades adicionales como BubbleSizes, Values & XValues deben establecerse en consecuencia. Al ejecutar el código siguiente, se agrega un gráfico de burbujas a la hoja de cálculo.

#### **Gráfico de líneas con marcadores de datos**

Para crear un gráfico de líneas con marcadores de datos, [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) debe configurarse en *ChartType.LineWithDataMarkers* y algunas propiedades adicionales como área de fondo, Marcadores de series, Values & XValues deben establecerse en consecuencia. Al ejecutar el código siguiente, se agrega un gráfico de líneas con marcadores de datos a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateLineWithDataMarkerChart-1.py" >}}

## **Temas avanzados**
- [Leer y manipular los gráficos de Excel 2016](/cells/es/python-net/read-and-manipulate-excel-2016-charts/)
- [Gestionar los ejes de los gráficos de Excel](/cells/es/python-net/chart-axes/)
- [Configurar la apariencia del gráfico](/cells/es/python-net/setting-chart-appearance/)
- [Tipos de gráficos](/cells/es/python-net/chart-types/)
- [Personalizar gráficos](/cells/es/python-net/customizing-charts/)
- [Establecer la fuente de datos para el gráfico](/cells/es/python-net/data-formatting-in-charts/)
- [Gestionar las etiquetas de datos de los gráficos de Excel](/cells/es/python-net/insert-datalabels-to-chart/)
- [Generar un gráfico mediante Procesamiento de Marcadores Inteligentes](/cells/es/python-net/generate-chart-by-processing-smart-markers/)
- [Obtener hoja de cálculo del gráfico](/cells/es/python-net/get-worksheet-of-the-chart/)
- [Gestionar leyenda de gráficos de Excel](/cells/es/python-net/chart-legend/)
- [Manipular tamaño de posición y diseñar gráfico](/cells/es/python-net/manipulate-position-size-and-designer-chart/)
- [Crear gráficos circulares con líneas de líder](/cells/es/python-net/creating-pie-chart-with-leader-lines/)
- [Formas en gráficos](/cells/es/python-net/controls-in-charts/)
- [Gestionar títulos de gráficos de Excel](/cells/es/python-net/chart-and-axis-titles/)
- [Representación de gráficos](/cells/es/python-net/chart-rendering/)
- [Obtener texto de la ecuación de la línea de tendencia del gráfico](/cells/es/python-net/get-equation-text-of-chart-trendline/)
