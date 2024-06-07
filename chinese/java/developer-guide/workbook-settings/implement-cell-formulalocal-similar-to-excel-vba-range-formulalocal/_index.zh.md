---
title: 实现类似于Excel VBA范围.FormulaLocal的单元格.FormulaLocal
type: docs
weight: 20
url: /zh/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能的使用场景**
Microsoft Excel公式在不同的区域、语言或语言中的名称可能不同。例如，在*德语*中，*SUM*函数称为*SUMME*。Aspose.Cells无法处理非英语函数名称。在*Microsoft Excel VBA*中，有一个*Range.FormulaLocal*属性，按照其语言或区域返回函数的名称。Aspose.Cells还为此提供了[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)属性。然而，仅当您实现了[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))方法时，此属性才能正常工作。 
## **实现类似于Excel VBA范围.FormulaLocal的单元格.FormulaLocal**
以下示例代码解释了如何实现[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))方法。该方法返回标准函数的本地名称。如果标准函数名称为*SUM*，它将返回*UserFormulaLocal_SUM*。您可以根据需要更改代码，并返回正确的本地函数名称，例如*SUM*在*德语*中为*SUMME*，*TEXT*在*俄语*中为*ТЕКСТ*。请参考下方给出的示例代码的控制台输出。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **控制台输出**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
