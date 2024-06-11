---
title: 实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal
type: docs
weight: 20
url: /zh/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能的使用场景**
Microsoft Excel公式在不同的时区、地区或语言中可能有不同的名称。例如，*SUM*函数在*German*中被称为*SUMME*。Aspose.Cells无法处理非英文函数名称。在*Microsoft Excel VBA*中，有一个*Range.FormulaLocal*属性，返回函数名称与其语言或地区的对应关系。Aspose.Cells也提供了[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)属性来实现此目的。然而，只有在实现[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))方法时才能使用该属性。 
## **实现类似于Excel VBA Range.FormulaLocal的Cell.FormulaLocal**
以下示例代码解释了如何实现[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))方法。该方法返回标准函数的本地名称。如果标准函数名称为*SUM*，它将返回*UserFormulaLocal_SUM*。您可以根据需要更改代码并返回正确的本地函数名称，例如*SUM*在*German*中为*SUMME*，*TEXT*在*Russian*中为*ТЕКСТ*。还请参见下面给出的示例代码的控制台输出作为参考。
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **控制台输出**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
