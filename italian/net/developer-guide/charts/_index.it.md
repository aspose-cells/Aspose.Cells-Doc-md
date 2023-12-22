---
title: Crea e gestisci grafico
description: Scopri come utilizzare Aspose.Cells for .NET per creare grafici in Microsoft Excel. La nostra guida mostrerà i diversi tipi di grafici che possono essere creati, nonché come personalizzarne l'aspetto e la formattazione.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Grafici
type: docs
weight: 130
url: /it/net/creating-charts/
description: Crea un grafico in CSharp per Excel e file ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

È possibile aggiungere una varietà di grafici ai fogli di calcolo con Aspose.Cells. Aspose.Cells fornisce molti oggetti grafici flessibili. In questo argomento vengono descritti gli oggetti grafici Aspose.Cells'.

{{% /alert %}}

##  **Creazione di grafici**

###  **Semplicemente creando un grafico**
È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **Cose da sapere per creare un grafico**

Prima di creare grafici è importante comprendere alcuni concetti di base utili durante la creazione di grafici utilizzando Aspose.Cells.

####  **Oggetti grafici**

 Aspose.Cells fornisce una serie speciale di classi nel file[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)spazio dei nomi utilizzato per creare i grafici supportati da Aspose.Cells. Queste classi vengono utilizzate per creare *oggetti grafici**, che fungono da elementi costitutivi del grafico. Gli oggetti grafici sono elencati di seguito:

- Serie, una singola serie di dati in un grafico.
- Axis, l'asse di un grafico.
- Grafico, un singolo grafico Excel.
- ChartArea, l'area del grafico nel foglio di lavoro.
- ChartDataTable, una tabella di dati del grafico.
- ChartFrame, l'oggetto frame in un grafico.
- ChartPoint, un singolo punto in una serie in un grafico.
- ChartPointCollection, una raccolta che contiene tutti i punti in una serie.
- Grafici, una raccolta di oggetti Chart.
- DataLabels, una raccolta di tutti gli oggetti DataLabel per la serie specificata.
- FillFormat, formato di riempimento per una forma.
- Floor, il pavimento di un grafico 3D.
- Legend, la legenda del grafico.
- Linea, la linea del grafico.
- SeriesCollection, una raccolta di oggetti Series.
- TickLabels, le etichette dei segni di graduazione associati ai segni di graduazione sull'asse del grafico.
- Titolo, il titolo di un grafico o di un asse.
- Trendline, una linea di tendenza in un grafico.
- TrendlineCollection, una raccolta di tutti gli oggetti Trendline per la serie di dati specificata.
- Muri, i muri di un grafico 3D.

####  **Utilizzo degli oggetti grafici**

