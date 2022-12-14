---
title: 实施 Cell.FormulaLocal 类似于 Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /zh/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **可能的使用场景**

 Microsoft Excel 公式在不同的语言环境或地区或语言中可能有不同的名称。例如，**和**函数被调用**夏日**在德国。 Aspose.Cells 无法使用非英语函数名称。在 Microsoft Excel VBA 中，有**范围.FormulaLocal**根据函数的语言或区域返回函数名称的属性。 Aspose.Cells还提供[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)为此目的的财产。但是，此属性仅在您实施时才有效[**GlobalizationSettings.GetLocalFunctionName（字符串标准名称）**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。

## **实施 Cell.FormulaLocal 类似于 Excel VBA Range.FormulaLocal**

下面的示例代码解释了如何实现[**GlobalizationSettings.GetLocalFunctionName（字符串标准名称）**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。该方法返回标准函数的本地名称。如果标准函数名是**和** 它返回**UserFormulaLocal_SUM**.您可以根据需要更改代码并返回正确的本地函数名称，例如**和**是**夏日**用德语和**文本**是**ТЕКСТ**用俄语。另请参阅下面给出的示例代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
