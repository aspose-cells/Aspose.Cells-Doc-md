---
title: Formato de Datos
type: docs
weight: 80
url: /es/java/data-formatting/
---

## **Enfoques para Formatear Datos en Celdas**
Es un hecho común que si las celdas de la hoja de cálculo están formateadas adecuadamente, se vuelve más fácil para los usuarios leer el contenido (datos) de la celda. Hay muchas formas de formatear celdas y su contenido. La forma más sencilla es formatear celdas usando Microsoft Excel en un entorno WYSIWYG mientras se crea una Hoja de Cálculo de Diseñador. Después de crear la hoja de cálculo de diseñador, puedes abrir la hoja de cálculo usando Aspose.Cells manteniendo todas las configuraciones de formato guardadas con la hoja de cálculo. Otra forma de formatear celdas y su contenido es usar la API de Aspose.Cells. En este tema, describiremos dos enfoques para formatear celdas y su contenido con el uso de la API de Aspose.Cells.
### **Formato de celdas**
Los desarrolladores pueden formatear celdas y su contenido utilizando la API flexible de Aspose.Cells. Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una colección de Cells. Cada elemento en la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) representa un objeto de la clase **Cell**.

Aspose.Cells proporciona la propiedad [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), utilizada para establecer el estilo de formato de una celda. Además, Aspose.Cells también proporciona una clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) que se utiliza para el mismo propósito. Aplica diferentes tipos de estilos de formato en las celdas para establecer sus colores de fondo o primer plano, bordes, fuentes, alineaciones horizontal y vertical, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.
#### **Usando el Método setStyle**
Cuando se aplican diferentes estilos de formato a diferentes celdas, es mejor usar el método setStyle de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). A continuación se muestra un ejemplo para demostrar el uso del método setStyle para aplicar varias configuraciones de formato en una celda.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Usando el Objeto de Estilo**
Al aplicar el mismo estilo de formato a diferentes celdas, usa el objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

1. Agregar un objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) a la colección de Estilos de la clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) llamando al método createStyle de la clase Workbook.
1. Acceder al objeto de Estilo recién agregado desde la colección de Estilos.
1. Establecer las propiedades deseadas del objeto de Estilo para aplicar las configuraciones de formato deseadas.
1. Asignar el objeto de Estilo configurado a la propiedad de Estilo de cualquier celda deseada.

Este enfoque puede mejorar significativamente la eficiencia de sus aplicaciones y también ahorrar memoria.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Aplicar efectos de relleno de degradado**
Para aplicar sus deseado efectos de relleno de degradado a la celda, use el método setTwoColorGradient del objeto Style correspondientemente.
#### **Ejemplo de Código**
La siguiente salida se logra ejecutando el código a continuación. 

**Aplicando efectos de relleno de degradado** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Configurando Ajustes de Alineación**
Cualquiera que haya usado Microsoft Excel para formatear celdas estará familiarizado con las configuraciones de alineación en Microsoft Excel.

**Ajustes de alineación en Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Como puedes ver en la figura anterior, hay diferentes tipos de opciones de alineación:

- [Alineación de texto](/cells/es/java/data-formatting/) (horizontal y vertical)
- [Sangría](/cells/es/java/data-formatting/)
- [Orientación](/cells/es/java/data-formatting/)
- [Control de texto](/cells/es/java/data-formatting/)
- [Dirección del texto](/cells/es/java/data-formatting/)

Todos estos ajustes de alineación son completamente compatibles con Aspose.Cells y se discuten con más detalle a continuación.
### **Configurando Ajustes de Alineación**
Aspose.Cells provee una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La clase Worksheet provee una colección Cells. Cada elemento en la colección Cells representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells provee el método setStyle en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) que es usado para el formato de la celda. La clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) provee propiedades útiles para configurar ajustes de fuente.

Seleccione cualquier tipo de alineación de texto usando la enumeración TextAlignmentType. Los tipos predefinidos de alineación de texto en la enumeración TextAlignmentType son:

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
{{% alert color="primary" %}} 

También puedes aplicar el ajuste distribuido justificado utilizando el método Style.setJustifyDistributed().

{{% /alert %}} 
#### **Alineación horizontal**
Utiliza el método setHorizontalAlignment del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) para alinear el texto horizontalmente.

El siguiente resultado se logra al ejecutar el código de ejemplo a continuación:

**Alineando el texto horizontalmente** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Alineación vertical**
Utiliza el método setVerticalAlignment del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) para alinear el texto verticalmente.

El siguiente resultado se obtiene al establecer VerticalAlignment en centrado.

