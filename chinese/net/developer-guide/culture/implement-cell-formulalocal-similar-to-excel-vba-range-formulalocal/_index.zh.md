---
title: 实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal
type: docs
weight: 30
url: /zh/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能的使用场景**

Microsoft Excel公式在不同语言、地区或国家/地区可能有不同的名称。例如，**SUM** 函数在德语中称为**SUMME**。Aspose.Cells无法处理非英语函数名称。在Microsoft Excel VBA中，有一个**Range.FormulaLocal** 属性，根据其语言或地区返回函数的名称。Aspose.Cells也为此提供了[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)属性。但是，只有在您实现[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法时，此属性才能正常工作。

## **实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal**

以下示例代码解释了如何实现[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。该方法返回标准函数的本地名称。如果标准函数名称为**SUM**，它将返回**UserFormulaLocal_SUM**。您可以根据需要更改代码并返回正确的本地函数名称，例如**SUM** 在德语中是**SUMME**，**TEXT** 在俄语中是**ТЕКСТ**。还请参考下面给出的示例代码的控制台输出作为参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **控制台输出**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
