---
title: Formateo de datos
type: docs
weight: 80
url: /es/java/data-formatting/
---
## **Enfoques para formatear datos en Cells**
Es un hecho común que si las celdas de la hoja de trabajo tienen el formato adecuado, a los usuarios les resultará más fácil leer el contenido (datos) de la celda. Hay muchas formas de formatear celdas y su contenido. La forma más sencilla es dar formato a las celdas utilizando Microsoft Excel en un entorno WYSIWYG al crear una hoja de cálculo de diseñador. Después de crear la hoja de cálculo del diseñador, puede abrir la hoja de cálculo usando Aspose.Cells manteniendo todas las configuraciones de formato guardadas con la hoja de cálculo. Otra forma de dar formato a las celdas y su contenido es usar Aspose.Cells API. En este tema, describiremos dos enfoques para dar formato a las celdas y su contenido con el uso de Aspose.Cells API.
### **Formateo Cells**
 Los desarrolladores pueden formatear celdas y su contenido utilizando el API flexible de Aspose.Cells. Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class proporciona una colección Cells. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)colección representa un objeto de**Cell** clase.

 Aspose.Cells proporciona el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) propiedad en el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class, que se utiliza para establecer el estilo de formato de una celda. Además, Aspose.Cells también proporciona un[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) clase que se utiliza para servir al mismo propósito. Aplique diferentes tipos de estilos de formato en las celdas para establecer sus colores de fondo o de primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.
#### **Usando el método setStyle**
 Al aplicar diferentes estilos de formato a diferentes celdas, es mejor usar el método setStyle del[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase. A continuación se proporciona un ejemplo para demostrar el uso del método setStyle para aplicar varias configuraciones de formato en una celda.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Uso del objeto de estilo**
 Al aplicar el mismo estilo de formato a diferentes celdas, use el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) objeto.

1.  Agrega un[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) objeto a la colección Styles de la[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase llamando al método createStyle de la clase Workbook.
1. Acceda al objeto Estilo recién agregado desde la colección Estilos.
1. Establezca las propiedades deseadas del objeto Estilo para aplicar la configuración de formato deseada.
1. Asigne el objeto Estilo configurado a la propiedad Estilo de cualquier celda deseada.

Este enfoque puede mejorar en gran medida la eficiencia de sus aplicaciones y también ahorrar memoria.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Aplicación de efectos de relleno degradado**
Para aplicar los efectos de relleno de degradado deseados a la celda, utilice el método setTwoColorGradient del objeto Style según corresponda.
#### **Ejemplo de código**
 El siguiente resultado se logra ejecutando el siguiente código.

**Aplicación de efectos de relleno degradado** 

![todo:imagen_alternativa_texto](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configuración de ajustes de alineación**
Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con la configuración de alineación en Microsoft Excel.

**Configuración de alineación en Microsoft Excel** 

![todo:imagen_alternativa_texto](data-formatting_2.png)

Como puede ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- [Alineación del texto](/cells/es/java/data-formatting/) (horizontal Vertical)
- [Sangría](/cells/es/java/data-formatting/).
- [Orientación](/cells/es/java/data-formatting/).
- [control de texto](/cells/es/java/data-formatting/).
- [Dirección del texto](/cells/es/java/data-formatting/).

Todas estas configuraciones de alineación son totalmente compatibles con Aspose.Cells y se analizan con más detalle a continuación.
### **Configuración de ajustes de alineación**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

 La clase Worksheet proporciona una colección Cells. Cada elemento de la colección Cells representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase.

Aspose.Cells proporciona el método setStyle en el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase que se utiliza para formatear una celda. los[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) class proporciona propiedades útiles para configurar los ajustes de fuente.

Seleccione cualquier tipo de alineación de texto mediante la enumeración TextAlignmentType. Los tipos de alineación de texto predefinidos en la enumeración TextAlignmentType son:

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
{{% alert color="primary" %}} 

También puede aplicar la configuración distribuida justificada mediante el método Style.setJustifyDistributed().

{{% /alert %}} 
#### **Alineación horizontal**
 Utilizar el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) el método setHorizontalAlignment del objeto para alinear el texto horizontalmente.

El siguiente resultado se logra ejecutando el siguiente código de ejemplo:

**Alinear el texto horizontalmente** 

![todo:imagen_alternativa_texto](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Alineamiento vertical**
 Utilizar el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) método setVerticalAlignment del objeto para alinear el texto verticalmente.

El siguiente resultado se logra cuando VerticalAlignment se establece en el centro.

**Alinear el texto verticalmente** 

![todo:imagen_alternativa_texto](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Sangría**
 Es posible establecer el nivel de sangría del texto en una celda usando el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) método setIndentLevel del objeto.

El siguiente resultado se logra cuando IndentLevel se establece en 2.

**Nivel de sangría ajustado a 2** 

![todo:imagen_alternativa_texto](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientación**
 Establecer la orientación (rotación) del texto en una celda con el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) método setRotationAngle del objeto.

El siguiente resultado se logra cuando el ángulo de rotación se establece en 25.

**Ángulo de rotación establecido en 25** 

![todo:imagen_alternativa_texto](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Control de texto**
La siguiente sección explica cómo controlar el texto configurando el ajuste de texto, reducir para ajustar y otras opciones de formato.
#### **Texto de ajuste**
Envolver texto en una celda hace que sea más fácil de leer: la altura de la celda se ajusta para ajustarse a todo el texto, en lugar de cortarlo o extenderse a las celdas adyacentes.

 Active o desactive el ajuste de texto con el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) método setTextWrapped del objeto.

El siguiente resultado se logra cuando el ajuste de texto está habilitado.

**Texto envuelto dentro de la celda** 

![todo:imagen_alternativa_texto](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Encogimiento para encajar**
 Una opción para ajustar texto en un campo es reducir el tamaño del texto para que se ajuste a las dimensiones de una celda. Esto se hace configurando el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) propiedad IsTextWrapped del objeto para**verdadero**.

El siguiente resultado se logra cuando el texto se reduce para que quepa en la celda.

**Texto reducido para caber dentro de los límites de la celda** 

![todo:imagen_alternativa_texto](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Fusionando Cells**
Al igual que Microsoft Excel, Aspose.Cells admite la combinación de varias celdas en una sola.

El siguiente resultado se logra si las tres celdas de la primera fila se fusionan para crear una sola celda grande.

**Tres celdas fusionadas para crear una celda grande** 

![todo:imagen_alternativa_texto](data-formatting_9.png)

 Utilizar el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) el método Merge de la colección para combinar celdas. El método Merge toma los siguientes parámetros:

- Primera fila, la primera fila desde donde comenzar a fusionar.
- Primera columna, la primera columna desde donde comenzar a fusionar.
- Número de filas, el número de filas para fusionar.
- Número de columnas, el número de columnas para fusionar.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Dirección del texto**
Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

 El orden de lectura se establece con el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/style) propiedad TextDirection del objeto. Aspose.Cells proporciona tipos de dirección de texto predefinidos en la enumeración TextDirectionType.

