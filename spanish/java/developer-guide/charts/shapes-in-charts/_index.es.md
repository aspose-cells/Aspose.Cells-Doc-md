---
title: Controles en Gráficos
linktitle: Formas en el gráfico
type: docs
weight: 60
url: /es/java/controls-in-charts/
---
{{% alert color="primary" %}}

veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc. en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Adición de control de etiquetas al gráfico**

Las etiquetas proporcionan un medio para dar información a los usuarios sobre el contenido de una hoja de cálculo. Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

 Él[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) clase proporciona un método llamado[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), que se usa para agregar un control de etiqueta a un gráfico. A continuación se muestra una lista de los parámetros utilizados para el método:

- **parte superior** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

 El método devuelve un objeto de la[**Etiqueta**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) clase, donde el[**Etiqueta**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)class representa una etiqueta en el gráfico. Tiene algunos miembros importantes como se detalla a continuación:

- [**Texto**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)La propiedad especifica la cadena de título de una etiqueta.
- [**Llenar**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) La propiedad especifica los atributos de color de relleno.

El siguiente ejemplo muestra cómo agregar una etiqueta al gráfico. El ejemplo utiliza un archivo de diseñador que tiene un gráfico. Usamos este archivo para insertar una etiqueta en el gráfico.

A continuación se muestra una captura de pantalla del archivo del diseñador.

**El gráfico del diseñador**

![todo:imagen_alternativa_texto](controls-in-charts_1.png)

A continuación se muestra el código original para agregar una etiqueta al gráfico. El siguiente resultado se genera al ejecutar el código.

**Se agrega una etiqueta en el gráfico.**

![todo:imagen_alternativa_texto](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Adición de control de cuadro de texto al gráfico**

 Una forma de resaltar información importante en un informe es utilizar un cuadro de texto. Por ejemplo, ingrese texto para resaltar el nombre de la empresa o para indicar la región geográfica con las ventas más altas. Él[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) clase proporciona un método llamado[**agregarTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), que se utiliza para agregar un control de cuadro de texto a un gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **parte superior** – el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura**– la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

 El método devuelve un objeto de la[**Caja de texto**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) clase donde el[**Caja de texto**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)class representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo agregar un cuadro de texto a un gráfico. El ejemplo utiliza el archivo de diseñador anterior que tiene un gráfico. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico.

A continuación se muestra el código original para agregar un cuadro de texto al gráfico. El siguiente resultado se genera al ejecutar el código.

**Se agrega un cuadro de texto en el gráfico.**

![todo:imagen_alternativa_texto](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Agregar imagen al gráfico**

Aspose.Cells le permite insertar imágenes en un gráfico. Por ejemplo, agregue una imagen para enfatizar o dar más significado a un gráfico o su contenido, o inserte un archivo de imagen de marca.

 Él[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) clase proporciona un método llamado[**añadirPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), que se utiliza para agregar un objeto de imagen al gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **parte superior**– el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda**– el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **arroyo** – un objeto de flujo que contiene los datos de la imagen.
- **anchoEscala** – la escala del ancho de la imagen, un valor porcentual.
- **alturaEscala** – la escala de altura de la imagen, un valor porcentual.

 El método devuelve un objeto de la[**Fotografía**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) clase donde el[**Fotografía**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)class representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseñador anterior que tiene un gráfico. Usamos este archivo para insertar una imagen en el gráfico.

A continuación se muestra el código original para agregar una imagen al gráfico. El siguiente resultado se genera al ejecutar el código

**Se inserta una imagen en el gráfico.**

![todo:imagen_alternativa_texto](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Agregar casilla de verificación en el gráfico**

Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico utilizando[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) enumeración. El siguiente ejemplo muestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:imagen_alternativa_texto](controls-in-charts_5.jpg)

Él[archivo de salida](InsertCheckboxInChartSheet_out.xlsx)generado por el siguiente fragmento de código se adjunta para su referencia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
