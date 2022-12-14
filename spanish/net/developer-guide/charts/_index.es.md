---
title: Crear y administrar gráfico
linktitle: Gráficos
type: docs
weight: 130
url: /es/net/creating-charts/
description: Cree un gráfico en CSharp para archivos Excel y ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Es posible agregar una variedad de gráficos a las hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. Este tema trata sobre los objetos de gráficos Aspose.Cells.

{{% /alert %}}

## **Creación de gráficos**

### **Simplemente creando un gráfico**
Es sencillo crear un gráfico con Aspose.Cells con los siguientes códigos de ejemplo:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Cosas que debe saber para crear un gráfico**

Antes de crear gráficos, es importante comprender algunos conceptos básicos que son útiles al crear gráficos con Aspose.Cells.

#### **Objetos de gráficos**

Aspose.Cells proporciona un conjunto especial de clases en el[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) espacio de nombres utilizado para crear los gráficos admitidos por Aspose.Cells. Estas clases se utilizan para crear**graficar objetos**, que actúan como bloques de creación de gráficos. Los objetos gráficos se enumeran a continuación:

- Serie, una sola serie de datos en un gráfico.
- Axis, el eje de un gráfico.
- Gráfico, un solo gráfico de Excel.
- ChartArea, el área del gráfico en la hoja de cálculo.
- ChartDataTable, una tabla de datos de gráfico.
- ChartFrame, el objeto de marco en un gráfico.
- ChartPoint, un solo punto en una serie en un gráfico.
- ChartPointCollection, una colección que contiene todos los puntos de una serie.
- Charts, una colección de objetos Chart.
- DataLabels, una colección de todos los objetos DataLabel para la serie especificada.
- FillFormat, formato de relleno para una forma.
- Piso, el piso de un gráfico 3D.
- Leyenda, la leyenda del gráfico.
- Línea, la línea del gráfico.
- SeriesCollection, una colección de objetos Series.
- TickLabels, las etiquetas de marca de graduación asociadas con las marcas de graduación en un eje de gráfico.
- Título, el título de un gráfico o eje.
- Línea de tendencia, una línea de tendencia en un gráfico.
- TrendlineCollection, una colección de todos los objetos Trendline para la serie de datos especificada.
- Paredes, las paredes de un gráfico 3D.

#### **Uso de objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus respectivas clases y proporcionan propiedades y métodos específicos para realizar tareas específicas. Use objetos de gráficos para crear gráficos.

Agregue cualquier tipo de gráfico a una hoja de trabajo usando el[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) recopilación. Cada artículo en el[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) colección representa un[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objeto. A[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)El objeto encapsula todos los demás objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo usar algunos objetos gráficos básicos para crear un gráfico simple.

### **Crear gráfico usando Aspose.Cells**

**Pasos:**

1.  Agregue algunos datos a las celdas de la hoja de trabajo con el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objetos[**poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)método.
 Esto se utilizará como fuente de datos para el gráfico.
1.  Agregue un gráfico a la hoja de trabajo llamando al[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) colección[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) método, encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objeto.
1.  Especifique el tipo de gráfico con el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)enumeración.
 Por ejemplo, el siguiente ejemplo utiliza el[**ChartType.Pirámide**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)value como el tipo de gráfico.
