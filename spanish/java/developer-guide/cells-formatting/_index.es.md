---
title: Formatos de las Celdas
type: docs
weight: 100
url: /es/java/cells-formatting/
---

## **Añadiendo Bordes a las Celdas**
Microsoft Excel permite a los usuarios formatear celdas añadiendo bordes.

**Configuración de bordes en Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

El tipo de borde depende de dónde se añada. Por ejemplo, un borde superior se añade en la posición superior de una celda. Los usuarios también pueden modificar el estilo de línea y el color de los bordes.

Con Aspose.Cells, los desarrolladores pueden añadir bordes y personalizar su apariencia de la misma forma flexible que en Microsoft Excel.
### **Añadiendo Bordes a las Celdas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada ítem en la colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/celula).

Aspose.Cells proporciona el método [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/celula) usado para establecer el estilo de formato de una celda. Además, se utiliza el objeto de la clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) que proporciona propiedades para configurar la configuración de fuente.
#### **Añadir bordes a una celda**
Añadir bordes a una celda con el método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). El tipo de borde se pasa como parámetro. Todos los tipos de bordes están predefinidos en la enumeración [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Tipos de Bordes**|**Descripción**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La línea de borde inferior|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Una línea diagonal de arriba izquierda a abajo derecha|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Una línea diagonal de abajo izquierda a arriba derecha|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La línea de borde izquierdo|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La línea de borde derecho|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La línea de borde superior|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Solo para estilos dinámicos, como el formato condicional.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Solo para estilo dinámico, como formato condicional.|
Para establecer el color de la línea, seleccione un color utilizando la enumeración [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) y páselo al parámetro Color del método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Los estilos de línea están predefinidos en la enumeración [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Estilos de Línea**|**Descripción**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Representa línea de guion punteado fina|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Representa línea de guion punto-punto-punteado fina|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representa línea punteada|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representa línea de puntos|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representa línea doble|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representa línea fina|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Representa línea de guion punteado medio|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Representa línea de guion punto-punto-punteado medio|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Representa línea de guion medio|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representa ninguna línea|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representa línea media|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Representa línea de guion punteado medio inclinado|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representa línea gruesa|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representa línea fina|
Seleccione uno de los estilos de línea anteriores y luego asígnelo al método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).

A continuación se genera la siguiente salida al ejecutar el código a continuación.

**Bordes aplicados en todos los lados de una celda** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Agregar bordes a un rango de celdas**
Es posible agregar bordes a un rango de celdas en lugar de solo a una celda individual. Primero, cree un rango de celdas llamando al método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), que toma los siguientes parámetros:

- **Primera fila**, la primera fila del rango.
- **Primer columna**, la primera columna del rango.
- **Número de filas**, el número de filas en el rango.
- **Número de columnas**, el número de columnas en el rango.

El método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) devuelve un objeto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range), que contiene el rango especificado. El objeto [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) proporciona un método [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) que toma los siguientes parámetros:

