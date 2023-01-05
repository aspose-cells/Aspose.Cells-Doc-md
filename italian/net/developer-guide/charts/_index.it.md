---
title: Crea e gestisci grafico
linktitle: Grafici
type: docs
weight: 130
url: /it/net/creating-charts/
description: Crea un grafico in CSharp per i file Excel e ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

È possibile aggiungere una varietà di grafici ai fogli di calcolo con Aspose.Cells. Aspose.Cells fornisce molti oggetti grafici flessibili. Questo argomento tratta gli oggetti grafici Aspose.Cells'.

{{% /alert %}}

## **Creazione di grafici**

### **Semplicemente creando un grafico**
È semplice creare un grafico con Aspose.Cells con i seguenti codici di esempio:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Cose da sapere per la creazione di un grafico**

Prima di creare grafici è importante comprendere alcuni concetti di base utili durante la creazione di grafici utilizzando Aspose.Cells.

#### **Oggetti grafici**

Aspose.Cells fornisce una serie speciale di classi nel[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) spazio dei nomi utilizzato per creare i grafici supportati da Aspose.Cells. Queste classi vengono utilizzate per creare**oggetti grafici**, che fungono da elementi costitutivi del grafico. Gli oggetti grafici sono elencati di seguito:

- Serie, una singola serie di dati in un grafico.
- Axis, l'asse di un grafico.
- Grafico, un singolo grafico di Excel.
- ChartArea, l'area del grafico nel foglio di lavoro.
- ChartDataTable, una tabella di dati del grafico.
- ChartFrame, l'oggetto frame in un grafico.
- ChartPoint, un singolo punto in una serie in un grafico.
- ChartPointCollection, una raccolta che contiene tutti i punti in una serie.
- Grafici, una raccolta di oggetti grafici.
- DataLabels, una raccolta di tutti gli oggetti DataLabel per la serie specificata.
- FillFormat, riempie il formato per una forma.
- Floor, il pavimento di un grafico 3D.
- Legenda, la legenda del grafico.
- Linea, la linea del grafico.
- SeriesCollection, una raccolta di oggetti Series.
- TickLabels, le etichette dei segni di graduazione associate ai segni di graduazione su un asse del grafico.
- Titolo, il titolo di un grafico o di un asse.
- Trendline, una linea di tendenza in un grafico.
- TrendlineCollection, una raccolta di tutti gli oggetti Trendline per la serie di dati specificata.
- Muri, i muri di un grafico 3D.

#### **Utilizzo di oggetti grafici**

Come accennato in precedenza, tutti gli oggetti grafici sono istanze delle rispettive classi e forniscono proprietà e metodi specifici per eseguire attività specifiche. Usa gli oggetti grafici per creare grafici.

