---
title: Crear y administrar gráfico
description: Aprenda a utilizar Aspose.Cells for .NET para crear gráficos en Microsoft Excel. Nuestra guía demostrará los diferentes tipos de gráficos que se pueden crear, así como también cómo personalizar su apariencia y formato.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Gráficos
type: docs
weight: 130
url: /es/net/creating-charts/
description: Cree un gráfico en CSharp para Excel y archivos ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Es posible agregar una variedad de gráficos a las hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. En este tema se analizan los objetos de gráficos Aspose.Cells'.

{{% /alert %}}

##  **Crear gráficos**

###  **Simplemente creando un gráfico**
Es sencillo crear un gráfico con Aspose.Cells con los siguientes códigos de ejemplo:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **Cosas que debe saber para crear un gráfico**

Antes de crear gráficos, es importante comprender algunos conceptos básicos que resultan útiles al crear gráficos utilizando Aspose.Cells.

####  **Objetos gráficos**

 Aspose.Cells proporciona un conjunto especial de clases en el[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)espacio de nombres utilizado para crear los gráficos admitidos por Aspose.Cells. Estas clases se utilizan para crear *objetos de gráficos**, que actúan como bloques de construcción del gráfico. Los objetos de gráficos se enumeran a continuación:

- Serie, una única serie de datos en un gráfico.
- Eje, el eje de un gráfico.
- Gráfico, un único gráfico de Excel.
- ChartArea, el área del gráfico en la hoja de trabajo.
- ChartDataTable, una tabla de datos de gráficos.
- ChartFrame, el objeto de marco en un gráfico.
- ChartPoint, un único punto de una serie en un gráfico.
- ChartPointCollection, una colección que contiene todos los puntos de una serie.
- Gráficos, una colección de objetos Gráfico.
- DataLabels, una colección de todos los objetos DataLabel de la serie especificada.
- FillFormat, formato de relleno para una forma.
- Piso, el piso de un gráfico 3D.
- Leyenda, la leyenda del gráfico.
- Línea, la línea del gráfico.
- SeriesCollection, una colección de objetos de la serie.
- TickLabels, las etiquetas de marcas de graduación asociadas con las marcas de graduación en un eje del gráfico.
- Título, el título de un gráfico o eje.
- Línea de tendencia, una línea de tendencia en un gráfico.
- TrendlineCollection, una colección de todos los objetos Trendline para la serie de datos especificada.
- Paredes, las paredes de un gráfico 3D.

####  **Usar objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus respectivas clases y proporcionan propiedades y métodos específicos para realizar tareas específicas. Utilice objetos de gráficos para crear gráficos.

 Agregue cualquier tipo de gráfico a una hoja de trabajo usando el[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) recopilación. Cada elemento en el[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) colección representa un[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objeto. A[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)El objeto encapsula todos los demás objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo utilizar algunos objetos gráficos básicos para crear un gráfico simple.

###  **Crear gráfico usando Aspose.Cells**

**Pasos:**

1. Agregue algunos datos a las celdas de la hoja de trabajo con el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) objetos[**Poner valor**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)método.
 Esto se utilizará como fuente de datos para el gráfico.
1.  Agregue un gráfico a la hoja de trabajo llamando al[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) colección[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) método, encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objeto.
1.  Especifique el tipo de gráfico con el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)enumeración.
 Por ejemplo, el siguiente ejemplo utiliza el[**Tipo de gráfico.Pirámide**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)valor como tipo de gráfico.
