---
title: Configuraciones de Alineación
description: En la biblioteca Aspose.Cells, puedes usar configuraciones de alineación celular para ajustar la disposición y visualización del texto. Al ajustar configuraciones como la alineación horizontal, alineación vertical y ajuste del texto, tienes más control sobre cómo fluye el texto en las celdas. Este documento te proporcionará pasos detallados y código de muestra para ayudarte a comprender rápidamente cómo usar Aspose.Cells para las configuraciones de alineación celular.
keywords: Aspose.Cells, alineación celular, alineación horizontal, alineación vertical, ajuste del texto
type: docs
weight: 20
url: /es/net/cells-alignment-settings/
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

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells proporciona métodos [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) para la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) proporciona propiedades útiles para configurar los ajustes de alineación.

Seleccione cualquier tipo de alineación de texto utilizando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype). Los tipos de alineación de texto predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) son:

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

También puedes aplicar la justificación distribuida usando la configuración [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) property.

{{% /alert %}}

#### **Alineación horizontal**

Usa la propiedad [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Alineación vertical**

Similar a la alineación horizontal, usa la propiedad [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Sangría**

Es posible establecer el nivel de sangría del texto en una celda con la propiedad [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientación**

Establece la orientación (rotación) del texto en una celda con la propiedad [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

##### **Envolver texto**

Envolver el texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes. Establece el ajuste de texto en on o off con la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Reducir para ajustar**

Una opción para envolver texto en un campo es reducir el tamaño del texto para ajustarse a las dimensiones de una celda. Esto se hace configurando la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) como **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells admite combinar varias celdas en una. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al método [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). El método [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) toma los siguientes parámetros para combinar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

La otra forma es llamar primero al método [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) para crear un rango de celdas a fusionar. El método [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) toma el mismo conjunto de parámetros que el método [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) discutido anteriormente y devuelve un objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). El objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) también proporciona un método [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) que fusiona el rango especificado en el objeto [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/net/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/net/line-breaks-and-text-wrapping/)

