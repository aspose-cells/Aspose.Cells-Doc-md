---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /es/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Posibles escenarios de uso**

 Microsoft Las fórmulas de Excel pueden tener diferentes nombres en diferentes lugares, regiones o idiomas. Por ejemplo,**SUMA**la funcion se llama**SUMA** en alemán. Aspose.Cells no puede funcionar con nombres de funciones que no estén en inglés. En Microsoft Excel VBA, hay**Rango.FormulaLocal**propiedad que devuelve el nombre de la función según su idioma o región. Aspose.Cells también proporciona[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)propiedad para este fin. Sin embargo, esta propiedad solo funcionará cuando implemente[**GlobalizationSettings.GetLocalFunctionName(string nombre estándar)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)método.

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

 El siguiente código de ejemplo explica cómo implementar[**GlobalizationSettings.GetLocalFunctionName(string nombre estándar)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) método. El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es**SUMA** , vuelve**UserFormulaLocal_SUM** Puede cambiar el código según sus necesidades y devolver los nombres de funciones locales correctos, por ejemplo**SUMA** es**SUMA** en alemán y**TEXTO** es**ТЕКСТ**en ruso. Consulte también la salida de la consola del código de muestra que se proporciona a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
