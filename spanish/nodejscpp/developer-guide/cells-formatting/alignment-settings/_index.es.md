---
title: Configuraciones de Alineación
linktitle: Configuraciones de Alineación
description: En la biblioteca Aspose.Cells, puedes usar configuraciones de alineación de celdas para ajustar el diseño y la visualización del texto usando Node.js vía C++. Este documento proporciona pasos detallados y código de ejemplo para usar Aspose.Cells en configuraciones de alineación de celdas.
keywords: Aspose.Cells, alineación de celdas, alineación horizontal, alineación vertical, ajuste de texto en Node.js vía C++
type: docs
weight: 20
url: /es/nodejs-cpp/cells-alignment-settings/
---

## **Configurando Ajustes de Alineación**

### **Configuraciones de Alineación en Microsoft Excel**

Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con las configuraciones de alineación en Microsoft Excel.

Como puedes ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría
- Orientación.
- Control de texto.
- Dirección del texto.

Todos estos ajustes de alineación son completamente compatibles con Aspose.Cells y se discuten con más detalle a continuación.

### **Ajustes de alineación en Aspose.Cells**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells proporciona métodos [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) y [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) para la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) que se usan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) ofrece propiedades útiles para configurar configuraciones de alineación.

Selecciona cualquier tipo de alineación de texto usando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype). Los tipos de alineación predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) son:

|**Tipos de Alineación de Texto**|**Descripción**|
| :- | :- |
|Bottom|Representa la alineación del texto inferior|
|Center|Representa la alineación del texto centrado|
|CenterAcross|Representa la alineación del texto centrado a través|
|Distributed|Representa la alineación del texto distribuido|
|Fill|Representa la alineación del texto de relleno|
|General|Representa la alineación del texto general|
|Justify|Representa la alineación del texto justificado|
|Left|Representa la alineación del texto a la izquierda|
|Right|Representa la alineación del texto a la derecha|
|Top|Representa la alineación del texto superior|
|JustifiedLow|Alinea el texto con una longitud de kashida ajustada para el texto árabe.|
|ThaiDistributed|Distribuye texto en tailandés especialmente, porque cada carácter se trata como una palabra.|

{{% alert color="primary" %}}

También puedes aplicar la configuración de justificación distribuida usando el método [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-).

{{% /alert %}}

#### **Alineación horizontal**

Usa el método [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Alineación vertical**

De manera similar a la alineación horizontal, usa el método [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Sangría**

Es posible establecer el nivel de sangría del texto en una celda con el método [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Orientación**

Establece la orientación (rotación) del texto en una celda con el método [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

##### **Envolver texto**

Envolver texto en una celda facilita su lectura: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o desbordarse a celdas adyacentes. Configura el ajuste de texto activándolo o desactivándolo con el método [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Reducir para ajustar**

Una opción para ajustar el texto en un campo es reducir el tamaño del texto para que quepa en las dimensiones de la celda. Esto se hace configurando el método [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) en **verdadero**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells soporta fusionar varias celdas en una sola. Aspose.Cells ofrece dos enfoques para esta tarea. Uno es llamar al método [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). El método [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) recibe los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


La otra forma es primero llamar al método [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) para crear un rango de celdas a fusionar. El método [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) recibe los mismos parámetros que el método [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) mencionado arriba y devuelve un objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). El objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) también proporciona un método [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) que une el rango especificado en el objeto [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se configura con la propiedad [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
