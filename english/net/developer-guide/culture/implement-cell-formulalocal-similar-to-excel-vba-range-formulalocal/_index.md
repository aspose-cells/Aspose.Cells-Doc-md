---
title: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel formulas may have different names in different locales, regions, or languages. For example, the **SUM** function is called **SUMME** in German. Aspose.Cells cannot work with non‑English function names. In Microsoft Excel VBA, there is the **Range.FormulaLocal** property that returns the name of the function in its language or region. Aspose.Cells also provides the [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) property for this purpose. However, this property will only work when you implement the [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) method.

## **Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal**

The following sample code explains how to implement the [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) method. The method returns the local name of the standard function. If the standard function name is **SUM**, it returns **UserFormulaLocal_SUM**. You can change the code as per your needs and return the correct local function names, e.g., **SUM** is **SUMME** in German and **TEXT** is **ТЕКСТ** in Russian. Please also see the console output of the sample code given below for reference.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Console Output**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
