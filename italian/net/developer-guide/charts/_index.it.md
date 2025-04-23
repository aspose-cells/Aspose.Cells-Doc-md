---
title: Creare e gestire il grafico
description: Scopri come usare Aspose.Cells for .NET per creare grafici in Microsoft Excel. La nostra guida dimostrerà i diversi tipi di grafici che possono essere creati, così come come personalizzarne l aspetto e la formattazione.
keywords: Aspose.Cells for .NET, Creazione del grafico, Microsoft Excel, Tipi di grafici, Personalizzazione, Aspetto, Formattazione.
linktitle: Grafici
type: docs
weight: 130
url: /it/net/creating-charts/
description: Creare un grafico in CSharp per file Excel e ODS.
keywords: creare un grafico, fare un grafico 
---

{{% alert color="primary" %}}

È possibile aggiungere una varietà di grafici ai fogli elettronici con Aspose.Cells. Aspose.Cells fornisce molti oggetti flessibili per la creazione dei grafici. Questo argomento discute gli oggetti per la creazione dei grafici di Aspose.Cells.

{{% /alert %}}

## **Creazione di grafici**

### **Creazione semplice di un grafico**
È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Cose da sapere per creare un grafico**

Prima di creare i grafici è importante capire alcuni concetti di base che sono utili quando si creano grafici usando Aspose.Cells.

#### **Oggetti per la creazione dei grafici**

Aspose.Cells fornisce un insieme speciale di classi nello spazio dei nomi [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) usate per creare i grafici supportati da Aspose.Cells. Queste classi sono usate per creare **oggetti per la creazione dei grafici**, che agiscono come componenti fondamentali per la creazione del grafico. Gli oggetti per la creazione dei grafici sono elencati di seguito:

- Serie, una singola serie di dati in un grafico.
- Asse, l'asse di un grafico.
- Grafico, un singolo grafico di Excel.
- Area del grafico, l'area del grafico nel foglio di lavoro.
- ChartDataTable, una tabella dati del grafico.
- ChartFrame, l'oggetto frame in un grafico.
- ChartPoint, un singolo punto in una serie in un grafico.
- ChartPointCollection, una raccolta che contiene tutti i punti di una serie.
- Grafici, una collezione di oggetti Chart.
- DataLabels, una collezione di tutti gli oggetti DataLabel per la serie specificata.
- FillFormat, formato di riempimento per una forma.
- Pavimento, il pavimento di un grafico 3D.
- Legenda, la legenda del grafico.
- Linea, la linea del grafico.
- SeriesCollection, una collezione di oggetti Series.
- TickLabels, le etichette contrassegnate associate ai contrassegni su un asse del grafico.
- Titolo, il titolo di un grafico o asse.
- Linea di tendenza, una linea di tendenza in un grafico.
- TrendlineCollection, una collezione di tutti gli oggetti Linea di tendenza per la serie di dati specificata.
- Pareti, le pareti di un grafico 3D.

#### **Utilizzo di oggetti di tracciamento**

Come già detto, tutti gli oggetti di tracciamento sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire compiti specifici. Utilizzare gli oggetti di tracciamento per creare grafici.

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando la collezione [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts). Ogni elemento nella collezione [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) rappresenta un oggetto [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart). Un oggetto [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) racchiude tutti gli altri oggetti di tracciamento necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni semplici oggetti di tracciamento per creare un grafico semplice.

### **Crea un grafico utilizzando Aspose.Cells**

**Passaggi:**

1. Aggiungi alcuni dati alle celle del foglio di lavoro con il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) dell'oggetto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Questo sarà utilizzato come origine dati per il grafico.
1. Aggiungi un grafico al foglio di lavoro chiamando il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) della raccolta [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection), incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
1. Specifica il tipo di grafico con l'enumerazione [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).
   Ad esempio, l'esempio sotto usa il valore [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) come tipo di grafico.
1. Accedi al nuovo oggetto [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) dalla raccolta [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) passando il suo indice.
1. Usa uno qualsiasi degli oggetti di grafici incapsulati nell'oggetto [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) per gestire il grafico.
   L'esempio sotto utilizza l'oggetto di grafici [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) per specificare l'origine dati del grafico.

Quando si aggiunge una fonte dati al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3"), o una sequenza di celle non contigue (come "A1, A3, A5"), o una sequenza di valori (come "1,2,3").

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizza diversi oggetti di grafici per creare grafici diversi.

