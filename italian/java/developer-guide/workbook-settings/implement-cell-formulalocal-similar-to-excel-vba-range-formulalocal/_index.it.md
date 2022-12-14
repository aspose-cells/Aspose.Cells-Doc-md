---
title: Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /it/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Possibili scenari di utilizzo**
Microsoft Le formule di Excel possono avere nomi diversi in impostazioni locali, regioni o lingue diverse. Per esempio,*SOMMA*viene chiamata la funzione*ESTATE*in*Tedesco*. Aspose.Cells non può funzionare con nomi di funzioni non inglesi. In*Microsoft Eccellere VBA*, c'è* *un*Intervallo.FormulaLocale*proprietà che restituisce il nome della funzione in base alla lingua o all'area geografica. Aspose.Cells fornisce anche[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)proprietà a tale scopo. Tuttavia, questa proprietà funzionerà solo quando implementerai[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) metodo.
## **Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**
Il codice di esempio seguente spiega come implementare[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) metodo. Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è*SOMMA*, ritorna*UserFormulaLocal_SUM*. È possibile modificare il codice in base alle proprie esigenze e restituire i nomi delle funzioni locali corretti, ad es*SOMMA*è*ESTATE*in*Tedesco*e*TESTO*è*ТЕКСТ*in*russo*. Si prega di consultare anche l'output della console del codice di esempio fornito di seguito per un riferimento.
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Uscita console**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
