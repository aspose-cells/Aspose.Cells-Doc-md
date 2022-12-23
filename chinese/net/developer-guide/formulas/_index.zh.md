---
title: 管理 Excel 文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells 可以简单的获取、设置和计算excel文件的公式。
---
## **介绍**

Microsoft Excel 引人注目的功能之一是它能够使用公式和函数处理数据。 Microsoft Excel 提供了一组内置函数和公式，可帮助用户快速执行复杂的计算。 Aspose.Cells 还提供了大量内置函数和公式，可帮助开发人员轻松计算值。 Aspose.Cells还支持插件功能。此外，Aspose.Cells 支持 Aspose.Cells 中的数组和 R1C1 公式。

## **使用公式和函数**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)收藏。 Cells 集合中的每个项目代表[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级。

可以使用提供的属性和方法将公式应用于单元格[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类，下面更详细地讨论。

- 使用内置函数。
- 使用附加功能。
- 使用数组公式。
- 创建 R1C1 公式。

## **使用内置函数**

内置函数或公式作为现成的函数提供，以减少开发人员的工作量和时间。看[内置函数列表](/cells/zh/net/supported-formula-functions/)由 Aspose.Cells 支持。功能按字母顺序列出。未来将支持更多功能。

 Aspose.Cells 支持 Microsoft Excel 提供的大部分公式或函数。开发人员可以通过 API 或[设计师电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/). Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性将公式添加到单元格。**复杂的公式**， 例如

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

在 Aspose.Cells 中也受支持。将公式应用于单元格时，始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时所做的那样，并使用逗号 (,) 分隔函数参数。

在下面的示例中，一个复杂的公式应用于工作表的第一个单元格[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)收藏。该公式使用内置**如果**Aspose.Cells提供的功能。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **使用插件功能**

我们可以有一些用户定义的公式，我们希望将其作为 excel 加载项包含在内。设置 cell.Formula 函数时，内置函数可以正常工作，但是需要使用附加函数设置自定义函数或公式。

 Aspose.Cells 提供使用以下功能注册添加功能的功能[**工作表.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index).之后，当我们设置 cell.Formula = anyFunctionFromAddIn 时，输出的 Excel 文件包含从 AddIn 函数计算出的值。

在下面的示例代码中注册插件功能需要下载XLAM文件。同样，可以下载输出文件“test_udf.xlsx”来检查输出。

[测试UDF.xlam](81920908.xlam)

[测试_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **使用数组公式**

数组公式是将数组而不是单个数字作为构成公式的函数的参数的公式。当显示数组公式时，它被大括号 ({}) 包围。

一些 Microsoft Excel 函数返回值数组。要使用数组公式计算多个结果，请将数组输入到一系列单元格中，这些单元格的行数和列数与数组参数相同。

可以通过调用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**设置数组公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法。这[**设置数组公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法采用以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，用于填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **使用 R1C1 公式**

添加一个**R1C1**将样式公式引用到具有[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级'[**R1C1公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)财产。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **推进主题**
- [先例和家属](/cells/zh/net/precedents-and-dependents/)
- [在公式中设置外部链接](/cells/zh/net/set-external-links-in-formulas/)
- [在新行中输入数据时自动在表或列表对象中传播公式](/cells/zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [命名范围的设置公式](/cells/zh/net/setting-formula-for-named-range/)
- [设置公式 - 非英语用户须知](/cells/zh/net/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/net/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/net/specify-maximum-rows-of-shared-formula/)
- [支持的 Excel 函数](/cells/zh/net/supported-formula-functions/)