Aggiungi qualsiasi tipo di grafico a un foglio di lavoro utilizzando il file[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collezione. Ogni elemento del[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) collezione rappresenta a[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oggetto. UN[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)object incapsula tutti gli altri oggetti grafici necessari per personalizzare l'aspetto del grafico. La sezione successiva mostra come utilizzare alcuni oggetti grafici di base per creare un grafico semplice.

### **Crea grafico utilizzando Aspose.Cells**

**Passi:**

1.  Aggiungi alcuni dati alle celle del foglio di lavoro con il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) dell'oggetto[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)metodo.
 Questo verrà utilizzato come origine dati per il grafico.
1.  Aggiungere un grafico al foglio di lavoro chiamando il metodo[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) della collezione[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) metodo, incapsulato nel[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)oggetto.
1.  Specificare il tipo di grafico con il[**Tipo di grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)enumerazione.
 Ad esempio, l'esempio seguente utilizza il file[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)value come tipo di grafico.
1.  Accedi al nuovo[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) oggetto dal[**Grafici**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)raccolta passandone l'indice.
1.  Utilizzare uno qualsiasi degli oggetti grafici incapsulati nel file[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)oggetto per gestire il grafico.
 L'esempio seguente utilizza il[**SerieCollezione**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)grafico per specificare l'origine dati del grafico.

Quando si aggiungono dati di origine al grafico, l'origine dati può essere un intervallo di celle (come "A1:C3") o una sequenza di celle non contigue (come "A1, A3, A5") o una sequenza di valori (come "1,2,3").

Questi passaggi generali ti consentono di creare qualsiasi tipo di grafico. Utilizzare diversi oggetti grafici per creare grafici diversi.

 È possibile creare diversi tipi di grafici con Aspose.Cells. Tutti i grafici standard supportati da Aspose.Cells sono predefiniti in un'enumerazione denominata[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

I tipi di grafico predefiniti sono:

|**Tipi di grafici**|**Descrizione**|
|:- |:- |
|Colonna|Rappresenta il grafico a colonne in cluster|
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
|RadarConMarcatoriDati|Rappresenta il grafico radar con marcatori di dati|
|RadarRiempito|Rappresenta il grafico radar riempito|
|Superficie3D|Rappresenta il grafico a superficie 3D|
|SuperficieWireframe3D|Rappresenta il grafico a superficie 3D wireframe|
|SuperficieContorno|Rappresenta il grafico di contorno|
|SuperficieContornoWireframe|Rappresenta il grafico di contorno Wireframe|
|Bolla|Rappresenta il grafico a bolle|
|Bolla3D|Rappresenta il grafico a bolle 3D|
|Cilindro|Rappresenta il grafico a cilindro|
|CilindroImpilato|Rappresenta il grafico a cilindri in pila|
|Cilindro impilato al 100%.|Rappresenta il grafico a cilindri impilati al 100%.|
|Barra Cilindrica|Rappresenta il grafico a barre cilindrico.|
|CylindericalBarStacked|Rappresenta il grafico a barre cilindrico in pila|
|CylindericalBar100Percent Stacked|Rappresenta il grafico a barre cilindrico in pila al 100%.|
|Colonna Cilindrica3D|Rappresenta il grafico a colonne cilindriche 3D|
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
|PyramidBar|Rappresenta il grafico a barre a piramide|
|PyramidBar Impilato|Rappresenta il grafico a barre a piramide impilata|
|PyramidBar100Percent Stacked|Rappresenta il grafico a barre a piramide in pila al 100%.|
|Piramide Colonna 3D|Rappresenta il grafico a colonne della piramide 3D|
{{% alert color="primary" %}}

Quando assegni un intervallo di celle come origine dati, puoi impostare solo l'intervallo da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido mentre "C3:A1" non è valido.

{{% /alert %}}

#### **Grafico a piramide**

Quando viene eseguito il codice di esempio, al foglio di lavoro viene aggiunto un grafico a piramide.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Grafico a linee**

 Nell'esempio sopra, semplicemente cambiando il file[**Tipo di grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) a*Linea*crea un grafico a linee. La fonte completa è fornita di seguito. quando il codice viene eseguito, al foglio di lavoro viene aggiunto un grafico a linee.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Grafico a bolle**

 Per creare un grafico a bolle, il[**Tipo di grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) deve essere impostato su[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)e alcune proprietà extra come BubbleSizes, Values e XValues devono essere impostate di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunto un grafico a bolle.

#### **Linea con grafico indicatore di dati**

 Per creare una linea con il grafico dell'indicatore di dati,[**Tipo di grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)deve essere impostato su*ChartType.LineWithDataMarkers*alcune proprietà extra come l'area di sfondo, gli indicatori di serie, i valori e i valori XV devono essere impostati di conseguenza. Dopo aver eseguito il codice seguente, al foglio di lavoro viene aggiunta una riga con il grafico dell'indicatore di dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Argomenti avanzati**
- [Leggi e manipola i grafici di Excel 2016](/cells/it/net/read-and-manipulate-excel-2016-charts/)
- [Gestisci gli assi dei grafici di Excel](/cells/it/net/chart-axes/)
- [Impostazione dell'aspetto del grafico](/cells/it/net/setting-chart-appearance/)
- [Tipi di grafici](/cells/it/net/chart-types/)
- [Personalizzazione dei grafici](/cells/it/net/customizing-charts/)
- [Impostare l'origine dati per il grafico](/cells/it/net/data-formatting-in-charts/)
- [Gestisci le etichette dati dei grafici di Excel](/cells/it/net/insert-datalabels-to-chart/)
- [Genera grafico elaborando marcatori intelligenti](/cells/it/net/generate-chart-by-processing-smart-markers/)
- [Ottieni Foglio di lavoro del grafico](/cells/it/net/get-worksheet-of-the-chart/)
- [Gestisci la legenda dei grafici di Excel](/cells/it/net/chart-legend/)
- [Manipola la dimensione della posizione e il grafico del progettista](/cells/it/net/manipulate-position-size-and-designer-chart/)
- [Creazione di un grafico a torta con linee guida](/cells/it/net/creating-pie-chart-with-leader-lines/)
- [Forme nei grafici](/cells/it/net/controls-in-charts/)
- [Gestisci i titoli dei grafici di Excel](/cells/it/net/chart-and-axis-titles/)
- [Rappresentazione del grafico](/cells/it/net/chart-rendering/)
- [Ottieni il testo dell'equazione della linea di tendenza del grafico](/cells/it/net/get-equation-text-of-chart-trendline/)
