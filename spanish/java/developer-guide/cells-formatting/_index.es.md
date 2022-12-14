---
title: Cells Formatos
type: docs
weight: 100
url: /es/java/cells-formatting/
---
## **Adición de bordes a Cells**
Microsoft Excel permite a los usuarios formatear celdas agregando bordes.

**Configuración de bordes en Microsoft Excel** 

![todo:imagen_alternativa_texto](cells-formatting_1.png)

El tipo de borde depende de dónde se agregue. Por ejemplo, un borde superior es uno que se agrega a la posición superior de una celda. Los usuarios también pueden modificar el estilo y el color de las líneas de los bordes.

Con Aspose.Cells, los desarrolladores pueden agregar bordes y personalizar su aspecto de la misma forma flexible que en Microsoft Excel.
### **Adición de bordes a Cells**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

 Aspose.Cells proporciona el[establecerEstilo](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) método en el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase utilizada para establecer el estilo de formato de una celda. Asimismo, el objeto de la[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class se utiliza y proporciona propiedades para configurar los ajustes de fuente.
#### **Adición de bordes a un Cell**
 Agregar bordes a una celda con el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[establecer borde](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) método. El tipo de borde se pasa como parámetro. Todos los tipos de borde están predefinidos en el[Tipo de borde](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)enumeración.

|**Tipos de borde**|**Descripción**|
|:- |:- |
|[BORDE INFERIOR](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|La línea del borde inferior|
|[DIAGONAL_ABAJO](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Una línea diagonal desde la parte superior izquierda hasta la parte inferior derecha|
|[DIAGONAL_ARRIBA](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Una línea diagonal desde abajo a la izquierda hasta arriba a la derecha|
|[BORDE_IZQUIERDO](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|La línea del borde izquierdo|
|[BORDE_DERECHO](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|La línea del borde derecho|
|[SUPERIOR_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|La línea del borde superior|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Solo para estilo dinámico, como el formato condicional.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Solo para estilo dinámico, como el formato condicional.|
 Para establecer el color de la línea, seleccione un color con el[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumeración y pásela al[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[establecer borde](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) parámetro Color del método. Los estilos de línea están predefinidos en el[Tipo de borde de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumeración.

|**Estilos de línea**|**Descripción**|
|:- |:- |
|[GUION PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Representa una línea delgada de puntos y guiones|
|[ESTRELLARSE_PUNTO_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Representa una línea delgada de puntos y guiones|
|[PUNTUAL](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representa la línea discontinua|
|[PUNTEADO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representa la línea punteada|
|[DOBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representa doble línea.|
|[PELO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representa la línea del cabello.|
|[MEDIO_ESTRELLARSE_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Representa una línea de puntos y guiones medianos|
|[MEDIO_ESTRELLARSE_PUNTO PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Representa una línea mediana de puntos y guiones|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Representa una línea discontinua mediana|
|[NINGUNA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representa ninguna línea|
|[MEDIO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representa la línea media|
|[INCLINADO_ESTRELLARSE_PUNTO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Representa una línea inclinada de puntos y guiones medianos|
|[GRUESO](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representa línea gruesa|
|[DELGADA](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representa una línea delgada|
 Seleccione uno de los estilos de línea anteriores y luego asígnelo al[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style)objetos[establecer borde](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) método.

El siguiente resultado se genera al ejecutar el siguiente código.

**Bordes aplicados en todos los lados de una celda** 

![todo:imagen_alternativa_texto](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Adición de bordes a un rango de Cells**
 Es posible agregar bordes a un rango de celdas en lugar de solo una celda. Primero, cree un rango de celdas llamando al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[crearRango](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), que toma los siguientes parámetros:

- **Primera fila**, la primera fila del rango.
- **Primera columna**, la primera columna del rango.
- **Número de filas**, el número de filas en el rango.
- **Número de columnas**, el número de columnas en el rango.

 los[crearRango](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) método devuelve un[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objeto, que contiene el rango especificado. los[Rango](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objeto proporciona un[establecerEsquemaFronteras](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) método que toma los siguientes parámetros:

- **Tipo de borde de celda**, el estilo de línea de borde, seleccionado de la[Tipo de borde de celda](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)enumeración.
- **Color**, el color de la línea del borde, seleccionado de la[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)enumeración.

El siguiente resultado se genera al ejecutar el siguiente código.

**Bordes aplicados en un rango de celdas** 

![todo:imagen_alternativa_texto](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **colores y paleta**
Una paleta es el número de colores disponibles para usar en la creación de una imagen. El uso de una paleta estandarizada en una presentación le permite al usuario crear una apariencia consistente. Cada archivo Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

**Configuraciones de paleta en Microsoft Excel** 

![todo:imagen_alternativa_texto](cells-formatting_4.png)

Con Aspose.Cells no solo es posible usar colores existentes sino también colores personalizados. Antes de usar un color personalizado, agréguelo a la paleta. Este tema explica cómo agregar colores personalizados a la paleta.
### **Adición de colores personalizados a la paleta**
Aspose.Cells también admite una paleta de 56 colores. Arriba se muestra una paleta de colores estándar. Si desea utilizar un color personalizado que no está definido en la paleta, deberá agregar ese color a la paleta antes de usarlo.

{{% alert color="primary" %}} 

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Entonces, cuando cambie la paleta, tenga mucho cuidado. Además, esta es la limitación en el formato de archivo XLS (Excel 97 - 2003), ya que no existe tal limitación para XLSX u otros formatos de archivo avanzados de MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Excel Microsoft. La clase proporciona la[cambioPaleta](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) método que toma los siguientes parámetros para agregar un color personalizado para modificar la paleta:

- **Color personalizado**, el color personalizado que se agregará a la paleta.
- **Índice**, el índice del color que se reemplazará con el color personalizado. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado a la paleta antes de aplicarlo en una fuente.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Colores y patrones de fondo**
Microsoft Excel puede establecer los colores de primer plano (contorno) y de fondo (relleno) de las celdas y los patrones de fondo como se muestra a continuación.

**Configuración de colores y patrones de fondo en Microsoft Excel** 

![todo:imagen_alternativa_texto](cells-formatting_5.png)

Aspose.Cells también es compatible con estas funciones de forma flexible. En este tema, aprendemos a usar estas funciones usando Aspose.Cells.
### **Configuración de colores y patrones de fondo**
Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

Aspose.Cells proporciona el[establecerEstilo](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) método en el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase que se utiliza para establecer el formato de una celda. Asimismo, el objeto de la[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style)La clase se puede utilizar para configurar los ajustes de fuente.

{{% alert color="primary" %}} 

 Para establecer el color de primer plano o de fondo de una celda, utilice el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[establecerColor de fondo](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) o[establecerColor de primer plano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) propiedades. Estas propiedades sólo entran en vigor si el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[establece un patron](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) la propiedad está configurada.

{{% /alert %}} 

los[establecerColor de primer plano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)La propiedad establece el color de sombreado de la celda.

los[establece un patron](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La propiedad especifica el patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona el[Tipo de fondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)enumeración que contiene un conjunto de tipos predefinidos de patrones de fondo.

|**tipo de patrón**|**Descripción**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Representa un patrón de sombreado diagonal|
|[RAYA_DIAGONAL](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Representa el patrón de rayas diagonales|
|[GRIS_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Representa un 6,25 % de patrón gris|
|[GRIS_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Representa un patrón gris del 12,5 %|
|[GRIS_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Representa un 25 % de patrón gris|
|[GRIS_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Representa un patrón gris del 50 %|
|[GRIS_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Representa un patrón gris del 75 %|
|[RAYA_HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Representa el patrón de rayas horizontales|
|[NINGUNA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|No representa antecedentes|
|[REVERSO_DIAGONAL_RAYA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Representa el patrón de rayas diagonales inversas|
|[SÓLIDO](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representa un patrón sólido|
|[GRUESO_DIAGONAL_CRUZADA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Representa un patrón de sombreado diagonal grueso|
|[DELGADA_DIAGONAL_CRUZADA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Representa un patrón de sombreado diagonal delgado|
|[DELGADA_DIAGONAL_RAYA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Representa un patrón de rayas diagonales delgadas|
|[DELGADA_HORIZONTAL_CRUZADA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Representa un patrón de sombreado horizontal delgado|
|[DELGADA_HORIZONTAL_RAYA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Representa un patrón de rayas horizontales delgadas|
|[DELGADA_REVERSO_RAYA_DIAGONAL](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Representa un patrón de rayas diagonales inversas delgadas|
|[DELGADA_VERTICAL_RAYA](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Representa un patrón de rayas verticales delgadas|
|[RAYA_VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Representa el patrón de rayas verticales|
En el ejemplo a continuación, el color de primer plano de la celda A1 está configurado pero A2 está configurado para tener colores de primer plano y de fondo con un patrón de fondo de rayas verticales.

El siguiente resultado se genera al ejecutar el código.

**Colores de primer plano y de fondo aplicados en celdas con patrones de fondo** 

![todo:imagen_alternativa_texto](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Importante saber**
{{% alert color="primary" %}} 

-  Para establecer el color frontal o de fondo de una celda, use el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[Color de primer plano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) o[Color de fondo](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) propiedades. Ambas propiedades tendrán efecto sólo si el[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objetos[Patrón](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) la propiedad está configurada.
-  los[Color de primer plano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) La propiedad establece el color de sombra de la celda.
 los[Patrón](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) La propiedad especifica el tipo de patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona una enumeración,[Tipo de fondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)que contiene un conjunto de tipos predefinidos de patrones de fondo.
-  Si selecciona[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) valor de la[Tipo de fondo](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) enumeración, el color de primer plano no se aplica.
 Asimismo, el color de fondo no se aplica si selecciona el[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) o[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) valores.
-  Al recuperar el sombreado/color de relleno de la celda, si[Estilo.Patrón](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) es[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Estilo.Color de primer plano](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) regresará*Color.Vacío*.

{{% /alert %}} 
## **Formateo de caracteres seleccionados en un Cell**
[Tratar con la configuración de fuentes](/cells/es/java/dealing-with-font-settings/) explicó cómo formatear celdas, pero solo cómo formatear el contenido de las celdas completas. ¿Qué sucede si desea formatear solo los caracteres seleccionados?

Aspose.Cells admite esta función. Este tema explica cómo utilizar esta característica.
### **Dar formato a los caracteres seleccionados**
Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

los[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase proporciona[caracteres](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) método que toma los siguientes parámetros para seleccionar un rango de caracteres en una celda:

- **Índice de comienzo**, el índice del carácter desde el que comenzar la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

En el archivo de salida, en la celda A1", la palabra 'Visita' tiene el formato de fuente predeterminado pero 'Aspose!' es negrita y azul.

**Formateo de caracteres seleccionados** 

![todo:imagen_alternativa_texto](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Si usted está interesado en[dar formato a una parte de texto enriquecido en una celda](/cells/es/java/access-and-update-the-portions-of-rich-text-of-cell/) , considere usar el[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) y Cell.setCharacters métodos. los[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) se va a usar para acceder a las partes del texto y luego se pueden hacer enmiendas usando el método Cell.setCharacters mientras que el**obtener**método devuelve una matriz de[Configuración de fuente](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) objetos que se pueden manipular para establecer varias propiedades, como el nombre de la fuente, el color de la fuente, la negrita, etc. y**establecer** El método se puede utilizar para aplicar los cambios.

{{% /alert %}}

## **Temas avanzados**
- [Configuración de alineación](/cells/es/java/cells-alignment-settings/)
- [Formato condicional](/cells/es/java/conditional-formatting/)
- [Formateo de datos](/cells/es/java/data-formatting/)
- [Temas y colores de Excel](/cells/es/java/excel-2007-themes-and-colors/)
- [Tratar con la configuración de fuentes](/cells/es/java/dealing-with-font-settings/)
- [Dar formato a la hoja de trabajo Cells en un libro de trabajo](/cells/es/java/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas de 1904](/cells/es/java/implement-1904-date-system/)
- [Fusión y desfusión Cells](/cells/es/java/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/java/cells-number-settings/)
- [Conservar el prefijo de comillas simples del valor o rango Cell](/cells/es/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Estilo y formato de datos](/cells/es/java/styling-and-data-formatting/)