Come accennato in precedenza, tutti gli oggetti grafici sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire attività specifiche. Utilizzare gli oggetti grafici per creare grafici.

 Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando il file[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collezione. Ogni elemento in[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) la raccolta rappresenta a[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oggetto. UN[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)L'oggetto incapsula tutti gli altri oggetti grafici necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni oggetti grafici di base per creare un grafico semplice.

###  **Crea grafico utilizzando Aspose.Cells**

**Passaggi:**

1. Aggiungi alcuni dati alle celle del foglio di lavoro con il comando[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) dell'oggetto[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metodo.
 Questo verrà utilizzato come origine dati per il grafico.
1.  Aggiungi un grafico al foglio di lavoro chiamando il file[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) collezione[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) metodo, incapsulato nel[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)oggetto.
1.  Specificare il tipo di grafico con[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)enumerazione.
 Ad esempio, l'esempio seguente utilizza il file[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)valore come tipo di grafico.
1.  Accedi al nuovo[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oggetto da[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)collection passando il relativo indice.
1.  Utilizza uno qualsiasi degli oggetti grafici incapsulati nel file[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)oggetto per gestire il grafico.
 L'esempio seguente utilizza il file[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)oggetto grafico per specificare l'origine dati del grafico.

Quando si aggiungono dati di origine al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3") o una sequenza di celle non contigue (come "A1, A3, A5") o una sequenza di valori (come "1,2,3").

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti grafici per creare grafici diversi.

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione denominata[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

I tipi di grafico predefiniti sono:

|**Tipi di grafici**|**Descrizione**|
| :- | :- |
|Colonna|Rappresenta un istogramma in cluster|
|Colonna in pila|Rappresenta un grafico a colonne in pila|
|Colonna100PercentImpilata|Rappresenta un grafico a colonne in pila al 100%.|
|Colonna3DCraggruppata|Rappresenta un istogramma a colonne raggruppate 3D|
|Colonna3DStacked|Rappresenta un grafico a colonne in pila 3D|
|Colonna3D100PercentImpilata|Rappresenta un grafico a colonne in pila 3D al 100%.|
|Colonna3D|Rappresenta il grafico a colonne 3D|
|Sbarra|Rappresenta il grafico a barre cluster|
|Bar Stacked|Rappresenta il grafico a barre in pila|
|Bar100PercentImpilato|Rappresenta il grafico a barre in pila al 100%.|
|Bar3DClustered|Rappresenta il grafico a barre raggruppate 3D|
|Bar3DStacked|Rappresenta il grafico a barre in pila 3D|
|Bar3D100PercentImpilato|Rappresenta il grafico a barre in pila 3D al 100%.|
|Linea|Rappresenta il grafico a linee|
|LineStacked|Rappresenta il grafico a linee in pila|
|Linea 100% in pila|Rappresenta il grafico a linee in pila al 100%.|
|LineaConMarcatoriDati|Rappresenta il grafico a linee con indicatori di dati|
|LineStackedWithDataMarkers|Rappresenta un grafico a linee in pila con indicatori di dati|
|Line100PercentStackedWithDataMarkers|Rappresenta un grafico a linee in pila al 100% con indicatori di dati|
|Linea3D|Rappresenta il grafico a linee 3D|
|Torta|Rappresenta il grafico a torta|
|Torta3D|Rappresenta il grafico a torta 3D|
|PiePie|Rappresenta il grafico a torta o a torta|
|TortaEsplosa|Rappresenta il grafico a torta esploso|
|Pie3DEsploso|Rappresenta il grafico a torta esploso 3D|
|PieBar|Rappresenta la barra del grafico a torta|
|Dispersione|Rappresenta il grafico a dispersione|
|ScatterConnectedByCurvesWithDataMarker|Rappresenta un grafico a dispersione collegato da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta un grafico a dispersione collegato da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da linee, senza indicatori di dati|
|La zona|Rappresenta il grafico ad area|
|AreaStacked|Rappresenta il grafico ad area in pila|
|Area100PercentImpilata|Rappresenta il grafico ad area in pila al 100%.|
|Area3D|Rappresenta il grafico ad area 3D|
|Area3DStacked|Rappresenta il grafico ad area in pila 3D|
|Area3D100PercentImpilata|Rappresenta il grafico ad area in pila 3D al 100%.|
|Ciambella|Rappresenta il grafico a ciambella|
|Ciambellaesploso|Rappresenta il grafico a ciambella esploso|
|Radar|Rappresenta il grafico radar|
|RadarConDataMarkers|Rappresenta un grafico radar con indicatori di dati|
|Radarriempito|Rappresenta il grafico radar riempito|
|Superficie3D|Rappresenta il grafico di superficie 3D|
|SuperficieWireframe3D|Rappresenta il grafico di superficie 3D Wireframe|
|Contornosuperficie|Rappresenta il diagramma di contorno|
|SurfaceContourWireframe|Rappresenta il diagramma di contorno del wireframe|
|Bolla|Rappresenta il grafico a bolle|
|Bubble3D|Rappresenta il grafico a bolle 3D|
|Cilindro|Rappresenta il grafico del cilindro|
|Cilindro impilato|Rappresenta il grafico dei cilindri in pila|
|Cilindro100%impilato|Rappresenta il grafico dei cilindri in pila al 100%.|
|Barra cilindrica|Rappresenta un grafico a barre cilindriche.|
|Barra cilindrica impilata|Rappresenta un grafico a barre cilindriche in pila|
|Barra cilindrica100%impilato|Rappresenta un grafico a barre cilindriche in pila al 100%.|
|Colonna cilindrica3D|Rappresenta un grafico a colonne cilindriche 3D|
|Cono|Rappresenta il grafico a cono|
|Cono Stacked|Rappresenta il grafico a cono in pila|
|Cono100%impilato|Rappresenta il grafico a cono impilato al 100%.|
|ConicalBar|Rappresenta il grafico a barre coniche|
|ConicalBarStacked|Rappresenta il grafico a barre coniche in pila|
|ConicalBar100PercentStacked|Rappresenta il grafico a barre coniche in pila al 100%.|
|Colonna conica3D|Rappresenta un istogramma conico 3D|
|Piramide|Rappresenta il grafico piramidale|
|PyramidStacked|Rappresenta il grafico a piramide in pila|
|Piramide100%Impilato|Rappresenta il grafico a piramide in pila al 100%.|
|PyramidBar|Rappresenta il grafico a barre piramidale|
|PyramidBarStacked|Rappresenta il grafico a barre piramidali in pila|
|PyramidBar100PercentStacked|Rappresenta il grafico a barre piramidali in pila al 100%.|
|PiramideColonna3D|Rappresenta il grafico a colonne piramidale 3D|
{{% alert color="primary" %}}

Quando assegni un intervallo di celle come origine dati, puoi impostare solo l'intervallo dall'alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

####  **Grafico piramidale**

Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **Grafico a linee**

 Nell'esempio sopra, semplicemente cambiando il file[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) A*Linea*crea un grafico a linee. La fonte completa è fornita di seguito. quando il codice viene eseguito, al foglio di lavoro viene aggiunto un grafico a linee.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **Grafico a bolle**

 Per creare un grafico a bolle, il[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) deve essere impostato su[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)e alcune proprietà extra come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunto un grafico a bolle.

####  **Linea con grafico indicatore dati**

 Per creare una linea con il grafico degli indicatori di dati,[**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)deve essere impostato su*ChartType.LineWithDataMarkers*alcune proprietà extra come l'area di sfondo, gli indicatori di serie, i valori e i valori XV devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunta una linea con il grafico degli indicatori di dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **Argomenti avanzati**
- [Leggere e manipolare grafici Excel 2016](/cells/it/net/read-and-manipulate-excel-2016-charts/)
- [Gestisci gli assi dei grafici Excel](/cells/it/net/chart-axes/)
- [Impostazione dell'aspetto della carta](/cells/it/net/setting-chart-appearance/)
- [Tipi di grafici](/cells/it/net/chart-types/)
- [Personalizzazione dei grafici](/cells/it/net/customizing-charts/)
- [Imposta l'origine dati per il grafico](/cells/it/net/data-formatting-in-charts/)
- [Gestisci DataLabel dei grafici Excel](/cells/it/net/insert-datalabels-to-chart/)
- [Genera grafico elaborando gli indicatori intelligenti](/cells/it/net/generate-chart-by-processing-smart-markers/)
- [Ottieni il foglio di lavoro del grafico](/cells/it/net/get-worksheet-of-the-chart/)
- [Gestisci la legenda dei grafici Excel](/cells/it/net/chart-legend/)
- [Manipolare le dimensioni della posizione e il grafico del designer](/cells/it/net/manipulate-position-size-and-designer-chart/)
- [Creazione di un grafico a torta con linee guida](/cells/it/net/creating-pie-chart-with-leader-lines/)
- [Forme nei grafici](/cells/it/net/controls-in-charts/)
- [Gestisci i titoli dei grafici Excel](/cells/it/net/chart-and-axis-titles/)
- [Rappresentazione del grafico](/cells/it/net/chart-rendering/)
- [Ottieni il testo dell'equazione della linea di tendenza del grafico](/cells/it/net/get-equation-text-of-chart-trendline/)
