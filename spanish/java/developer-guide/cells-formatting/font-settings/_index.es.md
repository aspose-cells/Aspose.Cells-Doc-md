---
title: Tratar con la configuración de fuentes
linktitle: Configuración de fuentes
type: docs
weight: 20
url: /es/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

La apariencia del texto se puede controlar cambiando la configuración de la fuente. Estos ajustes de fuente pueden incluir el nombre, el estilo, el tamaño, el color y otros efectos de las fuentes, como se muestra a continuación en la figura:

**Configuración de fuente en Microsoft Excel** 

![todo:imagen_alternativa_texto](dealing-with-font-settings_1.png)

Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de la fuente de las celdas.

{{% /alert %}} 
## **Configuración de ajustes de fuente**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) que representa un archivo de Excel Microsoft. Él[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase. Él[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. Cada artículo en el[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección representa un objeto de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)clase.

 Aspose.Cells proporciona el[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) clase'[establecerEstilo](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ), utilizado para establecer el formato de una celda. Asimismo, el objeto de la[Estilo](https://reference.aspose.com/cells/java/com.aspose.cells/Style)La clase proporciona propiedades para configurar los ajustes de fuente.

Este artículo muestra cómo:

- [Aplicar una fuente específica al texto.](/cells/es/java/dealing-with-font-settings/)
- [Establecer texto en negrita](/cells/es/java/dealing-with-font-settings/).
- [Establecer el tamaño de fuente](/cells/es/java/dealing-with-font-settings/).
- [Establecer el color de la fuente](/cells/es/java/dealing-with-font-settings/).
- [Subrayar texto](/cells/es/java/dealing-with-font-settings/).
- [texto tachado](/cells/es/java/dealing-with-font-settings/).
- [Establecer texto en subíndice](/cells/es/java/dealing-with-font-settings/).
- [Establecer texto en superíndice](/cells/es/java/dealing-with-font-settings/).
### **Configuración del nombre de la fuente**
 Aplique una fuente específica al texto en las celdas usando el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[escoger un nombre](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Configuración del estilo de fuente en negrita**
 Establezca el texto en negrita configurando el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[poner en negrita](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) propiedad a**verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Configuración del tamaño de fuente**
 Establezca el tamaño de la fuente con el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[establecerTamaño](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Configuración del tipo de subrayado de fuente**
 Subraya el texto con el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[establecerSubrayado](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) propiedad. Aspose.Cells ofrece varios tipos de subrayado de fuente predefinidos en el[FuenteSubrayadoTipo](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)enumeración.

|**Tipos de subrayado de fuente**|**Descripción**|
|:- |:- |
|[NINGUNO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|sin subrayar|
|[ÚNICO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Un solo subrayado|
|[DOBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Explicación doble|
|[CONTABILIDAD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Un solo subrayado contable|
|[DOBLE_CONTABILIDAD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Subrayado de doble contabilidad|
|[ESTRELLARSE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Subrayado discontinuo|
|[ESTRELLARSE_PUNTO_PUNTO_PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Subrayado grueso de puntos y guiones|
|[ESTRELLARSE_PUNTO_PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Subrayado de puntos y guiones gruesos|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Subrayado discontinuo grueso|
|[DASH_LARGO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Subrayado discontinuo largo|
|[ESTRELLARSE_LARGO_PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Subrayado grueso de trazos largos|
|[PUNTO GUIÓN](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Subrayado de puntos y guiones|
|[PUNTO_PUNTO_ESTRELLARSE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Guión-Punto-Punto Subrayado|
|[PUNTEADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Subrayado punteado|
|[DOTTED_PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Subrayado punteado grueso|
|[PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Subrayado grueso|
|[ONDA](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Subrayado de onda|
|[ONDULADO_DOBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Subrayado de doble onda|
|[ONDULADO_PESADO](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Subrayado de onda pesada|
|` `[PALABRAS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Subrayar solo caracteres que no sean espacios|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Configuración del color de fuente**
 Establezca el color de la fuente con el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[establecerColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) propiedad. Seleccione cualquier color de la[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) enumeración y asignar el color seleccionado a la[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[establecerColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Configuración del efecto de tachado en el texto**
 Texto tachado con el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[tachar](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Subíndice de configuración**
 Haga superíndice de texto usando el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[establecerSubíndice](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Configuración de superíndice**
 Aplicar superíndice al texto con el[Fuente](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objetos[conjuntoSuperíndice](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Temas avanzados**
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