1.  Accede a lo nuevo[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) objeto de la[**Gráficos**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)colección pasando su índice.
1.  Utilice cualquiera de los objetos de gráficos encapsulados en el[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)Objeto para gestionar el gráfico.
 El siguiente ejemplo utiliza el[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objeto de gráfico para especificar la fuente de datos del gráfico.

Al agregar datos de origen al gráfico, el origen de datos puede ser un rango de celdas (como "A1:C3"), una secuencia de celdas no contiguas (como "A1, A3, A5") o una secuencia de valores (como "1,2,3").

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear diferentes gráficos.

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración denominada[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Los tipos de gráficos predefinidos son:

|**Tipos de gráficos**|**Descripción**|
| :- | :- |
|Columna|Representa un gráfico de columnas agrupadas|
|Columna Apilada|Representa un gráfico de columnas apiladas|
|Columna100PorcentajeApilada|Representa un gráfico de columnas 100% apiladas|
|Columna3DClustered|Representa un gráfico de columnas agrupadas en 3D|
|Columna3DSapilada|Representa un gráfico de columnas apiladas en 3D|
|Columna3D100PorcentajeApilado|Representa un gráfico de columnas 100 % apiladas en 3D|
|Columna3D|Representa un gráfico de columnas 3D|
|Bar|Representa un gráfico de barras agrupadas|
|barra apilada|Representa un gráfico de barras apiladas|
|Barra100PorCientoApilados|Representa un gráfico de barras apiladas al 100 %.|
|Bar3DClustered|Representa un gráfico de barras agrupadas en 3D|
|Barra3DSapilada|Representa un gráfico de barras apiladas en 3D|
|Bar3D100PorcentajeApilado|Representa un gráfico de barras 100 % apiladas en 3D|
|Línea|Representa un gráfico de líneas|
|líneaapilada|Representa un gráfico de líneas apiladas|
|Línea100PorcentajeApilado|Representa un gráfico de líneas 100% apiladas|
|Línea con marcadores de datos|Representa un gráfico de líneas con marcadores de datos.|
|Línea apilada con marcadores de datos|Representa un gráfico de líneas apiladas con marcadores de datos|
|Línea 100 por ciento apilada con marcadores de datos|Representa un gráfico de líneas 100 % apiladas con marcadores de datos|
|Línea 3D|Representa un gráfico de líneas 3D|
|Tarta|Representa un gráfico circular|
|pastel3D|Representa un gráfico circular 3D|
|Pastel Pastel|Representa un gráfico circular|
|PastelExplotado|Representa un gráfico circular desglosado|
|pastel3DExplotado|Representa un gráfico circular despiezado en 3D|
|Barra de pastel|Representa la barra del gráfico circular|
|Dispersión|Representa un gráfico de dispersión|
|Dispersión conectada por curvas con marcador de datos|Representa un gráfico de dispersión conectado por curvas, con marcadores de datos|
|Dispersión conectada por curvas sin marcador de datos|Representa un gráfico de dispersión conectado por curvas, sin marcadores de datos|
|DispersiónConnectedByLinesWithDataMarker|Representa un gráfico de dispersión conectado por líneas, con marcadores de datos|
|DispersiónConectadoPorLineasSinMarcadorDeDatos|Representa un gráfico de dispersión conectado por líneas, sin marcadores de datos|
|Área|Representa un gráfico de áreas|
|ÁreaApilada|Representa un gráfico de áreas apiladas|
|Área100PorCientoApilado|Representa un gráfico de áreas 100% apiladas|
|Área3D|Representa un gráfico de áreas 3D|
|Área3DSapiladas|Representa un gráfico de áreas apiladas en 3D|
|Área3D100PorcentajeApilado|Representa un gráfico de áreas 100% apiladas en 3D|
|Rosquilla|Representa el gráfico de anillos|
|DonutExplotado|Representa un gráfico de anillos desglosado|
|Radar|Representa un gráfico de radar|
|RadarConMarcadores De Datos|Representa un gráfico radial con marcadores de datos.|
|RadarLleno|Representa un gráfico de radar lleno|
|Superficie3D|Representa un gráfico de superficie 3D|
|SuperficieAlámbrica3D|Representa un gráfico de superficie 3D de estructura alámbrica|
|Contorno de superficie|Representa un gráfico de contorno|
|SuperficieContornoEstructura Alámbrica|Representa un gráfico de contorno de estructura alámbrica|
|Burbuja|Representa gráfico de burbujas|
|burbuja3d|Representa gráfico de burbujas 3D|
|Cilindro|Representa el gráfico de cilindros.|
|CilindroApilado|Representa un gráfico de cilindros apilados|
|Cilindro100PorCientoApilado|Representa un gráfico de cilindros 100 % apilados.|
|Barra cilíndrica|Representa un gráfico de barras cilíndricas.|
|CilindroBarApilados|Representa un gráfico de barras cilíndricas apiladas|
|Barra cilíndrica 100 por ciento apilada|Representa un gráfico de barras cilíndricas 100% apiladas|
|Columna Cilíndrica3D|Representa un gráfico de columnas cilíndricas 3D|
|Cono|Representa el gráfico de conos|
|ConoApilado|Representa un gráfico de conos apilados|
|Cono100PorCientoApilados|Representa un gráfico de conos 100% apilados|
|Barra cónica|Representa un gráfico de barras cónicas|
|Barra CónicaApiladas|Representa un gráfico de barras cónicas apiladas|
|Barra cónica 100 por ciento apilada|Representa un gráfico de barras cónicas 100% apiladas|
|Columna Cónica3D|Representa un gráfico de columnas cónicas 3D|
|Pirámide|Representa el gráfico piramidal|
|pirámideapilada|Representa un gráfico piramidal apilado|
|Pirámide100PorCientoApilados|Representa un gráfico piramidal 100% apilado|
|Barra Pirámide|Representa un gráfico de barras piramidal|
|PirámideBarApilados|Representa un gráfico de barras piramidales apiladas|
|PyramidBar100PorcentajeApilado|Representa un gráfico de barras piramidal 100% apilado|
|PirámideColumna3D|Representa un gráfico de columnas piramidal 3D|
{{% alert color="primary" %}}

Cuando asigna un rango de celdas como fuente de datos, solo puede establecer el rango desde la parte superior izquierda hasta la parte inferior derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" no es válido.

{{% /alert %}}

####  **Gráfico piramidal**

Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **Gráfico de linea**

 En el ejemplo anterior, simplemente cambiando el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) a*Línea*crea un gráfico de líneas. La fuente completa se proporciona a continuación. cuando se ejecuta el código, se agrega un gráfico de líneas a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **Gráfico de burbujas**

 Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) tiene que estar configurado en[**Tipo de gráfico.Burbuja**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)y algunas propiedades adicionales, como BubbleSizes, Values y XValues, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo.

