---
title: Formato de celdas
description: Aprenda a dar formato y estilo a las celdas en Aspose.Cells for .NET, incluido el formato de números, el formato de fecha, los estilos de fuente y otras opciones de estilo de celda. Nuestra guía le ayudará a crear hojas de cálculo atractivas y de aspecto profesional.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/net/cells-formatting/
---
##  **Introducción**

{{% alert color="primary" %}}

 Aspose.Cells proporciona la[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos de la[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) clase, utilizada para obtener/establecer el estilo de formato de una celda. Aspose.Cells también proporciona un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)clase.

{{% /alert %}}

##  **Cómo formatear Cells usando los métodos GetStyle y SetStyle**

Aplique diferentes tipos de estilos de formato en celdas para establecer colores de fondo o primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

###  **Cómo utilizar los métodos GetStyle y SetStyle**

 Si los desarrolladores necesitan aplicar diferentes estilos de formato a diferentes celdas, entonces es mejor obtener el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) de la celda usando[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) método, especifique los atributos de estilo y luego aplique el formato usando[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)método. A continuación se proporciona un ejemplo para demostrar este enfoque para aplicar varios formatos en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **Cómo utilizar un objeto de estilo para dar formato diferente Cells**

 Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto. Siga los pasos a continuación para utilizar el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto:

1.  Agrega un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto llamando al[**Crear estilo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) método de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase
1.  Accede a los recién agregados[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  Establezca las propiedades/atributos deseados del[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto para aplicar la configuración de formato deseada
1.  Asigne el configurado[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto a las celdas deseadas

Este enfoque puede mejorar enormemente la eficiencia de sus aplicaciones y también ahorrar memoria.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Cómo utilizar Microsoft estilos predefinidos de Excel 2007**

Si necesita aplicar diferentes estilos de formato para Microsoft Excel 2007, aplique estilos usando Aspose.Cells API. A continuación se proporciona un ejemplo para demostrar este enfoque para aplicar un estilo predefinido en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Cómo dar formato a los caracteres seleccionados en un Cell**

Tratar con la configuración de fuentes explica cómo formatear el texto en las celdas, pero solo explica cómo formatear todo el contenido de la celda. ¿Qué sucede si desea formatear solo los caracteres seleccionados?

Aspose.Cells también admite esta función. Este tema explica cómo utilizar esta función de forma eficaz.

###  **Cómo dar formato a los caracteres seleccionados**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene el[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 El[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase proporciona la[**Caracteres**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)Método que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- *Índice de inicio**, el índice del carácter desde el que comienza la selección.
- *Número de caracteres**, el número de caracteres a seleccionar.

 El[**Caracteres**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) El método devuelve una instancia del[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)clase que permite a los desarrolladores formatear los caracteres de la misma manera que lo harían con una celda, como se muestra a continuación en el ejemplo de código. En el archivo de salida, en la celda A1, la palabra 'Visita' tendrá el formato de fuente predeterminada pero 'Aspose!' es negrita y azul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Si está interesado en formatear una parte del texto enriquecido en una celda, considere usar el[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) métodos. El[[**Cell.GetCaracteres**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) Se utilizará este método para acceder a las partes del texto y luego se podrán realizar modificaciones utilizando el[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) método mientras que el**Conseguir** El método devuelve una matriz de[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objetos que se pueden manipular para establecer varias propiedades, como nombre de fuente, color de fuente, negrita, etc. y**Colocar** Se puede utilizar el método para aplicar los cambios.

{{% /alert %}}

##  **Cómo dar formato a filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato a las celdas una por una suele llevar más tiempo y no es una buena solución.
Para solucionar este problema, Aspose.Cells proporciona una forma sencilla y rápida que se analiza en detalle en este artículo.

###  **Formato de filas y columnas**

 Aspose.Cells proporciona una clase, la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. El[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección proporciona una[**Filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)recopilación.

###  **Cómo dar formato a una fila**

 Cada elemento en el[**Filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) colección representa un[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row) objeto. El[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row)objeto ofrece la[**Aplicar estilo**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) método utilizado para establecer el formato de la fila. Para aplicar el mismo formato a una fila, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto. Los pasos a continuación muestran cómo usarlo.

1.  Agrega un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) oponerse a la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase llamando a su[**Crear estilo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)método.
1.  Selecciona el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)propiedades del objeto para aplicar la configuración de formato.
1.  Active los atributos relevantes para el[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objeto.
1.  Asigne el configurado[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) oponerse a la[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **Cómo dar formato a una columna**

 El[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección también proporciona una[**columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) recopilación. Cada elemento en el[**columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) colección representa un[**Columna**](https://reference.aspose.com/cells/net/aspose.cells/column) objeto. similar a un[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row) objeto, el[**Columna**](https://reference.aspose.com/cells/net/aspose.cells/column) objeto también ofrece la[**Aplicar estilo**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)Método para formatear una columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **Temas avanzados**
- [Configuración de alineación](/cells/es/net/cells-alignment-settings/)
- [Configuración de borde](/cells/es/net/cells-border-settings/)
- [Establezca formatos condicionales de archivos Excel y ODS.](/cells/es/net/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/net/excel-themes-and-colors/)
- [Configuración de relleno](/cells/es/net/cells-fill-settings/)
- [Configuración de fuente](/cells/es/net/cells-font-settings/)
- [Dar formato a la hoja de trabajo Cells en un libro de trabajo](/cells/es/net/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fecha 1904](/cells/es/net/implement-1904-date-system/)
- [Fusionando y separando Cells](/cells/es/net/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/net/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

