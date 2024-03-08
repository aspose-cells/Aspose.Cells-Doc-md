---
title: Personalización de gráficos
type: docs
weight: 15
url: /es/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **Crear gráficos**

Es posible agregar una variedad de gráficos a las hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. En este tema se analizan los objetos de gráficos Aspose.Cells'.

###  **Simplemente creando un gráfico**

Es sencillo crear un gráfico con Aspose.Cells con los siguientes códigos de ejemplo:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **Cosas que debe saber para crear un gráfico**

Antes de crear gráficos, es importante comprender algunos conceptos básicos que resultan útiles al crear gráficos utilizando Aspose.Cells.

####  **Objetos gráficos**

Aspose.Cells proporciona un conjunto especial de clases que se utilizan para crear todo tipo de gráficos. Estas clases se utilizan para crear *objetos de gráficos**, que actúan como bloques de construcción del gráfico. Los objetos de gráficos se enumeran a continuación:

- [**Eje**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), el eje de un gráfico.
- [**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un único gráfico de Excel.
- [**Área del gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), el área del gráfico en la hoja de trabajo.
- [**Tabla de datos del gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabla de datos del gráfico.
- [**Marco de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), el objeto de marco en un gráfico.
- [**Punto de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un solo punto en una serie en un gráfico.
- [**Colección ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una colección que contiene todos los puntos de una serie.
- [**Colección de gráficos**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , una coleccion de[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objetos.
-  DataLabels, DataLabels para lo especificado[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**Punto de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Línea de tendencia**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**Formato de relleno**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), rellena el formato de una forma.
- [**Piso**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)el suelo de un gráfico 3D.
- [**Leyenda**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la leyenda del gráfico.
- [**Línea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la línea del gráfico.
- [**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , una coleccion de[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objetos.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), representa una única serie de datos en un gráfico.
- [**Etiquetas de marca**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), las etiquetas de marcas asociadas con las marcas en un eje del gráfico.
- [**Título**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), el título de un gráfico o eje.
- [**Línea de tendencia**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una línea de tendencia en un gráfico.
- [**Colección Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una colección de todos los objetos Trendline para la serie de datos especificada.
- [**Paredes**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), las paredes de un gráfico 3D.

####  **Usar objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus respectivas clases y proporcionan propiedades y métodos específicos para realizar tareas específicas. Utilice objetos de gráficos para crear gráficos.

 Agregue cualquier tipo de gráfico a una hoja de trabajo usando el[**Colección de gráficos**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) recopilación. Cada elemento en el[**Colección de gráficos**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) colección representa un[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objeto. A[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)El objeto encapsula todos los objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo utilizar algunos objetos gráficos básicos para crear un gráfico simple.

###  **Crear un gráfico simple**

Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración denominada[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Los tipos de gráficos predefinidos son:

|**Tipos de gráficos**|**Descripción**|
| :- | :- |
|Columna|Representa el gráfico de columnas agrupadas|
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
|Dispersión|Representa el gráfico de dispersión|
|Dispersión conectada por curvas con marcador de datos|Representa el gráfico de dispersión conectado por curvas, con marcadores de datos.|
|Dispersión conectada por curvas sin marcador de datos|Representa el gráfico de dispersión conectado por curvas, sin marcadores de datos.|
|DispersiónConnectedByLinesWithDataMarker|Representa el gráfico de dispersión conectado por líneas, con marcadores de datos.|
|DispersiónConectadoPorLineasSinMarcadorDeDatos|Representa el gráfico de dispersión conectado por líneas, sin marcadores de datos.|
|Área|Representa un gráfico de áreas|
|ÁreaApilada|Representa un gráfico de áreas apiladas|
|Área100PorCientoApilado|Representa un gráfico de áreas 100% apiladas|
|Área3D|Representa un gráfico de áreas 3D|
|Área3DSapiladas|Representa un gráfico de áreas apiladas en 3D|
|Área3D100PorcentajeApilado|Representa un gráfico de áreas 100% apiladas en 3D|
|Rosquilla|Representa el gráfico de anillos|
|DonutExplotado|Representa un gráfico de anillos desglosado|
|Radar|Representa el gráfico de radar|
|RadarConMarcadores De Datos|Representa el gráfico radial con marcadores de datos.|
|RadarLleno|Representa un gráfico de radar lleno|
|Superficie3D|Representa un gráfico de superficie 3D|
|SuperficieAlámbrica3D|Representa el gráfico de superficie 3D de estructura alámbrica.|
|Contorno de superficie|Representa un gráfico de contorno|
|SuperficieContornoEstructura Alámbrica|Representa un gráfico de contorno de estructura alámbrica|
|Burbuja|Representa gráfico de burbujas|
|burbuja3d|Representa gráfico de burbujas 3D|
|Cilindro|Representa el gráfico de cilindros.|
|CilindroApilado|Representa un gráfico de cilindros apilados|
|Cilindro100PorCientoApilado|Representa un gráfico de cilindros 100 % apilados.|
|Barra cilíndrica|Representa un gráfico de barras cilíndricas.|
|CilíndricoBarApilados|Representa un gráfico de barras cilíndricas apiladas|
|CilíndricoBarra100PorCientoApilado|Representa un gráfico de barras cilíndricas 100% apiladas|
|CilíndricoColumna3D|Representa un gráfico de columnas cilíndricas 3D|
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
|Barra Pirámide|Representa el gráfico de barras piramidal.|
|PirámideBarApilados|Representa un gráfico de barras piramidales apiladas|
|PyramidBar100PorcentajeApilado|Representa un gráfico de barras piramidal 100% apilado|
|PirámideColumna3D|Representa un gráfico de columnas piramidal 3D|
Para crear un gráfico usando Aspose.Cells:

1. Agregue algunos datos a las celdas de la hoja de trabajo con el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objetos[**valor ajustado**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)método.
 Esto se utilizará como fuente de datos para el gráfico.
1.  Agregue un gráfico a la hoja de trabajo llamando al[**Colección de gráficos**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) colección[*agregar*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) método, encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objeto.
1.  Especifique el tipo de gráfico con el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)enumeración.
 Por ejemplo, el ejemplo utiliza el[**Tipo de gráfico.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)valor como tipo de gráfico.
1.  Accede a lo nuevo[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objeto de la[**Colección de gráficos**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)colección pasando su índice.
1.  Utilice cualquiera de los objetos de gráficos encapsulados en el[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Objeto para gestionar el gráfico.
 El siguiente ejemplo utiliza el[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objeto de gráfico para especificar la fuente de datos del gráfico.

Al agregar datos de origen al gráfico, el origen de datos puede ser un rango de celdas (como "A1:C3"), una secuencia de celdas no contiguas (como "A1, A3, A5") o una secuencia de valores (como "1,2,3").

{{% alert color="primary" %}}

Cuando asigna un rango de celdas como fuente de datos, solo puede establecer el rango desde la parte superior izquierda hasta la parte inferior derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" no es válido.

{{% /alert %}}

Estos pasos generales le permiten crear cualquier tipo de gráfico. Utilice diferentes objetos de gráficos para crear diferentes gráficos.

Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de trabajo como se muestra a continuación.

**Gráfico piramidal con su fuente de datos.**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)tiene que estar configurado en[**Tipo de gráfico.BURBUJA**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)algunas propiedades adicionales, como BubbleSizes, Values y XValues, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo como se muestra a continuación.

**Gráfico de burbujas con su fuente de datos.**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **Línea con gráfico de marcador de datos**

Para crear una línea con un gráfico de marcador de datos, el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)tiene que estar configurado en[**Tipo de gráfico.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) y algunas propiedades adicionales, como el área de fondo, los marcadores de serie, los valores y los valores XV, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega una línea con un gráfico de marcador de datos a la hoja de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **Crear gráficos personalizados**

Hasta ahora, cuando hemos analizado los gráficos, hemos analizado los gráficos estándar que tienen sus configuraciones de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero Aspose.Cells también admite la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato.

###  **Crear gráficos personalizados**

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución usando Aspose.Cells simple API.

 Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objeto mientras que el[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objeto sirve como una colección de[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objetos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de utilizar diferentes tipos de gráficos para diferentes series de datos (recopilados en un[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objeto).

{{% alert color="primary" %}}

 Actualmente, Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de pila de columnas, pero en futuras versiones se admitirán más gráficos. Para obtener una lista completa de los gráficos estándar que admite Aspose.Cells, lea el[Tipos de gráficos](/cells/es/java/chart-types/) artículo.

{{% /alert %}}

El siguiente código de ejemplo demuestra cómo crear gráficos personalizados. En este ejemplo, usaremos un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo.

**Gráfico personalizado que combina gráficos de columnas y líneas**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Ejemplo de programación**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Para ver una lista de los tipos de gráficos admitidos, lea el[Tipos de gráficos](/cells/es/java/chart-types/) artículo.

{{% /alert %}}

