---
title: Formato de celdas
description: Aprenda a dar formato y estilo a las celdas en Aspose.Cells for .NET, incluido el formato de números, el formato de fechas, los estilos de fuente y otras opciones de estilo de celda. Nuestra guía le ayudará a crear hojas de cálculo atractivas y con aspecto profesional.
keywords: Aspose.Cells for .NET, formato de celda, estilo, formato de números, formato de fechas, estilo de fuente, opciones de estilo de celda, hoja de cálculo, crear, apariencia profesional, formato de filas y columnas.
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/net/cells-formatting/
---

## **Introducción**

{{% alert color="primary" %}}

Aspose.Cells proporciona los métodos [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) de la clase [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell), utilizados para obtener/establecer el estilo de formato de una celda. Aspose.Cells también proporciona una clase [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{% /alert %}}

## **Cómo dar formato a las celdas usando los métodos GetStyle y SetStyle**

Aplica diferentes tipos de estilos de formato en las celdas para establecer colores de fondo o primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

### **Cómo utilizar los métodos GetStyle y SetStyle**

Si los desarrolladores necesitan aplicar diferentes estilos de formato a diferentes celdas, entonces es mejor obtener el [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) de la celda usando el método [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle), especificar los atributos de estilo y luego aplicar el formato usando el método [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle). A continuación se muestra un ejemplo para demostrar este enfoque de aplicar varios formatos a una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Cómo utilizar el objeto Style para dar formato a diferentes celdas**

Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar el objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Siga los pasos a continuación para usar el objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style):

1. Agregue un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) llamando al método [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)
1. Acceda al nuevo objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)
1. Establezca las propiedades/atributos deseados del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) para aplicar la configuración de formato deseada
1. Asigne el objeto configurado [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a las celdas deseadas

Este enfoque puede mejorar significativamente la eficiencia de sus aplicaciones y también ahorrar memoria.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Cómo utilizar los estilos predefinidos de Microsoft Excel 2007**

Si necesita aplicar diferentes estilos de formato para Microsoft Excel 2007, aplique estilos usando la API de Aspose.Cells. A continuación se muestra un ejemplo para demostrar este enfoque de aplicar un estilo predefinido en una celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Cómo formatear caracteres seleccionados en una celda**

La sección sobre la configuración de fuentes explica cómo formatear texto en las celdas, pero solo explica cómo formatear todo el contenido de la celda. ¿Qué sucede si desea formatear solo caracteres seleccionados?

Aspose.Cells también admite esta función. Este tema explica cómo usar esta función de manera efectiva.

### **Cómo formatear caracteres seleccionados**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene la colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) proporciona el método [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- **Índice de inicio**, el índice del carácter desde el que comienza la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

El método [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) devuelve una instancia de la clase [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) que permite a los desarrolladores formatear los caracteres de la misma manera que lo harían con una celda como se muestra a continuación en el ejemplo de código. En el archivo de salida, en la celda A1, la palabra 'Visit' tendrá un formato con la fuente predeterminada, pero 'Aspose!' está en negrita y azul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Si está interesado en formatear una parte de Rich Text en una celda, considere utilizar los métodos [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) y [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). El método [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) se utiliza para acceder a las partes del texto y luego se pueden realizar modificaciones usando el método [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) mientras que el método **Get** devuelve una matriz de objetos [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) que se pueden manipular para establecer diversas propiedades como el nombre de la fuente, el color de la fuente, negrita, etc. y el método **Set** se puede utilizar para aplicar los cambios.

{{% /alert %}}

## **Cómo formatear filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato en celdas una por una a menudo lleva más tiempo y no es una buena solución.
Para abordar este problema, Aspose.Cells proporciona una forma simple y rápida discutida en detalle en este artículo.

### **Formato de filas y columnas**

Aspose.Cells proporciona una clase, el [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceso a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) proporciona una colección [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows).

### **Cómo dar formato a una fila**

Cada elemento en la colección [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) representa un objeto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row). El objeto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) ofrece el método [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) utilizado para establecer el formato de la fila. Para aplicar el mismo formato a una fila, use el objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Los pasos a continuación muestran cómo usarlo.

1. Agregue un objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) llamando a su método [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle).
1. Establezca las propiedades del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) para aplicar la configuración de formato.
1. Active los atributos relevantes para el objeto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).
1. Asigne el objeto configurado [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) a la clase [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Cómo dar formato a una columna**

La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) también proporciona una colección [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns). Cada elemento en la colección [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) representa un objeto [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column). Similar a un objeto [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), el objeto [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) también ofrece el método [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) para dar formato a una columna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Temas avanzados**
- [Configuración de alineación](/cells/es/net/cells-alignment-settings/)
- [Configuración de bordes](/cells/es/net/cells-border-settings/)
- [Establecer formatos condicionales de archivos de Excel y ODS.](/cells/es/net/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/net/excel-themes-and-colors/)
- [Configuración de relleno](/cells/es/net/cells-fill-settings/)
- [Configuración de fuente](/cells/es/net/cells-font-settings/)
- [Dar formato a celdas de hoja de cálculo en un libro de trabajo](/cells/es/net/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas 1904](/cells/es/net/implement-1904-date-system/)
- [Combinar y descombinar celdas](/cells/es/net/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/net/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