|**Tipos de dirección de texto**|**Descripción**|
|:- |:- |
|Contexto|El orden de lectura consistente con el idioma del primer carácter ingresado|
|De izquierda a derecha|Orden de lectura de izquierda a derecha|
|De derecha a izquierda|Orden de lectura de derecha a izquierda|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





El siguiente resultado se logra si el orden de lectura del texto se establece de derecha a izquierda.

**Configuración del orden de lectura de texto de derecha a izquierda** 

![todo:imagen_alternativa_texto](data-formatting_10.png)
## **Formateo de caracteres seleccionados en un Cell**
[Tratar con la configuración de fuentes](/cells/es/java/dealing-with-font-settings/)explicó cómo formatear celdas, pero solo cómo formatear el contenido de todas las celdas. ¿Qué sucede si desea formatear solo los caracteres seleccionados?

Aspose.Cells admite esta función. Este tema explica cómo utilizar esta característica.
### **Dar formato a los caracteres seleccionados**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. La clase Libro de trabajo contiene una colección de Hojas de trabajo que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. La clase Worksheet proporciona una colección Cells. Cada elemento de la colección Cells representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase.

La clase Cell proporciona un método de caracteres que toma los siguientes parámetros para seleccionar un rango de caracteres en una celda:

- **Índice de comienzo**, el índice del carácter desde el que comenzar la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

En el archivo de salida, en la celda A1", la palabra 'Visita' tiene el formato de fuente predeterminado pero 'Aspose!' es negrita y azul.

**Formateo de caracteres seleccionados** 

