---
title: Implementa la Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /it/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Possibili Scenari di Utilizzo**

Le formule di Microsoft Excel possono avere nomi diversi in diverse località, regioni o lingue. Ad esempio, la funzione **SUM** viene chiamata **SUMME** in tedesco. Aspose.Cells non può lavorare con nomi di funzioni non in inglese. In Microsoft Excel VBA, c'è la proprietà **Range.FormulaLocal** che restituisce il nome della funzione in base alla lingua o alla regione. Aspose.Cells fornisce anche la proprietà [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando implementerai il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname).

## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

Il seguente codice di esempio spiega come implementare il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è **SUM**, restituisce **UserFormulaLocal_SUM**. Puoi modificare il codice in base alle tue esigenze e restituire i nomi corretti delle funzioni locali come ad esempio **SUM** è **SUMME** in tedesco e **TEXT** è **ТЕКСТ** in russo. Consulta anche l'output della console del codice di esempio qui sotto a titolo di riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Output della console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
