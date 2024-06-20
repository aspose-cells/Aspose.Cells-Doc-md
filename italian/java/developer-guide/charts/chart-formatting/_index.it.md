---
title: Formattazione del Grafico
type: docs
weight: 20
url: /it/java/chart-formatting/
---

## **Impostazione dell'aspetto del grafico**

In [Tipi di grafici](/cells/it/java/chart-types/), abbiamo dato una breve introduzione ai tipi di grafici e oggetti per la creazione di grafici offerti da Aspose.Cells.

In questo articolo, discutiamo come personalizzare l'aspetto dei grafici impostando diversi tipi di proprietà:

- [Impostare l'area del grafico](/cells/it/java/chart-formatting/#setting-chart-area).
- [Impostare le linee del grafico](/cells/it/java/chart-formatting/#setting-chart-lines).
- [Applicazione dei temi](/cells/it/java/formato-grafico/#applicazione-dei-temi-microsoft-excel-20072010-ai-grafici).
- [Impostazione dei titoli per grafici e assi](/cells/it/java/formato-grafico/#impostazione-dei-titoli-dei-grafici-o-degli-assi).
- [Lavorare con le linee di griglia](/cells/it/java/formato-grafico/#impostazione-delle-linee-di-griglia-principali).
- [Impostazione dei bordi per le pareti posteriori e laterali](/cells/it/java/formato-grafico/#impostazione-dei-bordi-per-le-pareti-posteriori-e-laterali).

### **Impostazione dell'Area del Grafico**

Ci sono diversi tipi di aree in un grafico e Aspose.Cells fornisce la flessibilità di modificare l'aspetto di ciascuna area. Gli sviluppatori possono applicare diverse impostazioni di formattazione su un'area cambiando il suo colore principale, colore di sfondo e formato di riempimento, ecc.

Nell'esempio di seguito, abbiamo applicato diverse impostazioni di formattazione su diversi tipi di aree di un grafico. Queste aree includono:

- Area del tracciato
- Area del grafico
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) area
- L'area di un singolo punto in un [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito:

**Un grafico a colonne con aree riempite** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Impostazione delle Linee del Grafico**

Gli sviluppatori possono anche applicare diversi tipi di stili alle linee o ai marker dei dati del [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) come mostrato di seguito nell'esempio. Eseguendo il codice di esempio verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito:

**Grafico a colonne dopo l'applicazione degli stili delle linee** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Applicazione dei Temi Microsoft Excel 2007/2010 ai Grafici**

Gli sviluppatori possono applicare diversi temi e colori di Microsoft Excel al [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) o ad altri oggetti del grafico come mostrato nell'esempio qui sotto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Impostare i Titoli dei Grafici o degli Assi**

Puoi usare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG come mostrato di seguito.

**Impostazione titoli di un grafico & dei suoi assi utilizzando Microsoft Excel** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells consente anche ai sviluppatori di impostare i titoli di un grafico e dei suoi assi durante l'esecuzione. Tutti i grafici e i loro assi contengono un metodo [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) che può essere utilizzato per impostare i propri titoli, come mostrato di seguito in un esempio. Dopo aver eseguito il codice di esempio, verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito:

**Grafico a colonne dopo l'impostazione dei titoli** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Impostazione delle linee principali della griglia**

#### **Nascondere le linee di griglia principali**

I sviluppatori possono controllare la visibilità delle linee principali della griglia utilizzando il metodo [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) dell'oggetto [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line). Dopo aver nascosto le linee principali della griglia, un grafico a colonne aggiunto al foglio di lavoro avrà l'aspetto seguente:

**Un grafico a colonne con linee principali della griglia nascoste** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Modifica delle impostazioni delle linee di griglia principali**

I sviluppatori possono non solo controllare la visibilità delle linee principali della griglia ma anche altre proprietà, incluso il colore. Dopo aver impostato il colore delle linee principali della griglia, un grafico a colonne aggiunto al foglio di lavoro avrà l'aspetto seguente:

**Grafico a colonne con linee principali della griglia colorate** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Impostazione dei bordi per il retro e i lati del grafico**

Dal rilascio di Microsoft Excel 2007, le pareti di un grafico 3D sono state divise in due parti: parete laterale e parete posteriore, quindi dobbiamo usare due oggetti [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) per rappresentarli separatamente e è possibile accedervi utilizzando [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) e [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

L'esempio riportato di seguito mostra come impostare il bordo della parete laterale utilizzando attributi diversi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Cambia la posizione e le dimensioni del grafico**

A volte, è necessario modificare la posizione o le dimensioni del grafico nuovo o esistente all'interno del foglio di lavoro. Aspose.Cells fornisce la proprietà [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) per raggiungere questo obiettivo. È possibile utilizzare le sue sotto-proprietà per ridimensionare il grafico con nuove **altezza** e **larghezza** o riposizionarlo con nuove coordinate **X** e **Y**.

### **Modifica della posizione e delle dimensioni del grafico**

Per cambiare la posizione (coordinate X, Y) e le dimensioni (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

L'esempio seguente spiega l'uso delle proprietà sopra. Carica il foglio di lavoro esistente che contiene un grafico nel suo primo foglio. Poi ridimensiona, riposiziona il grafico e salva il foglio di lavoro.

Prima dell'esecuzione del codice di esempio, il file sorgente appare così:

**Dimensioni e posizione del grafico prima dell'esecuzione del codice di esempio** 

![todo:image_alt_text](chart-formatting_7.png)

Dopo l'esecuzione, il file di output appare così:

**Dimensioni e posizione del grafico dopo l'esecuzione del codice di esempio** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipolazione dei Grafici del Designer**

Ci sarà un momento in cui potresti avere bisogno di manipolare o modificare i grafici nei file di modello del tuo designer. Aspose.Cells supporta pienamente la manipolazione dei grafici di progettazione con i suoi contenuti ed elementi. I dati, i contenuti dei grafici, l'immagine di sfondo e la formattazione possono essere preservati con precisione.

### **Manipolazione dei grafici di progettazione nei file di modello**

Per manipolare i grafici di progettazione in un file di modello, utilizzare tutte le chiamate API relative ai grafici. Ad esempio, utilizzare la proprietà [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) per ottenere la raccolta di grafici esistenti nel file di modello.

#### **Creazione di un Grafico**

Nell'esempio seguente viene mostrato come creare un grafico a torta. Manipoleremo questo grafico in seguito. L'output seguente è generato dal codice.

**Il grafico a torta di input** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipolazione del Grafico**

Nell'esempio seguente viene mostrato come manipolare il grafico esistente. In questo esempio modifichiamo il grafico creato in precedenza. L'output seguente è generato dal codice. Si noti che il colore del titolo del grafico è cambiato da blu a nero e 'Inghilterra 30000' è stato modificato in 'Regno Unito, 30K'.

**Il grafico a torta è stato modificato** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipolazione di un Grafico a Linee nel Modello del Designer**

In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.

Per prima cosa, dai un'occhiata al grafico a linee di progettazione.

**Il grafico a linee di input** 

![todo:image_alt_text](chart-formatting_11.png)

Ora manipoliamo il grafico a linee (contenuto nel file **linechart.xls**) utilizzando il seguente codice. Il seguente output è generato dal codice.

**Il grafico a linee manipolato** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Utilizzo delle Sparklines**

Microsoft Excel 2010 può analizzare le informazioni in modi più variati che mai. Consente agli utenti di monitorare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. Le Sparklines sono mini-grafici che è possibile inserire all'interno delle celle, in modo da poter visualizzare dati e grafici sulla stessa tabella. Quando le sparklines vengono utilizzate correttamente, l'analisi dei dati è più rapida e diretta. Forniscono inoltre una visione semplice delle informazioni, evitando fogli di lavoro affollati con molti grafici elaborati.

Aspose.Cells fornisce un'API per manipolare le sparklines nei fogli di calcolo.

### **Le Sparklines in Microsoft Excel**

Per inserire sparklines in Microsoft Excel 2010:

1. Selezionare le celle in cui si desidera che compaiano le sparklines. Per renderle facili da visualizzare, selezionare le celle a lato dei dati.
1. Fare clic su **Inserisci** nella barra multifunzione e quindi scegliere **colonna** nel gruppo **Sparklines**.

![todo:image_alt_text](chart-formatting_13.png)

1. Selezionare o inserire l'intervallo di celle nel foglio di lavoro che contiene i dati di origine.
   I grafici appaiono.

Le Sparklines ti aiutano a vedere le tendenze, ad esempio, o il record di vittorie o sconfitte per una lega di softball. Le Sparklines possono persino riassumere l'intera stagione di ciascuna squadra nella lega.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines utilizzando Aspose.Cells**

I programmatori possono creare, eliminare o leggere sparklines (nel file modello) utilizzando l'API fornita da Aspose.Cells. Aggiungendo grafici personalizzati per un determinato intervallo di dati, i programmatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree di celle selezionate.

L'esempio di seguito mostra la funzione Sparklines. L'esempio mostra come:

1. Aprire un semplice file modello.
1. Leggere le informazioni delle sparklines per un foglio di lavoro.
1. Aggiungere nuove sparklines per un dato intervallo di dati in un'area di celle.
1. Salvare il file Excel su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Applicazione del formato 3D al grafico**

Potresti avere bisogno di stili di grafici 3D in modo da ottenere solo i risultati per il tuo scenario. Le API di Aspose.Cells forniscono l'API rilevante per applicare la formattazione 3D di Microsoft Excel 2007 come dimostrato in questo articolo.

### **Impostazione del formato 3D per il grafico**

Di seguito è riportato un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Microsoft Excel 2007. Dopo l'esecuzione del codice di esempio sopra, verrà aggiunto un diagramma a colonne (con effetti 3D) al foglio di lavoro come mostrato di seguito.

**Un grafico a colonne con formattazione 3D**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Per un elenco completo dei tipi di grafici 2D e 3D supportati, vedere [Tipi di grafici supportati per il rendering](/cells/it/java/chart-rendering/#supported-chart-types-for-rendering)

{{% /alert %}}

## **Argomenti avanzati**
- [Imposta l'immagine come riempimento di sfondo nel grafico](/cells/it/java/set-picture-as-background-fill-in-the-chart/)
