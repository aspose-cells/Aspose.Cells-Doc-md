---
title: Ridurre il tempo di calcolo del metodo Cell.Calculate
type: docs
weight: 860
url: /it/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Possibili Scenari di Utilizzo

Normalmente, si consiglia agli utenti di chiamare il metodo [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) una volta e quindi ottenere i valori calcolati delle singole celle. Ma a volte, gli utenti non vogliono calcolare l'intero workbook. Vogliono semplicemente calcolare una singola cella. Aspose.Cells fornisce la proprietà [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) che puoi impostare su **false** e ridurrà significativamente il tempo di calcolo di una singola cella. Perché quando la proprietà ricorsiva è impostata su **true**, tutte le dipendenze delle celle vengono ricalcolate a ogni chiamata. Ma quando la proprietà ricorsiva è impostata su **false**, le celle dipendenti vengono calcolate una sola volta e non vengono ricalcolate nelle chiamate successive.
## **Ridurre il tempo di calcolo del metodo Cell.Calculate()**
Il seguente codice di esempio illustra l'uso della proprietà [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive). Si prega di eseguire questo codice con il [file excel di esempio](5472288.xlsx) fornito e controllare l'output della console. Si noterà che l'impostazione della proprietà ricorsiva su **false** ha ridotto notevolmente il tempo di calcolo. Si prega anche di leggere i commenti per una migliore comprensione di questa proprietà.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Output della console**
Questo è l'output della console del codice di esempio sopra eseguito con il [file excel di esempio](5472288.xlsx) sul nostro computer. Si prega di notare che il proprio output potrebbe differire, ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su **false** sarà sempre inferiore rispetto a impostarla su **true**.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
