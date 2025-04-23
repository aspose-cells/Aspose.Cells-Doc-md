---
title: Formato de celdas
description: Aprende cómo formatear y estilizar celdas en Aspose.Cells para Python via .NET, incluyendo formato numérico, formato de fecha, estilos de fuente y otras opciones de estilo de celda. Nuestra guía te ayudará a crear hojas de cálculo atractivas y con aspecto profesional.
keywords: Aspose.Cells para Python via .NET, formateo de celdas, estilos, formato numérico, formato de fecha, estilo de fuente, opciones de estilo de celda, hoja de cálculo, crear, aspecto profesional, formatear filas y columnas.
linktitle: Formato de celdas
type: docs
weight: 120
url: /es/python-net/cells-formatting/
---

## **Introducción**

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET proporciona los métodos [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) y [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) de la clase [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell), utilizados para obtener y establecer el estilo de formateo de una celda. Aspose.Cells para Python via .NET también ofrece una clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{% /alert %}}

## **Cómo dar formato a las celdas usando los métodos GetStyle y SetStyle**

Aplica diferentes tipos de estilos de formato en las celdas para establecer colores de fondo o primer plano, bordes, fuentes, alineaciones horizontales y verticales, nivel de sangría, dirección del texto, ángulo de rotación y mucho más.

### **Cómo utilizar los métodos GetStyle y SetStyle**

Si los desarrolladores necesitan aplicar diferentes estilos de formato a diferentes celdas, entonces es mejor obtener el [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) de la celda usando el método [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style), especificar los atributos de estilo y luego aplicar el formato usando el método [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style). A continuación se muestra un ejemplo para demostrar este enfoque de aplicar varios formatos a una celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Cómo utilizar el objeto Style para dar formato a diferentes celdas**

Si los desarrolladores necesitan aplicar el mismo estilo de formato a diferentes celdas, pueden usar el objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Siga los pasos a continuación para usar el objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style):

1. Agregue un objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) llamando al método [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)
1. Acceda al nuevo objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)
1. Establezca las propiedades/atributos deseados del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para aplicar la configuración de formato deseada
1. Asigne el objeto configurado [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) a las celdas deseadas

Este enfoque puede mejorar significativamente la eficiencia de sus aplicaciones y también ahorrar memoria.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Cómo utilizar los estilos predefinidos de Microsoft Excel 2007**

Si necesitas aplicar estilos de formateo diferentes para Microsoft Excel 2007, aplica estilos usando la API de Aspose.Cells para Python via .NET. A continuación se muestra un ejemplo para demostrar este enfoque al aplicar un estilo predefinido en una celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Cómo formatear caracteres seleccionados en una celda**

La sección sobre la configuración de fuentes explica cómo formatear texto en las celdas, pero solo explica cómo formatear todo el contenido de la celda. ¿Qué sucede si desea formatear solo caracteres seleccionados?

Aspose.Cells para Python via .NET también soporta esta característica. Este tema explica cómo usar esta característica de manera efectiva.

### **Cómo formatear caracteres seleccionados**

Aspose.Cells para Python via .NET proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene la colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja en un archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) proporciona el método [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) que toma los siguientes parámetros para seleccionar un rango de caracteres dentro de una celda:

- **Índice de inicio**, el índice del carácter desde el que comienza la selección.
- **Número de caracteres**, el número de caracteres a seleccionar.

El método [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) devuelve una instancia de la clase [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) que permite a los desarrolladores formatear los caracteres de la misma manera que lo harían con una celda como se muestra a continuación en el ejemplo de código. En el archivo de salida, en la celda A1, la palabra 'Visit' tendrá un formato con la fuente predeterminada, pero 'Aspose!' está en negrita y azul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Si estás interesado en formatear una porción de texto enriquecido en una celda, considera usar los métodos [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) y [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). El método [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) se usa para acceder a las porciones del texto y luego realizar cambios usando el método [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters), mientras que el método **Get** devuelve un arreglo de objetos [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) que pueden manipularse para establecer varias propiedades como nombre de fuente, color de fuente, negrita, etc., y el método **Set** puede usarse para aplicar los cambios.

{{% /alert %}}

## **Cómo formatear filas y columnas**

A veces, los desarrolladores necesitan aplicar el mismo formato en filas o columnas. Aplicar formato en celdas una por una a menudo lleva más tiempo y no es una buena solución.
Para abordar este tema, Aspose.Cells para Python via .NET ofrece una forma sencilla y rápida, detallada en este artículo.

### **Formato de filas y columnas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja en el archivo de Excel. Una hoja se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) proporciona una colección [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows).

### **Cómo dar formato a una fila**

Cada elemento en la colección [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) representa un objeto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row). El objeto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) ofrece el método [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) utilizado para establecer el formato de la fila. Para aplicar el mismo formato a una fila, use el objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Los pasos a continuación muestran cómo usarlo.

1. Agregue un objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) a la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) llamando a su método [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style).
1. Establezca las propiedades del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) para aplicar la configuración de formato.
1. Active los atributos relevantes para el objeto [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).
1. Asigne el objeto configurado [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) a la clase [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Cómo dar formato a una columna**

La colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) también proporciona una colección [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns). Cada elemento en la colección [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) representa un objeto [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column). Similar a un objeto [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), el objeto [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) también ofrece el método [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) para dar formato a una columna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Temas avanzados**
- [Configuración de alineación](/cells/es/python-net/cells-alignment-settings/)
- [Configuración de bordes](/cells/es/python-net/cells-border-settings/)
- [Establecer formatos condicionales de archivos de Excel y ODS.](/cells/es/python-net/conditional-formatting/)
- [Temas y colores de Excel](/cells/es/python-net/excel-themes-and-colors/)
- [Configuración de relleno](/cells/es/python-net/cells-fill-settings/)
- [Configuración de fuente](/cells/es/python-net/cells-font-settings/)
- [Dar formato a celdas de hoja de cálculo en un libro de trabajo](/cells/es/python-net/format-worksheet-cells-in-a-workbook/)
- [Implementar el sistema de fechas 1904](/cells/es/python-net/implement-1904-date-system/)
- [Combinar y descombinar celdas](/cells/es/python-net/merging-and-unmerging-cells/)
- [Configuración de números](/cells/es/python-net/cells-number-settings/)
- [Obtener y establecer estilo para celdas](/cells/es/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

