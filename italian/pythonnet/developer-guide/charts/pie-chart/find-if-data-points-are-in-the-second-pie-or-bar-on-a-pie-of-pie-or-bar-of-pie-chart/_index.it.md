---
title: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
description: Impara come usare Aspose.Cells per Python via .NET per scoprire se i punti dati sono nel secondo grafico a torta o barra di un grafico a torta di torte o bar di torte. La nostra guida dimostrerà come identificare e accedere alla torta secondaria o alla barra secondaria, permettendoti di analizzare e manipolare efficacemente i dati.
keywords: Aspose.Cells per Python via .NET, Grafico a torta di torta, Grafico a barre di torta, Torta secondaria, Barra secondaria, Analisi dati, Manipolazione dei dati.
type: docs
weight: 180
url: /it/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi verificare se i punti dati della serie sono nella seconda torta su *Pie of Pie* o nella barra di *Bar of Pie* usando Aspose.Cells per Python via .NET. Usa la proprietà [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) per determinarlo.

Si prega di scaricare il [file excel di esempio](5115193.xlsx) utilizzato nel seguente codice di esempio e vedere il suo output sulla console. Se si apre il [file excel di esempio](5115193.xlsx), si noterà che tutti i punti dati inferiori a 10 sono all'interno del grafico a barre di *Grafico a Barre di Torta* come mostrato anche dall'output sulla console.

## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**
Il seguente codice di esempio mostra come trovare se i punti dati sono nel secondo grafico a torta o a barre su un grafico *Torta di torte* o *Barra di torte*.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Output della console**
Vedi il seguente output della console generato dopo l'esecuzione del codice di esempio con il [file Excel di esempio](5115193.xlsx). Se [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) è **falso**, il punto dati si trova all’interno della Torta; se è **vero**, il punto dati è all’interno della Barra.



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
{{< app/cells/assistant language="python-net" >}}
