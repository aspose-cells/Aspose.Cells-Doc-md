---
title: 管理Excel文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells可以简单的获取、设置、计算excel文件的公式。
description: 了解如何通过 Aspose.Cells for NET API 管理 Excel 文件的公式。
keywords: How to calculate formulas in C#, Formulas and Functions using C#, C# Manage Built-in Functions, How to Use Add-in Functions with C#, How to Use Array Formula via C#, How to Use R1C1 Formula in C#.
---
##  **介绍**

Microsoft Excel 引人注目的功能之一是它能够使用公式和函数处理数据。 Microsoft Excel提供了一组内置函数和公式，可以帮助用户快速执行复杂的计算。 Aspose.Cells还提供了大量内置函数和公式，帮助开发人员轻松计算值。 Aspose.Cells还支持附加功能。另外，Aspose.Cells支持Aspose.Cells中的数组和R1C1公式。

##  **如何使用公式和函数**

Aspose.Cells提供一堂课，[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中的每个工作表的集合。工作表由以下形式表示[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。 Cells集合中的每一项代表一个对象[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

可以使用由提供的属性和方法将公式应用于单元格[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类，下面将详细讨论。

- 使用内置函数。
- 使用附加功能。
- 使用数组公式。
- 创建 R1C1 公式。

##  **如何使用内置函数**

内置函数或公式作为现成函数提供，以减少开发人员的精力和时间。看[内置函数列表](/cells/zh/net/supported-formula-functions/)由 Aspose.Cells 支持。功能按字母顺序列出。未来将支持更多功能。

 Aspose.Cells 支持 Microsoft Excel 提供的大多数公式或函数。开发者可以通过API或[设计师电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)。 Aspose.Cells 支持大量数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性将公式添加到单元格。 *复杂的公式**，例如

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

在 Aspose.Cells 中也受支持。将公式应用于单元格时，请始终以等号 (=) 开头，就像在 Microsoft Excel 中创建公式时一样，并使用逗号 (,) 分隔函数参数。

在下面的示例中，一个复杂的公式应用于工作表的第一个单元格[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。该公式使用内置**IF**Aspose.Cells提供的功能。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

##  **如何使用插件功能**

我们可以有一些用户定义的公式，我们希望将其包含为 Excel 加载项。设置 cell.Formula 函数时，内置函数可以正常工作，但需要使用加载项函数设置自定义函数或公式。

 Aspose.Cells 提供了使用以下功能注册附加功能的功能[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index)。之后，当我们设置 cell.Formula = anyFunctionFromAddIn 时，输出 Excel 文件包含 AddIn 函数的计算值。

应下载以下 XLAM 文件用于注册以下示例代码中的插件功能。同样，可以下载输出文件“test_udf.xlsx”来检查输出。

[测试UDF.xlam](81920908.xlam)

[测试_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

##  **如何使用数组公式**

数组公式是采用数组（而不是单个数字）作为构成公式的函数的参数的公式。当显示数组公式时，它被大括号 ({}) 括起来。

某些 Microsoft Excel 函数返回值数组。要使用数组公式计算多个结果，请将数组输入到行数和列数与数组参数相同的单元格区域中。

可以通过调用将数组公式应用于单元格[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**设置数组公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法。这[**设置数组公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法采用以下参数：

- *数组公式**，数组公式。
- *行数**，填充数组公式结果的行数。
- *列数**，填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

##  **如何使用 R1C1 公式**

添加一个**R1C1**将样式公式引用到单元格[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**R1C1公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

##  **高级主题**
- [先例和家属](/cells/zh/net/precedents-and-dependents/)
- [在公式中设置外部链接](/cells/zh/net/set-external-links-in-formulas/)
- [在新行中输入数据时自动传播表或列表对象中的公式](/cells/zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [命名范围的设置公式](/cells/zh/net/setting-formula-for-named-range/)
- [设置公式 - 非英语用户注意事项](/cells/zh/net/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/net/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/net/specify-maximum-rows-of-shared-formula/)
- [支持的 Excel 函数](/cells/zh/net/supported-formula-functions/)