1.  Accede al nuevo[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objeto de la[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)colección pasando su índice.
1.  Utilice cualquiera de los objetos de gráficos encapsulados en el[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)objeto para gestionar el gráfico.
 El siguiente ejemplo utiliza el[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objeto de gráfico para especificar la fuente de datos del gráfico.

Al agregar datos de origen al gráfico, el origen de datos puede ser un rango de celdas (como "A1:C3"), una secuencia de celdas no contiguas (como "A1, A3, A5") o una secuencia de valores (como "1,2,3").

Estos pasos generales le permiten crear cualquier tipo de gráfico. Use diferentes objetos de gráficos para crear diferentes gráficos.

 Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración denominada[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Los tipos de gráficos predefinidos son:

|**Tipos de gráficos**|**Descripción**|
|:- |:- |
|Columna|Representa el gráfico de columnas agrupadas|
|Columna apilada|Representa el gráfico de columnas apiladas|
|Columna100PorcentajeApilado|Representa un gráfico de columnas apiladas al 100 %|
|Columna 3D agrupada|Representa el gráfico de columnas agrupadas en 3D|
|Columna3Dapilada|Representa el gráfico de columnas apiladas en 3D|
|Columna3D100PorcentajeApilado|Representa un gráfico de columnas apiladas al 100 % en 3D|
|Columna3D|Representa el gráfico de columnas 3D|
|Bar|Representa el gráfico de barras agrupadas|
|Barra apilada|Representa el gráfico de barras apiladas|
|Bar100Por CientoApilado|Representa un gráfico de barras apiladas al 100 %|
|Bar3D Agrupado|Representa el gráfico de barras agrupadas en 3D|
|Bar3DSapilado|Representa el gráfico de barras apiladas en 3D|
|Bar3D100Por CientoApilado|Representa un gráfico de barras apiladas al 100 % en 3D|
|Línea|Representa el gráfico de líneas|
|línea apilada|Representa el gráfico de líneas apiladas|
|Línea100PorcentajeApilado|Representa un gráfico de líneas apiladas al 100 %|
|LíneaConMarcadoresDeDatos|Representa el gráfico de líneas con marcadores de datos|
|Línea apilada con marcadores de datos|Representa el gráfico de líneas apiladas con marcadores de datos|
|Línea100PorcentajeApiladoConMarcadoresDeDatos|Representa un gráfico de líneas apiladas al 100 % con marcadores de datos|
|Línea3D|Representa el gráfico de líneas 3D|
|Tarta|Representa gráfico circular|
|Pie3D|Representa gráfico circular 3D|
|Pastel Pastel|Representa circular de gráfico circular|
|PastelExplotado|Representa el gráfico circular explotado|
|Pie3DExplotado|Representa un gráfico circular explotado en 3D|
|PieBar|Representa la barra del gráfico circular|
|Dispersión|Representa el gráfico de dispersión|
|ScatterConnectedByCurvesWithDataMarker|Representa el gráfico de dispersión conectado por curvas, con marcadores de datos|
|DispersiónConectadoPorCurvasSinMarcador de datos|Representa el gráfico de dispersión conectado por curvas, sin marcadores de datos|
|ScatterConnectedByLinesWithDataMarker|Representa el gráfico de dispersión conectado por líneas, con marcadores de datos|
|ScatterConnectedByLinesWithoutDataMarker|Representa el gráfico de dispersión conectado por líneas, sin marcadores de datos|
|Área|Representa el gráfico de área|
|Área apilada|Representa el gráfico de áreas apiladas|
|Área100PorcentajeApilado|Representa un gráfico de áreas apiladas al 100 %|
|Área3D|Representa el gráfico de área 3D|
|Area3DSapilado|Representa el gráfico de áreas apiladas en 3D|
|Área3D100PorcentajeApilado|Representa el gráfico de áreas apiladas al 100 % en 3D|
|Rosquilla|Representa el gráfico de anillos|
|RosquillaExplotó|Representa el gráfico de anillos expandido|
|Radar|Representa gráfico de radar|
|RadarConMarcadoresDeDatos|Representa el gráfico de radar con marcadores de datos|
|Lleno de radar|Representa el gráfico de radar lleno|
|Superficie3D|Representa gráfico de superficie 3D|
|SuperficieAlambrado3D|Representa el gráfico de superficie 3D de estructura alámbrica|
|SuperficieContorno|Representa gráfico de contorno|
|SuperficieContornoEstructura metálica|Representa el gráfico de contorno de estructura alámbrica|
|Burbuja|Representa gráfico de burbujas|
|Burbuja3D|Representa gráfico de burbujas 3D|
|Cilindro|Representa el gráfico de cilindros|
|CilindroApilado|Representa el gráfico de cilindros apilados|
|Cilindro100PorcentajeApilado|Representa el gráfico de cilindros 100 % apilados|
|Barra cilíndrica|Representa el gráfico de barras cilíndricas.|
|CilindroicalBarApilado|Representa el gráfico de barras cilíndricas apiladas|
|CilindroicalBar100PorcentajeApilado|Representa un gráfico de barras cilíndricas apiladas al 100 %|
|CilindroicalColumna3D|Representa el gráfico de columnas cilíndricas en 3D|
|Cono|Representa el gráfico de cono|
|ConoApilado|Representa el gráfico de conos apilados|
|Cono100Por CientoApilado|Representa un gráfico de conos apilados al 100 %|
|Barracónica|Representa el gráfico de barras cónicas|
|Barra CónicaApilada|Representa el gráfico de barras cónicas apiladas|
|CónicoBar100PorcentajeApilado|Representa un gráfico de barras cónicas apiladas al 100 %|
|ColumnaCónica3D|Representa el gráfico de columnas cónicas 3D|
|Pirámide|Representa gráfico piramidal|
|Pirámide apilada|Representa el gráfico de pirámide apilada|
|Pirámide100Por CientoApilado|Representa un gráfico piramidal 100 % apilado|
|PirámideBar|Representa el gráfico de barras de la pirámide|
|PirámideBarApilado|Representa el gráfico de barras de pirámides apiladas|
|PirámideBar100PorcentajeApilado|Representa un gráfico de barras piramidal 100 % apilado|
|PirámideColumna3D|Representa el gráfico de columnas de la pirámide 3D|
{{% alert color="primary" %}}

Cuando asigna un rango de celdas como fuente de datos, solo puede establecer el rango de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" no es válido.

{{% /alert %}}

#### **Gráfico piramidal**

Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Gráfico de linea**

 En el ejemplo anterior, simplemente cambiando el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) a*Línea*crea un gráfico de líneas. La fuente completa se proporciona a continuación. cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Gráfico de burbujas**

 Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) tiene que ser configurado para[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)y algunas propiedades adicionales, como BubbleSizes, Values y XValues, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo.

#### **Línea con gráfico de marcador de datos**

 Para crear una línea con el gráfico de marcador de datos,[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)tiene que ser configurado para*ChartType.LineWithDataMarkers*algunas propiedades adicionales, como el área de fondo, los marcadores de serie, los valores y los valores XV, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega una línea con el gráfico de marcador de datos a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Temas avanzados**
- [Leer y manipular gráficos de Excel 2016](/cells/es/net/read-and-manipulate-excel-2016-charts/)
- [Administrar ejes de gráficos de Excel](/cells/es/net/chart-axes/)
- [Configuración de la apariencia del gráfico](/cells/es/net/setting-chart-appearance/)
- [Tipos de gráficos](/cells/es/net/chart-types/)
- [Personalización de gráficos](/cells/es/net/customizing-charts/)
- [Establecer fuente de datos para el gráfico](/cells/es/net/data-formatting-in-charts/)
- [Administrar etiquetas de datos de gráficos de Excel](/cells/es/net/insert-datalabels-to-chart/)
- [Generar gráfico procesando marcadores inteligentes](/cells/es/net/generate-chart-by-processing-smart-markers/)
- [Obtener hoja de trabajo del gráfico](/cells/es/net/get-worksheet-of-the-chart/)
- [Administrar gráficos de Leyenda de Excel](/cells/es/net/chart-legend/)
- [Manipular el tamaño de la posición y el gráfico del diseñador](/cells/es/net/manipulate-position-size-and-designer-chart/)
- [Creación de un gráfico circular con líneas guía](/cells/es/net/creating-pie-chart-with-leader-lines/)
- [Formas en gráficos](/cells/es/net/controls-in-charts/)
- [Administrar títulos de gráficos de Excel](/cells/es/net/chart-and-axis-titles/)
- [Representación de gráficos](/cells/es/net/chart-rendering/)
- [Obtener el texto de la ecuación de la línea de tendencia del gráfico](/cells/es/net/get-equation-text-of-chart-trendline/)