- **Tipo de borde de celda**, el estilo de la línea de borde, seleccionado de la enumeración [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- **Color**, el color de la línea de borde, seleccionado de la enumeración [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

A continuación se genera la siguiente salida al ejecutar el código a continuación.

**Bordes aplicados en un rango de celdas** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Colores y paleta**
Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

**Configuraciones de paleta en Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Con Aspose.Cells no solo es posible utilizar colores existentes, sino también colores personalizados. Antes de usar un color personalizado, agréguelo a la paleta. Este tema explica cómo agregar colores personalizados a la paleta.
### **Agregar colores personalizados a la paleta**
Aspose.Cells también admite una paleta de 56 colores. Una paleta de colores estándar se muestra arriba. Si desea utilizar un color personalizado que no está definido en la paleta, deberá agregar ese color a la paleta antes de usarlo.

{{% alert color="primary" %}} 

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta se modifica y cualquier elemento en el archivo formateado con el color anterior se cambia. Por lo tanto, al cambiar la paleta, tenga mucho cuidado. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no existe tal limitación para XLSX u otros formatos avanzados de archivos de MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase proporciona el método [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) que toma los siguientes parámetros para agregar un color personalizado y modificar la paleta:

- **Color personalizado**, el color personalizado que se agregará a la paleta.
- **Índice**, el índice del color que será reemplazado con el color personalizado. Debe estar entre 0 y 55.

El ejemplo a continuación agrega un color personalizado a la paleta antes de aplicarlo a una fuente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Colores y patrones de fondo**
Microsoft Excel puede establecer los colores de primer plano (contorno) y de fondo (relleno) de celdas y patrones de fondo, como se muestra a continuación.

**Estableciendo colores y patrones de fondo en Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a usar estas características utilizando Aspose.Cells.
### **Estableciendo Colores y Patrones de Fondo**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene un [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada elemento en la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells proporciona el método [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) que se utiliza para establecer el formato de una celda. También se puede utilizar el objeto de la clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) para configurar la configuración de fuente.

{{% alert color="primary" %}} 

Para establecer el color de primer plano o de fondo de una celda, utilice las propiedades [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) o [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Estas propiedades solo entran en efecto si la propiedad [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) está configurada.

{{% /alert %}} 

La propiedad [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) establece el color de sombreado de la celda.

La propiedad [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) especifica el patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona la enumeración [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) que contiene un conjunto de tipos predefinidos de patrones de fondo.

|**Tipo de Patrón**|**Descripción**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Representa un patrón de sombreado diagonal cruzado|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Representa un patrón de raya diagonal|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Representa un patrón de gris al 6.25%|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Representa un patrón de gris al 12.5%|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Representa un patrón de gris al 25%|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Representa un patrón de gris al 50%|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Representa un patrón de gris al 75%|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Representa un patrón de rayas horizontales|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Representa sin fondo|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Representa un patrón de rayas diagonales invertidas|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representa un patrón sólido|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Representa un patrón de cuadrícula diagonal gruesa|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Representa un patrón de cuadrícula diagonal delgada|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Representa un patrón de rayas diagonales delgadas|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Representa un patrón de cuadrícula horizontal delgada|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Representa un patrón de rayas horizontales delgadas|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Representa un patrón de rayas diagonales invertidas delgadas|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Representa un patrón de rayas verticales delgadas|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Representa un patrón de rayas verticales|
En el ejemplo a continuación, el color de primer plano de la celda A1 está establecido pero A2 está configurada para tener tanto el color de primer plano como el color de fondo con un patrón de fondo de rayas verticales.

La siguiente salida se genera al ejecutar el código.

**Colores de primer plano y fondo aplicados en celdas con patrones de fondo** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Importante saber**
{{% alert color="primary" %}} 

- Para configurar el color de primer plano o fondo de una celda, utilice las propiedades [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) o [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Ambas propiedades solo tendrán efecto si se configura la propiedad [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).
- La propiedad [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) establece el color de sombreado de la celda.
  La propiedad [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells proporciona una enumeración, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), que contiene un conjunto de tipos predefinidos de patrones de fondo.
- Si selecciona el valor [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) de la enumeración [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), el color de primer plano no se aplica.
  Del mismo modo, el color de fondo no se aplica si selecciona los valores [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) o [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- Al recuperar el color de sombreado/relleno de una celda, si [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) es [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) devolverá *Color.Empty*.

{{% /alert %}} 
## **Formato de caracteres seleccionados en una celda**
El artículo [Dealing with Font Settings](/cells/es/java/dealing-with-font-settings/) explica cómo dar formato a las celdas, pero solo cómo dar formato al contenido de las celdas completas. ¿Qué ocurre si desea formatear solo algunos caracteres seleccionados?

Aspose.Cells admite esta función. Este tema explica cómo utilizar esta característica.
### **Formato de caracteres seleccionados**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene un [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada elemento en la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

La clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) proporciona un método [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) que toma los siguientes parámetros para seleccionar un rango de caracteres en una celda:

- **Índice de inicio**, el índice del carácter desde el que se inicia la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

En el archivo de salida, en la celda A1, la palabra 'Visitar' está formateada con la fuente predeterminada pero 'Aspose!' está en negrita y azul.

**Formato de caracteres seleccionados** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Si está interesado en [formatear una parte del texto enriquecido en una celda](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/), considere usar los métodos [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) y Cell.setCharacters. El método [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) se usa para acceder a las partes del texto y luego se pueden realizar modificaciones mediante el método Cell.setCharacters, mientras que el método **get** devuelve una matriz de objetos [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) que se pueden manipular para establecer varias propiedades como el nombre de fuente, el color de fuente, la negrita, etc., y el método **set** se puede utilizar para aplicar los cambios.

{{% /alert %}}

## **Temas avanzados**
- [Configuración de alineación](/cells/es/java/cells-alignment-settings/)
- [Formato condicional](/cells/es/java/conditional-formatting/)
- [Formato de datos](/cells/es/java/data-formatting/)
- [Temas y colores de Excel](/cells/es/java/excel-2007-themes-and-colors/)
- [Tratamiento de configuraciones de fuente](/cells/es/java/dealing-with-font-settings/)
- [Dar formato a celdas de hoja de cálculo en un libro de trabajo](/cells/es/java/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas 1904](/cells/es/java/implement-1904-date-system/)
- [Combinar y descombinar celdas](/cells/es/java/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/java/cells-number-settings/)
- [Preservar el prefijo de comilla simple del valor de la celda o rango](/cells/es/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Estilo y formato de datos](/cells/es/java/styling-and-data-formatting/)
