---
title: 实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal
type: docs
weight: 20
url: /zh/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能的使用场景**
Microsoft Excel 中的公式在不同地区或语言中可能有不同的名称。例如，*SUM* 函数在德语中叫作 *SUMME*。Aspose.Cells 不能处理非英语的函数名。在 *Microsoft Excel VBA* 中，有 *Range.FormulaLocal* 属性，可以返回根据其语言或区域的函数名。Aspose.Cells 也提供 [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) 属性实现此功能，但仅在实现 [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) 方法时有效。 
## **实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal**
以下示例演示了如何实现 [GlobalizationSettings.getLocalFunctionName(String standardName)] 方法。该方法返回标准函数的本地名称。例如，标准函数名 *SUM* 对应 *UserFormulaLocal_SUM*。你可以根据需要修改代码，以返回正确的本地函数名，比如，*SUM* 在德语中是 *SUMME*，*TEXT* 在俄语中是 *ТЕКСТ*。下面的控制台输出示例为参考。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **控制台输出**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
