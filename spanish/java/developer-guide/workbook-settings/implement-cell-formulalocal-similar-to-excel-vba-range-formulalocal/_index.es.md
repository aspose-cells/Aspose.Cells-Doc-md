---
title: Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /es/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Escenarios de uso posibles**
Las fórmulas de Microsoft Excel pueden tener nombres diferentes en diferentes localidades, regiones o idiomas. Por ejemplo, la función *SUM* se llama *SUMME* en *Alemán*. Aspose.Cells no puede trabajar con nombres de funciones que no sean en inglés. En *Microsoft Excel VBA*, hay una propiedad *Range.FormulaLocal* que devuelve el nombre de la función en función de su idioma o región. Aspose.Cells también proporciona la propiedad [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implementes el método [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) 
## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**
El siguiente código de ejemplo explica cómo implementar el método [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es *SUM*, devuelve *UserFormulaLocal_SUM*. Puedes modificar el código según tus necesidades y devolver los nombres correctos de las funciones locales, por ejemplo, *SUM* es *SUMME* en *Alemán* y *TEXT* es *ТЕКСТ* en *Ruso*. También debes consultar la salida de la consola del código de ejemplo que se proporciona abajo como referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Salida de la consola**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
