---
title: Personalizzazione dei grafici
type: docs
weight: 15
url: /it/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **Creazione di grafici**

È possibile aggiungere una varietà di grafici ai fogli di calcolo con Aspose.Cells. Aspose.Cells fornisce molti oggetti grafici flessibili. In questo argomento vengono descritti gli oggetti grafici Aspose.Cells'.

###  **Semplicemente creando un grafico**

È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **Cose da sapere per creare un grafico**

Prima di creare grafici è importante comprendere alcuni concetti di base utili durante la creazione di grafici utilizzando Aspose.Cells.

####  **Oggetti grafici**

Aspose.Cells fornisce un set speciale di classi utilizzate per creare tutti i tipi di grafici. Queste classi vengono utilizzate per creare *oggetti grafici**, che fungono da elementi costitutivi del grafico. Gli oggetti grafici sono elencati di seguito:

- [**Asse**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), l'asse di un grafico.
- [**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un singolo grafico Excel.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), l'area del grafico nel foglio di lavoro.
- [**GraficoDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabella di dati del grafico.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), l'oggetto frame in un grafico.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un singolo punto in una serie in un grafico.
- [**Collezione ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una raccolta che contiene tutti i punti in una serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , una collezione di[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)oggetti.
-  DataLabels, DataLabels per quanto specificato[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Linea di tendenza**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), eccetera.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), riempi il formato per una forma.
- [**Pavimento**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)il pavimento di un grafico 3D.
- [**Leggenda**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la legenda del grafico.
- [**Linea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la linea del grafico.
- [**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , una collezione di[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)oggetti.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), rappresenta una singola serie di dati in un grafico.
- [**Etichette di spunta**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), le etichette dei segni di graduazione associati ai segni di graduazione sull'asse del grafico.
- [**Titolo**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), il titolo di un grafico o di un asse.
- [**Linea di tendenza**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una linea di tendenza in un grafico.
- [**Collezione Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una raccolta di tutti gli oggetti Trendline per la serie di dati specificata.
- [**Muri**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), le pareti di un grafico 3D.

####  **Utilizzo degli oggetti grafici**

Come accennato in precedenza, tutti gli oggetti grafici sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire attività specifiche. Utilizzare gli oggetti grafici per creare grafici.

 Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando il file[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) collezione. Ogni elemento in[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) la raccolta rappresenta a[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) oggetto. UN[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)L'oggetto incapsula tutti gli oggetti grafici necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni oggetti grafici di base per creare un grafico semplice.

###  **Creazione di un grafico semplice**

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione denominata[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). I tipi di grafico predefiniti sono:

|**Tipi di grafici**|**Descrizione**|
| :- | :- |
|Colonna|Rappresenta l'istogramma in cluster|
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
|ScatterConnectedByCurvesWithDataMarker|Rappresenta il grafico a dispersione collegato da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta il grafico a dispersione collegato da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta il grafico a dispersione collegato da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta il grafico a dispersione collegato da linee, senza indicatori di dati|
|La zona|Rappresenta il grafico ad area|
|AreaStacked|Rappresenta il grafico ad area in pila|
|Area100PercentImpilata|Rappresenta il grafico ad area in pila al 100%.|
|Area3D|Rappresenta il grafico ad area 3D|
|Area3DStacked|Rappresenta il grafico ad area in pila 3D|
|Area3D100PercentImpilata|Rappresenta il grafico ad area in pila 3D al 100%.|
|Ciambella|Rappresenta il grafico a ciambella|
|Ciambellaesploso|Rappresenta il grafico a ciambella esploso|
|Radar|Rappresenta la carta radar|
|RadarConDataMarkers|Rappresenta la carta radar con indicatori di dati|
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
|Barra cilindrica 100% impilata|Rappresenta un grafico a barre cilindriche in pila al 100%.|
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
Per creare un grafico utilizzando Aspose.Cells:

1. Aggiungi alcuni dati alle celle del foglio di lavoro con il comando[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) dell'oggetto[**valore impostato**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)metodo.
 Questo verrà utilizzato come origine dati per il grafico.
1.  Aggiungi un grafico al foglio di lavoro chiamando il file[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) collezione[*aggiungere*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ), incapsulato nel metodo[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)oggetto.
1.  Specificare il tipo di grafico con[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)enumerazione.
 Ad esempio, l'esempio utilizza il file[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)valore come tipo di grafico.
1.  Accedi al nuovo[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) oggetto da[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)collection passando il relativo indice.
1.  Utilizza uno qualsiasi degli oggetti grafici incapsulati nel file[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)oggetto per gestire il grafico.
 L'esempio seguente utilizza il file[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)oggetto grafico per specificare l'origine dati del grafico.

Quando si aggiungono dati di origine al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3") o una sequenza di celle non contigue (come "A1, A3, A5") o una sequenza di valori (come "1,2,3").

{{% alert color="primary" %}}

Quando assegni un intervallo di celle come origine dati, puoi impostare solo l'intervallo dall'alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti grafici per creare grafici diversi.

Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide come mostrato di seguito.

**Grafico a piramide con la relativa origine dati**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Per creare un grafico a bolle, il[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)deve essere impostato su[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)e alcune proprietà extra come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Dopo aver eseguito il codice seguente, un grafico a bolle viene aggiunto al foglio di lavoro come mostrato di seguito.

**Grafico a bolle con la relativa origine dati**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **Linea con grafico indicatore dati**

Per creare una linea con un grafico con indicatori di dati, il file[**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)deve essere impostato su[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) e alcune proprietà extra come l'area di sfondo, gli indicatori di serie, i valori e i valori XV devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunta una linea con un grafico con indicatori di dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **Creazione di grafici personalizzati**

Finora, quando abbiamo parlato dei grafici, abbiamo esaminato i grafici standard che hanno le loro impostazioni di formattazione standard. Definiamo solo l'origine dati, impostiamo alcune proprietà e il grafico viene creato con le sue impostazioni di formato predefinite. Ma Aspose.Cells supporta anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato.

###  **Creazione di grafici personalizzati**

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando Aspose.Cells semplice API.

 Un grafico è composto da una serie di dati. Ciascuna serie di dati in Aspose.Cells è rappresentata da a[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) oggetto mentre il[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) L'oggetto funge da raccolta di[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)oggetti. Quando creano un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati (raccolti in un file[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)oggetto).

{{% alert color="primary" %}}

 Attualmente Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, a linee, a colonne e in pila, ma nelle versioni future saranno supportati più grafici. Per un elenco completo dei grafici standard supportati da Aspose.Cells, leggere il[Tipi di grafici](/cells/it/java/chart-types/) articolo.

{{% /alert %}}

Il codice di esempio seguente mostra come creare grafici personalizzati. In questo esempio utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

**Grafico personalizzato che combina grafici a colonne e a linee**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_3.png)

**Esempio di programmazione**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Per visualizzare un elenco dei tipi di grafici supportati, leggere il[Tipi di grafici](/cells/it/java/chart-types/) articolo.

{{% /alert %}}

