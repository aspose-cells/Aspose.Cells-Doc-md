---
title: Insertar imágenes y formas de archivos de Excel.
linktitle: Formas
type: docs
weight: 140
url: /es/python-net/insert-shapes/
description: Administrar imágenes, oleobject, formas en archivos de Excel.
---

{{% alert color="primary" %}}

A veces necesitas insertar algunas formas necesarias en la hoja de cálculo. Puedes necesitar insertar la misma forma en diferentes posiciones de la hoja de cálculo. O necesitas insertar formas en lotes en la hoja de cálculo.

¡No te preocupes! [Aspose.Cells](https://products.aspose.com/cells/) soporta todas estas operaciones.

{{% /alert %}}

Las formas en Excel se dividen principalmente en los siguientes tipos:
- **Imágenes**
- **OleObjects**
- **Líneas**
- **Rectángulos**
- **Formas Básicas**
- **Flechas en Bloque**
- **Formas de Ecuaciones**
- **Diagramas de Flujo**
- **Estrellas y Banderas**
- **Llamadas**

Este documento guía seleccionará una o dos formas de cada tipo para hacer ejemplos. A través de estos ejemplos, aprenderás cómo usar [Aspose.Cells](https://products.aspose.com/cells/) para insertar la forma especificada en la hoja de cálculo.

## **Agregar imágenes en una hoja de cálculo de Excel en C#**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:
Simplemente llame al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) de la colección [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (encapsulada en el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). El método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) toma los siguientes parámetros:

- **upper_left_row**, el índice de la fila superior izquierda.
- **upper_left_column**, el índice de la columna superior izquierda.
- **file_name**, el nombre del archivo de imagen, incluyendo la ruta.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-Pictures-AddingPictures-1.py" >}}


## **Insertar objetos OLE en una hoja de cálculo de Excel en C#**

Aspose.Cells para Python via .NET soporta añadir, extraer y manipular objetos OLE en hojas de cálculo. Por ello, Aspose.Cells para Python via .NET tiene la clase [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), utilizada para agregar un nuevo objeto OLE a la lista de colección. Otra clase, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:

- La propiedad [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) especifica los datos de imagen (icono) de tipo matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de cálculo.
- La propiedad [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) especifica los datos del objeto en forma de matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando hagas doble clic en el ícono del objeto OLE.

El siguiente ejemplo muestra cómo agregar un objeto(s) OLE a una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-OLE-InsertingOLEObjects-1.py" >}}

## **Insertar una línea en una hoja de cálculo de Excel en C#**

La forma de la línea pertenece a la categoría de **líneas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar la línea
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona la línea de 'Formas utilizadas recientemente' o 'Líneas'

![](line.png)

***Usando Aspose.Cells para Python via .NET***

Puedes utilizar el siguiente método para insertar una línea en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Line.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line2.png)



## **Insertar una flecha de línea en la hoja de cálculo de Excel en C#**

La forma de la flecha de línea pertenece a la categoría **Líneas**. Es un caso especial de línea.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar la flecha de línea
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione la flecha de línea de 'Formas usadas recientemente' o 'Líneas'

![](line_arrow1.png)

***Usando Aspose.Cells para Python via .NET***

Puede utilizar el siguiente método para insertar una flecha de línea en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

El método devuelve un objeto [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha de línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-LineArrow.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line_arrow2.png)



## **Insertar un rectángulo en la hoja de cálculo de Excel en C#**

La forma del rectángulo pertenece a la categoría de **Rectángulos**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar el rectángulo
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el rectángulo de 'Formas usadas recientemente' o 'Rectángulos'

![](rectangle.png)

***Usando Aspose.Cells para Python via .NET***

Puedes utilizar el siguiente método para insertar un rectángulo en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)

El método devuelve un objeto [RectangleShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un rectángulo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Rectangle.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](rectangle2.png)



## **Insertar un Cubo en la hoja de cálculo de Excel en C#**

La forma del cubo pertenece a la categoría de **Formas básicas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar el cubo
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el Cubo de **Formas básicas**

![](cube.png)

***Usando Aspose.Cells para Python via .NET***

Puede utilizar el siguiente método para insertar un cubo en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape add_auto_shape(type, upper_left_row, top, upper_left_column, left, height, width)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un cubo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Cube.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](cube2.png)



