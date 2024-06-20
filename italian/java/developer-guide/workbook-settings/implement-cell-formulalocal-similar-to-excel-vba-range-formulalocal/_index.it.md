---
title: Implementa la Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /it/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Possibili Scenari di Utilizzo**
Le formule di Microsoft Excel possono avere nomi diversi in diverse località o regioni o lingue. Ad esempio, la funzione *SUM* è chiamata *SUMME* in *tedesco*. Aspose.Cells non può lavorare con nomi di funzione non inglesi. In *Microsoft Excel VBA*, c'è una proprietà *Range.FormulaLocal* che restituisce il nome della funzione secondo la sua lingua o regione. Aspose.Cells fornisce anche la proprietà [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando si implementerà il metodo [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)). 
## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**
Il seguente codice di esempio spiega come implementare il metodo [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è *SUM*, restituisce *UserFormulaLocal_SUM*. È possibile modificare il codice secondo le proprie esigenze e restituire i nomi corretti delle funzioni locali come ad esempio *SUM* è *SUMME* in *tedesco* e *TEXT* è *ТЕКСТ* in *russo*. Si prega anche di consultare l'output della console del codice di esempio fornito di seguito per riferimento.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Output della console**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
