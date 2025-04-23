---  
title: Configuración de relleno
linktitle: Configuración de relleno  
description: Aprende cómo personalizar la configuración de relleno, fondo y estilo de las celdas usando la biblioteca Aspose.Cells para Node.js a través de C++.  
keywords: Aspose.Cells, Celdas, Configuración de Relleno, Fondo, Estilo, Node.js a través de C++  
type: docs  
weight: 50  
url: /es/nodejs-cpp/cells-fill-settings/  
---  

## **Colores y patrones de fondo**  

Microsoft Excel puede establecer los colores de primer plano (contorno) y fondo (relleno) de las celdas y los patrones de fondo.  

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a usar estas características utilizando Aspose.Cells.  

### **Estableciendo colores y patrones de fondo**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

La clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) tiene los métodos [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) y [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) que se usan para obtener y establecer el formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) proporciona propiedades para configurar los colores de primer plano y fondo de las celdas. Aspose.Cells ofrece una enumeración [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) que contiene un conjunto de tipos predefinidos de patrones de fondo, que se detallan a continuación.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Importante saber**  

{{% alert color="primary" %}}  

- Para establecer el color de primer plano o fondo de una celda, usa el método [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) del objeto [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) o [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-). Ambos métodos solo surtirán efecto si la propiedad [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) está configurada.  
- El método [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) establece el color de sombra de la celda.  
  El método [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) especifica el tipo de patrón de fondo utilizado para el color de primer plano o fondo. Aspose.Cells proporciona una enumeración, [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype). que contiene un conjunto de tipos predefinidos de patrones de fondo.  
- Si seleccionas el valor *BackgroundType.None* de la enumeración [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), el color de primer plano no se aplicará.  
  Del mismo modo, el color de fondo no se aplicará si selecciona los valores *BackgroundType.None* o *BackgroundType.Solid*.  
- Al recuperar el color de sombreado de la celda, si [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) es *BackgroundType.None*, [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) devolverá *Color.Empty*.  

{{% /alert %}}  

### **Aplicar efectos de relleno de degradado**  

Para aplicar tus efectos de relleno de gradiente deseados a la celda, utiliza el método [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) del objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) según corresponda.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Colores y paleta**  

Una paleta es el número de colores disponibles para utilizar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear un aspecto consistente. Cada archivo de Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.  

Con Aspose.Cells es posible no solo utilizar los colores existentes de la paleta, sino también colores personalizados. Antes de utilizar un color personalizado, agréguelo primero a la paleta.  

Este tema trata sobre cómo agregar colores personalizados a la paleta.  

### **Agregar colores personalizados a la paleta**  

Aspose.Cells soporta la paleta de colores de Microsoft Excel con 56 colores. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) proporciona un método [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) que recibe los siguientes parámetros para agregar un color personalizado y modificar la paleta:  

- Color personalizado, el color personalizado que se agregará.  
- Índice, el índice del color en la paleta que el color personalizado reemplazará. Debe estar entre 0-55.  

El siguiente ejemplo agrega un color personalizado (Orchid) a la paleta antes de aplicarlo a una fuente.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Por lo tanto, tenga mucho cuidado al cambiar la paleta. Además, esta es una limitación solo en el formato de archivo XLS (Excel 97 - 2003) ya que no hay tal limitación para formatos de archivo XLSX o más avanzados de MS Excel (2007/2010 o 2013).  

{{% /alert %}}  