## **Insertar una flecha de cuadro de referencia a la hoja de cálculo de Excel en C#**

La forma de la flecha de cuadro de referencia pertenece a la categoría **Flechas de bloque**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar la flecha de cuadro de referencia
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione la flecha de cuadro de referencia de **Flechas de bloque**

![](callout_quad_arrow.png)

***Usando Aspose.Cells para Python via .NET***

Puede utilizar el siguiente método para insertar una flecha de cuadro de referencia en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha de cuadro de referencia en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](callout_quad_arrow2.png)



## **Insertar un signo de multiplicación a una hoja de cálculo de Excel en C#**

La forma del signo de multiplicación pertenece a la categoría **Formas de ecuaciones**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el signo de multiplicación
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione el signo de multiplicación de **Formas de ecuaciones**

![](multiplication_sign.png)

***Usando Aspose.Cells para Python via .NET***

Puede utilizar el siguiente método para insertar un signo de multiplicación en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un signo de multiplicación en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multiplication_sign2.png)



## **Insertar un multidocumento en una hoja de cálculo de Excel en C#**

La forma del multidocumento pertenece a la categoría **Flujogramas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el multidocumento
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el multidocumento de **Flujogramas**

![](multidocument.png)

***Usando Aspose.Cells para Python via .NET***

Puedes usar el siguiente método para insertar un multidocumento en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un multidocumento en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Multidocument.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multidocument2.png)



## **Insertar una estrella de cinco puntas en la hoja de cálculo de Excel en C#**

La forma de la estrella de cinco puntas pertenece a la categoría de **Estrellas y Banderas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde desees insertar la estrella de cinco puntas
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona la estrella de cinco puntas de **Estrellas y Banderas**

![](star_5_points.png)

***Usando Aspose.Cells para Python via .NET***

Puedes usar el siguiente método para insertar una estrella de cinco puntas en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una estrella de cinco puntas en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-FivePointedStar.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](star_5_points2.png)



## **Insertar un globo de pensamiento en una hoja de cálculo de Excel en C#**

La forma de un globo de pensamiento pertenece a la categoría de **Llamadas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el globo de pensamiento
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione el globo de pensamiento de **Llamadas**

![](thought_bubble_cloud.png)

***Usando Aspose.Cells para Python via .NET***

Puede utilizar el siguiente método para insertar un globo de pensamiento en la hoja de cálculo.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un globo de pensamiento en una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.py" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](thought_bubble_cloud2.png)

## **Temas avanzados**
- [Cambiar los valores de ajuste de la forma](/cells/es/python-net/change-adjustment-values-of-the-shape/)
- [Copiar formas entre hojas de cálculo](/cells/es/python-net/copy-shapes-between-worksheets/)
- [Datos en Forma No Primitiva](/cells/es/python-net/data-in-non-primitive-shape/)
- [Encontrar la Posición Absoluta de la Forma dentro de la Hoja de Trabajo](/cells/es/python-net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Obtener Puntos de Conexión de la Forma](/cells/es/python-net/get-connection-points-from-shape/)
- [Gestionar Controles](/cells/es/python-net/managing-controls/)
- [Agregar Iconos a la Hoja de Trabajo](/cells/es/python-net/insert-svg-to-excel/)
- [Gestionar Objetos OLE](/cells/es/python-net/managing-ole-objects/)
- [Gestionar Imágenes](/cells/es/python-net/managing-pictures/)
- [Gestionar SmartArt](/cells/es/python-net/managing-smartart/)
- [Gestionar Cuadro de Texto](/cells/es/python-net/managing-textbox-of-excel/)
- [Agregar WordArt como Marca de Agua a la Hoja de Trabajo](/cells/es/python-net/add-wordart-watermark-to-worksheet/)
- [Actualizar Valores de Formas Vinculadas](/cells/es/python-net/refresh-values-of-linked-shapes/)
- [Enviar Forma al Frente o Atrás Dentro de la Hoja de Trabajo](/cells/es/python-net/send-shape-front-or-back-inside-the-worksheet/)
- [Gestionar Opciones de la Forma](/cells/es/python-net/managing-shape-options/)
- [Gestionar Opciones de Texto de la Forma](/cells/es/python-net/managing-shape-text-options/)
- [Extensiones Web - Complementos de Office](/cells/es/python-net/web-extensions-office-add-ins/)

{{< app/cells/assistant language="python-net" >}}
