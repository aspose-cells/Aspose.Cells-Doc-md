---  
title: 数字设置
linktitle: 数字设置  
description: Aspose.Cells是一个支持多种单元格数字设置的Node.js库。本文介绍如何使用Aspose.Cells库管理单元格的数字设置，以调整电子表格中的数字格式。  
keywords: Aspose.Cells、Node.js库、电子表格、单元格数字设置、格式、管理、数字与日期格式  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/cells-number-settings/  
---  

## **如何设置数字和日期的显示格式**  

微软Excel的一个非常强大的功能是允许用户设置数字值和日期的显示格式。我们知道数字数据可以代表不同的值，包括十进制、货币、百分比、小数或会计值等。这些数值的显示格式根据所表示的信息类型而不同。同样，日期或时间也可以以多种格式显示。  
Aspose.Cells支持此功能，并允许开发人员为数字或日期设置任何显示格式。  

### **如何在Microsoft Excel中设置显示格式**  

在Microsoft Excel中设置显示格式：  

1. 右键单击任何单元格。  
2. 选择**单元格格式**。将弹出一个对话框，用于设置任何值的显示格式。  

对话框左侧有许多类别，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells支持所有这些显示格式。  

Aspose.Cells提供了一个模块，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)模块包含一个[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)模块表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)模块提供一个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合，每个[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合中的项目代表[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)模块的对象。  

Aspose.Cells为[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)模块提供[**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--)和[**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)方法，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)模块提供一些处理数字和日期显示格式的有用属性。  

### **如何使用内置数字格式**  

Aspose.Cells提供一些内置的数字格式，用于配置数字和日期的显示格式。这些内置数字格式可以通过[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象的[**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)方法应用。所有内置数字格式都赋予了唯一的数字值。开发者可以将任意希望的数字值分配给[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象的[**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)方法，以应用显示格式。该方法速度快。支持的内置数字格式如下：  

|**数值**|**类型**|**格式字符串**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **如何使用自定义数字格式**  

为定义自定义的显示格式字符串，请使用[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象的[**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)方法。这种方法比预设格式更灵活，但速度较慢。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

如果使用[**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)方法设置数字格式，则会覆盖之前通过[**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)方法设置的任何格式，反之亦然。  

{{% /alert %}}  

## **高级主题**  
- [在设置Style.Custom属性时检查自定义数字格式](/cells/zh/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [支持的数字格式列表](/cells/zh/nodejs-cpp/list-of-supported-number-formats/)  
- [呈现自定义日期格式模式g和ge mm dd](/cells/zh/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [为工作簿指定自定义数值小数和分组分隔符](/cells/zh/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [指定DBNum自定义模式格式化](/cells/zh/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
