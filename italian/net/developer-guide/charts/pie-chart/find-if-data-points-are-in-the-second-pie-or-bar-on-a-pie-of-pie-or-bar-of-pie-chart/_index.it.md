---
title: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
description: Scopri come utilizzare Aspose.Cells for .NET per scoprire se i punti dati si trovano sulla seconda torta o barra su una torta di torta o barra di torta grafico. La nostra guida dimostrerà come identificare e accedere alla torta o barra secondaria su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
keywords: Aspose.Cells for .NET, Grafico a Torta di Torta, Grafico a Barre di Torta, Grafico Secondario a Torta, Grafico Secondario a Barre, Analisi dei Dati, Manipolazione dei Dati.
type: docs
weight: 180
url: /it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi scoprire se i punti dati di una serie sono nel secondo grafico a torta o nel grafico a barre usando Aspose.Cells. Si prega di utilizzare la proprietà [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) per determinarlo.

Si prega di scaricare il [file excel di esempio](5115193.xlsx) utilizzato nel seguente codice di esempio e vedere il suo output sulla console. Se si apre il [file excel di esempio](5115193.xlsx), si noterà che tutti i punti dati inferiori a 10 sono all'interno del grafico a barre di *Grafico a Barre di Torta* come mostrato anche dall'output sulla console.
## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**
Il seguente codice di esempio mostra come trovare se i punti dati sono nel secondo grafico a torta o a barre su un grafico *Torta di torte* o *Barra di torte*.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Output della console**
Si prega di vedere l'output della console generato dopo l'esecuzione del codice di esempio sopra con il [file excel di esempio](5115193.xlsx). Se [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) è **false**, il punto dati è all'interno della torta oppure se è **true**, allora il punto dati è all'interno della barra.



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
