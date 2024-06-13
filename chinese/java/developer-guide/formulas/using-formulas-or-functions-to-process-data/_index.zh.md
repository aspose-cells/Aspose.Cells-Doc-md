---
title: 使用公式或函数处理数据
type: docs
weight: 5
url: /zh/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Microsoft Excel 的一个引人注目的功能之一是其使用公式和函数处理数据的能力。Microsoft Excel 提供一组内置的函数和公式，帮助用户快速执行复杂的计算。Aspose.Cells 也提供了一大堆内置函数和公式，帮助开发人员轻松计算值。Aspose.Cells 还支持加入函数。此外，Aspose.Cells 还支持在 Aspose.Cells 中进行数组和 R1C1 公式。

{{% /alert %}}

## **使用公式和函数**

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了一个 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) 集合。 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) 集合中的每个项目代表 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的对象。

可以使用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类提供的属性和方法将公式应用于单元格，下面将详细讨论。

- [使用内置函数](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-built-in-functions)。
- [使用加载项函数](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-add-in-functions)。
- [处理数组公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-array-formula)。
- [创建 R1C1 公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula)。

## **使用内建函数**

内建函数或公式是提供的现成函数，以减少开发人员的工作量和时间。参见 [内建函数列表](/cells/zh/java/supported-formula-functions/)。这些函数以字母顺序列出。将来将支持更多函数。

Aspose.Cells 支持 Microsoft Excel 提供的大部分公式或函数。开发人员可以通过 API 或 [设计者电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/) 使用这些公式。Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。

使用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的 [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 属性向单元格添加公式。例如**复杂公式**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

Aspose.Cells也支持定义的函数。在将公式应用于单元格时，始终要以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

在下面的示例中，将复杂公式应用于工作表的 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) 集合的第一个单元格。该公式使用 Aspose.Cells 提供的内建 **IF** 函数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **使用加载项函数**

我们可以有一些自定义函数，希望将其包括为 Excel 加载项。当设置 [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 函数，内建函数正常工作，但有必要使用加载项函数设置自定义函数或公式。

Aspose.Cells提供了功能来使用[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean))注册增强功能。然后，当我们设置[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)= anyFunctionFromAddIn时，输出Excel文件包含来自增强功能的计算值。

可以下载以下 XLAM 文件以在下面的示例代码中注册加载项函数。类似地，可以下载输出文件"test_udf.xlsx"以检查输出。

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **使用数组公式**

数组公式是使用数组而不是单个数字作为公式的参数而工作的公式。显示数组公式时，用大括号（{}）括起来，如下所示。

**在 G2 单元格上设置数组公式** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

某些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的 [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) 方法向单元格应用数组公式。 [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) 方法接受以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **Number of Columns**，要填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **使用 R1C1 公式**

在 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的 [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) 属性中为单元格应用 **R1C1** 参考样式公式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

