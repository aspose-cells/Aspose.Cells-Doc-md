---
title: Personalizzazione dei grafici
type: docs
weight: 15
url: /it/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Creazione di grafici**

È possibile aggiungere una varietà di grafici ai fogli elettronici con Aspose.Cells. Aspose.Cells fornisce molti oggetti flessibili per la creazione dei grafici. Questo argomento discute gli oggetti per la creazione dei grafici di Aspose.Cells.

### **Creazione semplice di un grafico**

È semplice creare un grafico con Aspose.Cells con i seguenti esempi di codice:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Cose da sapere per la creazione di un grafico**

Prima di creare i grafici è importante capire alcuni concetti di base che sono utili quando si creano grafici usando Aspose.Cells.

#### **Oggetti per la creazione dei grafici**

Aspose.Cells fornisce un set speciale di classi utilizzate per creare tutti i tipi di grafici. Queste classi sono utilizzate per creare **oggetti di creazione di grafici**, che agiscono come blocchi di costruzione del grafico. Gli oggetti di creazione di grafici sono elencati di seguito:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), un asse di un grafico.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), un singolo grafico di Excel.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), l'area del grafico nel foglio di lavoro.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), una tabella di dati del grafico.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), l'oggetto frame in un grafico.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), un singolo punto in una serie in un grafico.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), una collezione che contiene tutti i punti in una serie.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), una collezione di [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) oggetti.
- DataLabels, Etichette dati per il [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) specificato, [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), ecc.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), formato di riempimento per una forma.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), il pavimento di un grafico 3D.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), la leggenda del grafico.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), la linea del grafico.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), una collezione di [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) oggetti.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), rappresenta una singola serie di dati in un grafico.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), le etichette dei segni di spunta associate ai segni di spunta su un asse del grafico.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), il titolo di un grafico o asse.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), una linea di tendenza in un grafico.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), una collezione di tutti gli oggetti Trendline per la serie di dati specificata.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), le pareti di un grafico 3D.

#### **Utilizzo di oggetti di tracciamento**

Come già detto, tutti gli oggetti di tracciamento sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire compiti specifici. Utilizzare gli oggetti di tracciamento per creare grafici.

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando la raccolta [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection). Ogni elemento nella raccolta [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) rappresenta un oggetto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart). Un oggetto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) racchiude tutti gli oggetti di creazione di grafici necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni oggetti di creazione di grafici di base per creare un grafico semplice.

### **Creazione di un grafico semplice**

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione chiamata [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). I tipi di grafico predefiniti sono:

