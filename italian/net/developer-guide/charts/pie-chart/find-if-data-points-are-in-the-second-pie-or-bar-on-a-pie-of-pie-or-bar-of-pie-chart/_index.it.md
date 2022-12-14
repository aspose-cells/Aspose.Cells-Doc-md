---
title: Scopri se i punti dati si trovano nella seconda torta o barra su un grafico a torta o a barre
type: docs
weight: 180
url: /it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Possibili scenari di utilizzo**
 Puoi scoprire se i punti dati della serie si trovano nella seconda torta*Torta di torta* grafico o nella barra di*Bar di torta* grafico utilizzando Aspose.Cells. Si prega di utilizzare il[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)proprietà per determinarlo.

 Si prega di scaricare il[file excel di esempio](5115193.xlsx) usato nel codice di esempio seguente e vedere il relativo output della console. Se apri il file[file excel di esempio](5115193.xlsx) , scoprirai che tutti i punti dati inferiori a 10 si trovano all'interno della barra di*Bar di torta*grafico come mostrato anche dall'output della console.
## **Scopri se i punti dati si trovano nella seconda torta o barra su un grafico a torta o a barre**
 Il codice di esempio seguente mostra come trovare se i punti dati si trovano nella seconda torta o barra su a*Torta di torta* o*Bar di torta*grafico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Uscita console**
 Si prega di vedere il seguente output della console generato dopo l'esecuzione del codice di esempio precedente con il file[file excel di esempio](5115193.xlsx) . Se[IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) è**falso** , il punto dati si trova all'interno della torta o se lo è**VERO**, il punto dati si trova all'interno della barra.



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
