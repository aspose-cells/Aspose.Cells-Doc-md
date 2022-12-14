---
title: Ajustes de relleno
type: docs
weight: 50
url: /es/net/cells-fill-settings/
---
## **Colores y patrones de fondo**

Microsoft Excel puede establecer los colores de primer plano (contorno) y de fondo (relleno) de las celdas y los patrones de fondo.

Aspose.Cells también es compatible con estas funciones de forma flexible. En este tema, aprendemos a usar estas funciones usando Aspose.Cells.

### **Configuración de colores y patrones de fondo**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 los[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) tiene el[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) y[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) métodos que se utilizan para obtener y establecer el formato de una celda. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para establecer los colores de primer plano y de fondo de las celdas. Aspose.Cells proporciona un[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumeración que contiene un conjunto de tipos predefinidos de patrones de fondo que se dan a continuación.

|**Patrones de fondo**|**Descripción**|
|:- |:- |
|Sombreado diagonal|Representa un patrón de sombreado diagonal|
|Raya Diagonal|Representa el patrón de rayas diagonales|
|gris6|Representa un 6,25 % de patrón gris|
|gris12|Representa un patrón gris del 12,5 %|
|gris25|Representa un 25 % de patrón gris|
|gris50|Representa un patrón gris del 50 %|
|gris75|Representa un patrón gris del 75 %|
|Franja horizontal|Representa el patrón de rayas horizontales|
|Ninguna|No representa antecedentes|
|Raya diagonal inversa|Representa el patrón de rayas diagonales inversas|
|Sólido|Representa un patrón sólido|
|GruesoDiagonalCrosshatch|Representa un patrón de sombreado diagonal grueso|
|ThinDiagonal Crossshatch|Representa un patrón de sombreado diagonal delgado|
|Raya Diagonal Delgada|Representa un patrón de rayas diagonales delgadas|
|FinoHorizontalSombreado|Representa un patrón de sombreado horizontal delgado|
|DelgadaHorizontalStripe|Representa un patrón de rayas horizontales delgadas|
|DelgadaReverseDiagonalStripe|Representa un patrón de rayas diagonales inversas delgadas|
|DelgadaVerticalStripe|Representa un patrón de rayas verticales delgadas|
|Franja vertical|Representa el patrón de rayas verticales|

En el ejemplo a continuación, el color de primer plano de la celda A1 está configurado pero A2 está configurado para tener colores de primer plano y de fondo con un patrón de fondo de rayas verticales.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Importante saber**

{{% alert color="primary" %}}

-  Para establecer el color frontal o de fondo de una celda, use el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) o[**Color de fondo**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) propiedades. Ambas propiedades tendrán efecto sólo si el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)la propiedad está configurada.
-  los[**Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)La propiedad establece el color de sombra de la celda.
 los[**Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)La propiedad especifica el tipo de patrón de fondo utilizado para el color de primer plano o de fondo. Aspose.Cells proporciona una enumeración,[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)que contiene un conjunto de tipos predefinidos de patrones de fondo.
-  Si selecciona*BackgroundType.Ninguno* valor de la[**Tipo de fondo**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)enumeración, el color de primer plano no se aplica.
 Asimismo, el color de fondo no se aplica si selecciona el*BackgroundType.Ninguno* o*BackgroundType.Solid* valores.
-  Al recuperar el sombreado/color de relleno de la celda, si[**Estilo.Patrón**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) es*BackgroundType.Ninguno*, [**Estilo.Color de primer plano**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) regresará*Color.Vacío*.

{{% /alert %}}

### **Aplicación de efectos de relleno degradado**

 Para aplicar los efectos de relleno de degradado deseados a la celda, use el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objetos[**EstablecerDosColorGradiente**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)método en consecuencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **colores y paleta**

Una paleta es el número de colores disponibles para usar en la creación de una imagen. El uso de una paleta estandarizada en una presentación le permite al usuario crear una apariencia consistente. Cada archivo Microsoft Excel (97-2003) tiene una paleta de 56 colores que se pueden aplicar a celdas, fuentes, líneas de cuadrícula, objetos gráficos, rellenos y líneas en un gráfico.

Con Aspose.Cells es posible no solo usar los colores existentes de la paleta sino también colores personalizados. Antes de usar un color personalizado, agréguelo primero a la paleta.

Este tema trata sobre cómo agregar colores personalizados a la paleta.

### **Adición de colores personalizados a la paleta**

Aspose.Cells es compatible con la paleta de 56 colores de Microsoft de Excel. Para usar un color personalizado que no está definido en la paleta, agregue el color a la paleta.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase proporciona un[**CambiarPaleta**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) método que toma los siguientes parámetros para agregar un color personalizado para modificar la paleta:

- Color personalizado, el color personalizado que se agregará.
- Índice, el índice del color en la paleta que reemplazará el color personalizado. Debe estar entre 0-55.

El siguiente ejemplo agrega un color personalizado (Orquídea) a la paleta antes de aplicarlo en una fuente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

La paleta solo contiene 56 colores. Cuando agrega un color personalizado a la paleta, la paleta cambia y cualquier elemento en el archivo formateado con el color anterior cambia. Entonces, cuando cambie la paleta, tenga mucho cuidado. Además, esta es la limitación en el formato de archivo XLS (Excel 97 - 2003), ya que no existe tal limitación para XLSX u otros formatos de archivo avanzados de MS Excel (2007/2010 o 2013).

{{% /alert %}}
