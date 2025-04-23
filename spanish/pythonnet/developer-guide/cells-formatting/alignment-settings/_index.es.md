---
title: Configuraciones de Alineación
description: En la biblioteca Aspose.Cells para Python via .NET, puedes usar configuraciones de alineación de celdas para ajustar la disposición y la visualización del texto. Al ajustar configuraciones como alineación horizontal, alineación vertical y ajuste de texto, tienes mayor control sobre cómo fluye el texto en las celdas. Este documento te proporcionará pasos detallados y código de ejemplo para ayudarte a entender rápidamente cómo usar Aspose.Cells para Python via .NET para configuraciones de alineación de celdas.
keywords: Aspose.Cells para Python via .NET, alineación de celda, alineación horizontal, alineación vertical, ajuste de texto
type: docs
weight: 20
url: /es/python-net/cells-alignment-settings/
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

Todas estas configuraciones de alineación son totalmente compatibles con Aspose.Cells para Python via .NET y se discuten en más detalle abajo.

### **Configuraciones de alineación en Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells para Python via .NET proporciona métodos [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) y [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) para la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) proporciona propiedades útiles para configurar configuraciones de alineación.

Seleccione cualquier tipo de alineación de texto utilizando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). Los tipos de alineación de texto predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) son:

|**Tipos de Alineación de Texto**|**Descripción**|
| :- | :- |
|GENERAL|Representa alineación de texto general|
|BOTTOM|Representa alineación de texto en la parte inferior|
|CENTER|Representa alineación de texto en el centro|
|CENTER_ACROSS|Representa alineación de texto centrada en atravesar|
|DISTRIBUTED|Representa alineación de texto distribuida|
|FILL|Representa alineación de texto de relleno|
|JUSTIFY|Representa alineación de texto justificada|
|LEFT|Representa alineación de texto a la izquierda|
|RIGHT|Representa alineación de texto a la derecha|
|TOP|Representa alineación de texto en la parte superior|
|JUSTIFIED_LOW|Alinea el texto con una longitud de khashida ajustada para texto árabe|
|THAI_DISTRIBUTED|Distribuye el texto tailandés de manera especial, ya que cada carácter se trata como una palabra|

{{% alert color="primary" %}}

También puedes aplicar la justificación distribuida usando la configuración [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed) property.

{{% /alert %}}

#### **Alineación horizontal**

Usa la propiedad [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Alineación vertical**

Similar a la alineación horizontal, usa la propiedad [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Sangría**

Es posible establecer el nivel de sangría del texto en una celda con la propiedad [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Orientación**

Establece la orientación (rotación) del texto en una celda con la propiedad [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

##### **Envolver texto**

Envolver el texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes. Establece el ajuste de texto en on o off con la propiedad [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Reducir para ajustar**

Una opción para envolver texto en un campo es reducir el tamaño del texto para ajustarse a las dimensiones de una celda. Esto se hace configurando la propiedad [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) como **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells para Python via .NET soporta fusionar varias celdas en una sola. Aspose.Cells para Python via .NET ofrece dos enfoques para esta tarea. Una forma es llamar al método [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). El método [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) toma los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

La otra forma es llamar primero al método [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) de la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) para crear un rango de celdas a fusionar. El método [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) toma el mismo conjunto de parámetros que el método [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) discutido anteriormente y devuelve un objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). El objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) también proporciona un método [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) que fusiona el rango especificado en el objeto [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Aspose.Cells para Python via .NET proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|CONTEXT|El orden de lectura consistente con el idioma del primer carácter ingresado|
|LEFT_TO_RIGHT|Orden de lectura de izquierda a derecha|
|RIGHT_TO_LEFT|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/python-net/line-breaks-and-text-wrapping/)