|**Tipi di grafico**|**Descrizione**|
| :- | :- |
|Column|Rappresenta il grafico a colonne raggruppate|
|ColumnStacked|Rappresenta il grafico a colonne sovrapposte|
|Column100PercentStacked|Rappresenta il grafico a colonne sovrapposte al 100%|
|Column3DClustered|Rappresenta il grafico a colonne raggruppate in 3D|
|Column3DStacked|Rappresenta il grafico a colonne sovrapposte in 3D|
|Column3D100PercentStacked|Rappresenta il grafico a colonne sovrapposte al 100% in 3D|
|Column3D|Rappresenta il grafico a colonne 3D|
|Bar|Rappresenta il grafico a barre raggruppate|
|BarStacked|Rappresenta il grafico a barre sovrapposte|
|Bar100PercentStacked|Rappresenta il grafico a barre sovrapposte al 100%|
|Bar3DClustered|Rappresenta il grafico a barre raggruppate 3D|
|Bar3DStacked|Rappresenta il grafico a barre sovrapposte 3D|
|Bar3D100PercentStacked|Rappresenta il grafico a barre sovrapposte al 100% 3D|
|Line|Rappresenta il grafico a linee|
|LineStacked|Rappresenta il grafico a linee sovrapposte|
|Line100PercentStacked|Rappresenta il grafico a linee sovrapposte al 100%|
|LineWithDataMarkers|Rappresenta il grafico a linee con marcatori di dati|
|LineStackedWithDataMarkers|Rappresenta il grafico a linee sovrapposte con marcatori di dati|
|Line100PercentStackedWithDataMarkers|Rappresenta il grafico a linee sovrapposte al 100% con marcatori di dati|
|Line3D|Rappresenta il grafico a linee 3D|
|Pie|Rappresenta il grafico a torta|
|Pie3D|Rappresenta il grafico a torta 3D|
|PiePie|Rappresenta il grafico a torta delle torte|
|PieExploded|Rappresenta il grafico a torta esplosa|
|Pie3DExploded|Rappresenta il grafico a torta 3D esplosa|
|PieBar|Rappresenta il grafico a barre delle torte|
|Scatter|Rappresenta il grafico a dispersione|
|ScatterConnectedByCurvesWithDataMarker|Rappresenta il grafico a dispersione connesso da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta il grafico a dispersione connesso da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta il grafico a dispersione connesso da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta il grafico a dispersione connesso da linee, senza indicatori di dati|
|Area|Rappresenta un grafico ad aree|
|AreaStacked|Rappresenta un grafico ad aree sovrapposte|
|Area100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte|
|Area3D|Rappresenta un grafico ad aree 3D|
|Area3DStacked|Rappresenta un grafico ad aree sovrapposte 3D|
|Area3D100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte 3D|
|Doughnut|Rappresenta un grafico a ciambella|
|DoughnutExploded|Rappresenta un grafico a ciambella esplosa|
|Radar|Rappresenta il grafico radar|
|RadarWithDataMarkers|Rappresenta il grafico radar con marcatori dati|
|RadarFilled|Rappresenta un grafico radar riempito|
|Surface3D|Rappresenta un grafico a superficie 3D|
|SurfaceWireframe3D|Rappresenta il grafico a superficie 3D a filo|
|SurfaceContour|Rappresenta un grafico a contorni|
|SurfaceContourWireframe|Rappresenta un grafico a contorni in filo|
|Bubble|Rappresenta il grafico a bolle|
|Bubble3D|Rappresenta il grafico a bolle in 3D|
|Cylinder|Rappresenta il grafico a cilindro|
|CylinderStacked|Rappresenta il grafico a cilindro sovrapposto|
|Cylinder100PercentStacked|Rappresenta il grafico a cilindro sovrapposto al 100%|
|CylindricalBar|Rappresenta il grafico a barre cilindriche|
|CylindricalBarStacked|Rappresenta il grafico a barre cilindriche impilato|
|CylindricalBar100PercentStacked|Rappresenta il grafico a barre cilindriche 100% impilato|
|CylindricalColumn3D|Rappresenta il grafico a colonne cilindriche 3D|
|Cone|Rappresenta il grafico a cono|
|ConeStacked|Rappresenta il grafico a cono sovrapposto|
|Cone100PercentStacked|Rappresenta il grafico a cono sovrapposto al 100%|
|ConicalBar|Rappresenta il grafico a barre coniche|
|ConicalBarStacked|Rappresenta il grafico a barre coniche sovrapposte|
|ConicalBar100PercentStacked|Rappresenta il grafico a barre coniche sovrapposte al 100%|
|ConicalColumn3D|Rappresenta il grafico a colonne coniche in 3D|
|Pyramid|Rappresenta il grafico a piramide|
|PyramidStacked|Rappresenta il grafico a piramide sovrapposta|
|Pyramid100PercentStacked|Rappresenta il grafico a piramide sovrapposta al 100%|
|PyramidBar|Rappresenta un grafico a barre piramidali|
|PyramidBarStacked|Rappresenta il grafico a barre a piramide sovrapposte
|PyramidBar100PercentStacked|Rappresenta il grafico a barre a piramide 100% sovrapposte
|PyramidColumn3D|Rappresenta il grafico a colonne a piramide 3D
Per creare un grafico utilizzando Aspose.Cells:

