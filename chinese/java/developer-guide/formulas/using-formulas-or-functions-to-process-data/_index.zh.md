---
title: 使用公式或函数处理数据
type: docs
weight: 5
url: /zh/java/get-and-set-formula/
---
{{% alert color="primary" %}}

Microsoft Excel 引人注目的功能之一是它能够使用公式和函数处理数据。 Microsoft Excel 提供了一组内置函数和公式，可帮助用户快速执行复杂的计算。 Aspose.Cells 还提供了大量内置函数和公式，可帮助开发人员轻松计算值。 Aspose.Cells还支持插件功能。此外，Aspose.Cells 支持 Aspose.Cells 中的数组和 R1C1 公式。

{{% /alert %}}

## **使用公式和函数**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。中的每一项[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合代表一个对象[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

可以使用提供的属性和方法将公式应用于单元格[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类，下面更详细地讨论。

- [使用内置函数](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [使用附加功能](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [使用数组公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [创建 R1C1 公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **使用内置函数**

内置函数或公式作为现成的函数提供，以减少开发人员的工作量和时间。看[内置函数列表](/cells/zh/java/supported-formula-functions/).这些函数按字母顺序列出。未来将支持更多功能。

 Aspose.Cells 支持 Microsoft Excel 提供的大部分公式或函数。开发人员可以通过 API 或[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和参考公式。

使用[**公式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)的财产[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类将公式添加到单元格。**复杂的公式**， 例如

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

在 Aspose.Cells 中也受支持。将公式应用于单元格时，始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时所做的那样，并使用逗号 (,) 分隔函数参数。

在下面的示例中，一个复杂的公式应用于工作表的第一个单元格[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)收藏。该公式使用内置**如果**Aspose.Cells提供的功能。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **使用插件功能**

我们可以将一些用户定义的公式作为 excel 加载项包含在内。当设置[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)function 内置函数工作正常，但是需要使用附加函数设置自定义函数或公式。

 Aspose.Cells 提供使用以下功能注册添加功能的功能[**工作表.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)).之后当我们设置[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn，输出 Excel 文件包含来自 AddIn 函数的计算值。

下面的示例代码中需要下载 XLAM 文件用于注册插件功能。同样，可以下载输出文件“test_udf.xlsx”来检查输出。

[测试UDF.xlam](TestUDF.xlam)

[测试_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **使用数组公式**

数组公式是使用数组而不是单个数字作为构成公式的函数的参数的公式。当显示数组公式时，它被大括号 ({}) 包围，如下所示。

**在单元格 G2 上设置数组公式** 

![待办事项：图像_替代_文本](using-formulas-or-functions-to-process-data_1.png)

一些 Microsoft Excel 函数返回值数组。要使用数组公式计算多个结果，请将数组输入到一系列单元格中，这些单元格的行数和列数与数组参数相同。

可以通过调用[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级'[**设置数组公式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)） 方法。这[**设置数组公式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)方法采用以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，用于填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **使用 R1C1 公式**

应用一个**R1C1**将样式公式引用到具有[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级'[**设置R1C1公式**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)财产。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