####  **Línea con gráfico de marcador de datos**

 Para crear una línea con el gráfico de marcadores de datos,[**Tipo de gráfico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)tiene que estar configurado en*ChartType.LineWithDataMarkers*algunas propiedades adicionales, como el área de fondo, los marcadores de serie, los valores y los valores XV, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega una línea con el gráfico de marcador de datos a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **Temas avanzados**
- [Leer y manipular gráficos de Excel 2016](/cells/es/net/read-and-manipulate-excel-2016-charts/)
- [Administrar ejes de gráficos de Excel](/cells/es/net/chart-axes/)
- [Configuración de la apariencia del gráfico](/cells/es/net/setting-chart-appearance/)
- [Tipos de gráficos](/cells/es/net/chart-types/)
- [Personalización de gráficos](/cells/es/net/customizing-charts/)
- [Establecer fuente de datos para el gráfico](/cells/es/net/data-formatting-in-charts/)
- [Administrar etiquetas de datos de gráficos de Excel](/cells/es/net/insert-datalabels-to-chart/)
- [Generar gráfico procesando marcadores inteligentes](/cells/es/net/generate-chart-by-processing-smart-markers/)
- [Obtener la hoja de trabajo del gráfico](/cells/es/net/get-worksheet-of-the-chart/)
- [Administrar gráficos de leyenda de Excel](/cells/es/net/chart-legend/)
- [Manipular el tamaño de la posición y el gráfico del diseñador](/cells/es/net/manipulate-position-size-and-designer-chart/)
- [Crear un gráfico circular con líneas guía](/cells/es/net/creating-pie-chart-with-leader-lines/)
- [Formas en gráficos](/cells/es/net/controls-in-charts/)
- [Administrar títulos de gráficos de Excel](/cells/es/net/chart-and-axis-titles/)
- [Representación de gráficos](/cells/es/net/chart-rendering/)
- [Obtener el texto de la ecuación de la línea de tendencia del gráfico](/cells/es/net/get-equation-text-of-chart-trendline/)