1. Aggiungi alcuni dati alle celle del foglio di lavoro con il metodo [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) dell'oggetto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).
   Questo sarà utilizzato come origine dati per il grafico.
1. Aggiungi un grafico al foglio di lavoro chiamando il metodo [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-) della collezione [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), racchiuso nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Specifica il tipo di grafico con l'enumerazione [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).
   Ad esempio, l'esempio utilizza il valore [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) come tipo di grafico.
1. Accedi al nuovo oggetto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) dalla raccolta [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) passando il suo indice.
1. Usa uno qualsiasi degli oggetti di grafici incapsulati nell'oggetto [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) per gestire il grafico.
   L'esempio sotto utilizza l'oggetto di grafici [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) per specificare l'origine dati del grafico.

Quando si aggiunge una fonte dati al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3"), o una sequenza di celle non contigue (come "A1, A3, A5"), o una sequenza di valori (come "1,2,3").

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come fonte dati, è possibile impostare l'intervallo solo dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" è non valido.

{{% /alert %}}

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti di grafici per creare grafici diversi.

Quando il codice di esempio viene eseguito, viene aggiunto un grafico piramidale al foglio di lavoro come mostrato di seguito.

**Grafico piramidale con la sua fonte dati**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Per creare un grafico a bolle, l'oggetto di creazione grafici [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) deve essere impostato su [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE) e alcune proprietà aggiuntive come BubbleSizes, Values & XValues devono essere impostate di conseguenza. Dopo l'esecuzione del seguente codice, viene aggiunto un grafico a bolle al foglio di lavoro come mostrato di seguito.

**Grafico a bolle con la sua fonte dati**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Grafico a linee con marcatori di dati**

Per creare un grafico a linee con marcatori di dati, l'oggetto [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) deve essere impostato su [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS) e alcune proprietà aggiuntive come area di sfondo, marcatori di serie, valori & XValues devono essere impostate di conseguenza. Dopo l'esecuzione del seguente codice, viene aggiunto un grafico a linee con marcatori di dati al foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Creazione di grafici personalizzati**

Finora, quando abbiamo parlato di grafici, abbiamo esaminato grafici standard che hanno le loro impostazioni di formattazione standard. Definiamo solo la fonte dati, impostiamo alcune proprietà e il grafico viene creato con le impostazioni di formato predefinite. Ma Aspose.Cells supporta anche la creazione di grafici personalizzati che consente agli sviluppatori di creare grafici con le proprie impostazioni di formato.

### **Creazione di grafici personalizzati**

Gli sviluppatori possono creare grafici personalizzati in fase di esecuzione utilizzando la semplice API di Aspose.Cells.

Un grafico è composto da una serie di dati. Ogni serie di dati in Aspose.Cells è rappresentata da un oggetto [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) mentre l'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) funge da collezione di [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) oggetti. Quando si crea un grafico personalizzato, gli sviluppatori hanno la libertà di utilizzare diversi tipi di grafici per serie di dati diverse (raccolte in un oggetto [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)).

{{% alert color="primary" %}}

Attualmente Aspose.Cells supporta solo grafici personalizzati che combinano grafici a torta, a linee, a colonne e a pila di colonne, ma ulteriori grafici saranno supportati nelle future versioni. Per un elenco completo dei grafici standard supportati da Aspose.Cells, leggere l'articolo [Tipi di grafico](/cells/it/java/chart-types/).

{{% /alert %}}

Il codice di esempio di seguito dimostra come creare grafici personalizzati. In questo esempio, utilizzeremo un grafico a colonne per la prima serie di dati e un grafico a linee per la seconda serie. Il risultato è che aggiungiamo un grafico a colonne, combinato con un grafico a linee, al foglio di lavoro.

**Grafico personalizzato che combina grafici a colonne e a linee**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Esempio di programmazione**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Per vedere un elenco dei tipi di grafico supportati, leggere l'articolo [Tipi di grafico](/cells/it/java/chart-types/).

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
