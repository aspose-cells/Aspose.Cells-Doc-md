---
title: Riduci il tempo di calcolo del metodo Cell.Calculate con Golang tramite C++
linktitle: Riduci il tempo di calcolo di Cell.Calculate
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per ridurre il tempo di calcolo dei metodi di calcolo delle celle in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per ottimizzare il metodo di calcolo delle celle e migliorare le prestazioni. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, metodi di calcolo delle celle, ottimizzazione, prestazioni, riduzione del tempo di calcolo
type: docs
weight: 100
url: /it/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possibili Scenari di Utilizzo**

Normalmente, si raccomanda agli utenti di chiamare il metodo [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) una volta e poi ottenere i valori calcolati delle singole celle. Ma alcune volte, gli utenti non vogliono calcolare l'intero workbook. Vogliono semplicemente calcolare una singola cella. Aspose.Cells fornisce la proprietà [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) che puoi impostare su **false** e questo ridurrà significativamente il tempo di calcolo delle singole celle. Perché quando la proprietà ricorsiva è impostata su **true**, allora tutti i dipendenti delle celle vengono ricalcolati ad ogni chiamata. Ma quando la proprietà ricorsiva è **false**, le celle dipendenti vengono calcolate una sola volta e non vengono ricalcolate nelle chiamate successive.

## **Ridurre il tempo di calcolo del metodo Cell.Calculate()**

Il seguente esempio di codice illustra l'uso della proprietà [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). Esegui questo codice con il [file Excel di esempio](5113710.xlsx) fornito e verifica l'output sulla console. Troverai che impostare la proprietà ricorsiva su **false** ha ridotto significativamente il tempo di calcolo. Leggi anche i commenti per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **Output della console**

Questo è l'output sulla console del codice di esempio sopra quando eseguito con il [file Excel di esempio](5113710.xlsx) sul nostro sistema. Nota che l'output può differire, ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su **false** sarà sempre inferiore rispetto ad averla impostata su **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
