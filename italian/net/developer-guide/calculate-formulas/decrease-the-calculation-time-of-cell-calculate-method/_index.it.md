---
title: Diminuire il tempo di calcolo del metodo Cell.Calculate
type: docs
weight: 100
url: /it/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Possibili scenari di utilizzo**

Normalmente, consigliamo agli utenti di chiamare[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)metodo una volta e quindi ottenere i valori calcolati delle singole celle. Ma a volte, gli utenti non vogliono calcolare l'intera cartella di lavoro. Vogliono solo calcolare una singola cella. Aspose.Cells fornisce[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) proprietà che puoi impostare**falso** e ridurrà significativamente il tempo di calcolo della singola cella. Perché quando la proprietà ricorsiva è impostata su**VERO** , quindi tutti i dipendenti delle celle vengono ricalcolati a ogni chiamata. Ma quando la proprietà ricorsiva è**falso**, le celle dipendenti vengono calcolate solo una volta e non vengono calcolate nuovamente nelle chiamate successive.

## **Diminuire il tempo di calcolo del metodo Cell.Calculate()**

 Il codice di esempio seguente illustra l'utilizzo di[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) proprietà. Si prega di eseguire questo codice con il file given[file excel di esempio](5113710.xlsx) e controlla l'output della sua console. Scoprirai che impostando la proprietà ricorsiva su**falso**ha ridotto significativamente il tempo di calcolo. Si prega di leggere anche i commenti per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Uscita console**

 Questo è l'output della console del codice di esempio precedente quando eseguito con il file given[file excel di esempio](5113710.xlsx)sulla nostra macchina. Tieni presente che l'output potrebbe differire ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su**falso** sarà sempre inferiore all'impostazione su**VERO**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
