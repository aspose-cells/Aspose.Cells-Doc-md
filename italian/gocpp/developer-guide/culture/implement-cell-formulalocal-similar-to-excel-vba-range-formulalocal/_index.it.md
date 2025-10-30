---
title: Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal con Golang via C++
linktitle: Implementa Cell.FormulaLocal
type: docs
weight: 30
url: /it/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Impara come implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal usando Aspose.Cells con Golang via C++.
---

## **Possibili Scenari di Utilizzo**

Le formule di Microsoft Excel possono avere nomi diversi in diverse località, regioni o lingue. Ad esempio, la funzione **SUM** viene chiamata **SUMME** in tedesco. Aspose.Cells non può lavorare con nomi di funzioni non in inglese. In Microsoft Excel VBA, c'è la proprietà **Range.FormulaLocal** che restituisce il nome della funzione in base alla lingua o alla regione. Aspose.Cells fornisce anche la proprietà [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando implementerai il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

Il seguente codice di esempio spiega come implementare il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è **SUM**, restituisce **UserFormulaLocal_SUM**. Puoi modificare il codice in base alle tue esigenze e restituire i nomi corretti delle funzioni locali come ad esempio **SUM** è **SUMME** in tedesco e **TEXT** è **ТЕКСТ** in russo. Consulta anche l'output della console del codice di esempio qui sotto a titolo di riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **Output della console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
