---
title: 通过 C++ 在 Golang 中设置数字格式
linktitle: 数字设置
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持多种单元格数字设置。本文将介绍如何使用Aspose.Cells库管理单元格的数字格式，以便根据需要调整电子表格中的数字格式。
keywords: Aspose.Cells、C++库、电子表格、单元格数字设置、格式化、管理、数字和日期格式
type: docs
weight: 10
url: /zh/go-cpp/cells-number-settings/
---

## **如何设置数字和日期的显示格式**

Microsoft Excel的一个非常强大的特性是它允许用户设置数字值和日期的显示格式。我们知道，数字数据可以用来表示不同的值，包括小数、货币、百分比、分数或会计值等。所有这些数值根据表示的信息类型以不同的格式显示。类似地，日期或时间可以以多种格式显示。
Aspose.Cells支持此功能，并允许开发人员为数字或日期设置任何显示格式。

### **如何在Microsoft Excel中设置显示格式**

在Microsoft Excel中设置显示格式：

1. 右键单击任何单元格。
1. 选择**设置单元格格式**。将会出现一个对话框，用于设置任何类型值的显示格式。

在对话框的左侧，有许多值类别，如**常规**、**数字**、**货币**、**会计**、**日期**、**时间**、**百分比**等。Aspose.Cells支持所有这些显示格式。

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供一个[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的每个项都表示[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

Aspose.Cells为[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类提供了[**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/)和[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)方法。这些方法用于获取和设置单元格的格式设置。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类提供了一些有用的属性，用于处理数字和日期的显示格式。

### **如何使用内置数字格式**

Aspose.Cells提供了一些内置数字格式来配置数字和日期的显示格式。这些内置数字格式可以通过[**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/)对象的[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)属性应用。所有内置数字格式都具有唯一的数值。开发人员可以将任何所需的数值分配给[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象的[**Number**](https://reference.aspose.com/cells/go-cpp/style/getnumber/)属性，以应用显示格式。这种方法速度快。Aspose.Cells支持的内置数字格式如下。

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
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings.go" >}}
### **如何使用自定义数字格式**

要为设置显示格式定义自定义的格式字符串，请使用[**Style**](https://reference.aspose.com/cells/go-cpp/style/)对象的[**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)属性。这种方法不像使用预设格式那样快，但它更灵活。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberSettings-1.go" >}}
{{% alert color="primary" %}}

如果使用[**Custom**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)属性设置数字格式，则会覆盖之前使用[**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/)属性设置的格式，反之亦然。

{{% /alert %}}

## **高级主题**
- [在设置Style.Custom属性时检查自定义数字格式](/cells/zh/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [支持的数字格式列表](/cells/zh/cpp/list-of-supported-number-formats/)
- [呈现自定义日期格式模式g和ge mm dd](/cells/zh/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [为工作簿指定自定义数值小数和分组分隔符](/cells/zh/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [指定DBNum自定义模式格式化](/cells/zh/cpp/specifying-dbnum-custom-pattern-formatting/)
