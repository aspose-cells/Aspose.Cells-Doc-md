---
title: Formato de celdas
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/net/cells-formatting/
description: Establezca el formato de número, el borde y el color de fondo para los archivos de Excel en .NET Framework, .NET Core, Mono o Xamarin Platforms.
---
## **Introducción**

{{% alert color="primary" %}}

 Aspose.Cells proporciona el[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos de la[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) clase, utilizada para obtener/establecer el estilo de formato de una celda. Aspose.Cells también proporciona un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)clase.

{{% /alert %}}

## **Formatee Cells usando los métodos GetStyle y SetStyle**

Aplique diferentes tipos de estilos de formato en las celdas para establecer colores de fondo o de primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

### **Uso de los métodos GetStyle y SetStyle**

 Si los desarrolladores necesitan aplicar diferentes estilos de formato a diferentes celdas, entonces es mejor obtener el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) de la celda usando[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) método, especifique los atributos de estilo y luego aplique el formato usando[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)método. A continuación se proporciona un ejemplo para demostrar este enfoque para aplicar varios formatos en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Uso de objetos de estilo para formatear diferentes Cells**

 Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto. Siga los pasos a continuación para usar el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto:

1.  Agrega un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto llamando al[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metodo de la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase
1.  Accede a los recién agregados[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto
1.  Establezca las propiedades/atributos deseados del[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto para aplicar la configuración de formato deseada
1. Asignar el configurado[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)oponerse a las celdas deseadas

Este enfoque puede mejorar en gran medida la eficiencia de sus aplicaciones y también ahorrar memoria.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Usando Microsoft Excel 2007 Estilos predefinidos**

Si necesita aplicar diferentes estilos de formato para Microsoft Excel 2007, aplique estilos usando Aspose.Cells API. A continuación se proporciona un ejemplo para demostrar este enfoque para aplicar un estilo predefinido en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Formateo de caracteres seleccionados en un Cell**

Tratar con la configuración de fuente explica cómo dar formato al texto en las celdas, pero solo explica cómo dar formato a todo el contenido de la celda. ¿Qué sucede si desea formatear solo los caracteres seleccionados?

Aspose.Cells también admite esta función. Este tema explica cómo usamos esta característica de manera efectiva.

### **Dar formato a los caracteres seleccionados**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase contiene el[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 los[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) la clase proporciona la[**Caracteres**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)método que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- **Índice de comienzo**, el índice del carácter desde el que comienza la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

 los[**Caracteres**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) método devuelve una instancia de la[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)class que permite a los desarrolladores formatear los caracteres de la misma manera que lo harían con una celda, como se muestra a continuación en el ejemplo de código. En el archivo de salida, en la celda A1, la palabra 'Visita' se formateará con la fuente predeterminada pero 'Aspose!' es negrita y azul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Si está interesado en formatear una porción de texto enriquecido en una celda, considere usar el[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) métodos. los[[**Cell.Obtener personajes**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) se va a utilizar el método para acceder a las partes del texto y luego se pueden hacer enmiendas usando el[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) método mientras que el**Obtener**método devuelve una matriz de[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objetos que se pueden manipular para establecer varias propiedades, como el nombre de la fuente, el color de la fuente, la negrita, etc. y**Establecer** El método se puede utilizar para aplicar los cambios.

{{% /alert %}}

## **Formateo de filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato en las celdas una por una a menudo lleva más tiempo y no es una buena solución.
Para abordar este problema, Aspose.Cells proporciona una forma simple y rápida que se analiza en detalle en este artículo.

### **Formateo de filas y columnas**

 Aspose.Cells proporciona una clase, el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)colección proporciona una[**filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)recopilación.

### **Dar formato a una fila**

 Cada artículo en el[**filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) colección representa un[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row) objeto. los[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row)objeto ofrece la[**AplicarEstilo**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) método utilizado para establecer el formato de la fila. Para aplicar el mismo formato a una fila, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto. Los pasos a continuación muestran cómo usarlo.

1.  Agrega un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetar a la[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase llamando a su[**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)método.
1.  Selecciona el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)propiedades del objeto para aplicar la configuración de formato.
1.  Active los atributos relevantes para el[**Bandera de estilo**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objeto.
1. Asignar el configurado[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetar a la[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row)objeto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Dar formato a una columna**

 los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección también proporciona una[**columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) recopilación. Cada artículo en el[**columnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) colección representa un[**Columna**](https://reference.aspose.com/cells/net/aspose.cells/column) objeto. Similar a un[**Fila**](https://reference.aspose.com/cells/net/aspose.cells/row) objeto, el[**Columna**](https://reference.aspose.com/cells/net/aspose.cells/column) objeto también ofrece la[**AplicarEstilo**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)método para dar formato a una columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Temas avanzados**
- [Configuración de alineación](/cells/es/net/cells-alignment-settings/)
- [Configuración de borde](/cells/es/net/cells-border-settings/)
- [Establecer formatos condicionales de archivos Excel y ODS.](/cells/es/net/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/net/excel-themes-and-colors/)
- [Ajustes de relleno](/cells/es/net/cells-fill-settings/)
- [Configuración de fuentes](/cells/es/net/cells-font-settings/)
- [Dar formato a la hoja de trabajo Cells en un libro de trabajo](/cells/es/net/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas de 1904](/cells/es/net/implement-1904-date-system/)
- [Fusión y desfusión Cells](/cells/es/net/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/net/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

