---
title: Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /it/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Possibili scenari di utilizzo**

 Le formule di Microsoft Excel possono avere nomi diversi in impostazioni locali, regioni o lingue diverse. Per esempio,**SOMMA**viene chiamata la funzione**ESTATE** in tedesco. Aspose.Cells non può funzionare con nomi di funzioni non inglesi. In Microsoft Excel VBA, c'è**Intervallo.FormulaLocale**proprietà che restituisce il nome della funzione in base alla lingua o all'area geografica. Aspose.Cells fornisce anche[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)proprietà a tale scopo. Tuttavia, questa proprietà funzionerà solo quando implementerai[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)metodo.

## **Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

 Il codice di esempio seguente spiega come implementare[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) metodo. Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è**SOMMA** , ritorna**UserFormulaLocal_SUM** È possibile modificare il codice in base alle proprie esigenze e restituire i nomi delle funzioni locali corretti, ad es**SOMMA** è**ESTATE** in tedesco e**TESTO** è**ТЕКСТ**in russo. Si prega di consultare anche l'output della console del codice di esempio fornito di seguito per un riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
