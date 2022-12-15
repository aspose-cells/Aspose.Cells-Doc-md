---
title: Configuración de fuentes
type: docs
weight: 30
url: /es/net/cells-font-settings/
---
{{% alert color="primary" %}}

La apariencia de un texto se puede controlar cambiando la configuración de la fuente. La configuración de fuentes puede incluir el nombre, el estilo, el tamaño, el color y otros efectos de las fuentes. Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de la fuente de las celdas.

{{% /alert %}}

## **Configuración de ajustes de fuente**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) recopilación. Cada artículo en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección representa un objeto de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)clase.

 Aspose.Cells proporciona el[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) clase'[**ObtenerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y[**EstablecerEstilo**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) métodos que se utilizan para obtener y establecer el estilo de formato de una celda. los[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)La clase proporciona propiedades para configurar los ajustes de fuente.

### **Configuración del nombre de la fuente**

 Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda usando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[Nombre](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Configuración del estilo de fuente en negrita**

 Los desarrolladores pueden poner el texto en negrita configurando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**es negrita**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Configuración del tamaño de fuente**

Establezca el tamaño de fuente con el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**Tamaño**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Configuración del color de fuente**

Utilizar el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propiedad para establecer el color de la fuente. Seleccione cualquier color de la enumeración Color (parte del marco .NET) y asígnelo al[**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propiedad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Configuración del tipo de subrayado de fuente**

Utilizar el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**Subrayar**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)propiedad para subrayar texto. Aspose.Cells ofrece varios tipos de subrayado de fuente predefinidos en el[**FuenteSubrayadoTipo**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) enumeración.

|**Tipos de subrayado de fuente**|**Descripción**|
|:- |:- |
|Contabilidad|Un solo subrayado contable|
|Doble|Explicación doble|
|ContabilidadDoble|Subrayado de doble contabilidad|
|Ninguna|sin subrayar|
|Único|Un solo subrayado|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Configuración del efecto de tachado**

Aplique el tachado configurando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objetos[**estachado**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Configuración del efecto de subíndice**

Aplicar subíndice configurando el[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objetos[**essubscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Configuración del efecto de superíndice en la fuente**

 Los desarrolladores pueden aplicar el efecto de superíndice en la fuente configurando el[**EsSuperíndice**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) propiedad de la[**Estilo.Fuente**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) oponerse a**verdadero**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