**Alineando el texto verticalmente** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Sangría**
Es posible establecer el nivel de sangría del texto en una celda utilizando el método setIndentLevel del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Se logra la siguiente salida cuando se establece IndentLevel en 2.

**Nivel de sangría ajustado a 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientación**
Establezca la orientación (rotación) del texto en una celda con el método setRotationAngle del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Se logra la siguiente salida cuando se establece el ángulo de rotación en 25.

**Ángulo de rotación establecido en 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Control de texto**
La siguiente sección explica cómo controlar el texto mediante el ajuste del ajuste de texto, el ajuste al tamaño y otras opciones de formato.
#### **Envolver texto**
El ajuste de texto en una celda facilita la lectura: la altura de la celda se ajusta para que quepa todo el texto, en lugar de cortarlo o derramarse en celdas adyacentes.

Establezca el ajuste de texto en on u off con el método setTextWrapped del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Se logra la siguiente salida cuando el ajuste de texto está habilitado.

**Texto envuelto dentro de la celda** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Reducir para ajustar**
Una opción para ajustar el texto en un campo es reducir el tamaño del texto para que quepa en las dimensiones de la celda. Esto se hace configurando la propiedad IsTextWrapped del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) en **true**.

Se logra la siguiente salida cuando el texto se reduce para ajustarse a la celda.

**Texto reducido para ajustarse dentro de los límites de la celda** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Combinar celdas**
Al igual que Microsoft Excel, Aspose.Cells admite fusionar varias celdas en una sola.

Se logra la siguiente salida si se fusionan las tres celdas de la primera fila para crear una gran celda única.

**Tres celdas fusionadas para crear una gran celda** 

![todo:image_alt_text](data-formatting_9.png)

Utilice el método Fusión de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) para fusionar celdas. El método Fusión toma los siguientes parámetros:

- Primera fila, la primera fila desde donde se inicia la fusión.
- Primera columna, la primera columna desde donde se inicia la fusión.
- Número de filas, el número de filas a fusionar.
- Número de columnas, el número de columnas a fusionar.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Dirección del texto**
Es posible establecer el orden de lectura del texto en las celdas. El orden de lectura es el orden visual en el que se muestran los caracteres, palabras, etc. Por ejemplo, el inglés es un idioma de izquierda a derecha, mientras que el árabe es un idioma de derecha a izquierda.

El orden de lectura se establece con la propiedad DirecciónTexto del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style). Aspose.Cells proporciona tipos predefinidos de dirección del texto en la enumeración TextDirectionType.

|**Tipos de dirección de texto**|**Descripción**|
| :- | :- |
|Context|El orden de lectura es coherente con el idioma del primer carácter introducido|
|LeftToRight|Orden de lectura de izquierda a derecha|
|RightToLeft|Orden de lectura de derecha a izquierda|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Se logra la siguiente salida si se establece el orden de lectura del texto de derecha a izquierda.

**Establecer el orden de lectura del texto de derecha a izquierda** 

![todo:image_alt_text](data-formatting_10.png)
## **Formato de caracteres seleccionados en una celda**
[Tratamiento de la configuración de fuente](/cells/es/java/dealing-with-font-settings/) explicó cómo formatear celdas, pero solo cómo formatear el contenido de las celdas completas. ¿Qué sucede si desea formatear solo caracteres seleccionados?

Aspose.Cells admite esta función. Este tema explica cómo utilizar esta característica.
### **Formato de caracteres seleccionados**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una colección de hojas de cálculo que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase Worksheet proporciona una colección de celdas. Cada elemento en la colección de celdas representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La clase Cell proporciona el método characters que toma los siguientes parámetros para seleccionar un rango de caracteres en una celda:

- **Índice de inicio**, el índice del carácter desde el que se inicia la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

En el archivo de salida, en la celda A1, la palabra 'Visitar' está formateada con la fuente predeterminada pero 'Aspose!' está en negrita y azul.

