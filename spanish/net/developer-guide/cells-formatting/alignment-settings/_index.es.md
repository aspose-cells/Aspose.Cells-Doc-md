---
title: Configuración de alineación
description: En la biblioteca Aspose.Cells, puede utilizar la configuración de alineación de celdas para ajustar el diseño y la visualización del texto. Al ajustar configuraciones como la alineación horizontal, la alineación vertical y el ajuste de texto, tiene más control sobre cómo fluye el texto en las celdas. Este documento le proporcionará pasos detallados y código de muestra para ayudarle a comprender rápidamente cómo utilizar Aspose.Cells para la configuración de alineación de celdas.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /es/net/cells-alignment-settings/
---
##  **Configuración de ajustes de alineación**

###  **Configuración de alineación en Microsoft Excel**

Cualquiera que haya utilizado Microsoft Excel para formatear celdas estará familiarizado con la configuración de alineación en Microsoft Excel.

Como puede ver en la figura anterior, existen diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría.
- Orientación.
- Control de texto.
- Dirección del texto.

Todas estas configuraciones de alineación son totalmente compatibles con Aspose.Cells y se analizan con más detalle a continuación.

###  **Configuración de alineación en Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos para el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase que se utilizan para obtener y establecer el formato de una celda. El[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades útiles para configurar los ajustes de alineación.

 Seleccione cualquier tipo de alineación de texto usando el[**Tipo de alineación de texto**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) enumeración. Los tipos de alineación de texto predefinidos en el[**Tipo de alineación de texto**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)enumeración son:

|**Tipos de alineación de texto**|**Descripción**|
| :- | :- |
|Abajo|Representa la alineación del texto inferior.|
|Centro|Representa la alineación central del texto.|
|CentroA través|Representa el centro a lo largo de la alineación del texto.|
|Repartido|Representa la alineación del texto distribuido.|
|Llenar|Representa la alineación del texto de relleno|
|General|Representa la alineación general del texto.|
|Justificar|Representa justificar la alineación del texto.|
|Izquierda|Representa la alineación del texto a la izquierda.|
|Bien|Representa la alineación correcta del texto.|
|Arriba|Representa la alineación superior del texto.|
|JustificadoBajo|Alinea el texto con una longitud kashida ajustada para texto árabe.|
|TailandésDistribuido|Distribuye especialmente texto tailandés, porque cada carácter se trata como una palabra.|

{{% alert color="primary" %}}

 También puede aplicar la configuración distribuida de justificación utilizando el[**Estilo.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) propiedad.

{{% /alert %}}

####  **Alineación horizontal**

 Utilizar el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Alineación horizontal**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)propiedad para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **Alineamiento vertical**

 De forma similar a la alineación horizontal, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Alineamiento vertical**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)propiedad para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **Sangría**

 Es posible establecer el nivel de sangría del texto en una celda con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Nivel de sangría**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **Orientación**

 Establezca la orientación (rotación) del texto en una celda con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Ángulo de rotación**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **Control de texto**

La siguiente sección analiza cómo controlar el texto configurando el ajuste del texto, la reducción para ajustarlo y otras opciones de formato.

#####  **Texto envolvente**

 Ajustar el texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para ajustarse a todo el texto, en lugar de cortarlo o extenderse a las celdas adyacentes. Active o desactive el ajuste de texto con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Está envuelto en texto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **Reducir para ajustarse**

 Una opción para ajustar el texto en un campo es reducir el tamaño del texto para que se ajuste a las dimensiones de una celda. Esto se hace configurando el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Está envuelto en texto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propiedad a *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **Fusionando Cells**

 Al igual que Microsoft Excel, Aspose.Cells admite la combinación de varias celdas en una. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) método. El[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)El método toma los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a fusionarse.
- Primera columna: la primera columna desde donde comenzar a fusionar.
- Número de filas: el número de filas que se fusionarán.
- Número de columnas: el número de columnas que se fusionarán.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

La otra forma es llamar primero al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Crear rango**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) Método para crear un rango de celdas que se fusionarán. El[**Crear rango**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) El método toma el mismo conjunto de parámetros que el del[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) método discutido anteriormente y devuelve un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto. El[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) El objeto también proporciona una[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) método que fusiona el rango especificado en el[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range)objeto.

#####  **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

 El orden de lectura se establece con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Dirección del texto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) propiedad. Aspose.Cells proporciona tipos de dirección de texto predefinidos en el[**Tipo de dirección de texto**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)enumeración.

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Contexto|El orden de lectura coherente con el idioma del primer carácter ingresado.|
|De izquierda a derecha|Orden de lectura de izquierda a derecha|
|De derecha a izquierda|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **Temas avanzados**
- [Cambiar la alineación Cells y mantener el formato existente](/cells/es/net/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/net/line-breaks-and-text-wrapping/)

