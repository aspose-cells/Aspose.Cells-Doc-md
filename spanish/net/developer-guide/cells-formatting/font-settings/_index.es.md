---
title: Configuración de fuente
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la configuración de fuente de las celdas, lo que permite a los usuarios personalizar el estilo y propiedades de la fuente de las celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para configurar la fuente de celdas.
keywords: Aspose.Cells, Celdas, Configuración de fuente, Estilos, Propiedades
type: docs
weight: 30
url: /es/net/cells-font-settings/
---

{{% alert color="primary" %}}

La apariencia de un texto puede ser controlada cambiando la configuración de fuente. La configuración de fuente puede incluir el nombre, estilo, tamaño, color y otros efectos de las fuentes. Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de fuente de las celdas.

{{% /alert %}}

## **Configuración de fuente**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells proporciona las clases [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) y los métodos [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) y [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) que se utilizan para obtener y establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) proporciona propiedades para configurar la configuración de fuente.

### **Establecer nombre de fuente**

Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda utilizando la propiedad [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Establecer estilo de fuente en negrita**

Los desarrolladores pueden hacer que el texto esté en negrita configurando la propiedad [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) en **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Establecer tamaño de fuente**

Establezca el tamaño de fuente con la propiedad [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Establecer color de fuente**

Utilice la propiedad [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) para establecer el color de fuente. Seleccione cualquier color de la enumeración Color (parte del marco .NET) y asígnele a la propiedad [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Establecer tipo de subrayado de fuente**

Utilice la propiedad [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) para subrayar texto. Aspose.Cells ofrece varios tipos de subrayado de fuente predefinidos en la enumeración [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype).

|**Tipos de subrayado de fuente**|**Descripción**|
| :- | :- |
|Accounting|Un solo subrayado contable|
|Double|Doble subrayado|
|DoubleAccounting|Doble subrayado|
|None|Sin subrayado|
|Single|Un solo subrayado|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Establecer efecto tachado**

Aplicar el tachado configurando la propiedad [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) en **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Establecer efecto subíndice**

Aplicar subíndice configurando la propiedad [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) en **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Establecer efecto superíndice en fuente**

Los desarrolladores pueden aplicar el efecto superíndice en la fuente configurando la propiedad [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) del objeto [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) en **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