**Formato de caracteres seleccionados** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Si está interesado en [formatear una parte de texto enriquecido en una [celda](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/), considere usar los métodos Cell.getCharacters & Cell.setCharacters. El método Cell.getCharacters se utiliza para acceder a las partes del texto y luego se pueden realizar modificaciones usando el método Cell.setCharacters, mientras que el método **get** devuelve una serie de objetos FontSetting que se pueden manipular para establecer varias propiedades como el nombre de la fuente, el color de la fuente, la negrita, etc. y el método **set** se puede utilizar para aplicar los cambios.

{{% /alert %}} 
## **Activar Hojas y Hacer que una Celda sea Activa o Seleccionar un Rango de Celdas en la Hoja de Cálculo**
A veces, es posible que necesite activar una hoja de cálculo específica para que sea la primera que se muestra cuando alguien abre el archivo en Microsoft Excel. También puede necesitar activar una celda específica de manera que las barras de desplazamiento se desplacen hacia la celda activa para que sea claramente visible. Aspose.Cells es capaz de realizar todas las tareas mencionadas anteriormente.

Una hoja activa es la hoja en la que está trabajando en un libro de trabajo. El nombre en la pestaña de la hoja activa está en negrita de forma predeterminada. Por otro lado, una celda activa es la celda que está seleccionada y en la que se introduce datos cuando se comienza a escribir. Solo una celda está activa a la vez. La celda activa está rodeada por un borde grueso para que se muestre contra las demás celdas. Aspose.Cells también le permite seleccionar un rango de celdas en la hoja de cálculo.
### **Activar una Hoja y Hacer que una Celda sea Activa**
Aspose.Cells proporciona una API específica para estas tareas. Por ejemplo, el método WorksheetCollection.setActiveSheetIndex es útil para establecer una hoja activa. Del mismo modo, el método Worksheet.setActiveCell se utiliza para establecer y obtener una celda activa en una hoja de cálculo.

Si desea que las barras de desplazamiento horizontal y vertical se desplacen a la posición del índice de fila y columna para mostrar una buena vista de los datos seleccionados cuando el archivo se abre en Microsoft Excel, utilice las propiedades Worksheet.setFirstVisibleRow y Worksheet.setFirstVisibleColumn.

El siguiente ejemplo muestra cómo activar una hoja de cálculo y hacer que una celda en ella sea activa. Las barras de desplazamiento se desplazan para hacer que la 2ª fila y la 2ª columna sean su primera fila y columna visible.

**Establecer la celda B2 como celda activa** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Seleccionar un Rango de Celdas en la Hoja de Cálculo**
Aspose.Cells proporciona el método Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Usando el último parámetro - removeOthers - como true, se eliminan otras selecciones de celdas o rangos de celdas en la hoja.

El siguiente ejemplo muestra cómo seleccionar un rango de celdas en la hoja de cálculo activa.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Todas las clases y métodos mencionados están disponibles con la versión con licencia de Aspose.Cells.

{{% /alert %}} 
## **Formatos de filas y columnas**
Dar formato a las filas y columnas en una hoja de cálculo para darle al informe una apariencia es posiblemente la característica más utilizada de la aplicación Excel. Las API de Aspose.Cells también proporcionan esta funcionalidad a través de su modelo de datos exponiendo la clase Estilo, que maneja principalmente todas las características relacionadas con el estilo, como la fuente y sus atributos, la alineación del texto, los colores de fondo/primero plano, los bordes, el formato de visualización para números y literales de fecha, entre otros. Otra clase útil que proporcionan las API de Aspose.Cells es StyleFlag, que permite la reutilización del objeto Estilo 

En este artículo, intentaremos explicar cómo usar la API Aspose.Cells for Java para aplicar formato a filas y columnas. 
### **Formato de filas y columnas**
Aspose.Cells proporciona una clase, [Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una Colección de hojas de cálculo que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase Hoja de cálculo. La clase [Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona la colección Celdas. La colección Celdas proporciona una colección de Filas
#### **Dar formato a una fila**
Cada elemento en la colección de Filas representa un objeto Fila. El objeto Fila ofrece el método applyStyle utilizado para aplicar formato a una fila.

Para aplicar el mismo formato a una fila, use el objeto Estilo:

1. Agregue un objeto Estilo a la clase Libro de trabajo llamando a su método createStyle.
1. Configure las propiedades del objeto Estilo para aplicar la configuración de formato.
1. Asigne el objeto Estilo configurado al método applyStyle de un objeto Fila





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Dar formato a una columna**
La colección Celdas proporciona una colección de Columnas. Cada elemento en la colección de Columnas representa un objeto Columna. Similar al objeto Fila, el objeto Columna ofrece el método applyStyle utilizado para establecer el formato de la columna. Utilice el método applyStyle del objeto Columna para dar formato a una columna de la misma manera que una fila.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Configuración del formato de visualización de números y fechas para filas y columnas**
Si el requisito es establecer el formato de visualización de números y fechas para una fila o columna completa, el proceso es más o menos el mismo que se discutió anteriormente, sin embargo, en lugar de establecer parámetros para el contenido textual, establecerá el formato para números y fechas usando Style.Number o Style.Custom. Tenga en cuenta que la propiedad Style.Number es de tipo entero y se refiere a los formatos de fecha y número integrados, mientras que la propiedad Style.Custom es de tipo cadena y acepta los patrones válidos.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Configuración de formatos de visualización de números y [Fechas](/cells/es/java/data-formatting/).

{{% /alert %}}
