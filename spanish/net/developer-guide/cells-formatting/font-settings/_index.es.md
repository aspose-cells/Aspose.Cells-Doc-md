---
title: Configuración de fuente
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la configuración de fuentes de las celdas, lo que permite a los usuarios personalizar el estilo de fuente y las propiedades de las celdas. Este artículo presentará cómo utilizar la biblioteca Aspose.Cells para configurar la configuración de fuente de celda.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /es/net/cells-font-settings/
---
{{% alert color="primary" %}}

La apariencia de un texto se puede controlar cambiando la configuración de fuente. La configuración de fuente puede incluir el nombre, estilo, tamaño, color y otros efectos de las fuentes. Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de fuentes de las celdas.

{{% /alert %}}

##  **Configurar los ajustes de fuente**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada elemento en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase'[**Obtener estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**Establecer estilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos que se utilizan para obtener y establecer el estilo de formato de una celda. El[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para configurar los ajustes de fuente.

###  **Configuración del nombre de la fuente**

 Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda usando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[Nombre](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Establecer el estilo de fuente en negrita**

 Los desarrolladores pueden poner el texto en negrita configurando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**es negrita**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)propiedad a *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Configuración del tamaño de fuente**

Establezca el tamaño de fuente con el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**Tamaño**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Configuración del color de fuente**

Utilizar el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propiedad para establecer el color de fuente. Seleccione cualquier color de la enumeración de colores (parte del marco .NET) y asígnelo al[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Configuración del tipo de subrayado de fuente**

Utilizar el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**Subrayar**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)propiedad para subrayar texto. Aspose.Cells ofrece varios tipos de subrayado de fuente predefinidos en el[**Tipo de fuente subrayado**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) enumeración.

|**Tipos de subrayado de fuente**|**Descripción**|
| :- | :- |
|Contabilidad|Un único subrayado contable|
|Doble|Explicación doble|
|Doble Contabilidad|Subrayado contable doble|
|Ninguno|Sin subrayado|
|Soltero|Un solo subrayado|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Configuración del efecto de tachado**

Aplicar tachado estableciendo el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**Es tachado**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)propiedad a *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Configuración del efecto de subíndice**

Aplicar subíndice configurando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**EsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)propiedad a *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Configurar el efecto de superíndice en la fuente**

 Los desarrolladores pueden aplicar el efecto de superíndice en la fuente configurando el[**EsSuperíndice**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) propiedad de la[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objeto de *verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

