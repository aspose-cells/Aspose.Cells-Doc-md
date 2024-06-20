---
title: Controles en gráficos
linktitle: Formas en el gráfico
type: docs
weight: 60
url: /es/java/controls-in-charts/
---

{{% alert color="primary" %}}

A veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc., en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Agregar control de etiqueta al gráfico**

Las etiquetas proporcionan un medio para dar información a los usuarios sobre el contenido de la hoja de cálculo. Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) proporciona un método llamado [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), utilizado para agregar un control de etiqueta a un gráfico. A continuación se muestra una lista de los parámetros utilizados para el método:

- **arriba** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento horizontal de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **width** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto de la clase [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label), donde la clase [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) representa una etiqueta en el gráfico. Tiene algunos miembros importantes, como se detalla a continuación:

- La propiedad [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) especifica una cadena de título de la etiqueta.
- La propiedad [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) especifica los atributos del color de relleno.

El siguiente ejemplo muestra cómo agregar una etiqueta al gráfico. El ejemplo utiliza un archivo de diseño que tiene un gráfico en él. Utilizamos este archivo para insertar una etiqueta en el gráfico.

A continuación se muestra una captura de pantalla del archivo de diseño.

**El gráfico de diseño**

![todo:image_alt_text](controls-in-charts_1.png)

A continuación se muestra el código original para agregar una etiqueta al gráfico. El siguiente resultado se genera al ejecutar el código.

**Se añade una etiqueta en el gráfico**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Añadiendo un Control de Cuadro de Texto al Gráfico**

Una forma de resaltar información importante en un informe es mediante el uso de un cuadro de texto. Por ejemplo, introducir texto para resaltar el nombre de la empresa o indicar la región geográfica con mayores ventas. La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) proporciona un método llamado [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), que se utiliza para añadir un control de cuadro de texto a un gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **left** – el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** - la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** - el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto de la clase [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox), donde la clase [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo agregar un cuadro de texto a un gráfico. El ejemplo utiliza el archivo de diseño anterior que tiene un gráfico en él. Utilizamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico.

A continuación se muestra el código original para agregar un cuadro de texto al gráfico. El siguiente resultado se genera al ejecutar el código.

**Se añade un cuadro de texto en el gráfico**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Añadiendo una Imagen al Gráfico**

Aspose.Cells te permite insertar imágenes en un gráfico. Por ejemplo, agregar una imagen para resaltar o dar más significado a un gráfico o sus contenidos, o insertar un archivo de imagen de marca.

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) proporciona un método llamado [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), que se utiliza para añadir un objeto de imagen al gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **flujo** - un objeto de flujo que contiene los datos de la imagen.
- **escalaAncho** - la escala del ancho de la imagen, un valor porcentual.
- **escalaAlto** - la escala de la altura de la imagen, un valor porcentual.

El método devuelve un objeto de la clase [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) donde la clase [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) representa un objeto imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseño anterior que tiene un gráfico en él. Usamos este archivo para insertar una imagen en el gráfico.

A continuación se muestra el código original para agregar una imagen al gráfico. La siguiente salida se genera al ejecutar el código

**Se inserta una imagen en el gráfico**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Agregar casilla de verificación en el gráfico**

Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico mediante la enumeración [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType). El siguiente ejemplo demuestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:image_alt_text](controls-in-charts_5.jpg)

El [archivo de salida](InsertCheckboxInChartSheet_out.xlsx) generado por el siguiente fragmento de código se adjunta para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
