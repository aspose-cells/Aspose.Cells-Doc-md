---
title: Formas en gráficos con Golang vía C++
linktitle: Formas en gráficos
description: Aprende cómo usar Aspose.Cells for C++ para agregar controles y personalizar gráficos en Microsoft Excel. Nuestra guía demostrará cómo manipular elementos del gráfico, ajustar el formato y mejorar la apariencia y usabilidad general de tus gráficos.
keywords: Aspose.Cells for C++, Controles de gráficos, Personalización de gráficos, Microsoft Excel, Elementos de gráficos, Formato.
type: docs
weight: 70
url: /es/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

A veces es necesario insertar objetos de dibujo como etiquetas, cuadros de texto, imágenes, etc., en un gráfico. Aspose.Cells puede agregar los controles a un gráfico en tiempo de ejecución.

{{% /alert %}}

## **Agregar control de etiqueta al gráfico**

Las etiquetas proporcionan un medio para proporcionar información a los usuarios sobre el contenido de una hoja de cálculo.
Aspose.Cells le permite agregar y manipular etiquetas incluso en gráficos.

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) proporciona un método llamado [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/), usado para agregar un control de etiqueta a un gráfico. A continuación hay una lista de los parámetros utilizados para el método:

- **arriba** – el desplazamiento vertical de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** – el desplazamiento horizontal de la etiqueta desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** – la altura de la etiqueta, en unidades de 1/4000 del área del gráfico.
- **ancho** – el ancho de la etiqueta, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/). La clase [**Label**](https://reference.aspose.com/cells/go-cpp/label/) representa una etiqueta en el gráfico. Tiene algunos miembros importantes:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (propiedad) – especifica la cadena de texto del encabezado de la etiqueta.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (propiedad) - especifica los atributos del color de relleno.

Con el siguiente ejemplo se muestra cómo añadir una etiqueta al gráfico. El ejemplo utiliza un archivo del diseñador (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar una etiqueta en el gráfico. A continuación se muestra el código original para añadir una etiqueta al gráfico. La siguiente salida se genera al ejecutar el código.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Añadiendo un Control de Cuadro de Texto al Gráfico**

Una forma de resaltar información importante en un informe es usar un cuadro de texto. Por ejemplo, ingresar texto para resaltar el nombre de la empresa o indicar la región geográfica con mayores ventas. La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) proporciona un método llamado [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/), que se usa para agregar un control de cuadro de texto a un gráfico. A continuación, la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical del cuadro de texto desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **altura** - la altura del cuadro de texto, en unidades de 1/4000 del área del gráfico.
- **ancho** - el ancho del cuadro de texto, en unidades de 1/4000 del área del gráfico.

El método devuelve un objeto [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/). La clase [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) representa un cuadro de texto en el gráfico.

El siguiente ejemplo muestra cómo añadir un cuadro de texto a un gráfico. El ejemplo utiliza el archivo del diseñador anterior (**exp_piechart.xls**) que contiene un gráfico. Usamos este archivo para insertar un cuadro de texto en el gráfico para mostrar el título del gráfico. A continuación se muestra el código original para añadir un cuadro de texto al gráfico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Añadiendo una Imagen al Gráfico**

Aspose.Cells te permite insertar imágenes en un gráfico. Por ejemplo, agregar una imagen para resaltar o dar más significado a un gráfico o sus contenidos, o insertar un archivo de imagen de marca.

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) proporciona un método llamado [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/), que se usa para agregar un objeto de imagen al gráfico. A continuación, la lista de parámetros utilizados para el método:

- **arriba** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **izquierda** - el desplazamiento vertical de la imagen desde la esquina superior izquierda en unidades de 1/4000 del área del gráfico.
- **flujo** - un objeto de flujo que contiene los datos de la imagen.
- **escalaAncho** - la escala del ancho de la imagen, un valor porcentual.
- **escalaAlto** - la escala de la altura de la imagen, un valor porcentual.

El método devuelve un objeto [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/). La clase [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) representa un objeto de imagen en el gráfico.

El siguiente ejemplo muestra cómo agregar una imagen al gráfico. El ejemplo utiliza el archivo de diseñador anterior (**exp_piechart.xls**) que tiene un gráfico en él. Utilizamos este archivo para insertar una imagen en el gráfico. A continuación se muestra el código original para agregar una imagen al gráfico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Agregar casilla de verificación en el gráfico**

Aspose.Cells le permite insertar casillas de verificación en una hoja de gráfico utilizando la enumeración [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/). El siguiente ejemplo demuestra cómo agregar una casilla de verificación a una hoja de gráfico.

La siguiente imagen muestra la hoja de gráfico con la casilla de verificación en el archivo de salida.

![todo:image_alt_text](controls-in-charts_1.jpg)

El [archivo de salida](101089316.xlsx) generado por el siguiente fragmento de código se adjunta para su referencia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Temas avanzados**
- [Agregar marca de agua de WordArt al gráfico](/cells/es/cpp/add-wordart-watermark-to-chart/)
