---
title: Configuración de relleno
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite el establecimiento de la configuración de relleno de las celdas, lo que permite a los usuarios personalizar el fondo y el estilo de las celdas. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para establecer la configuración de relleno de las celdas.
keywords: Aspose.Cells, Celdas, Configuración de relleno, Fondo, Estilo
type: docs
weight: 50
url: /es/net/cells-fill-settings/
---

## **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y fondo (relleno) de las celdas y los patrones de fondo.

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a usar estas características utilizando Aspose.Cells.

### **Estableciendo colores y patrones de fondo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) tiene los métodos [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) y [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) que se utilizan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) proporciona propiedades para establecer los colores de primer plano y fondo de las celdas. Aspose.Cells proporciona una enumeración [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) que contiene un conjunto de tipos predefinidos de patrones de fondo que se indican a continuación.

|**Patrones de fondo**|**Descripción**|
| :- | :- |
|DiagonalCrosshatch|Representa un patrón de entrecruzado diagonal|
|DiagonalStripe|Representa un patrón de rayas diagonales|
|Gray6|Representa un patrón gris del 6.25%|
|Gray12|Representa un patrón gris del 12.5%|
|Gray25|Representa un patrón gris del 25%|
|Gray50|Representa un patrón gris del 50%|
|Gray75|Representa un patrón gris del 75%|
|HorizontalStripe|Representa un patrón de rayas horizontales|
|None|Representa ningún fondo|
|ReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas|
|Solid|Representa un patrón sólido|
|ThickDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal grueso|
|ThinDiagonalCrosshatch|Representa un patrón de entrecruzado diagonal delgado|
|ThinDiagonalStripe|Representa un patrón de rayas diagonales delgado|
|ThinHorizontalCrosshatch|Representa un patrón de entrecruzado horizontal delgado|
|ThinHorizontalStripe|Representa un patrón de rayas horizontales delgado|
|ThinReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas delgado|
|ThinVerticalStripe|Representa un patrón de rayas verticales delgado|
|VerticalStripe|Representa un patrón de rayas verticales|

En el ejemplo a continuación, el color de primer plano de la celda A1 está establecido pero A2 está configurada para tener tanto el color de primer plano como el color de fondo con un patrón de fondo de rayas verticales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Importante saber**

{{% alert color="primary" %}}

- Para establecer el color de primer plano o fondo de una celda, utilice las propiedades [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) o [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Ambas propiedades solo tendrán efecto si la propiedad [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) está configurada.
- La propiedad [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) establece el color de sombreado de la celda.
  La propiedad [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells proporciona una enumeración, [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), que contiene un conjunto de tipos predefinidos de patrones de fondo.
- Si selecciona el valor *BackgroundType.None* de la enumeración [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), el color de primer plano no se aplicará.
  Del mismo modo, el color de fondo no se aplicará si selecciona los valores *BackgroundType.None* o *BackgroundType.Solid*.
- Al recuperar el color de sombreado de la celda, si [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) es *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) devolverá *Color.Empty*.

{{% /alert %}}

### **Aplicar efectos de relleno de degradado**

Para aplicar sus efectos deseados de relleno de degradado a la celda, utilice el método [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) del objeto [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) según corresponda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Colores y paleta**

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells es posible no solo utilizar los colores existentes de la paleta, sino también colores personalizados. Antes de utilizar un color personalizado, agréguelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Agregar colores personalizados a la paleta**

Aspose.Cells soporta la paleta de colores de Microsoft Excel con 56 colores. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) proporciona un método [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) que toma los siguientes parámetros para agregar un color personalizado y modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}
