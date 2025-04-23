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

Aspose.Cells proporciona el método [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) usado para establecer el estilo de formato de una celda. Además, se usa un objeto de la clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) que proporciona propiedades para configurar las opciones de fuente.
#### **Añadir bordes a una celda**
Agrega bordes a una celda con el método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). El tipo de borde se pasa como parámetro. Todos los tipos de borde están predefinidos en la enumeración [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Tipos de Bordes**|**Descripción**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com/aspose.cells/bordertype#BOTTOM-BORDER)|La línea de borde inferior|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|Una línea diagonal de arriba izquierda a derecha inferior|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|Una línea diagonal de abajo izquierda a arriba derecha|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|La línea de borde izquierda|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|La línea de borde derecha|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|La línea de borde superior|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Solo para estilos dinámicos, como el formato condicional.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Solo para estilo dinámico, como formato condicional.|
Para establecer el color de línea, selecciona un color utilizando la enumeración [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) y pásalo al parámetro [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) del método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Los estilos de línea están predefinidos en la enumeración [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Estilos de Línea**|**Descripción**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|Representa una línea delgada raya-punto|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|Representa una línea delgada raya-punto-punto|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representa línea punteada|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representa línea de puntos|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representa línea doble|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representa línea fina|
|[MEDIO_DOS PUNTOS](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|Representa línea mediana de guiones y puntos|
|[MEDIO_DOS PUNTOS_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|Representa línea de guiones y puntos medio|
|[MEDIO_GUIONES](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|Representa línea de guiones medianos|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representa ninguna línea|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representa línea media|
|[DIAGONAL_DALTADA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|Representa línea diagonal inclinada de guiones largos|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representa línea gruesa|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representa línea fina|
Seleccione uno de los estilos de línea anteriores y luego asígnele al método [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) del objeto [Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style).

A continuación se genera la siguiente salida al ejecutar el código a continuación.

**Bordes aplicados en todos los lados de una celda** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Agregar bordes a un rango de celdas**
Es posible agregar bordes a un rango de celdas en lugar de solo a una celda. Primero, cree un rango de celdas llamando al método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), que acepta los siguientes parámetros:

- **Primera fila**, la primera fila del rango.
- **Primer columna**, la primera columna del rango.
- **Número de filas**, el número de filas en el rango.
- **Número de columnas**, el número de columnas en el rango.

El método [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) devuelve un objeto [Rango](https://reference.aspose.com/cells/java/com.aspose.cells/Range), que contiene el rango especificado. El objeto [Rango](https://reference.aspose.com/cells/java/com.aspose.cells/Range) proporciona un método [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) que acepta los siguientes parámetros:

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

Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Microsoft Excel. La clase ofrece el método [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) que toma los siguientes parámetros para agregar un color personalizado y modificar la paleta:

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

Aspose.Cells proporciona el método [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) en la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) que se usa para establecer el formato de una celda. Además, el objeto de la clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) puede usarse para configurar las opciones de fuente.

{{% alert color="primary" %}} 

Para establecer el color de primer plano o de fondo de una celda, utilice las propiedades [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) o [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Estas propiedades solo entran en efecto si la propiedad [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) del objeto [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) está configurada.

{{% /alert %}} 

La propiedad [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) establece el color de sombreado de la celda.

La propiedad [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) especifica el patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona la enumeración [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) que contiene un conjunto de tipos predefinidos de patrones de fondo.

|**Tipo de Patrón**|**Descripción**|
| :- | :- |
|[CROSSHATCH_DIAGONAL](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|Representa un patrón de rayas diagonales cruzadas|
|[RAYAS_DIAGONALES](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|Representa un patrón de rayas diagonales|
|[GRIS_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|Representa patrón gris de 6.25%|
|[GRIS_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|Representa patrón gris de 12.5%|
|[GRIS_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|Representa patrón gris de 25%|
|[GRIS_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|Representa patrón gris de 50%|
|[GRIS_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|Representa patrón gris de 75%|
|[RAYAS_HORIZONTALES](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|Representa patrón de rayas horizontales|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Representa sin fondo|
|[RAYAS_DIAGONAL_INVERSA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|Representa patrón de rayas diagonales inversas|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representa un patrón sólido|
|[CROSSHATCH_DIAGONAL_GRUESO](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|Representa patrón de rayas diagonales gruesas|
|[CROSSHATCH_DIAGONAL_FINO](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|Representa patrón de rayas diagonales finas|
|[RAYAS_DIAGONAL_FINAS](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|Representa patrón de rayas diagonales finas|
|[CROSSHATCH_HORIZONTAL_FINAS](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|Representa patrón de cruce horizontal fino|
|[RAYAS_HORIZONTALES_FINAS](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|Representa patrón de rayas horizontales finas|
|[RAYAS_INVERTIDAS_DIAGONALES](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|Representa patrón de rayas diagonales invertidas finas|
|[RAYAS_VERTICALES_FINAS](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|Representa patrón de rayas verticales finas|
|[RAYAS_VERTICALES](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|Representa patrón de rayas verticales|
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

La clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) proporciona el método [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-) que acepta los siguientes parámetros para seleccionar un rango de caracteres en una celda:

- **Índice de inicio**, el índice del carácter desde el que se inicia la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

En el archivo de salida, en la celda A1, la palabra 'Visitar' está formateada con la fuente predeterminada pero 'Aspose!' está en negrita y azul.

**Formato de caracteres seleccionados** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Si estás interesado en [formatear una porción de Texto Enriquecido en una celda](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/), considera usar los métodos [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) y Cell.setCharacters. El método [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) se usa para acceder a las porciones del texto y luego se pueden hacer modificaciones usando el método Cell.setCharacters, mientras que el método **get** devuelve un array de objetos [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) que se pueden manipular para establecer varias propiedades como nombre de fuente, color de fuente, negrita, etc., y el método **set** puede usarse para aplicar los cambios.

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
{{< app/cells/assistant language="java" >}}
