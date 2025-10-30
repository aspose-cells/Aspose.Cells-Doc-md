---
title: Configuración de alineación con Golang a través de C++
linktitle: Configuraciones de Alineación
description: En la biblioteca Aspose.Cells, puedes usar configuraciones de alineación celular para ajustar la disposición y visualización del texto. Al ajustar configuraciones como la alineación horizontal, alineación vertical y ajuste del texto, tienes más control sobre cómo fluye el texto en las celdas. Este documento te proporcionará pasos detallados y código de muestra para ayudarte a comprender rápidamente cómo usar Aspose.Cells para las configuraciones de alineación celular.
keywords: Aspose.Cells, alineación celular, alineación horizontal, alineación vertical, ajuste del texto
type: docs
weight: 20
url: /es/go-cpp/cells-alignment-settings/
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

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite el acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Cada elemento en la colección [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells proporciona métodos [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) y [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) para la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) proporciona propiedades útiles para configurar los ajustes de alineación.

Seleccione cualquier tipo de alineación de texto utilizando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/). Los tipos de alineación de texto predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) son:

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

También puedes aplicar la justificación distribuida usando la configuración [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/) property.

{{% /alert %}}

#### **Alineación horizontal**

Usa la propiedad [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Alineación vertical**

Similar a la alineación horizontal, usa la propiedad [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Sangría**

Es posible establecer el nivel de sangría del texto en una celda con la propiedad [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Orientación**

Establece la orientación (rotación) del texto en una celda con la propiedad [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

##### **Envolver texto**

Envolver el texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes. Establece el ajuste de texto en on o off con la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Reducir para ajustar**

Una opción para envolver texto en un campo es reducir el tamaño del texto para ajustarse a las dimensiones de una celda. Esto se hace configurando la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) como **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells admite combinar varias celdas en una. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) de la colección [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/). El método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) toma los siguientes parámetros para combinar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
La otra forma es llamar primero al método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) de la colección [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) para crear un rango de celdas a fusionar. El método [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) toma el mismo conjunto de parámetros que el método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) discutido anteriormente y devuelve un objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). El objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) también proporciona un método [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) que fusiona el rango especificado en el objeto [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) del objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/). Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/cpp/line-breaks-and-text-wrapping/)
