---
title: Formato de gráfico
type: docs
weight: 20
url: /es/java/chart-formatting/
---
## **Configuración de la apariencia del gráfico**

 En[Tipos de gráficos](/cells/es/java/chart-types/), dimos una breve introducción a los tipos de gráficos y objetos de gráficos que ofrece Aspose.Cells.

En este artículo, discutimos cómo personalizar la apariencia de los gráficos configurando una serie de propiedades diferentes:

- [Configuración del área del gráfico](/cells/es/java/chart-formatting/#setting-chart-area).
- [Configuración de líneas de gráfico](/cells/es/java/chart-formatting/#setting-chart-lines).
- [Aplicar temas](/cells/es/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Establecer títulos para gráficos y ejes](/cells/es/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Trabajar con líneas de cuadrícula](/cells/es/java/chart-formatting/#setting-major-gridlines).
- [Configuración de bordes para paredes traseras y laterales](/cells/es/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Configuración del área del gráfico**

Hay diferentes tipos de áreas en un gráfico y Aspose.Cells brinda la flexibilidad de modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, color de fondo y formato de relleno, etc.

En el ejemplo que se muestra a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- área de parcela
- Área de gráfico
- [**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) zona
- El área de un solo punto en un[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas a la hoja de trabajo como se muestra a continuación:

**Un gráfico de columnas con áreas rellenas** 

![todo:imagen_alternativa_texto](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Configuración de líneas de gráfico**

 Los desarrolladores también pueden aplicar diferentes tipos de estilos en las líneas o marcadores de datos del[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)como se muestra a continuación en el ejemplo. Al ejecutar el código de ejemplo, se agrega un gráfico de columnas a la hoja de trabajo, como se muestra a continuación:

**Gráfico de columnas después de aplicar estilos de línea** 

![todo:imagen_alternativa_texto](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Aplicar Microsoft temas de Excel 2007/2010 a los gráficos**

Los desarrolladores pueden aplicar diferentes Microsoft temas y colores de Excel al[**SerieColección**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)u otros objetos del gráfico, como se muestra en el siguiente ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Configuración de los títulos de gráficos o ejes**

Puede usar Microsoft Excel para configurar los títulos de un gráfico y sus ejes en un entorno WYSIWYG como se muestra a continuación.

**Establecer títulos de un gráfico y sus ejes usando Microsoft Excel** 

![todo:imagen_alternativa_texto](chart-formatting_3.png)

 Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen un[**Título.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)método que se puede utilizar para establecer sus títulos como se muestra a continuación en un ejemplo. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas a la hoja de trabajo como se muestra a continuación:

**Gráfico de columnas después de configurar títulos** 

![todo:imagen_alternativa_texto](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Configuración de líneas de cuadrícula principales**

#### **Ocultar líneas de cuadrícula principales**

 Los desarrolladores pueden controlar la visibilidad de las principales líneas de cuadrícula mediante el[**conjuntoVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) metodo de la[**Línea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)objeto. Después de ocultar las líneas de cuadrícula principales, un gráfico de columnas agregado a la hoja de trabajo tiene la siguiente apariencia:

**Un gráfico de columnas con líneas de cuadrícula principales ocultas** 

![todo:imagen_alternativa_texto](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Cambio de la configuración de las líneas de cuadrícula principales**

Los desarrolladores no solo pueden controlar la visibilidad de las principales líneas de cuadrícula, sino también otras propiedades, incluido su color, etc. Después de establecer el color de las principales líneas de cuadrícula, un gráfico de columnas agregado a la hoja de trabajo tendrá la siguiente apariencia:

**Gráfico de columnas con líneas de cuadrícula principales coloreadas** 

![todo:imagen_alternativa_texto](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Configuración de bordes para paredes traseras y laterales**

 Desde el lanzamiento de Microsoft Excel 2007, las paredes de un gráfico 3D se han dividido en dos partes: pared lateral y pared trasera, por lo que tenemos que usar dos[**Paredes**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) objetos para representarlos por separado y puede acceder a ellos usando[**Gráfico.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) y[**Gráfico.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

El ejemplo que se muestra a continuación muestra cómo establecer el borde de la pared lateral usando diferentes atributos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Cambiar la posición y el tamaño del gráfico**

 A veces, desea cambiar la posición o el tamaño del gráfico nuevo o existente dentro de la hoja de trabajo. Aspose.Cells proporciona el[**Gráfico.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)propiedad para lograrlo. Puede usar sus subpropiedades para cambiar el tamaño del gráfico con nuevos**altura** y**ancho** o reubicarlo con nuevo** X** y**Coordenadas Y**.

### **Modificación de la posición y el tamaño del gráfico**

Para cambiar la posición del gráfico (coordenadas X, Y) y el tamaño (alto, ancho), use estas propiedades:

1. [**Gráfico.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Gráfico.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Gráfico.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Gráfico.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

El siguiente ejemplo explica el uso de las propiedades anteriores. Carga el libro de trabajo existente que contiene un gráfico en su primera hoja de trabajo. Luego, cambia el tamaño y la posición del gráfico y guarda el libro de trabajo.

Antes de la ejecución del código de muestra, el archivo fuente se ve así:

**Tamaño y posición del gráfico antes de la ejecución del código de muestra** 

![todo:imagen_alternativa_texto](chart-formatting_7.png)

Después de la ejecución, el archivo de salida se ve así:

**Tamaño y posición del gráfico después de la ejecución del código de muestra** 

![todo:imagen_alternativa_texto](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulación de gráficos de diseñador**

Hay un momento en el que es posible que necesite manipular o modificar los gráficos en los archivos de plantilla de su diseñador. Aspose.Cells es totalmente compatible con la manipulación de gráficos de diseño con sus contenidos y elementos. Los datos, el contenido del gráfico, la imagen de fondo y el formato se pueden conservar con precisión.

### **Manipulación de gráficos de Designer en los archivos de plantilla**

 Para manipular gráficos de diseñador en un archivo de plantilla, use todas las llamadas relacionadas con gráficos API. Por ejemplo, use[**Hoja de trabajo.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) propiedad para obtener la colección de gráficos existente en el archivo de plantilla.

#### **Crear un gráfico**

El siguiente ejemplo muestra cómo crear un gráfico circular. Manipularemos este gráfico más adelante. El siguiente resultado es generado por el código.

**El gráfico circular de entrada** 

![todo:imagen_alternativa_texto](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulación del gráfico**

El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo modificamos el gráfico creado anteriormente. El siguiente resultado es generado por el código. Tenga en cuenta que el color del título del gráfico ha cambiado de azul a negro y que 'Inglaterra 30000' se ha cambiado a 'Reino Unido, 30K'.

**El gráfico circular ha sido modificado.** 

![todo:imagen_alternativa_texto](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulación de un gráfico de líneas en la plantilla del diseñador**

En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.

Primero, eche un vistazo al gráfico de líneas del diseñador.

**El gráfico de líneas de entrada** 

![todo:imagen_alternativa_texto](chart-formatting_11.png)

 Ahora manipulamos el gráfico de líneas (que está contenido en el**gráfico de líneas.xls** archivo) usando el siguiente código. El siguiente resultado es generado por el código.

**El gráfico de líneas manipulado** 

![todo:imagen_alternativa_texto](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Uso de minigráficos**

Microsoft Excel 2010 puede analizar la información de más formas que nunca. Permite a los usuarios rastrear y resaltar tendencias de datos importantes con nuevas herramientas de visualización y análisis de datos. Los minigráficos son minigráficos que puede colocar dentro de las celdas para poder ver los datos y el gráfico en la misma tabla. Cuando los minigráficos se utilizan correctamente, el análisis de datos es más rápido y más preciso. También brindan una vista simple de la información, evitando hojas de trabajo abarrotadas con muchos gráficos ocupados.

Aspose.Cells proporciona un API para manipular minigráficos en hojas de cálculo.

### **Minigráficos en Microsoft Excel**

Para insertar minigráficos en Microsoft Excel 2010:

1. Seleccione las celdas donde desea que aparezcan los minigráficos. Para que sean fáciles de ver, seleccione celdas al lado de los datos.
1.  Hacer clic**Insertar** en la cinta y luego elija**columna** en el**minigráficos** grupo.

![todo:imagen_alternativa_texto](chart-formatting_13.png)

1. Seleccione o ingrese el rango de celdas en la hoja de cálculo que contiene los datos de origen.
 Aparecen los gráficos.

Los minigráficos lo ayudan a ver tendencias, por ejemplo, o el registro de victorias o derrotas de una liga de softbol. Los minigráficos pueden incluso resumir la temporada completa de cada equipo de la liga.

![todo:imagen_alternativa_texto](chart-formatting_14.png)

### **Minigráficos usando Aspose.Cells**

Los desarrolladores pueden crear, eliminar o leer minigráficos (en el archivo de plantilla) utilizando el API proporcionado por Aspose.Cells. Al agregar gráficos personalizados para un rango de datos determinado, los desarrolladores tienen la libertad de agregar diferentes tipos de gráficos diminutos a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función Minigráficos. El ejemplo muestra cómo:

1. Abra un archivo de plantilla simple.
1. Leer información de minigráficos para una hoja de trabajo.
1. Agregue nuevos minigráficos para un rango de datos dado a un área de celda.
1. Guarda el archivo de Excel en el disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Aplicar formato 3D al gráfico**

Es posible que necesite estilos de gráficos en 3D para poder obtener solo los resultados de su escenario. Las API Aspose.Cells proporcionan el API relevante para aplicar el formato 3D Microsoft de Excel 2007 como se muestra en este artículo.

### **Configuración del formato 3D en el gráfico**

continuación se proporciona un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D Microsoft Excel 2007. Después de ejecutar el código de ejemplo anterior, se agregará un gráfico de columnas (con efectos 3D) a la hoja de trabajo, como se muestra a continuación.

**Un gráfico de columnas con formato 3D**

![todo:imagen_alternativa_texto](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 Para obtener una lista completa de los gráficos 2D y 3D compatibles, consulte[Tipos de gráficos admitidos para la representación](/cells/es/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Temas avanzados**
- [Establecer imagen como fondo Rellenar el gráfico](/cells/es/java/set-picture-as-background-fill-in-the-chart/)
