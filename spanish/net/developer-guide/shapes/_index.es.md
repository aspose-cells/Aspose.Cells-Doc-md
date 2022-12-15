---
title: Inserte imágenes y formas de archivos de Excel.
linktitle: formas
type: docs
weight: 140
url: /es/net/insert-shapes/
description: Administre imágenes, oleobject, formas en archivos de Excel.
---
{{% alert color="primary" %}}

A veces, necesita insertar algunas formas necesarias en la hoja de trabajo. Es posible que deba insertar la misma forma en diferentes posiciones de la hoja de trabajo. O necesita insertar formas por lotes en la hoja de trabajo.

 ¡No te preocupes![Aspose.Cells](https://products.aspose.com/cells/) soporta todas estas operaciones.

{{% /alert %}}

Las formas en Excel se dividen principalmente en los siguientes tipos:
- **Fotos**
- **OleObjetos**
- **Líneas**
- **Rectángulos**
- **Formas básicas**
- **flechas de bloque**
- **Formas de ecuación**
- **diagramas de flujo**
- **estrellas y pancartas**
- **Rótulos**

Este documento guía seleccionará una o dos formas de cada tipo para hacer muestras. A través de estos ejemplos, aprenderá a usar[Aspose.Cells](https://products.aspose.com/cells/) para insertar la forma especificada en la hoja de cálculo.

## **Adición de imágenes en la hoja de cálculo de Excel en C#**

Agregar imágenes a una hoja de cálculo es muy fácil. Solo se necesitan unas pocas líneas de código:
 Simplemente llame al[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodo de la[**Fotos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) colección (encapsulada en el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objeto). los[**Agregar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)método toma los siguientes parámetros:

- **Índice de la fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de la columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Insertar objetos OLE en la hoja de cálculo de Excel en C#**

Aspose.Cells admite agregar, extraer y manipular objetos OLE en hojas de trabajo. Por esta razón, Aspose.Cells tiene la[**OleObjectCollectionOleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) clase, utilizada para agregar un nuevo objeto OLE a la lista de recopilación. Otra clase,[**Objeto OLE**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representa un objeto OLE. Tiene algunos miembros importantes:

-  los[**Datos de imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)La propiedad especifica los datos de la imagen (icono) del tipo de matriz de bytes. La imagen se mostrará para mostrar el objeto OLE en la hoja de trabajo.
-  los[**ObjetoDatos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)La propiedad especifica los datos del objeto en forma de una matriz de bytes. Estos datos se mostrarán en su programa relacionado cuando haga doble clic en el icono Objeto OLE.

El siguiente ejemplo muestra cómo agregar objetos OLE a una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Insertar una línea en la hoja de cálculo de Excel en C#**

 La forma de la línea pertenece a la**líneas** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar la línea
- Haga clic en el menú Insertar y haga clic en Formas.
- Luego, seleccione la línea de 'Formas usadas recientemente' o 'Líneas'

![](line.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar una línea en la hoja de cálculo.

{{% alert color="primary" %}}

[Agregar línea de forma de línea pública (
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 El método devuelve un[LíneaForma](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line2.png)



## **Insertar una flecha de línea en la hoja de cálculo de Excel en C#**

 La forma de flecha de línea pertenece a la**Líneas**categoría. Es un caso especial de línea.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar la flecha de línea
- Haga clic en el menú Insertar y haga clic en Formas.
- Luego, seleccione la flecha de línea de 'Formas usadas recientemente' o 'Líneas'

![](line_arrow1.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar una flecha de línea en la hoja de trabajo.

{{% alert color="primary" %}}

[Agregar línea de forma de línea pública (
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 El método devuelve un[LíneaForma](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha de línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line_arrow2.png)



## **Insertar un rectángulo en una hoja de cálculo de Excel en C#**

 La forma de rectángulo pertenece a la**Rectángulos** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar el rectángulo
- Haga clic en el menú Insertar y haga clic en Formas.
- Luego, seleccione el rectángulo de 'Formas usadas recientemente' o 'Rectángulos'

![](rectangle.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar un rectángulo en la hoja de cálculo.

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 El método devuelve un[Forma rectangular](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un rectángulo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](rectangle2.png)



## **Insertar un cubo en una hoja de cálculo de Excel en C#**

 La forma de cubo pertenece a la**Formas básicas** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar el cubo
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione el Cubo de**Formas básicas**

![](cube.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar un cubo en la hoja de cálculo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un cubo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](cube2.png)



## **Insertar una flecha cuádruple de llamada en la hoja de cálculo de Excel en C#**

 La forma de la flecha cuádruple de llamada pertenece a la**flechas de bloque** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar la flecha cuádruple de llamada
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione la flecha cuádruple de llamada de**flechas de bloque**

![](callout_quad_arrow.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar una flecha cuádruple de llamada en la hoja de trabajo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha cuádruple de llamada en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](callout_quad_arrow2.png)



## **Insertar un signo de multiplicación en la hoja de cálculo de Excel en C#**

 La forma del signo de multiplicación pertenece a la**Formas de ecuación** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar el signo de multiplicación
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione el signo de multiplicación de**Formas de ecuación**

![](multiplication_sign.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar un signo de multiplicación en la hoja de trabajo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar el signo de multiplicación en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multiplication_sign2.png)



## **Inserción de un multidocumento a la hoja de cálculo de Excel en C#**

La forma de multidocumento pertenece a la**diagramas de flujo** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar el multidocumento
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione el multidocumento de**diagramas de flujo**

![](multidocument.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar un multidocumento en la hoja de cálculo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar varios documentos en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multidocument2.png)



## **Insertar una estrella de cinco puntas en la hoja de cálculo de Excel en C#**

 La forma de estrella de cinco puntas pertenece a la**estrellas y pancartas** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar la estrella de cinco puntas
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione la estrella de cinco puntas de**estrellas y pancartas**

![](star_5_points.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar una estrella de cinco puntas en la hoja de trabajo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una estrella de cinco puntas en una hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](star_5_points2.png)



## **Insertar una nube de burbujas de pensamiento en la hoja de cálculo de Excel en C#**

 La forma de la nube de burbujas de pensamiento pertenece a la**Rótulos** categoría.

***En Microsoft Excel (por ejemplo 2007):***

- Seleccione la celda donde desea insertar la nube de burbujas de pensamiento
- Haga clic en el menú Insertar y haga clic en Formas.
-  Luego, seleccione la nube de burbujas de pensamiento de**Rótulos**

![](thought_bubble_cloud.png)

***Usando Aspose.Cells***

Puede usar el siguiente método para insertar una nube de burbujas de pensamiento en la hoja de trabajo.

{{% alert color="primary" %}}

[Forma pública AddAutoShape(
 tipo AutoShapeType,
 int fila superior izquierda,
 en la parte superior,
 int columna superior izquierda,
 int izquierda,
 altura interna,
 ancho int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 El método devuelve un[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objeto.

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una nube de burbujas de pensamiento en una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](thought_bubble_cloud2.png)

## **Temas avanzados**
- [Cambiar los valores de ajuste de la forma](/cells/es/net/change-adjustment-values-of-the-shape/)
- [Copiar formas entre hojas de trabajo](/cells/es/net/copy-shapes-between-worksheets/)
- [Datos en forma no primitiva](/cells/es/net/data-in-non-primitive-shape/)
- [Encontrar la posición absoluta de la forma dentro de la hoja de trabajo](/cells/es/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Obtener puntos de conexión de la forma](/cells/es/net/get-connection-points-from-shape/)
- [Gestión de controles](/cells/es/net/managing-controls/)
- [Agregar iconos a la hoja de trabajo](/cells/es/net/insert-svg-to-excel/)
- [Gestión de objetos OLE](/cells/es/net/managing-ole-objects/)
- [Gestión de imágenes](/cells/es/net/managing-pictures/)
- [Administrar arte inteligente](/cells/es/net/managing-smartart/)
- [Gestión de cuadro de texto](/cells/es/net/managing-textbox-of-excel/)
- [Agregar marca de agua de WordArt a la hoja de trabajo](/cells/es/net/add-wordart-watermark-to-worksheet/)
- [Actualizar valores de formas vinculadas](/cells/es/net/refresh-values-of-linked-shapes/)
- [Enviar forma al frente o al reverso dentro de la hoja de trabajo](/cells/es/net/send-shape-front-or-back-inside-the-worksheet/)
- [Administrar opciones de forma](/cells/es/net/managing-shape-options/)
- [Administrar opciones de texto de formas](/cells/es/net/managing-shape-text-options/)
- [Extensiones web: complementos de Office](/cells/es/net/web-extensions-office-add-ins/)

