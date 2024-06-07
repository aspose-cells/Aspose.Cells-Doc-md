---
title: 使用公式或函数处理数据
type: docs
weight: 5
url: /zh/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Microsoft Excel的一个引人注目的功能之一是使用公式和函数处理数据的能力。Microsoft Excel提供一组内置函数和公式，帮助用户快速执行复杂计算。Aspose.Cells还提供了大量内置函数和公式，帮助开发人员轻松计算值。此外，Aspose.Cells支持增值函数。此外，Aspose.Cells支持数组和R1C1公式。

{{% /alert %}}

## **使用公式和函数**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了一个[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合中的每个项目表示[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

可以使用[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供的属性和方法将公式应用于单元格，下面将对此进行更详细的讨论。

- [使用内置函数](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-built-in-functions)。
- [使用增值函数](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-add-in-functions)。
- [使用数组公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-array-formula)。
- [创建R1C1公式](/cells/zh/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula)。

## **使用内置函数**

内置函数或公式是提供的现成函数，可减少开发人员的工作量和时间。查看[内置函数列表](/cells/zh/java/supported-formula-functions/)。这些函数按字母顺序列出。将来将支持更多函数。

Aspose.Cells支持Microsoft Excel提供的大多数公式或函数。开发人员可以通过API或设计电子表格来使用这些公式。Aspose.Cells支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。

使用[**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)属性来向单元格添加公式的[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类。例如，**复杂公式**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

在Aspose.Cells中也受到支持。将公式应用于单元格时，始终使用等号(=)开头字符串，就像在Microsoft Excel中创建公式时一样，并使用逗号(,)分隔函数参数。

在下面的示例中，将复杂公式应用于工作表[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)集合的第一个单元格。该公式使用Aspose.Cells提供的内置**IF**函数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **使用加载项函数**

我们可以定义一些用户自定义公式，想要将其包含在Excel加载项中。在设置内置函数正常工作的情况下[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)，但需要使用加载项函数设置自定义函数或公式。

Aspose.Cells提供功能以注册加载项函数使用[**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)。之后当我们设置[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)= anyFunctionFromAddIn时，输出的Excel文件中包含来自加载项函数的计算值。

下面的XLAM文件可用于下载，以在下面的示例代码中注册加载项函数。类似地，输出文件"test_udf.xlsx"可供下载以检查输出。

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **使用数组公式**

数组公式是使用数组而不是单个数字作为公式的参数的公式。当显示数组公式时，它将被大括号({})包围，如下所示。

**在单元格G2中设置数组公式** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

一些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将该数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)方法向单元格应用数组公式。[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)方法接受以下参数:

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **使用R1C1公式**

使用[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)属性将**R1C1**参考样式公式应用于单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