È possibile creare molti tipi diversi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione chiamata [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

I tipi di grafico predefiniti sono:

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
|ScatterConnectedByCurvesWithDataMarker|Rappresenta un grafico a dispersione collegato da curve, con indicatori di dati|
|ScatterConnectedByCurvesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da curve, senza indicatori di dati|
|ScatterConnectedByLinesWithDataMarker|Rappresenta un grafico a dispersione collegato da linee, con indicatori di dati|
|ScatterConnectedByLinesWithoutDataMarker|Rappresenta un grafico a dispersione collegato da linee, senza indicatori di dati|
|Area|Rappresenta un grafico ad aree|
|AreaStacked|Rappresenta un grafico ad aree sovrapposte|
|Area100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte|
|Area3D|Rappresenta un grafico ad aree 3D|
|Area3DStacked|Rappresenta un grafico ad aree sovrapposte 3D|
|Area3D100PercentStacked|Rappresenta un grafico ad aree 100% sovrapposte 3D|
|Doughnut|Rappresenta un grafico a ciambella|
|DoughnutExploded|Rappresenta un grafico a ciambella esplosa|
|Radar|Rappresenta un grafico radar|
|RadarWithDataMarkers|Rappresenta un grafico radar con indicatori di dati|
|RadarFilled|Rappresenta un grafico radar riempito|
|Surface3D|Rappresenta un grafico a superficie 3D|
|SurfaceWireframe3D|Rappresenta un grafico a superficie in filo 3D|
|SurfaceContour|Rappresenta un grafico a contorni|
|SurfaceContourWireframe|Rappresenta un grafico a contorni in filo|
|Bubble|Rappresenta il grafico a bolle|
|Bubble3D|Rappresenta il grafico a bolle in 3D|
|Cylinder|Rappresenta il grafico a cilindro|
|CylinderStacked|Rappresenta il grafico a cilindro sovrapposto|
|Cylinder100PercentStacked|Rappresenta il grafico a cilindro sovrapposto al 100%|
|CylindericalBar|Rappresenta il grafico a barre cilindriche|
|CylindericalBarStacked|Rappresenta il grafico a barre cilindriche sovrapposte|
|CylindericalBar100PercentStacked|Rappresenta il grafico a barre cilindriche sovrapposte al 100%|
|CylindericalColumn3D|Rappresenta il grafico a colonne cilindriche in 3D|
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
|PyramidBar|Rappresenta il grafico a barre piramidali|
|PyramidBarStacked|Rappresenta il grafico a barre a piramide sovrapposte
|PyramidBar100PercentStacked|Rappresenta il grafico a barre a piramide 100% sovrapposte
|PyramidColumn3D|Rappresenta il grafico a colonne a piramide 3D
{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, è possibile impostare solo l'intervallo da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

#### **Grafico a piramide**

Quando il codice di esempio viene eseguito, viene aggiunto un grafico a piramide al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Grafico a linee**

Nell'esempio precedente, semplicemente cambiando il [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) in *Line* si crea un grafico a linee. La fonte completa è fornita di seguito. Quando il codice viene eseguito, viene aggiunto un grafico a linee al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Grafico a bolle**

Per creare un grafico a bolle, il [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) deve essere impostato su [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) e alcune proprietà aggiuntive come BubbleSizes, Values & XValues devono essere impostate di conseguenza. Dopo aver eseguito il seguente codice, viene aggiunto un grafico a bolle al foglio di lavoro.

#### **Grafico a linee con marcatori di dati**

Per creare un grafico a linee con marcatori di dati, [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) deve essere impostato su *ChartType.LineWithDataMarkers* e alcune proprietà aggiuntive come area di sfondo, marcatori di serie, valori & XValues devono essere impostate di conseguenza. Dopo aver eseguito il seguente codice, viene aggiunto un grafico a linee con marcatori di dati al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Argomenti avanzati**
- [Lettura e manipolazione dei grafici di Excel 2016](/cells/it/net/read-and-manipulate-excel-2016-charts/)
- [Gestisci gli assi dei grafici di Excel](/cells/it/net/chart-axes/)
- [Impostazione dell'aspetto del grafico](/cells/it/net/setting-chart-appearance/)
- [Tipi di Grafico](/cells/it/net/chart-types/)
- [Personalizzazione di Grafici](/cells/it/net/customizing-charts/)
- [Imposta origine dati per il grafico](/cells/it/net/data-formatting-in-charts/)
- [Gestisci le etichette dati dei grafici di Excel](/cells/it/net/insert-datalabels-to-chart/)
- [Genera grafico mediante l'elaborazione di marcatori smart](/cells/it/net/generate-chart-by-processing-smart-markers/)
- [Ottieni il foglio di lavoro del grafico](/cells/it/net/get-worksheet-of-the-chart/)
- [Gestisci la leggenda dei grafici di Excel](/cells/it/net/chart-legend/)
- [Manipolare posizione, dimensione e progettazione del grafico](/cells/it/net/manipulate-position-size-and-designer-chart/)
- [Creazione di un grafico a torta con linee guida](/cells/it/net/creating-pie-chart-with-leader-lines/)
- [Forme nei grafici](/cells/it/net/controls-in-charts/)
- [Gestire i titoli dei grafici di Excel](/cells/it/net/chart-and-axis-titles/)
- [Rendering del grafico](/cells/it/net/chart-rendering/)
- [Ottieni il testo dell'equazione della retta di tendenza del grafico](/cells/it/net/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="csharp" >}}
