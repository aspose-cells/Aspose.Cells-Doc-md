---
title: 管理Excel文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells可以简单地获取、设置和计算Excel文件的公式
description: 通过Aspose.Cells for NET API学习如何管理Excel文件的公式
keywords: 如何在C#中计算公式，使用C#公式和函数，C#管理内置函数，如何在C#中使用插件函数，如何通过C#使用数组公式，如何在C#中使用R1C1公式
---

## **介绍**

Microsoft Excel引人注目的一个功能之一是其处理数据的能力以及公式和函数。Microsoft Excel提供了一组内置函数和公式，帮助用户快速执行复杂计算。Aspose.Cells还提供了一大批内置函数和公式，帮助开发人员轻松计算值。Aspose.Cells还支持插件函数。此外，Aspose.Cells支持数组和R1C1公式。

## **如何使用公式和函数**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供一个[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)集合，Cells集合中的每个项表示[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的对象。

通过[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类提供的属性和方法将公式应用到单元格是可能的

- 使用内置函数
- 使用插件函数
- 使用数组公式
- 创建R1C1公式

## **如何使用内置函数**

内建功能或公式作为现成的函数提供，以减少开发人员的工作量和时间。查看Aspose.Cells支持的[内建函数列表](/cells/zh/net/supported-formula-functions/)。这些函数按字母顺序列出。未来将支持更多函数。

Aspose.Cells支持Microsoft Excel提供的大部分公式或函数。开发人员可以通过API或[设计表格](/cells/zh/net/what-is-a-designer-spreadsheet/)使用这些公式。Aspose.Cells支持一大批数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。

使用[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的[**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)属性向单元格添加公式。例如，复杂的公式

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

在Aspose.Cells中也受到支持。将公式应用于单元格时，始终使用等号(=)开头字符串，就像在Microsoft Excel中创建公式时一样，并使用逗号(,)分隔函数参数。

在下面的示例中，将复杂公式应用于工作表的第一个单元格的[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)集合。该公式使用Aspose.Cells提供的内置**IF**函数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **如何使用插件函数**

我们可以有一些希望作为Excel插件包含的用户定义的公式。在设置cell.Formula函数时，内置函数能够正常工作，但是需要使用插件函数来设置定制的函数或公式。

Aspose.Cells提供了使用[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index)注册插件函数的功能。之后，当我们设置cell.Formula = anyFunctionFromAddIn时，输出的Excel文件会包含来自插件函数的计算值。

以下XLAM文件将用于在下面的示例代码中注册插件函数。类似地，可以下载输出文件“test_udf.xlsx”以检查输出。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **如何使用数组公式**

数组公式是使用数组而不是单个数字作为组成公式的函数的参数的公式。显示数组公式时，需要用大括号({})括起来。

一些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将该数组输入到与数组参数具有相同行数和列数的单元格范围中。

通过调用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) 方法可以将数组公式应用到单元格。[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) 方法接收以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **如何使用R1C1公式**

使用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [**R1C1Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) 属性向单元格添加 **R1C1** 引用样式公式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **高级主题**
- [先行关系和后继关系](/cells/zh/net/precedents-and-dependents/)
- [在公式中设置外部链接](/cells/zh/net/set-external-links-in-formulas/)
- [在新行中输入数据时，自动在表格或列表对象中传播公式](/cells/zh/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [为命名范围设置公式](/cells/zh/net/setting-formula-for-named-range/)
- [设置公式-非英语用户请注意](/cells/zh/net/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/net/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/net/specify-maximum-rows-of-shared-formula/)
- [支持的Excel函数](/cells/zh/net/supported-formula-functions/)

