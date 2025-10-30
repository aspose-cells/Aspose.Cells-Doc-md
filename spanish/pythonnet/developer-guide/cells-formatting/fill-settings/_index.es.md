---
title: Configuración de relleno
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo. Soporta configurar los ajustes de relleno de las celdas, permitiendo a los usuarios personalizar el fondo y el estilo de las celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para Python via .NET para establecer los ajustes de relleno de las celdas.
keywords: Aspose.Cells para Python via .NET, Celdas, Configuración de Relleno, Fondo, Estilo
type: docs
weight: 50
url: /es/python-net/cells-fill-settings/
---

## **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y fondo (relleno) de las celdas y los patrones de fondo.

Aspose.Cells para Python via .NET también soporta estas funciones de manera flexible. En este tema, aprendemos a usar estas funciones usando Aspose.Cells.

### **Estableciendo colores y patrones de fondo**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo del archivo Excel. Una hoja de cálculo se representa mediante la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

El [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) tiene los métodos [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) y [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) que se usan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) proporciona propiedades para establecer los colores de primer plano y fondo de las celdas. Aspose.Cells para Python via .NET ofrece una enumeración [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) que contiene un conjunto de patrones de fondo predefinidos, que se muestran a continuación.

|**Patrones de fondo**|**Descripción**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Representa patrón de rayas diagonales cruzadas|
|DIAGONAL_STRIPE|Representa patrón de rayas diagonales|
|GRAY6|Representa patrón de gris del 6.25%|
|GRAY12|Representa patrón de gris del 12.5%|
|GRAY25|Representa patrón de gris del 25%|
|GRAY50|Representa patrón de gris del 50%|
|GRAY75|Representa un patrón de gris al 75%|
|HORIZONTAL_STRIPE|Representa un patrón de rayas horizontales|
|NONE|No representa fondo|
|REVERSE_DIAGONAL_STRIPE|Representa un patrón de rayas diagonales inversas|
|SOLID|Representa un patrón sólido|
|THICK_DIAGONAL_CROSSHATCH|Representa un patrón de tramado en cruz diagonal gruesa|
|THIN_DIAGONAL_CROSSHATCH|Representa un patrón de tramado en cruz diagonal fina|
|THIN_DIAGONAL_STRIPE|Representa un patrón de rayas diagonales finas|
|THIN_HORIZONTAL_CROSSHATCH|Representa un patrón de tramado cruzado horizontal fino|
|THIN_HORIZONTAL_STRIPE|Representa un patrón de rayas horizontales finas|
|THIN_REVERSE_DIAGONAL_STRIPE|Representa un patrón de rayas diagonales inversas finas|
|THIN_VERTICAL_STRIPE|Representa un patrón de rayas verticales finas|
|VERTICAL_STRIPE|Representa un patrón de rayas verticales|

En el ejemplo a continuación, el color de primer plano de la celda A1 está establecido pero A2 está configurada para tener tanto el color de primer plano como el color de fondo con un patrón de fondo de rayas verticales.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Importante saber**

{{% alert color="primary" %}}

- Para establecer el color de primer plano o fondo de una celda, utilice las propiedades [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) o [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Ambas propiedades solo tendrán efecto si la propiedad [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) está configurada.
- La propiedad [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) establece el color de sombreado de la celda.
  La propiedad [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells para Python via .NET proporciona una enumeración, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype). que contiene un conjunto de tipos de patrones de fondo predefinidos.
- Si selecciona el valor *BackgroundType.None* de la enumeración [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), el color de primer plano no se aplicará.
  Del mismo modo, el color de fondo no se aplicará si selecciona los valores *BackgroundType.None* o *BackgroundType.Solid*.
- Al recuperar el color de sombreado de la celda, si [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) es *BackgroundType.None*, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) devolverá *Color.Empty*.

{{% /alert %}}

### **Aplicar efectos de relleno de degradado**

Para aplicar sus efectos deseados de relleno de degradado a la celda, utilice el método [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) del objeto [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) según corresponda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Colores y paleta**

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells para Python via .NET es posible no solo usar los colores existentes de la paleta, sino también colores personalizados. Antes de usar un color personalizado, añádelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Agregar colores personalizados a la paleta**

Aspose.Cells para Python via .NET soporta la paleta de 56 colores de Microsoft Excel. Para usar un color personalizado que no está definido en la paleta, agrega el color a la paleta.

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) proporciona un método [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) que toma los siguientes parámetros para agregar un color personalizado y modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
