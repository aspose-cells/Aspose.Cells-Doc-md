---
title: Insertar formas en una hoja de cálculo en Aspose.Cells
type: docs
weight: 5
url: /es/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

A veces necesitas insertar algunas formas necesarias en la hoja de cálculo. Puedes necesitar insertar la misma forma en diferentes posiciones de la hoja de cálculo. O necesitas insertar formas en lotes en la hoja de cálculo.

¡No te preocupes! [Aspose.Cells](https://products.aspose.com/cells/) soporta todas estas operaciones.

{{% /alert %}}

Las formas en Excel se dividen principalmente en los siguientes tipos:
- **Líneas**
- **Rectángulos**
- **Formas Básicas**
- **Flechas en Bloque**
- **Formas de Ecuaciones**
- **Diagramas de Flujo**
- **Estrellas y Banderas**
- **Llamadas**

Este documento guía seleccionará una o dos formas de cada tipo para hacer ejemplos. A través de estos ejemplos, aprenderás cómo usar [Aspose.Cells](https://products.aspose.com/cells/) para insertar la forma especificada en la hoja de cálculo.



## **Insertar una línea en la hoja de trabajo**

La forma de la línea pertenece a la categoría de **líneas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar la línea
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona la línea de 'Formas utilizadas recientemente' o 'Líneas'

![](line.png)

***Usando Aspose.Cells***

Puedes utilizar el siguiente método para insertar una línea en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line2.png)



## **Insertar una flecha de línea en la hoja de trabajo**

La forma de la flecha de línea pertenece a la categoría **Líneas**. Es un caso especial de línea.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar la flecha de línea
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione la flecha de línea de 'Formas usadas recientemente' o 'Líneas'

![](line_arrow1.png)

***Usando Aspose.Cells***

Puede utilizar el siguiente método para insertar una flecha de línea en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha de línea en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](line_arrow2.png)



## **Insertar un rectángulo en la hoja de trabajo**

La forma del rectángulo pertenece a la categoría de **Rectángulos**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar el rectángulo
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el rectángulo de 'Formas usadas recientemente' o 'Rectángulos'

![](rectangle.png)

***Usando Aspose.Cells***

Puedes utilizar el siguiente método para insertar un rectángulo en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un rectángulo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](rectangle2.png)



## **Insertar un cubo en la hoja de trabajo**

La forma del cubo pertenece a la categoría de **Formas básicas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde deseas insertar el cubo
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el Cubo de **Formas básicas**

![](cube.png)

***Usando Aspose.Cells***

Puede utilizar el siguiente método para insertar un cubo en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un cubo en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](cube2.png)



## **Insertar una flecha de llamada en la hoja de trabajo**

La forma de la flecha de cuadro de referencia pertenece a la categoría **Flechas de bloque**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar la flecha de cuadro de referencia
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione la flecha de cuadro de referencia de **Flechas de bloque**

![](callout_quad_arrow.png)

***Usando Aspose.Cells***

Puede utilizar el siguiente método para insertar una flecha de cuadro de referencia en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una flecha de cuadro de referencia en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](callout_quad_arrow2.png)



## **Insertar un signo de multiplicación en la hoja de trabajo**

La forma del signo de multiplicación pertenece a la categoría **Formas de ecuaciones**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el signo de multiplicación
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione el signo de multiplicación de **Formas de ecuaciones**

![](multiplication_sign.png)

***Usando Aspose.Cells***

Puede utilizar el siguiente método para insertar un signo de multiplicación en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un signo de multiplicación en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multiplication_sign2.png)



## **Insertar un documento múltiple en la hoja de trabajo**

La forma del multidocumento pertenece a la categoría **Flujogramas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el multidocumento
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona el multidocumento de **Flujogramas**

![](multidocument.png)

***Usando Aspose.Cells***

Puedes usar el siguiente método para insertar un multidocumento en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un multidocumento en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](multidocument2.png)



## **Insertar una estrella de cinco puntas en la hoja de trabajo**

La forma de la estrella de cinco puntas pertenece a la categoría de **Estrellas y Banderas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Selecciona la celda donde desees insertar la estrella de cinco puntas
- Haga clic en el menú Insertar y luego en Formas.
- Luego, selecciona la estrella de cinco puntas de **Estrellas y Banderas**

![](star_5_points.png)

***Usando Aspose.Cells***

Puedes usar el siguiente método para insertar una estrella de cinco puntas en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar una estrella de cinco puntas en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](star_5_points2.png)



## **Insertar una nube de burbuja de pensamiento en la hoja de trabajo**

La forma de un globo de pensamiento pertenece a la categoría de **Llamadas**.

***En Microsoft Excel (por ejemplo, 2007):***

- Seleccione la celda donde desea insertar el globo de pensamiento
- Haga clic en el menú Insertar y luego en Formas.
- Luego, seleccione el globo de pensamiento de **Llamadas**

![](thought_bubble_cloud.png)

***Usando Aspose.Cells***

Puede utilizar el siguiente método para insertar un globo de pensamiento en la hoja de cálculo.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

El método devuelve un objeto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

El siguiente ejemplo muestra cómo insertar un globo de pensamiento en una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Ejecute el código anterior, obtendrá los siguientes resultados:

![](thought_bubble_cloud2.png)
