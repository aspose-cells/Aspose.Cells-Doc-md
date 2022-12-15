---
title: Personalizzazione dei grafici
type: docs
weight: 15
url: /it/java/creating-and-customizing-charts/
---
## **Creazione di grafici**

È possibile aggiungere una varietà di grafici ai fogli di calcolo con Aspose.Cells. Aspose.Cells fornisce molti oggetti grafici flessibili. Questo argomento tratta gli oggetti grafici Aspose.Cells'.

### **Semplicemente creando un grafico**

È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Cose da sapere per creare un grafico**

Prima di creare grafici è importante comprendere alcuni concetti di base utili durante la creazione di grafici utilizzando Aspose.Cells.

#### **Oggetti grafici**

 Aspose.Cells fornisce un insieme speciale di classi utilizzate per creare tutti i tipi di grafici. Queste classi sono utilizzate per creare**oggetti grafici**, che fungono da elementi costitutivi del grafico. Gli oggetti grafici sono elencati di seguito:

- [**Asse**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), l'asse di un grafico.
- [**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un singolo grafico di Excel.
- [**Area Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), l'area del grafico nel foglio di lavoro.
- [**GraficoDatiTabella**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabella di dati del grafico.
- [**GraficoFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), l'oggetto frame in un grafico.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un singolo punto in una serie in un grafico.
- [**RaccoltaChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una raccolta che contiene tutti i punti di una serie.
- [**Raccolta di grafici**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , una collezione di[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)oggetti.
-  DataLabels, DataLabels per l'oggetto specificato[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Linea di tendenza**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), eccetera.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), riempire il formato per una forma.
- [**Pavimento**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), il pavimento di un grafico 3D.
- [**Leggenda**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la legenda del grafico.
- [**Linea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la linea del grafico.
- [**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , una collezione di[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)oggetti.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), rappresenta una singola serie di dati in un grafico.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), le etichette dei segni di graduazione associate ai segni di graduazione su un asse del grafico.
- [**Titolo**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), il titolo di un grafico o di un asse.
- [**Linea di tendenza**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una linea di tendenza in un grafico.
- [**Collezione Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una raccolta di tutti gli oggetti Trendline per la serie di dati specificata.
- [**Muri**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), le pareti di un grafico 3D.

#### **Utilizzo di oggetti grafici**

Come accennato in precedenza, tutti gli oggetti grafici sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire attività specifiche. Usa gli oggetti grafici per creare grafici.

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando il file[**Raccolta di grafici**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) collezione. Ogni elemento del[**Raccolta di grafici**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) collezione rappresenta a[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) oggetto. UN[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)object incapsula tutti gli oggetti grafici necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni oggetti grafici di base per creare un grafico semplice.

### **Creazione di un grafico semplice**

 È possibile creare diversi tipi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione denominata[**Tipo di grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). I tipi di grafico predefiniti sono:

|**Tipi di grafici**|**Descrizione**|
|:- |:- |
|Colonna|Rappresenta l'istogramma a colonne raggruppate|
|ColonnaImpilato|Rappresenta il grafico a colonne in pila|
|Column100PercentStacked|Rappresenta il grafico a colonne in pila al 100%.|
|Column3DClustered|Rappresenta il grafico a colonne in cluster 3D|
|Column3DStacked|Rappresenta il grafico a colonne in pila 3D|
|Column3D100Percent Stacked|Rappresenta il grafico a colonne in pila 100% 3D|
|Colonna 3D|Rappresenta il grafico a colonne 3D|
|Sbarra|Rappresenta il grafico a barre in cluster|
|Bar Stacked|Rappresenta il grafico a barre in pila|
|Bar100Percent Stacked|Rappresenta il grafico a barre in pila al 100%.|
|Bar3DClustered|Rappresenta il grafico a barre in cluster 3D|
|Bar3DSimpilato|Rappresenta il grafico a barre in pila 3D|
|Bar3D100Percent Stacked|Rappresenta il grafico a barre in pila 3D al 100%.|
|Linea|Rappresenta il grafico a linee|
|LineImpilato|Rappresenta il grafico a linee in pila|
|Riga100Percent Stacked|Rappresenta il grafico a linee in pila al 100%.|
|LineWithDataMarkers|Rappresenta il grafico a linee con indicatori di dati|
|LineStackedWithDataMarkers|Rappresenta il grafico a linee in pila con indicatori di dati|
|Line100PercentStackedWithDataMarkers|Rappresenta il grafico a linee in pila al 100% con indicatori di dati|
|Linea3D|Rappresenta il grafico a linee 3D|
|Torta|Rappresenta il grafico a torta|
|Pie3D|Rappresenta il grafico a torta 3D|
|PiePie|Rappresenta la torta del grafico a torta|
|Torta Esplosa|Rappresenta il grafico a torta esploso|
|Pie3DEsploso|Rappresenta il grafico a torta esploso 3D|
|PieBar|Rappresenta la barra del grafico a torta|
|Disperdere|Rappresenta il grafico a dispersione|
|ScatterConnectedByCurvesWithDataMarker|Rappresenta il grafico a dispersione collegato da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta il grafico a dispersione collegato da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta il grafico a dispersione collegato da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta il grafico a dispersione collegato da linee, senza indicatori di dati|
|La zona|Rappresenta il grafico ad area|
|Area Stacked|Rappresenta il grafico ad area in pila|
|Area100Percent Stacked|Rappresenta il grafico ad area in pila al 100%.|
|Area3D|Rappresenta il grafico ad area 3D|
|Area3DSimpilato|Rappresenta il grafico ad area in pila 3D|
|Area3D100Percentuale impilata|Rappresenta il grafico ad area in pila 3D al 100%.|
|Ciambella|Rappresenta il grafico a ciambella|
|Ciambella Esploso|Rappresenta il grafico ad anello esploso|
|Radar|Rappresenta il grafico radar|
|RadarConMarcatoriDati|Rappresenta il grafico a radar con indicatori di dati|
|RadarRiempito|Rappresenta il grafico radar riempito|
|Superficie3D|Rappresenta il grafico a superficie 3D|
|SuperficieWireframe3D|Rappresenta il grafico a superficie 3D Wireframe|
|SuperficieContorno|Rappresenta il grafico di contorno|
|SuperficieContornoWireframe|Rappresenta il grafico di contorno Wireframe|
|Bolla|Rappresenta il grafico a bolle|
|Bolla3D|Rappresenta il grafico a bolle 3D|
|Cilindro|Rappresenta il grafico a cilindro|
|CilindroImpilato|Rappresenta il grafico a cilindri in pila|
|Cilindro impilato al 100%.|Rappresenta il grafico a cilindri impilati al 100%.|
|Barra cilindrica|Rappresenta il grafico a barre cilindrico.|
|Barra Cilindrica Impilata|Rappresenta il grafico a barre cilindrico in pila|
|Barra cilindrica100% impilata|Rappresenta il grafico a barre cilindrico in pila al 100%.|
|Colonna cilindrica 3D|Rappresenta il grafico a colonne cilindriche 3D|
|Cono|Rappresenta il grafico a cono|
|ConoImpilato|Rappresenta il grafico a cono in pila|
|Cono100Percent Stacked|Rappresenta il grafico a cono impilato al 100%.|
|Barra conica|Rappresenta il grafico a barre conico|
|ConicalBarImpilato|Rappresenta il grafico a barre coniche in pila|
|ConicalBar100PercentStacked|Rappresenta il grafico a barre coniche in pila al 100%.|
|Colonna conica 3D|Rappresenta il grafico a colonne coniche 3D|
|Piramide|Rappresenta il grafico a piramide|
|Piramide Impilata|Rappresenta il grafico a piramide in pila|
|Pyramid100Percent Stacked|Rappresenta il grafico a piramide in pila al 100%.|
|PyramidBar|Rappresenta il grafico a barre della piramide|
|PyramidBar Impilato|Rappresenta il grafico a barre a piramide impilata|
|PyramidBar100Percent Stacked|Rappresenta il grafico a barre a piramide in pila al 100%.|
|Piramide Colonna 3D|Rappresenta il grafico a colonne della piramide 3D|
Per creare un grafico utilizzando Aspose.Cells:

1.  Aggiungi alcuni dati alle celle del foglio di lavoro con il[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) dell'oggetto[**valore impostato**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)metodo.
 Questo verrà utilizzato come origine dati per il grafico.
1.  Aggiungere un grafico al foglio di lavoro chiamando il metodo[**Raccolta di grafici**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) della collezione[*Inserisci*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) metodo, incapsulato nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)oggetto.
1.  Specificare il tipo di grafico con il[**Tipo di grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)enumerazione.
 Ad esempio, l'esempio utilizza il[**TipoGrafico.PIRAMIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)value come tipo di grafico.
1.  Accedi al nuovo[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) oggetto dal[**Raccolta di grafici**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)raccolta passandone l'indice.
1.  Utilizzare uno qualsiasi degli oggetti grafici incapsulati nel file[**Grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)oggetto per gestire il grafico.
 L'esempio seguente utilizza il[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)grafico per specificare l'origine dati del grafico.

Quando si aggiungono dati di origine al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3") o una sequenza di celle non contigue (come "A1, A3, A5") o una sequenza di valori (come "1,2,3").

{{% alert color="primary" %}}

Quando assegni un intervallo di celle come origine dati, puoi impostare solo l'intervallo da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizzare diversi oggetti grafici per creare grafici diversi.

Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide come mostrato di seguito.

**Grafico a piramide con la relativa origine dati**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Per creare un grafico a bolle, il[**Tipo di grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)deve essere impostato su[**TipoGrafico.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)e alcune proprietà extra come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunto un grafico a bolle come mostrato di seguito.

**Grafico a bolle con la relativa origine dati**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Linea con grafico indicatore di dati**

Per creare una linea con un grafico indicatore di dati, il[**Tipo di grafico**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)deve essere impostato su[**Tipo di grafico.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) e alcune proprietà extra come l'area di sfondo, gli indicatori di serie, i valori e i valori XV devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunta una riga con un grafico di marcatori di dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Creazione di grafici personalizzati**

Finora, quando abbiamo discusso dei grafici, abbiamo esaminato i grafici standard che hanno le loro impostazioni di formattazione standard. Definiamo solo l'origine dati, impostiamo alcune proprietà e il grafico viene creato con le impostazioni di formato predefinite. Ma Aspose.Cells supporta anche la creazione di grafici personalizzati che consentono agli sviluppatori di creare grafici con le proprie impostazioni di formato.

### **Creazione di grafici personalizzati**

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando la semplice API Aspose.Cells.

 Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da a[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) oggetto mentre il[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) oggetto funge da raccolta di[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)oggetti. Durante la creazione di un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per diverse serie di dati (raccolte in un file[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)oggetto).

{{% alert color="primary" %}}

 Attualmente Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, a linee, a colonne e in pila di colonne, ma nelle versioni future saranno supportati più grafici. Per un elenco completo dei grafici standard supportati da Aspose.Cells, leggere il file[Tipi di grafici](/cells/it/java/chart-types/) articolo.

{{% /alert %}}

Il codice di esempio riportato di seguito mostra come creare grafici personalizzati. In questo esempio, utilizzeremo un istogramma per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un istogramma, combinato con un grafico a linee, al foglio di lavoro.

**Grafico personalizzato che combina grafici a colonne e a linee**

![cose da fare:immagine_alt_testo](creating-and-customizing-charts_3.png)

**Esempio di programmazione**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Per visualizzare un elenco dei tipi di grafici supportati, leggi il file[Tipi di grafici](/cells/it/java/chart-types/) articolo.

{{% /alert %}}

