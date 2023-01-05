---
title: Formas en gráficos
type: docs
weight: 70
url: /es/net/controls-in-charts/
---
{{% alert color="primary" %}}

veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc. en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Adición de control de etiquetas al gráfico**

Las etiquetas proporcionan un medio para dar información a los usuarios sobre el contenido de una hoja de cálculo.
Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

Él[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), utilizado para agregar un control de etiqueta a un gráfico. A continuación se muestra una lista de los parámetros utilizados para el método:

- **parte superior** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

 El método vuelve[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)objeto. Él[**Etiqueta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) class representa una etiqueta en el gráfico. Tiene algunos miembros importantes:

- [**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(propiedad): especifica la cadena de título de una etiqueta.
- [**Llenar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (propiedad): especifica los atributos de color de relleno.

El siguiente ejemplo muestra cómo agregar una etiqueta al gráfico. El ejemplo utiliza un archivo de diseñador (**exp_piechart.xls**) que tiene un gráfico en él. Usamos este archivo para insertar una etiqueta en el gráfico. A continuación se muestra el código original para agregar una etiqueta al gráfico. El siguiente resultado se genera al ejecutar el código.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Adición de control de cuadro de texto al gráfico**

 Una forma de resaltar información importante en un informe es utilizar un cuadro de texto. Por ejemplo, ingrese texto para resaltar el nombre de la empresa o para indicar la región geográfica con las ventas más altas. Él[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)que se utiliza para agregar un control de cuadro de texto a un gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **parte superior** – el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura**– la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

 El método vuelve[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) objeto. Él[**Caja de texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)class representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo agregar un cuadro de texto a un gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico. A continuación se muestra el código original para agregar un cuadro de texto al gráfico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Agregar imagen al gráfico**

Aspose.Cells le permite insertar imágenes en un gráfico. Por ejemplo, agregue una imagen para enfatizar o dar más significado a un gráfico o su contenido, o inserte un archivo de imagen de marca.

 Él[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AgregarImagenEnGráfico**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), que se utiliza para agregar un objeto de imagen al gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **parte superior**– el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda**– el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **arroyo** – un objeto de flujo que contiene los datos de la imagen.
- **anchoEscala** – la escala del ancho de la imagen, un valor porcentual.
- **alturaEscala** – la escala de altura de la imagen, un valor porcentual.

 El método devuelve un[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objeto. Él[**Fotografía**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)class representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Usamos este archivo para insertar una imagen en el gráfico. A continuación se muestra el código original para agregar una imagen al gráfico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Agregar casilla de verificación en el gráfico**

 Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico utilizando[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) enumeración. El siguiente ejemplo muestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:imagen_alternativa_texto](controls-in-charts_1.jpg)

 Él[archivo de salida](101089316.xlsx)generado por el siguiente fragmento de código se adjunta para su referencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Temas avanzados**
- [Agregar marca de agua de WordArt al gráfico](/cells/es/net/add-wordart-watermark-to-chart/)
