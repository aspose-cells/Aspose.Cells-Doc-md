---
title: Configuración de alineación
type: docs
weight: 20
url: /es/net/cells-alignment-settings/
---
## **Configuración de ajustes de alineación**

### **Configuración de alineación en Microsoft Excel**

Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con la configuración de alineación en Microsoft Excel.

Como puede ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- Alineación de texto (horizontal y vertical)
- Sangría.
- Orientación.
- Control de texto.
- Dirección del texto.

Todas estas configuraciones de alineación son totalmente compatibles con Aspose.Cells y se analizan con más detalle a continuación.

### **Ajustes de alineación en Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos para el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase que se utilizan para obtener y establecer el formato de una celda. Él[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades útiles para configurar los ajustes de alineación.

 Seleccione cualquier tipo de alineación de texto usando el[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) enumeración. Los tipos de alineación de texto predefinidos en el[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)enumeración son:

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

 También puede aplicar la configuración distribuida de justificación usando el[**Estilo.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) propiedad.

{{% /alert %}}

#### **Alineación horizontal**

 Utilizar el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Alineación horizontal**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)propiedad para alinear el texto horizontalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Alineamiento vertical**

 Similar a la alineación horizontal, use el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Alineamiento vertical**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)propiedad para alinear el texto verticalmente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Sangría**

 Es posible establecer el nivel de sangría del texto en una celda con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**nivel de sangría**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientación**

 Establecer la orientación (rotación) del texto en una celda con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Ángulo de rotación**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Control de texto**

La siguiente sección explica cómo controlar el texto configurando el ajuste de texto, reducir para ajustar y otras opciones de formato.

##### **Texto de ajuste**

 Envolver texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para ajustarse a todo el texto, en lugar de cortarlo o extenderse a las celdas adyacentes. Active o desactive el ajuste de texto con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**EsTextoEnvuelto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Encogimiento para encajar**

 Una opción para ajustar texto en un campo es reducir el tamaño del texto para que se ajuste a las dimensiones de una celda. Esto se hace configurando el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**EsTextoEnvuelto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Fusionando Cells**

 Al igual que Microsoft Excel, Aspose.Cells admite la combinación de varias celdas en una sola. Aspose.Cells proporciona dos enfoques para esta tarea. Una forma es llamar al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) método. Él[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)El método toma los siguientes parámetros para fusionar las celdas:

- Primera fila: la primera fila desde donde comenzar a fusionar.
- Primera columna: la primera columna desde donde comenzar a fusionar.
- Número de filas: el número de filas a fusionar.
- Número de columnas: el número de columnas a fusionar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 La otra forma es llamar primero al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) método para crear un rango de las celdas que se fusionarán. Él[**CrearRango**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) El método toma el mismo conjunto de parámetros que el del[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) método discutido anteriormente y devuelve un[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto. Él[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range) objeto también proporciona una[**Unir**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) método que fusiona el rango especificado en el[**Rango**](https://reference.aspose.com/cells/net/aspose.cells/range)objeto.

##### **Dirección del texto**

Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

 El orden de lectura se establece con el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Dirección del texto**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) propiedad. Aspose.Cells proporciona tipos de dirección de texto predefinidos en el[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)enumeración.

|**Tipos de dirección de texto**|**Descripción**|
|:- |:- |
|Contexto|El orden de lectura consistente con el idioma del primer carácter ingresado|
|De izquierda a derecha|Orden de lectura de izquierda a derecha|
|De derecha a izquierda|Orden de lectura de derecha a izquierda|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Temas avanzados**
- [Cambiar la alineación Cells y mantener el formato existente](/cells/es/net/change-cells-alignment-and-keep-existing-formatting/)
- [Saltos de línea y ajuste de texto](/cells/es/net/line-breaks-and-text-wrapping/)