![todo:imagen_alternativa_texto](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Si usted está interesado en[formatear una porción de texto enriquecido en una [celda]](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/) , considere usar los métodos Cell.getCharacters y Cell.setCharacters. El método Cell.getCharacters se debe usar para acceder a las partes del texto y luego se pueden hacer enmiendas usando el método Cell.setCharacters mientras que el**obtener** El método devuelve una matriz de objetos FontSetting que se pueden manipular para establecer varias propiedades: nombre de fuente, color de fuente, negrita, etc.**establecer** El método se puede utilizar para aplicar los cambios.

{{% /alert %}} 
## **Activar hojas y hacer un activo Cell o seleccionar un rango de Cells en la hoja de trabajo**
veces, es posible que deba activar una hoja de trabajo específica para que sea la primera que se muestre cuando alguien abra el archivo en Microsoft Excel. También es posible que deba activar una celda específica de tal manera que las barras de desplazamiento se desplacen a la celda activa para que sea claramente visible. Aspose.Cells es capaz de realizar todas las tareas mencionadas anteriormente.

Una hoja activa es la hoja en la que está trabajando en un libro de trabajo. El nombre en la pestaña de la hoja activa está en negrita por defecto. Mientras tanto, una celda activa es la celda que está seleccionada y en la que se ingresan los datos cuando comienza a escribir. Solo una celda está activa a la vez. La celda activa está rodeada por un borde grueso para que se vea contra las otras celdas. Aspose.Cells también le permite seleccionar un rango de celdas en la hoja de cálculo.
### **Activar una hoja y hacer un Cell activo**
Aspose.Cells proporciona un API específico para estas tareas. Por ejemplo, el método WorksheetCollection.setActiveSheetIndex es útil para configurar una hoja activa. De manera similar, el método Worksheet.setActiveCell se usa para establecer y obtener una celda activa en una hoja de cálculo.

Si desea que las barras de desplazamiento horizontal y vertical se desplacen a la posición del índice de fila y columna para brindar una buena vista de los datos seleccionados cuando se abre el archivo en Microsoft Excel, use las propiedades Worksheet.setFirstVisibleRow y Worksheet.setFirstVisibleColumn.

El siguiente ejemplo muestra cómo activar una hoja de cálculo y activar una celda en ella. Las barras de desplazamiento se desplazan para hacer que la segunda fila y la segunda columna sean sus primeras filas y columnas visibles.

**Configuración de la celda B2 como una celda activa** 

![todo:imagen_alternativa_texto](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Seleccionar un rango de Cells en la hoja de trabajo**
Aspose.Cells proporciona el método Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Usando el último parámetro - removeOthers - a verdadero, se eliminan otras selecciones de celdas o rangos de celdas en la hoja.

El siguiente ejemplo muestra cómo seleccionar un rango de celdas en la hoja de cálculo activa.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Todas las clases y métodos anteriores están disponibles con la versión con licencia de Aspose.Cells.

{{% /alert %}} 
## **Formateo de filas y columnas**
Dar formato a las filas y columnas de una hoja de cálculo para darle un aspecto al informe es posiblemente la función más utilizada de la aplicación Excel. Las API Aspose.Cells también brindan esta funcionalidad a través de su modelo de datos al exponer la clase Style, que maneja principalmente todas las funciones relacionadas con el estilo, como la fuente y sus atributos, la alineación del texto, los colores de fondo/primer plano, los bordes, el formato de visualización de números y literales de fecha, etc. . Otra clase útil que proporcionan las API Aspose.Cells es StyleFlag, que permite la reutilización del objeto Style.

En este artículo, intentaremos explicar cómo usar Aspose.Cells for Java API para aplicar formato a filas y columnas.
### **Formateo de filas y columnas**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase Worksheet. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class proporciona la colección Cells. La colección Cells proporciona una colección de filas.
#### **Dar formato a una fila**
Cada elemento de la colección Rows representa un objeto Row. El objeto Row ofrece el método applyStyle que se usa para aplicar formato a una fila.

Para aplicar el mismo formato a una fila, use el objeto Estilo:

1. Agregue un objeto Style a la clase Workbook llamando a su método createStyle.
1. Establezca las propiedades del objeto Estilo para aplicar la configuración de formato.
1. Asigne el objeto Style configurado al método applyStyle de un objeto Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Dar formato a una columna**
La colección Cells proporciona una colección Columnas. Cada elemento de la colección Columns representa un objeto Column. Similar al objeto Row, el objeto Column ofrece el método applyStyle que se utiliza para establecer el formato de la columna. Use el método applyStyle del objeto Column para formatear una columna de la misma manera que una fila.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Configuración del formato de visualización de números y fechas para filas y columnas**
Si el requisito es establecer el formato de visualización de números y fechas para una fila o columna completa, entonces el proceso es más o menos el mismo que se discutió anteriormente, sin embargo, en lugar de establecer parámetros para el contenido textual, configurará el formato de los números. y fechas usando Style.Number o Style.Custom. Tenga en cuenta que la propiedad Style.Number es de tipo entero y hace referencia a los formatos integrados de número y fecha, mientras que la propiedad Style.Custom es de tipo cadena y acepta los patrones válidos.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Consulte el artículo detallado sobre[Configuración de formatos de visualización de números y [fechas]](/cells/es/java/data-formatting/).

{{% /alert %}}
