---
title: Formato del gráfico
type: docs
weight: 20
url: /es/java/chart-formatting/
---

## **Configurar la apariencia del gráfico**

En [Tipos de gráficos](/cells/es/java/chart-types/), dimos una breve introducción a los tipos de gráficos y objetos de gráficos ofrecidos por Aspose.Cells.

En este artículo, discutimos cómo personalizar la apariencia de los gráficos configurando una serie de propiedades diferentes:

- [Configuración del área del gráfico](/cells/es/java/chart-formatting/#setting-chart-area).
- [Configuración de líneas de gráfico](/cells/es/java/chart-formatting/#setting-chart-lines).
- [Aplicar temas](/cells/es/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Configurar títulos para gráficos y ejes](/cells/es/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Trabajar con líneas de cuadrícula](/cells/es/java/chart-formatting/#setting-major-gridlines).
- [Configurar bordes para paredes traseras y laterales](/cells/es/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Configurando el área del gráfico**

Hay diferentes tipos de áreas en un gráfico y Aspose.Cells proporciona la flexibilidad de modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, color de fondo y formato de relleno, etc.

En el ejemplo dado a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- Área de trazado
- Área del gráfico
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) área
- El área de un solo punto en un [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas a la hoja de trabajo como se muestra a continuación:

**Un gráfico de columnas con áreas rellenas** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Configurando las líneas del gráfico**

Los desarrolladores también pueden aplicar diferentes tipos de estilos en las líneas o marcadores de datos del [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) como se muestra a continuación en el ejemplo. Al ejecutar el código de ejemplo, se agrega un gráfico de columnas a la hoja de trabajo como se muestra a continuación:

**Gráfico de columnas después de aplicar estilos de línea** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Aplicando temas de Microsoft Excel 2007/2010 a gráficos**

Los desarrolladores pueden aplicar diferentes temas y colores de Microsoft Excel al [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) u otros objetos de gráficos como se muestra en el ejemplo a continuación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Configuración de los Títulos de Gráficos o Ejes**

Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG como se muestra a continuación.

**Configuración de títulos de un gráfico y sus ejes utilizando Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen un método [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) que se puede usar para establecer sus títulos como se muestra en el siguiente ejemplo. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas a la hoja de cálculo como se muestra a continuación:

**Gráfico de columnas después de establecer los títulos** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Configuración de Líneas de Rejilla Principales**

#### **Ocultar líneas de cuadrícula principales**

Los desarrolladores pueden controlar la visibilidad de las líneas de rejilla principales mediante el uso del método [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) del objeto [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line). Después de ocultar las líneas de rejilla principales, un gráfico de columnas agregado a la hoja de cálculo tendrá el siguiente aspecto:

**Un gráfico de columnas con líneas de rejilla principales ocultas** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Cambiando la configuración de las líneas de cuadrícula principales**

Los desarrolladores no solo pueden controlar la visibilidad de las líneas de rejilla principales, sino también otras propiedades como su color, etc. Después de establecer el color de las líneas de rejilla principales, un gráfico de columnas agregado a la hoja de cálculo tendrá el siguiente aspecto:

**Gráfico de columnas con líneas de rejilla principales coloreadas** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Configuración de Bordes para Paredes Delanteras y Laterales**

Desde el lanzamiento de Microsoft Excel 2007, las paredes de un gráfico 3D se han dividido en dos partes: pared lateral y pared trasera, por lo que tenemos que usar dos objetos [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) para representarlas por separado y puedes acceder a ellas mediante [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) y [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

El ejemplo a continuación muestra cómo establecer el borde de la pared lateral utilizando diferentes atributos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Cambiar la Posición y el Tamaño del Gráfico**

A veces, quieres cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells proporciona la propiedad [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) para lograr esto. Puedes usar sus subpropiedades para cambiar el tamaño del gráfico con una nueva **altura** y **ancho** o reposicionarlo con nuevas coordenadas **X** y **Y**.

### **Modificación de la Posición y el Tamaño del Gráfico**

Para cambiar la posición (coordenadas X, Y) y el tamaño (altura, ancho) del gráfico, usa estas propiedades:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

El siguiente ejemplo explica el uso de las propiedades anteriores. Carga el libro de trabajo existente que contiene un gráfico en su primera hoja de trabajo. Luego redimensiona y reposiciona el gráfico y guarda el libro de trabajo.

Antes de la ejecución del código de ejemplo, el archivo fuente se ve así:

**Tamaño y posición del gráfico antes de la ejecución del código de ejemplo** 

![todo:image_alt_text](chart-formatting_7.png)

Después de la ejecución, el archivo de salida se ve así:

**Tamaño y posición del gráfico después de la ejecución del código de ejemplo** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulación de gráficos de diseñador**

Hay momentos en los que es posible que necesite manipular o modificar los gráficos en sus archivos de plantilla de diseñador. Aspose.Cells da soporte total para manipular gráficos de diseñador con sus contenidos y elementos. Los datos, contenidos del gráfico, imagen de fondo y formato se pueden conservar con precisión.

### **Manipulación de gráficos de diseñador en los archivos de plantilla**

Para manipular gráficos de diseñador en un archivo de plantilla, utilice todas las llamadas a la API relacionadas con el gráfico. Por ejemplo, use la propiedad [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) para obtener la colección de gráficos existente en el archivo de plantilla.

#### **Creación de un gráfico**

El siguiente ejemplo muestra cómo crear un gráfico circular. Más adelante manipularemos este gráfico. El siguiente resultado es generado por el código.

**El gráfico circular de entrada** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulación del gráfico**

El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado previamente. El siguiente resultado es generado por el código. Tenga en cuenta que el color del título del gráfico ha cambiado de azul a negro y 'Inglaterra 30000' se ha cambiado a 'Reino Unido, 30K'.

**El gráfico circular ha sido modificado** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**

En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.

Primero, echa un vistazo al gráfico de líneas del diseñador.

**El gráfico de líneas de entrada** 

![todo:image_alt_text](chart-formatting_11.png)

Ahora manipulamos el gráfico de líneas (que se encuentra en el archivo **linechart.xls**) usando el siguiente código. La siguiente salida es generada por el código.

**El gráfico de líneas manipulado** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Usando Sparklines**

Microsoft Excel 2010 puede analizar la información de más maneras que nunca. Permite a los usuarios realizar un seguimiento y resaltar tendencias importantes de datos con nuevas herramientas de análisis y visualización de datos. Las sparklines son mini gráficos que se pueden colocar dentro de las celdas para que puedas ver los datos y el gráfico en la misma tabla. Cuando se usan sparklines de manera adecuada, el análisis de datos es más rápido y preciso. También proporcionan una vista simple de la información, evitando hojas de cálculo sobrecargadas con una gran cantidad de gráficos ocupados.

Aspose.Cells proporciona una API para manipular sparklines en hojas de cálculo.

### **Sparklines en Microsoft Excel**

Para insertar sparklines en Microsoft Excel 2010:

1. Selecciona las celdas donde quieres que aparezcan las sparklines. Para que sean fáciles de ver, selecciona las celdas al lado de los datos.
1. Haz clic en **Insertar** en la cinta y luego elige **columna** en el grupo de **Sparklines**.

![todo:image_alt_text](chart-formatting_13.png)

1. Selecciona o ingresa el rango de celdas en la hoja de cálculo que contenga los datos fuente.
   Los gráficos aparecen.

Las sparklines te ayudan a ver tendencias, por ejemplo, el récord de victorias o derrotas de una liga de softbol. Las sparklines incluso pueden resumir toda la temporada de cada equipo en la liga.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines usando Aspose.Cells**

Los desarrolladores pueden crear, eliminar o leer sparklines (en el archivo de plantilla) usando la API proporcionada por Aspose.Cells. Al agregar gráficos personalizados para un rango de datos dado, los desarrolladores tienen la libertad de agregar diferentes tipos de pequeños gráficos a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función de Sparklines. El ejemplo muestra cómo:

1. Abrir un archivo de plantilla simple.
1. Leer la información de sparklines para una hoja de cálculo.
1. Agregar nuevas miniaturas para un rango de datos dado a un área de celdas.
1. Guardar el archivo de Excel en disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Aplicación de formato 3D al gráfico**

Es posible que necesite estilos de gráficos en 3D para obtener solo los resultados necesarios para su escenario. Las API de Aspose.Cells proporcionan la API relevante para aplicar el formato 3D de Microsoft Excel 2007, como se demuestra en este artículo.

### **Estableciendo formato 3D al gráfico**

A continuación se proporciona un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D de Microsoft Excel 2007. Después de ejecutar el código de ejemplo anterior, se agregará un gráfico de columnas (con efectos 3D) a la hoja de cálculo como se muestra a continuación.

**Un gráfico de columnas con formato 3D**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Para obtener una lista completa de los tipos de gráficos 2D y 3D admitidos, consulte [Tipos de gráficos admitidos para renderizar](/cells/es/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Temas avanzados**
- [Establecer una imagen como relleno de fondo en el gráfico](/cells/es/java/set-picture-as-background-fill-in-the-chart/)
