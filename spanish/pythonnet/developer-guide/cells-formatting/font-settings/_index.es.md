---
title: Configuración de fuente
description: Aspose.Cells es una biblioteca en Python para trabajar con archivos de hojas de cálculo. Soporta configurar los ajustes de fuente de las celdas, permitiendo a los usuarios personalizar el estilo y las propiedades de las celdas. Este artículo presentará cómo usar la biblioteca Aspose.Cells para Python via .NET para configurar la fuente de las celdas.
keywords: Aspose.Cells para Python via .NET, Celdas, Configuración de Fuente, Estilos, Propiedades
type: docs
weight: 30
url: /es/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

El aspecto y la sensación de un texto se puede controlar modificando la configuración de la fuente. La configuración de la fuente puede incluir el nombre, estilo, tamaño, color y otros efectos de la fuente. Al igual que Microsoft Excel, Aspose.Cells para Python via .NET también soporta configurar la apariencia de la fuente de las celdas.

{{% /alert %}}

## **Configuración de fuente**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Cada elemento en la colección [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells proporciona las clases [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) y los métodos [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) y [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) que se utilizan para obtener y establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) proporciona propiedades para configurar la configuración de fuente.

### **Establecer nombre de fuente**

Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda mediante la propiedad [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Establecer estilo de fuente en negrita**

Los desarrolladores pueden hacer que el texto esté en negrita configurando la propiedad [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) en **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Establecer tamaño de fuente**

Establezca el tamaño de fuente con la propiedad [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Establecer color de fuente**

Utilice la propiedad [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) para establecer el color de fuente. Seleccione cualquier color de la enumeración Color (parte del marco .NET) y asígnele a la propiedad [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Establecer tipo de subrayado de fuente**

Use la propiedad [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) para subrayar el texto. Aspose.Cells para Python via .NET ofrece varios tipos predefinidos de subrayado en la enumeración [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype).

|**Tipos de subrayado de fuente**|**Descripción**|
| :- | :- |
|ACCOUNTING|Un solo subrayado de contabilidad|
|DOUBLE|Subrayado doble|
|DOUBLE_ACCOUNTING|Subrayado de contabilidad doble|
|NONE|Sin subrayado|
|SINGLE|Un solo subrayado|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Establecer efecto tachado**

Aplicar el tachado configurando la propiedad [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) en **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Establecer efecto subíndice**

Aplicar subíndice configurando la propiedad [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) en **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Establecer efecto superíndice en fuente**

Los desarrolladores pueden aplicar el efecto superíndice en la fuente configurando la propiedad [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) del objeto [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) en **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


