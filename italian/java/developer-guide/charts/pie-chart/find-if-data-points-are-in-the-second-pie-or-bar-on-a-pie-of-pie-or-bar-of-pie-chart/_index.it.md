---
title: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
type: docs
weight: 910
url: /it/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
È possibile trovare se i punti dati della serie si trovano nel secondo cerchio nel grafico *Torta di Torta* o nella barra del grafico *Barra di Torta* utilizzando Aspose.Cells. Si prega di utilizzare la proprietà [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) per determinarlo.

Si prega di scaricare il [file excel di esempio](5473373.xlsx) utilizzato nel codice di esempio seguente e vedere il suo output sulla console. Se si apre il [file excel di esempio](5473373.xlsx), si noterà che tutti i punti dati inferiori a 10 si trovano all'interno della barra del grafico *Barra di Torta* come mostrato anche dall'output sulla console.
## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**
Il seguente codice di esempio mostra come trovare se i punti dati sono nel secondo grafico a torta o a barre su un grafico *Torta di torte* o *Barra di torte*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Output della console**
Si prega di vedere l'output della console generato dopo l'esecuzione del codice di esempio sopra con il [file excel di esempio](5473373.xlsx). Se [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) è **falso**, il punto dati si trova all'interno della Torta oppure se è **vero**, allora il punto dati si trova all'interno della Barra.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
