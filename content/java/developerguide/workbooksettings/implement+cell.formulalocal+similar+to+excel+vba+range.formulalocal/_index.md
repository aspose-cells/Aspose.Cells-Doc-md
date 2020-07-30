---
title : "Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal" 
description : "" 
weight : 12116 
toc : false
type: docs
url: /java/developerguide/workbooksettings/implement+cell.formulalocal+similar+to+excel+vba+range.formulalocal/
---

# Aspose.Cells for Java : Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal](#implement-cell.formulalocal-similar-to-excel-vba-range.formulalocal)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Microsoft Excel Formulas may have different names in different locales or regions or languages. For example, *SUM *function is called *SUMME *in *German*. Aspose.Cells cannot work with non-English function names. In *Microsoft Excel VBA*, there isa* Range.**FormulaLocal* property that returns the name of the function as per its language or region. Aspose.Cells also provides [Cell.FormulaLocal](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#FormulaLocal) property for this purpose. However, this property will only work when you will implement [GlobalizationSettings.getLocalFunctionName(String standardName)](https://apireference.aspose.com/java/cells/com.aspose.cells/globalizationsettings#getLocalFunctionName(java.lang.String)) method. 

## Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal

The following sample code explains how to implement [GlobalizationSettings.getLocalFunctionName(String standardName)](https://apireference.aspose.com/java/cells/com.aspose.cells/globalizationsettings#getLocalFunctionName(java.lang.String)) method. The method returns the local name of the standard function. If the standard function name is *SUM*, it returns *UserFormulaLocal\_SUM*. You can change the code as per your needs and return the correct local function names e.g. *SUM *is *SUMME *in *German *and *TEXT *is *ТЕКСТ *in *Russian*. Please also see the console output of the sample code given below for a reference.

## Sample Code

## Console Output

{{< code lang="cs" >}}
Formula Local: =UserFormulaLocal_SUM(A1:A2)
Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)
{{< /code >}}

