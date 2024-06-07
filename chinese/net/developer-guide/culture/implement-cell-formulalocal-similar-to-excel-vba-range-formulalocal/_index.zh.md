---
title: 实现类似于Excel VBA范围.FormulaLocal的单元格.FormulaLocal
type: docs
weight: 30
url: /zh/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能的使用场景**

微软Excel公式在不同的地区、区域或语言中可能有不同的名称。例如，**SUM**函数在德语中被称为**SUMME**。Aspose.Cells无法处理非英语函数名称。在Microsoft Excel VBA中，有**Range.FormulaLocal**属性，根据其语言或区域返回函数的名称。Aspose.Cells还提供了用于此目的的[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)属性。但是，只有在实现[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法后才能使用此属性。

## **实现类似于Excel VBA范围.FormulaLocal的单元格.FormulaLocal**

以下示例代码解释了如何实现[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。该方法返回标准函数的本地名称。如果标准函数名称是**SUM**，它就返回**UserFormulaLocal_SUM**。您可以根据需要更改代码，并返回正确的本地函数名称，例如**SUM**在德语中是**SUMME**，**TEXT**在俄语中是**ТЕКСТ**。还请查看下文给出的示例代码的控制台输出，进行参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **控制台输出**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
