---
title: Personalización de gráficos
type: docs
weight: 15
url: /es/java/creating-and-customizing-charts/
---
## **Creación de gráficos**

Es posible agregar una variedad de gráficos a las hojas de cálculo con Aspose.Cells. Aspose.Cells proporciona muchos objetos de gráficos flexibles. Este tema trata sobre los objetos de gráficos Aspose.Cells.

### **Simplemente creando un gráfico**

Es sencillo crear un gráfico con Aspose.Cells con los siguientes códigos de ejemplo:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Cosas que debe saber para crear un gráfico**

Antes de crear gráficos, es importante comprender algunos conceptos básicos que son útiles al crear gráficos con Aspose.Cells.

#### **Objetos de gráficos**

 Aspose.Cells proporciona un conjunto especial de clases que se utilizan para crear todo tipo de gráficos. Estas clases se utilizan para crear**graficando objetos**, que actúan como bloques de creación de gráficos. Los objetos gráficos se enumeran a continuación:

- [**Eje**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), el eje de un gráfico.
- [**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un único gráfico de Excel.
- [**Área de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), el área del gráfico en la hoja de cálculo.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabla de datos de gráficos.
- [**GráficoMarco**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), el objeto de marco en un gráfico.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un solo punto en una serie en un gráfico.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una colección que contiene todos los puntos de una serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , una coleccion de[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objetos.
-  DataLabels, DataLabels para el especificado[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**línea de tendencia**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**Formato de relleno**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), formato de relleno para una forma.
- [**Piso**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), el suelo de un gráfico 3D.
- [**Leyenda**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la leyenda del gráfico.
- [**Línea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la línea del gráfico.
- [**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , una coleccion de[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objetos.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), representa una única serie de datos en un gráfico.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), las etiquetas de marca de graduación asociadas con las marcas de graduación en un eje de gráfico.
- [**Título**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), el título de un gráfico o eje.
- [**línea de tendencia**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una línea de tendencia en un gráfico.
- [**Colección Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una colección de todos los objetos Trendline para la serie de datos especificada.
- [**Paredes**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), las paredes de un gráfico 3D.

#### **Uso de objetos de gráficos**

Como se mencionó anteriormente, todos los objetos de gráficos son instancias de sus respectivas clases y proporcionan propiedades y métodos específicos para realizar tareas específicas. Use objetos de gráficos para crear gráficos.

Agregue cualquier tipo de gráfico a una hoja de trabajo usando el[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) recopilación. Cada artículo en el[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) colección representa un[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objeto. A[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)El objeto encapsula todos los objetos de gráficos necesarios para personalizar la apariencia del gráfico. La siguiente sección muestra cómo usar algunos objetos gráficos básicos para crear un gráfico simple.

### **Crear un gráfico simple**

 Es posible crear muchos tipos diferentes de gráficos con Aspose.Cells. Todos los gráficos estándar admitidos por Aspose.Cells están predefinidos en una enumeración denominada[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Los tipos de gráficos predefinidos son:

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
|Radar|Representa el gráfico de radar|
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
|CilíndricoBar|Representa el gráfico de barras cilíndricas.|
|CilíndricoBarApilado|Representa el gráfico de barras cilíndricas apiladas|
|CilíndricoBar100PorcentajeApilado|Representa un gráfico de barras cilíndricas apiladas al 100 %|
|CilíndricoColumna3D|Representa el gráfico de columnas cilíndricas en 3D|
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
Para crear un gráfico usando Aspose.Cells:

1.  Agregue algunos datos a las celdas de la hoja de trabajo con el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) objetos[**valor ajustado**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)método.
 Esto se utilizará como fuente de datos para el gráfico.
1.  Agregue un gráfico a la hoja de trabajo llamando al[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) colección[*agregar*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) método, encapsulado en el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)objeto.
1.  Especifique el tipo de gráfico con el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)enumeración.
 Por ejemplo, el ejemplo utiliza el[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)value como el tipo de gráfico.
1.  Accede al nuevo[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) objeto de la[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)colección pasando su índice.
1.  Utilice cualquiera de los objetos de gráficos encapsulados en el[**Cuadro**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)objeto para gestionar el gráfico.
 El siguiente ejemplo utiliza el[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objeto de gráfico para especificar la fuente de datos del gráfico.

Al agregar datos de origen al gráfico, el origen de datos puede ser un rango de celdas (como "A1:C3"), una secuencia de celdas no contiguas (como "A1, A3, A5") o una secuencia de valores (como "1,2,3").

{{% alert color="primary" %}}

Cuando asigna un rango de celdas como fuente de datos, solo puede establecer el rango de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido mientras que "C3:A1" no es válido.

{{% /alert %}}

Estos pasos generales le permiten crear cualquier tipo de gráfico. Use diferentes objetos de gráficos para crear diferentes gráficos.

Cuando se ejecuta el código de ejemplo, se agrega un gráfico piramidal a la hoja de trabajo como se muestra a continuación.

**Gráfico piramidal con su fuente de datos**

![todo:imagen_alternativa_texto](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Para crear un gráfico de burbujas, el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)tiene que ser configurado para[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)y algunas propiedades adicionales, como BubbleSizes, Values y XValues, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega un gráfico de burbujas a la hoja de trabajo, como se muestra a continuación.

**Gráfico de burbujas con su fuente de datos**

![todo:imagen_alternativa_texto](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Línea con gráfico de marcador de datos**

Para crear una línea con un gráfico de marcador de datos, el[**Tipo de gráfico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)tiene que ser configurado para[**Tipo de gráfico.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) y algunas propiedades adicionales, como el área de fondo, los marcadores de serie, los valores y los valores XV, deben configurarse en consecuencia. Al ejecutar el siguiente código, se agrega una línea con un gráfico de marcador de datos a la hoja de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos discutido los gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero Aspose.Cells también admite la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con su propia configuración de formato.

### **Creación de gráficos personalizados**

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells simple API.

 Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objeto mientras que el[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objeto sirve como una colección de[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)objetos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recopilados en un[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)objeto).

{{% alert color="primary" %}}

 Actualmente, Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de pila de columnas, pero se admitirán más gráficos en versiones futuras. Para obtener una lista completa de los gráficos estándar compatibles con Aspose.Cells, lea el[Tipos de gráficos](/cells/es/java/chart-types/) artículo.

{{% /alert %}}

El siguiente código de ejemplo muestra cómo crear gráficos personalizados. En este ejemplo, vamos a utilizar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo.

**Gráfico personalizado que combina gráficos de columnas y líneas**

![todo:imagen_alternativa_texto](creating-and-customizing-charts_3.png)

**Ejemplo de programación**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Para ver una lista de los tipos de gráficos admitidos, lea la[Tipos de gráficos](/cells/es/java/chart-types/) artículo.

{{% /alert %}}

