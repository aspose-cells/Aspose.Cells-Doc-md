---
title: Configuración de alineación
type: docs
weight: 20
url: /es/java/cells-alignment-settings/
---
## **Configuración de ajustes de alineación**

## **Configuración de alineación en Microsoft Excel**

Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con la configuración de alineación en Microsoft Excel.

Como puede ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría.
- Orientación.
- Control de texto.
- Dirección del texto.

Todas estas configuraciones de alineación son totalmente compatibles con Aspose.Cells y se analizan con más detalle a continuación.

## **Ajustes de alineación en Aspose.Cells**

 Aspose.Cells proporciona[**ObtenerEstilo**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) y[**EstablecerEstilo**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) métodos para el[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase que se utilizan para obtener y establecer el formato de una celda. los[**Estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style)La clase proporciona propiedades útiles para configurar los ajustes de alineación.

 Seleccione cualquier tipo de alineación de texto usando el[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) enumeración. Los tipos de alineación de texto predefinidos en el[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)enumeración son:

|**Tipos de alineación de texto**|**Descripción**|
|:- |:- |
|Abajo|Representa la alineación del texto inferior|
|Centro|Representa la alineación del texto central|
|CenterAcross|Representa el centro a lo largo de la alineación del texto|
|Repartido|Representa la alineación de texto distribuida|
|Llenar|Representa la alineación del texto de relleno|
|General|Representa la alineación general del texto.|
|Justificar|Representa justificar la alineación del texto|
|Izquierda|Representa la alineación del texto a la izquierda|
|Derecha|Representa la alineación correcta del texto.|
|Parte superior|Representa la alineación del texto superior|
|JustificadoBajo|Alinea el texto con una longitud de kashida ajustada para el texto en árabe.|
|TailandésDistribuido|Distribuye especialmente el texto en tailandés, porque cada carácter se trata como una palabra.|

{{% alert color="primary" %}}

 También puede aplicar la configuración distribuida de justificación usando el[**Estilo.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) propiedad.

{{% /alert %}}

## **Alineación horizontal, vertical y sangría**

 Utilizar el[**Alineación horizontal**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) propiedad para alinear el texto horizontalmente y[**Alineamiento vertical**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)propiedad para alinear el texto verticalmente.
 Es posible establecer el nivel de sangría del texto en una celda con el[**nivel de sangría**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) propiedad
y tt solo afecta cuando la alineación horizontal es izquierda o derecha.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientación**

 Establecer la orientación (rotación) del texto en una celda con el[**Ángulo de rotación**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Control de texto**

La siguiente sección explica cómo controlar el texto configurando el ajuste de texto, reducir para ajustar y otras opciones de formato.

### **Texto de ajuste**

 Envolver texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para ajustarse a todo el texto, en lugar de cortarlo o extenderse a las celdas adyacentes. Active o desactive el ajuste de texto con el[**EsTextoEnvuelto**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Encogimiento para encajar**

 Una opción para ajustar texto en un campo es reducir el tamaño del texto para que se ajuste a las dimensiones de una celda. Esto se hace configurando el[**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) propiedad. a**verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Fusionando Cells**

 Al igual que Microsoft Excel, Aspose.Cells admite la combinación de varias celdas en una sola. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al[**Unir**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) método. El método toma los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a fusionar.
- Primera columna: la primera columna desde donde comenzar a fusionar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

 El orden de lectura se establece con el[**Dirección del texto**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) propiedad. Aspose.Cells proporciona tipos de dirección de texto predefinidos en el[**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)enumeración.

|**Tipos de dirección de texto**|**Descripción**|
|:- |:- |
|Contexto|El orden de lectura consistente con el idioma del primer carácter ingresado|
|De izquierda a derecha|Orden de lectura de izquierda a derecha|
|De derecha a izquierda|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Temas avanzados**
- [Cambiar la alineación Cells y mantener el formato existente](/cells/es/java/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/java/line-breaks-and-text-wrapping/)
