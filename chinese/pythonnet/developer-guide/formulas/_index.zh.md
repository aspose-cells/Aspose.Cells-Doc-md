---
title: 管理Excel文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/python-net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells for Python via .NET 可以轻松获取、设置和计算 Excel 文件中的公式。
description: 了解如何通过 Aspose.Cells for Python via .NET for NET API 管理 Excel 文件中的公式。
keywords: 如何用 Python 计算公式，使用 Python 处理公式和函数，Python 管理内置函数，以及如何结合插件函数使用 Python，使用 Python 进行数组公式和 R1C1 公式。
---

## **介绍**

微软 Excel 的一大亮点是其能用公式和函数处理数据。Excel 提供一套内置函数和公式，帮助用户快速完成复杂计算。Aspose.Cells for Python via .NET 也提供大量内置函数和公式，助开发者轻松实现值计算，还支持插件函数，以及数组和 R1C1 公式。

## **如何使用公式和函数**

Aspose.Cells for Python via .NET 提供了 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 类包含一个 [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) 集合，可以访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) 集合，每个 Cells 集合中的项目代表一个 [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) 类对象。

可以使用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类提供的属性和方法将公式应用到单元格中，下面将更详细地讨论。

- 使用内置函数。
- 使用插件函数。
- 使用数组公式。
- 创建R1C1公式。

## **如何使用内置函数**

内置函数或公式作为现成的功能提供，减少开发者的努力和时间。请参见 [Aspose.Cells for Python via .NET 支持的内置函数列表](/cells/zh/python-net/supported-formula-functions/)，按字母顺序列出。未来将支持更多函数。

Aspose.Cells for Python via .NET 支持大多数由微软 Excel 提供的公式和函数。开发者可以通过 API 或 [设计师电子表格]( /cells/zh/net/what-is-a-designer-spreadsheet/) 使用。这包括大量数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用类的公式。

使用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的[**formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula)属性向单元格添加公式。**复杂的公式**，例如

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, 在 Aspose.Cells for Python via .NET 也支持。应用公式到单元格时，必须以等号 (=) 开头，并用逗号（,）分隔参数，就像在微软 Excel 中一样。

在下面的示例中，将一个复杂公式应用于工作表的 [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) 集合的第一个单元格中。该公式使用 Aspose.Cells for Python via .NET 提供的内置 **IF** 函数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingBuiltinfunction-1.py" >}}

## **如何使用Add-in函数**

我们可以有一些自定义的公式，我们希望将其包含为Excel加载项。当设置cell.Formula函数内置函数正常工作时，但需要使用加载项函数设置自定义函数或公式。

Aspose.Cells for Python via .NET 提供注册插件函数的功能，使用 [**worksheets.register_add_in_function()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/register_add_in_function)。设置 cell.Formula = anyFunctionFromAddIn 后，生成的 Excel 文件会包含插件函数计算值。

可以下载以下XLAM文件以注册以下示例代码中的加载项函数。类似地，可以下载输出文件"test_udf.xlsx"以检查输出。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-RegisterAndCallFuncFromAddIn-1.py" >}}

## **如何使用数组公式**

数组公式是以数组作为参数的函数所组成的公式。在显示数组公式时，会用大括号({})括起来。

某些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的[**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula)方法将数组公式应用于单元格。[**set_array_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_array_formula)方法接受以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingArrayFunction-1.py" >}}

## **如何使用R1C1公式**

使用[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)类的[**r1c1_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/r1c1_formula)属性向单元格添加**R1C1**引用样式的公式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-ProcessDataUsingR1C1-1.py" >}}

## **高级主题**
- [前导和从属](/cells/zh/python-net/precedents-and-dependents/)
- [设置公式中的外部链接](/cells/zh/python-net/set-external-links-in-formulas/)
- [在输入新数据时自动传播表或列表对象中的公式](/cells/zh/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [为命名范围设置公式](/cells/zh/python-net/setting-formula-for-named-range/)
- [设置公式-非英语用户注意事项](/cells/zh/python-net/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/python-net/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/python-net/specify-maximum-rows-of-shared-formula/)
- [支持的Excel函数](/cells/zh/python-net/supported-formula-functions/)


{{< app/cells/assistant language="python-net" >}}
