---
title: Trova se i punti dati si trovano nella seconda fetta del grafico a torta o nel bar del grafico a barre su un grafico a torta o a barre con Golang tramite C++
linktitle: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
description: Impara come usare Aspose.Cells for C++ per scoprire se i punti dati sono nella seconda fetta o barra di un grafico a torta di fetta o di barra. La nostra guida dimostrerà come identificare e accedere alla fetta o barra secondaria in un grafico composito, consentendoti di analizzare e manipolare efficacemente i dati.
keywords: Aspose.Cells for C++, Grafico Torta di Fetta, Barra di Fetta, Fetta Secondaria, Barra Secondaria, Analisi dei Dati, Manipolazione dei Dati.
type: docs
weight: 180
url: /it/go-cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi determinare se i punti dati di una serie sono nella seconda torta sul grafico *Pie of Pie* o nel bar del grafico *Bar of Pie* usando Aspose.Cells. Per favore usa la proprietà [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/go-cpp/chartpoint/isinsecondaryplot/) per determinarlo.

Si prega di scaricare il [file excel di esempio](5115193.xlsx) utilizzato nel seguente codice di esempio e vedere il suo output sulla console. Se si apre il [file excel di esempio](5115193.xlsx), si noterà che tutti i punti dati inferiori a 10 sono all'interno del grafico a barre di *Grafico a Barre di Torta* come mostrato anche dall'output sulla console.

## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**
Il seguente codice di esempio mostra come trovare se i punti dati sono nel secondo grafico a torta o a barre su un grafico *Torta di torte* o *Barra di torte*.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfDataPointsAreInTheSecondPieOrBarOnAPieOfPieOrBarOfPieChart.go" >}}
## **Output della console**
Guarda la seguente output sulla console generata dopo l'esecuzione del codice di esempio con il [file Excel di esempio](5115193.xlsx). Se [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) è **falso**, il punto dati è all'interno della torta, se è **vero**, allora il punto dati è all'interno della barra.

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
