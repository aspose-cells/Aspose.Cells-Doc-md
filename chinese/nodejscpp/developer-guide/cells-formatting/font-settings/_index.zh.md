---  
title: Node.js 使用 C++ 进行字体设置  
linktitle: 字体设置  
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库。它支持设置单元格的字体设置，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用 Aspose.Cells 库设置单元格字体设置。  
keywords: Aspose.Cells，单元格，字体设置，样式，属性，Node.js 通过 C++  
type: docs  
weight: 30  
url: /zh/nodejs-cpp/cells-font-settings/  
---  

{{% alert color="primary" %}}  
通过更改字体设置可以控制文本的外观。字体设置可能包括字体的名称、样式、大小、颜色和其他效果。就像 Microsoft Excel 一样，Aspose.Cells 也支持配置单元格的字体设置。  
{{% /alert %}}  

## **配置字体设置**  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，可访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) 集合。每个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合中的项代表一个 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的对象。  

Aspose.Cells 提供 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的 [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) 和 [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) 方法，用于获取和设置单元格的格式样式。 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 类提供用于配置字体设置的属性。  

### **设置字体名称**  

开发人员可以通过使用 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [setName](https://reference.aspose.com/cells/nodejs-cpp/font/#setName-string-) 方法将任意字体应用于单元格内的文本。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontName.js" >}}


### **将字体样式设置为粗体**  

开发人员可以通过将 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setIsBold**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsBold-boolean-) 方法设置为 **true** 来将文本加粗。   

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetBoldStyle.js" >}}



### **设置字体大小**  

使用 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setSize**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSize-number-) 方法设置字体大小。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontSize.js" >}}


### **设置字体颜色**  

使用 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) 方法设置字体颜色。从颜色枚举（Node.js 部分）中选择任意颜色并赋值给 [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setColor-color-) 方法。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontColor.js" >}}


### **设置字体下划线类型**  

使用 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setUnderline**](https://reference.aspose.com/cells/nodejs-cpp/font/#setUnderline-fontunderlinetype-) 方法下划线文本。Aspose.Cells 提供各种预定义的字体下划线类型（在 [**FontUnderlineType**](https://reference.aspose.com/cells/nodejs-cpp/fontunderlinetype) 枚举中）。  

|**字体下划线类型**|**描述**|  
| :- | :- |  
|Accounting| 单下划线|  
|Double| 双下划线|  
|DoubleAccounting| 双帐目下划线|  
|None| 无下划线|  
|Single| 单下划线|  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontUnderline.js" >}}


### **设置删除线效果**  

通过将 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setIsStrikeout**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsStrikeout-boolean-) 方法设置为 **true** 来应用删除线。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}


### **设置下标效果**  

通过将 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setIsSubscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSubscript-boolean-) 方法设置为 **true** 来应用下标。  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetFontStrikeout.js" >}}



### **在字体上设置上标效果**  

开发人员可以通过将 [**Font**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) 对象的 [**setIsSuperscript**](https://reference.aspose.com/cells/nodejs-cpp/font/#setIsSuperscript-boolean-) 方法设置为 **true** 来在字体上应用上标效果。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-SetSuperscript.js" >}}


## **高级主题**  
- [在字体上应用上标和下标效果](/cells/zh/nodejs-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
