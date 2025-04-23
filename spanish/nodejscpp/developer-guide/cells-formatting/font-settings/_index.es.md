---  
title: Configuración de fuente con Node.js a través de C++  
linktitle: Configuración de fuente  
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hojas de cálculo. Soporta establecer la configuración de fuente de las celdas, permitiendo a los usuarios personalizar el estilo y las propiedades de la fuente. Este artículo presentará cómo usar la biblioteca Aspose.Cells para establecer la configuración de fuente de las celdas.  
keywords: Aspose.Cells, Celdas, Configuración de Fuente, Estilos, Propiedades, Node.js a través de C++  
type: docs  
weight: 30  
url: /es/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
La apariencia de un texto puede ser controlada cambiando la configuración de fuente. La configuración de fuente puede incluir el nombre, estilo, tamaño, color y otros efectos de las fuentes. Al igual que Microsoft Excel, Aspose.Cells también admite la configuración de fuente de las celdas.  
{{% /alert %}}  

## **Configuración de fuente**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Cada elemento en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) representa un objeto de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells proporciona los métodos [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) y [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) de la clase [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) que se usan para obtener y establecer el estilo de formato de una celda. La clase [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) proporciona propiedades para configurar la fuente.  

### **Establecer nombre de fuente**  

Los desarrolladores pueden aplicar cualquier fuente al texto dentro de una celda usando el método [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) del objeto.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **Establecer estilo de fuente en negrita**  

Los desarrolladores pueden hacer que el texto esté en negrita configurando el método [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) en **true**.   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **Establecer tamaño de fuente**  

Establece el tamaño de fuente con el método [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **Establecer color de fuente**  

Utilice el método [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) para establecer el color de la fuente. Seleccione cualquier color del enumerador Color (parte de Node.js) y asígnele al método [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **Establecer tipo de subrayado de fuente**  

Utilice el método [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) para subrayar el texto. Aspose.Cells ofrece varios tipos predefinidos de subrayado de fuente en la enumeración [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype).  

|**Tipos de subrayado de fuente**|**Descripción**|  
| :- | :- |  
|Accounting|Un solo subrayado contable|  
|Double|Doble subrayado|  
|DoubleAccounting|Doble subrayado|  
|None|Sin subrayado|  
|Single|Un solo subrayado|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **Establecer efecto tachado**  

Aplicar tachado configurando el método [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) a **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **Establecer efecto subíndice**  

Aplicar subíndice configurando el método [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) a **true**.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **Establecer efecto superíndice en fuente**  

Los desarrolladores pueden aplicar el efecto superíndice en la fuente configurando el método [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) del objeto [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) a **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **Temas avanzados**  
- [Aplicar efectos de superíndice y subíndice en fuentes](/cells/es/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo](/cells/es/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


