---
title: Ridurre il tempo di calcolo del metodo Cell.Calculate
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per ridurre il tempo di calcolo dei metodi di calcolo delle celle in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per ottimizzare il metodo di calcolo delle celle e migliorare le prestazioni. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, metodi di calcolo delle celle, ottimizzazione, prestazioni, riduzione del tempo di calcolo
type: docs
weight: 100
url: /it/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possibili Scenari di Utilizzo**

Normalmente consigliamo agli utenti di chiamare il metodo [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) una volta e quindi ottenere i valori calcolati delle singole celle. Ma a volte gli utenti non vogliono calcolare l'intero workbook. Vogliono solo calcolare una singola cella. Aspose.Cells fornisce la proprietà [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) che è possibile impostare su **false** e diminuirà significativamente il tempo di calcolo della cella individuale. Perché quando la proprietà ricorsiva è impostata su **true**, allora tutti i dipendenti delle celle vengono ricalcolati ad ogni chiamata. Ma quando la proprietà ricorsiva è **false**, allora le celle dipendenti vengono calcolate solo una volta e non vengono calcolate nuovamente nelle chiamate successive.

## **Ridurre il tempo di calcolo del metodo Cell.Calculate()**

Il seguente codice di esempio illustra l'utilizzo della proprietà [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive). Si prega di eseguire questo codice con il [file Excel di esempio](5113710.xlsx) e controllare il suo output sulla console. Troverete che impostando la proprietà ricorsiva su **false** ha ridotto significativamente il tempo di calcolo. Si prega inoltre di leggere i commenti per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Output della console**

Questo è l'output della console del codice di esempio precedente quando eseguito con il [file Excel di esempio](5113710.xlsx) sulla nostra macchina. Si prega di notare che il proprio output potrebbe differire, ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su **false** sarà sempre inferiore rispetto a quando è impostata su **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
