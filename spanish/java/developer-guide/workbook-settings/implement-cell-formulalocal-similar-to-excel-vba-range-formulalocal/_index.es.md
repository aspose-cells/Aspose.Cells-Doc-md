---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /es/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Posibles escenarios de uso**
Microsoft Las fórmulas de Excel pueden tener diferentes nombres en diferentes lugares, regiones o idiomas. Por ejemplo,*SUMA*la funcion se llama*SUMA*en*Alemán*Aspose.Cells no puede funcionar con nombres de funciones que no estén en inglés. En*Microsoft Excel VBA*, hay* *a*Rango.FormulaLocal*propiedad que devuelve el nombre de la función según su idioma o región. Aspose.Cells también proporciona[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)propiedad para este fin. Sin embargo, esta propiedad solo funcionará cuando implemente[GlobalizationSettings.getLocalFunctionName(String nombre estándar)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) método.
## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**
El siguiente código de ejemplo explica cómo implementar[GlobalizationSettings.getLocalFunctionName(String nombre estándar)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) método. El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es*SUMA*, vuelve*UserFormulaLocal_SUM*. Puede cambiar el código según sus necesidades y devolver los nombres de funciones locales correctos, por ejemplo*SUMA*es*SUMA*en*Alemán*y*TEXTO*es*ТЕКСТ*en*ruso*. Consulte también la salida de la consola del código de muestra que se proporciona a continuación para obtener una referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Salida de consola**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
