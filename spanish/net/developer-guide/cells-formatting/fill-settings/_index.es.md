---
title: Configuración de relleno
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la configuración de relleno de celdas, lo que permite a los usuarios personalizar el fondo y el estilo de las celdas. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para establecer la configuración de relleno de celdas.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /es/net/cells-fill-settings/
---
##  **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y de fondo (relleno) de celdas y patrones de fondo.

Aspose.Cells también admite estas características de manera flexible. En este tema, aprenderemos a utilizar estas funciones usando Aspose.Cells.

###  **Configuración de colores y patrones de fondo**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 El[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) tiene el[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) y[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) Métodos que se utilizan para obtener y configurar el formato de una celda. El[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para configurar los colores de primer plano y de fondo de las celdas. Aspose.Cells proporciona un[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumeración que contiene un conjunto de tipos predefinidos de patrones de fondo que se detallan a continuación.

|**Patrones de fondo**|**Descripción**|
| :- | :- |
|Diagonal Rayado|Representa un patrón de rayado diagonal.|
|raya diagonal|Representa un patrón de rayas diagonales.|
|gris6|Representa un 6,25% de patrón gris.|
|gris12|Representa un 12,5 % de patrón gris.|
|gris25|Representa un 25 % de patrón gris.|
|Gris50|Representa un 50 % de patrón gris.|
|gris75|Representa un 75 % de patrón gris.|
|Raya Horizontal|Representa un patrón de rayas horizontales.|
|Ninguno|No representa antecedentes|
|Raya Diagonal Inversa|Representa un patrón de rayas diagonales inversas.|
|Sólido|Representa un patrón sólido|
|GruesoDiagonal Rayado|Representa un patrón de rayado diagonal grueso.|
|Rayado diagonal delgado|Representa un patrón de rayado diagonal delgado.|
|raya diagonal delgada|Representa un patrón de rayas diagonales delgadas.|
|DelgadaHorizontal Rayado|Representa un patrón de rayado horizontal delgado|
|DelgadaRayaHorizontal|Representa un patrón de rayas horizontales delgadas.|
|DelgadaInversaDiagonalRaya|Representa un patrón de rayas diagonales inversas delgadas.|
|Raya vertical delgada|Representa un patrón de rayas verticales delgadas.|
|raya vertical|Representa un patrón de rayas verticales.|

En el siguiente ejemplo, el color de primer plano de la celda A1 está configurado, pero A2 está configurado para tener colores de primer plano y de fondo con un patrón de fondo de rayas verticales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Importante saber**

{{% alert color="primary" %}}

-  Para establecer el color de primer plano o de fondo de una celda, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) o[**Color de fondo**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) propiedades. Ambas propiedades tendrán efecto sólo si el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La propiedad está configurada.
-  El[**Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La propiedad establece el color de sombra de la celda.
 El[**Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La propiedad especifica el tipo de patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona una enumeración,[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). que contiene un conjunto de tipos predefinidos de patrones de fondo.
-  Si seleccionas*Tipo de fondo.Ninguno* valor de la[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumeración, el color de primer plano no se aplica.
 Del mismo modo, el color de fondo no se aplica si selecciona la opción*Tipo de fondo.Ninguno* o*Tipo de fondo. Sólido* valores.
-  Al recuperar el color de sombreado/relleno de la celda, si[**Estilo.Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) es *BackgroundType.Ninguno*,[**Estilo.Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) devolverá *Color.Vacío*.

{{% /alert %}}

###  **Aplicar efectos de relleno degradado**

 Para aplicar los efectos de relleno de degradado que desee a la celda, utilice el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**ConjuntoDegradadoDeDosColores**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)método en consecuencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Colores y paleta**

Una paleta es la cantidad de colores disponibles para usar en la creación de una imagen. El uso de una paleta estandarizada en una presentación permite al usuario crear una apariencia consistente. Cada archivo Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas de un gráfico.

Con Aspose.Cells es posible no sólo utilizar los colores existentes de la paleta sino también colores personalizados. Antes de usar un color personalizado, agréguelo primero a la paleta.

En este tema se analiza cómo agregar colores personalizados a la paleta.

###  **Agregar colores personalizados a la paleta**

Aspose.Cells admite la paleta de 56 colores de Microsoft Excel. Para utilizar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase proporciona un[**Cambiar paleta**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Método que toma los siguientes parámetros para agregar un color personalizado para modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que reemplazará el color personalizado. Debe estar entre 0 y 55.

El siguiente ejemplo agrega un color personalizado (Orquídea) a la paleta antes de aplicarlo a una fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La paleta sólo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento del archivo formateado con el color anterior cambia. Entonces, cuando cambies la paleta, ten mucho cuidado. Además, esta es la limitación solo en el formato de archivo XLS (Excel 97 - 2003), ya que no existe tal limitación para XLSX u otros formatos de archivo avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}
