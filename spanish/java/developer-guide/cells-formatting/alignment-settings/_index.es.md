---
title: Configuraciones de Alineación
type: docs
weight: 20
url: /es/java/cells-alignment-settings/
---

## **Configurando Ajustes de Alineación**

## **Configuraciones de Alineación en Microsoft Excel**

Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con las configuraciones de alineación en Microsoft Excel.

Como puedes ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría
- Orientación.
- Control de texto.
- Dirección del texto.

Todos estos ajustes de alineación son completamente compatibles con Aspose.Cells y se discuten con más detalle a continuación.

## **Ajustes de alineación en Aspose.Cells**

Aspose.Cells proporciona métodos [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) y [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) para la clase [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) proporciona propiedades útiles para configurar los ajustes de alineación.

Seleccione cualquier tipo de alineación de texto utilizando la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). Los tipos de alineación de texto predefinidos en la enumeración [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) son:

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

También puedes aplicar la justificación distribuida usando la configuración [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) property.

{{% /alert %}}

## **Alineación horizontal, vertical e indentación**

Utilice la propiedad [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) para alinear el texto horizontalmente y la propiedad [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) para alinear el texto verticalmente.
Es posible establecer el nivel de sangría del texto en una celda con la propiedad [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) 
y solo afecta cuando la alineación horizontal es izquierda o derecha.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientación**

Establezca la orientación (rotación) del texto en una celda con la propiedad [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Control de texto**

La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.

### **Envolver texto**

Envolver texto en una celda facilita su lectura: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes. Activar o desactivar el ajuste de texto con la propiedad [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Reducir para ajustar**

Una opción para envolver texto en un campo es reducir el tamaño del texto para que se ajuste a las dimensiones de la celda. Esto se hace configurando la propiedad [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) como **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Combinar celdas**

Al igual que Microsoft Excel, Aspose.Cells admite fusionar varias celdas en una. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al método [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-). El método toma los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a combinar.
- Primera columna: la primera columna desde donde comenzar a combinar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Temas avanzados**
- [Cambiar la alineación de las celdas y mantener el formato existente](/cells/es/java/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/java/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="java" >}}
