---
title: Implementa la Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /it/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Possibili Scenari di Utilizzo**
Le formule di Microsoft Excel potrebbero avere nomi diversi a seconda delle localizzazioni, regioni o lingue. Per esempio, la funzione *SUM* si chiama *SUMME* in *Tedesco*. Aspose.Cells non può funzionare con nomi di funzioni non in inglese. In *Microsoft Excel VBA*, esiste una proprietà *Range.FormulaLocal* che restituisce il nome della funzione secondo la sua lingua o regione. Aspose.Cells fornisce anche la proprietà [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando si implementa il metodo [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-). 
## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**
Il seguente esempio di codice spiega come implementare il metodo [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è *SUM*, restituisce *UserFormulaLocal_SUM*. Puoi modificare il codice secondo le tue esigenze e restituire i nomi corretti delle funzioni locali, ad esempio *SUM* è *SUMME* in *Tedesco* e *TEXT* è *ТЕКСТ* in *Russo*. Guarda anche l’output sulla console del codice di esempio di seguito per un riferimento.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Output della console**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
