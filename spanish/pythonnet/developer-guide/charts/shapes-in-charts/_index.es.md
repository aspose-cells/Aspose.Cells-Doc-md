---
title: Formas en gráficos
description: Aprende cómo usar Aspose.Cells para Python via .NET para agregar controles y personalizar gráficos en Microsoft Excel. Nuestra guía demostrará cómo manipular elementos del gráfico, ajustar el formato y mejorar la apariencia y usabilidad general de tus gráficos.
keywords: Aspose.Cells para Python via .NET, controles de gráficos, personalización de gráficos, Microsoft Excel, elementos del gráfico, formato.
type: docs
weight: 70
url: /es/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

A veces necesitas insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes y otros en un gráfico. Aspose.Cells para Python via .NET puede agregar controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Agregar control de etiqueta al gráfico**

Las etiquetas proporcionan un medio para proporcionar información a los usuarios sobre el contenido de una hoja de cálculo.
Aspose.Cells para Python via .NET permite agregar y manipular etiquetas incluso en gráficos.

La clase [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart), utilizado para agregar un control de etiqueta a un gráfico. A continuación, se muestra una lista de los parámetros utilizados para el método:

- **arriba** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento horizontal de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). La clase [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) representa una etiqueta en el gráfico. Tiene algunos miembros importantes:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (propiedad) - especifica la cadena de título de una etiqueta.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (propiedad) - especifica los atributos del color de relleno.

Con el siguiente ejemplo se muestra cómo añadir una etiqueta al gráfico. El ejemplo utiliza un archivo del diseñador (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar una etiqueta en el gráfico. A continuación se muestra el código original para añadir una etiqueta al gráfico. La siguiente salida se genera al ejecutar el código.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Añadiendo un Control de Cuadro de Texto al Gráfico**

Una forma de resaltar información importante en un informe es mediante el uso de un cuadro de texto. Por ejemplo, introducir texto para resaltar el nombre de la empresa o indicar la región geográfica con mayores ventas. La clase [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart), que se utiliza para añadir un control de cuadro de texto a un gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** - la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** - el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox). La clase [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo añadir un cuadro de texto a un gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico. A continuación se muestra el código original para añadir un cuadro de texto al gráfico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Añadiendo una Imagen al Gráfico**

Aspose.Cells para Python via .NET permite insertar imágenes en un gráfico. Por ejemplo, agregar una imagen para enfatizar o dar más significado a un gráfico o a su contenido, o insertar un archivo de imagen de marca.

La clase [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart), que se utiliza para añadir un objeto de imagen al gráfico. A continuación se muestra la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **flujo** - un objeto de flujo que contiene los datos de la imagen.
- **escalaAncho** - la escala del ancho de la imagen, un valor porcentual.
- **escalaAlto** - la escala de la altura de la imagen, un valor porcentual.

El método devuelve un objeto [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). La clase [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Utilizamos este archivo para insertar una imagen en el gráfico. A continuación se muestra el código original para agregar una imagen al gráfico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Agregar casilla de verificación en el gráfico**

Aspose.Cells para Python via .NET permite insertar casillas de verificación en una hoja de gráficos usando la enumeración [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype). El siguiente ejemplo demuestra cómo agregar una casilla de verificación a una hoja de gráficos.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:image_alt_text](controls-in-charts_1.jpg)

El [archivo de salida](101089316.xlsx) generado por el siguiente fragmento de código se adjunta para su referencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Temas avanzados**
- [Agregar marca de agua de WordArt al gráfico](/cells/es/python-net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="python-net" >}}
