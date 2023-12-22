---
title: Scopri se i punti dati si trovano nella seconda torta o nella barra di un grafico a torta o a barra della torta
description: Scopri come utilizzare Aspose.Cells for .NET per scoprire se i punti dati si trovano nella seconda torta o barra su una torta o barra di un grafico a torta. La nostra guida mostrerà come identificare e accedere alla torta o alla barra secondaria su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Possibili scenari di utilizzo**
 Puoi scoprire se i punti dati della serie si trovano nella seconda torta*Torta di torta* grafico o nella barra di*Barra di torta* grafico utilizzando Aspose.Cells. Si prega di utilizzare il[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)proprietà per determinarlo.

 Si prega di scaricare il[file Excel di esempio](5115193.xlsx)utilizzato nel codice di esempio seguente e visualizzarne l'output sulla console. Se apri il[file Excel di esempio](5115193.xlsx) , troverai che tutti i punti dati inferiori a 10 si trovano all'interno della barra di*Barra di torta*grafico come mostrato anche dall'output della console.
##  **Scopri se i punti dati si trovano nella seconda torta o nella barra di un grafico a torta o a barra della torta**
 Il codice di esempio seguente mostra come verificare se i punti dati si trovano nella seconda torta o barra su a*Torta di torta* O*Barra di torta*grafico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Uscita della console**
 Consulta il seguente output della console generato dopo l'esecuzione del codice di esempio riportato sopra con il file[file Excel di esempio](5115193.xlsx) . Se[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)è *false**, il punto dati è all'interno della torta o se è *true**, il punto dati è all'interno della barra.



{{< highlight "java" >}}

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
