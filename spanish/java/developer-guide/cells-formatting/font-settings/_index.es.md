---
title: Tratando con Configuraciones de Fuente
linktitle: Configuración de fuente
type: docs
weight: 20
url: /es/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

La apariencia del texto se puede controlar cambiando su configuración de fuente. Estas configuraciones de fuente pueden incluir el nombre, estilo, tamaño, color y otros efectos de las fuentes como se muestra a continuación en la figura:

**Configuración de fuente en Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de la fuente de las celdas.

{{% /alert %}} 
## **Configuración de fuente**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Cada elemento en la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) representa un objeto de la clase [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells proporciona el método [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) de la clase, usado para establecer el formato de una celda. Además, el objeto de la clase [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) proporciona propiedades para configurar la fuente.

Este artículo muestra cómo:

- [Aplicar una fuente específica al texto.](/cells/es/java/dealing-with-font-settings/)
- [Establecer texto en negrita](/cells/es/java/dealing-with-font-settings/).
- [Establecer el tamaño de fuente](/cells/es/java/dealing-with-font-settings/).
- [Establecer el color de la fuente](/cells/es/java/dealing-with-font-settings/).
- [Subrayar texto](/cells/es/java/dealing-with-font-settings/).
- [Tachar texto](/cells/es/java/dealing-with-font-settings/).
- [Establecer texto en subíndice](/cells/es/java/dealing-with-font-settings/).
- [Establecer texto en superíndice](/cells/es/java/dealing-with-font-settings/).
### **Establecer nombre de fuente**
Aplicar una fuente específica al texto en las celdas utilizando la propiedad [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Establecer estilo de fuente en negrita**
Establezca el texto en negrita estableciendo la propiedad [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) en **verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Establecer tamaño de fuente**
Establezca el tamaño de fuente utilizando la propiedad [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Establecer tipo de subrayado de fuente**
Subraye el texto con la propiedad [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font). Aspose.Cells ofrece varios tipos predefinidos de subrayado de fuente en la enumeración [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType).

|**Tipos de subrayado de fuente**|**Descripción**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Sin subrayado|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Un solo subrayado|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Doble subrayado|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Subrayado contable sencillo|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|Subrayado doble contable|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Subrayado punteado|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|Subrayado Dash-Dot-Dot grueso|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|Subrayado Dash-Dot grueso|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|Subrayado grueso a rayas|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|Subrayado largo a rayas|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|Subrayado largo a rayas grueso|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|Subrayado punto-guion|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|Subrayado punto-punto-guion|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Subrayado de guionado|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|Subrayado punteado grueso|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Subrayado grueso|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Subrayado ondulado|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|Subrayado doble ondulado|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|Subrayado ondulado grueso|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Subrayar solo caracteres no espaciales|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Establecer color de fuente**
Establecer el color de fuente con la propiedad [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font). Selecciona cualquier color de la enumeración [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) y asígnalo al color seleccionado al objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) usando la propiedad [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Aplicar efecto tachado al texto**
Tachar texto con la propiedad [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Ajustar subíndice**
Hacer el texto en subíndice usando la propiedad [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Ajustar superíndice**
Aplicar superíndice al texto con la propiedad [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) del objeto [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="java" >}}
