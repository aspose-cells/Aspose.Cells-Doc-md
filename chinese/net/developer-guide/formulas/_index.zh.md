---
title: 管理Excel文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells可以简单地获取、设置和计算Excel文件的公式。
description: 通过Aspose.Cells for NET APIs管理Excel文件的公式方法。
keywords: 如何在C#中计算公式，使用C#管理内置函数，如何在C#中使用插件函数，如何在C#中使用阵列公式，如何在C#中使用R1C1公式。
---

## **介绍**

Microsoft Excel的一个引人注目的功能是其使用公式和函数处理数据的能力。Microsoft Excel提供了一组内置函数和公式，帮助用户快速执行复杂计算。Aspose.Cells还提供了大量内置函数和公式，帮助开发者轻松计算值。Aspose.Cells还支持插件函数。此外，Aspose.Cells支持数组和R1C1公式。

## **如何使用公式和函数**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合。Cells集合中的每个项都代表了[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

可以使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供的属性和方法将公式应用到单元格中，下面将更详细地讨论。

- 使用内置函数。
- 使用插件函数。
- 使用数组公式。
- 创建R1C1公式。

## **如何使用内置函数**

内置函数或公式作为现成的函数提供，以减轻开发人员的工作和时间。请参阅Aspose.Cells支持的[内置函数列表](/cells/zh/net/supported-formula-functions/)。函数按字母顺序列出。将来将支持更多函数。

Aspose.Cells支持大多数Microsoft Excel提供的公式或函数。开发人员可以通过API或[设计人员已设计的电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)使用这些公式。Aspose.Cells支持一大堆数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性向单元格添加公式。**复杂的公式**，例如

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

Aspose.Cells也支持定义的函数。在将公式应用于单元格时，始终要以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

在下面的示例中，复杂的公式应用于工作表的第一个单元格的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合。该公式使用Aspose.Cells提供的内置**IF**函数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **如何使用Add-in函数**

我们可以有一些自定义的公式，我们希望将其包含为Excel加载项。当设置cell.Formula函数内置函数正常工作时，但需要使用加载项函数设置自定义函数或公式。

Aspose.Cells提供功能来使用[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index)注册加载项函数。之后，当我们设置cell.Formula = anyFunctionFromAddIn时，输出的Excel文件包含从AddIn函数计算出的值。

可以下载以下XLAM文件以注册以下示例代码中的加载项函数。类似地，可以下载输出文件"test_udf.xlsx"以检查输出。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **如何使用数组公式**

数组公式是以数组作为参数的函数所组成的公式。在显示数组公式时，会用大括号({})括起来。

某些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法将数组公式应用于单元格。[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula)方法接受以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **如何使用R1C1公式**

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula)属性向单元格添加**R1C1**引用样式的公式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **高级主题**
- [前导和从属](/cells/zh/net/precedents-and-dependents/)
- [设置公式中的外部链接](/cells/zh/net/set-external-links-in-formulas/)
- [在输入新数据时自动传播表或列表对象中的公式](/cells/zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [为命名范围设置公式](/cells/zh/net/setting-formula-for-named-range/)
- [设置公式-非英语用户注意事项](/cells/zh/net/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/net/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/net/specify-maximum-rows-of-shared-formula/)
- [支持的Excel函数](/cells/zh/net/supported-formula-functions/)

{{< app/cells/assistant language="csharp" >}}
