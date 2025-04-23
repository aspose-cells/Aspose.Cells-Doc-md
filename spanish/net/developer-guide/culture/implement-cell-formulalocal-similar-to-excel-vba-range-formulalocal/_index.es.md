---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /es/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Escenarios de uso posibles**

Las fórmulas de Microsoft Excel pueden tener diferentes nombres en diferentes lugares o regiones o idiomas. Por ejemplo, la función **SUMA** se llama **SUMME** en alemán. Aspose.Cells no puede trabajar con nombres de función no-ingleses. En Microsoft Excel VBA, hay una propiedad **Range.FormulaLocal** que devuelve el nombre de la función según su idioma o región. Aspose.Cells también proporciona la propiedad [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implemente el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname).

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

El siguiente código de ejemplo explica cómo implementar el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es **SUM**, devuelve **UserFormulaLocal_SUM**. Puede cambiar el código según sus necesidades y devolver los nombres de función locales correctos, por ejemplo **SUMA** es **SUMME** en alemán y **TEXTO** es **ТЕКСТ** en ruso. Por favor, consulte también la salida de consola del código de ejemplo dado abajo para referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
