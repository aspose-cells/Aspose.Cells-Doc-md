---
title: Formattazione del grafico
type: docs
weight: 20
url: /it/java/chart-formatting/
---
## **Impostazione dell'aspetto del grafico**

 In[Tipi di grafici](/cells/it/java/chart-types/), abbiamo fornito una breve introduzione ai tipi di grafici e oggetti grafici offerti da Aspose.Cells.

In questo articolo, discutiamo come personalizzare l'aspetto dei grafici impostando una serie di proprietà diverse:

- [Impostazione dell'area del grafico](/cells/it/java/chart-formatting/#setting-chart-area).
- [Impostazione delle linee del grafico](/cells/it/java/chart-formatting/#setting-chart-lines).
- [Applicazione di temi](/cells/it/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Impostazione di titoli su grafici e assi](/cells/it/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Lavorare con le linee della griglia](/cells/it/java/chart-formatting/#setting-major-gridlines).
- [Impostazione dei bordi per le pareti posteriori e laterali](/cells/it/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Impostazione dell'area del grafico**

Esistono diversi tipi di aree in un grafico e Aspose.Cells offre la flessibilità di modificare l'aspetto di ciascuna area. Gli sviluppatori possono applicare diverse impostazioni di formattazione su un'area modificandone il colore di primo piano, il colore di sfondo e il formato di riempimento, ecc.

Nell'esempio fornito di seguito, abbiamo applicato diverse impostazioni di formattazione su diversi tipi di aree di un grafico. Queste aree includono:

- Area del grafico
- Zona cartografica
- [**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) la zona
- L'area di un singolo punto in an[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Dopo aver eseguito il codice di esempio, un istogramma verrà aggiunto al foglio di lavoro come mostrato di seguito:

**Un istogramma con aree piene** 

![cose da fare:immagine_alt_testo](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Impostazione delle linee del grafico**

 Gli sviluppatori possono anche applicare diversi tipi di stili alle linee o agli indicatori di dati del file[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)come mostrato di seguito nell'esempio. L'esecuzione del codice di esempio aggiunge un istogramma al foglio di lavoro come mostrato di seguito:

**Istogramma dopo l'applicazione degli stili di linea** 

![cose da fare:immagine_alt_testo](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Applicazione di temi Microsoft Excel 2007/2010 ai grafici**

Gli sviluppatori possono applicare diversi temi e colori di Excel Microsoft al file[**SerieCollezione**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)o altri oggetti cartografici come mostrato nell'esempio seguente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Impostazione dei titoli dei grafici o degli assi**

È possibile utilizzare Microsoft Excel per impostare i titoli di un grafico e i suoi assi in un ambiente WYSIWYG come mostrato di seguito.

**Impostazione dei titoli di un grafico e dei suoi assi utilizzando Microsoft Excel** 

![cose da fare:immagine_alt_testo](chart-formatting_3.png)

 Aspose.Cells consente inoltre agli sviluppatori di impostare i titoli di un grafico e i suoi assi in fase di esecuzione. Tutti i grafici e i relativi assi contengono a[**Titolo.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)metodo che può essere utilizzato per impostare i loro titoli come mostrato di seguito in un esempio. Dopo aver eseguito il codice di esempio, un istogramma verrà aggiunto al foglio di lavoro come mostrato di seguito:

**Istogramma dopo aver impostato i titoli** 

![cose da fare:immagine_alt_testo](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Impostazione delle principali linee della griglia**

#### **Nascondere le principali linee della griglia**

 Gli sviluppatori possono controllare la visibilità delle principali griglie utilizzando il[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) metodo del[**Linea**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)oggetto. Dopo aver nascosto le linee della griglia principali, un istogramma aggiunto al foglio di lavoro ha il seguente aspetto:

**Un istogramma con griglie principali nascoste** 

![cose da fare:immagine_alt_testo](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Modifica delle impostazioni della griglia principale**

Gli sviluppatori non possono solo controllare la visibilità delle principali griglie, ma anche altre proprietà, incluso il colore, ecc. Dopo aver impostato il colore delle principali griglie, un istogramma aggiunto al foglio di lavoro avrà il seguente aspetto:

**Istogramma con griglia principale colorata** 

![cose da fare:immagine_alt_testo](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Impostazione dei bordi per le pareti posteriori e laterali**

 Dal rilascio di Microsoft Excel 2007, le pareti di un grafico 3D sono state divise in due parti: parete laterale e parete posteriore, quindi dobbiamo utilizzare due[**Muri**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) oggetti per rappresentarli separatamente ed è possibile accedervi utilizzando[**Grafico.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) e[**Grafico.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

L'esempio fornito di seguito mostra come impostare il bordo del fianco utilizzando diversi attributi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Modificare la posizione e le dimensioni del grafico**

 A volte, si desidera modificare la posizione o le dimensioni del grafico nuovo o esistente all'interno del foglio di lavoro. Aspose.Cells fornisce il[**Grafico.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)proprietà per raggiungere questo obiettivo. Puoi utilizzare le sue proprietà secondarie per ridimensionare il grafico con new**altezza** e**larghezza** o riposizionarlo con new** X** e**Coordinate Y**.

### **Modifica della posizione e delle dimensioni del grafico**

Per modificare la posizione (coordinate X, Y) e le dimensioni (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [**Grafico.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Grafico.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Grafico.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Grafico.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

L'esempio seguente spiega l'utilizzo delle proprietà precedenti. Carica la cartella di lavoro esistente che contiene un grafico nel suo primo foglio di lavoro. Quindi ridimensiona e riposiziona il grafico e salva la cartella di lavoro.

Prima dell'esecuzione del codice di esempio, il file sorgente ha questo aspetto:

**Dimensioni e posizione del grafico prima dell'esecuzione del codice di esempio** 

![cose da fare:immagine_alt_testo](chart-formatting_7.png)

Dopo l'esecuzione, il file di output si presenta così:

**Dimensioni e posizione del grafico dopo l'esecuzione del codice di esempio** 

![cose da fare:immagine_alt_testo](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipolazione di grafici Designer**

C'è un momento in cui potrebbe essere necessario manipolare o modificare i grafici nei file modello del designer. Aspose.Cells supporta pienamente la manipolazione dei grafici dei designer con i suoi contenuti ed elementi. I dati, i contenuti del grafico, l'immagine di sfondo e la formattazione possono essere preservati con precisione.

### **Manipolazione dei grafici Designer nei file modello**

 Per manipolare i grafici del designer in un file modello, utilizzare tutte le chiamate API relative al grafico. Ad esempio, usa[**Foglio di lavoro.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) property per ottenere la raccolta di grafici esistente nel file modello.

#### **Creazione di un grafico**

L'esempio seguente mostra come creare un grafico a torta. Manipoleremo questo grafico in seguito. Il seguente output è generato dal codice.

**Il grafico a torta di input** 

![cose da fare:immagine_alt_testo](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipolazione del grafico**

L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio modifichiamo il grafico creato sopra. Il seguente output è generato dal codice. Si noti che il colore del titolo del grafico è cambiato da blu a nero e "England 30000" è stato modificato in "United Kingdom, 30K".

**Il grafico a torta è stato modificato** 

![cose da fare:immagine_alt_testo](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipolazione di un grafico a linee nel modello Designer**

In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e cambieremo i loro colori di linea.

Innanzitutto, dai un'occhiata al grafico a linee del designer.

**Il grafico a linee di input** 

![cose da fare:immagine_alt_testo](chart-formatting_11.png)

 Ora manipoliamo il grafico a linee (che è contenuto nel file**grafico a linee.xls** file) utilizzando il seguente codice. Il seguente output è generato dal codice.

**Il grafico a linee manipolato** 

![cose da fare:immagine_alt_testo](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Utilizzo di sparkline**

Microsoft Excel 2010 può analizzare le informazioni in più modi che mai. Consente agli utenti di tracciare ed evidenziare importanti tendenze dei dati con nuovi strumenti di analisi e visualizzazione dei dati. I grafici sparkline sono mini-grafici che puoi posizionare all'interno delle celle in modo da poter visualizzare i dati e il grafico sulla stessa tabella. Quando i grafici sparkline vengono utilizzati correttamente, l'analisi dei dati è più rapida e mirata. Forniscono anche una semplice visualizzazione delle informazioni, evitando fogli di lavoro sovraffollati con molti grafici occupati.

Aspose.Cells fornisce un API per la manipolazione dei grafici sparkline nei fogli di calcolo.

### **Sparkline in Microsoft Excel**

Per inserire sparkline in Microsoft Excel 2010:

1. Seleziona le celle in cui vuoi che appaiano i grafici sparkline. Per facilitarne la visualizzazione, seleziona le celle a lato dei dati.
1.  Clic**Inserire** sul nastro e poi scegli**colonna** nel**Sparkline** gruppo.

![cose da fare:immagine_alt_testo](chart-formatting_13.png)

1. Seleziona o immetti l'intervallo di celle nel foglio di lavoro che contiene i dati di origine.
 Vengono visualizzati i grafici.

Gli sparkline ti aiutano a vedere le tendenze, ad esempio, o il record di vittorie o sconfitte per un campionato di softball. Gli sparkline possono anche riassumere l'intera stagione di ogni squadra del campionato.

![cose da fare:immagine_alt_testo](chart-formatting_14.png)

### **Sparkline utilizzando Aspose.Cells**

Gli sviluppatori possono creare, eliminare o leggere sparkline (nel file modello) utilizzando API fornito da Aspose.Cells. Aggiungendo grafici personalizzati per un determinato intervallo di dati, gli sviluppatori hanno la libertà di aggiungere diversi tipi di piccoli grafici alle aree delle celle selezionate.

L'esempio seguente mostra la funzionalità Sparkline. L'esempio mostra come:

1. Apri un semplice file modello.
1. Leggi le informazioni sugli sparkline per un foglio di lavoro.
1. Aggiungi nuovi grafici sparkline per un determinato intervallo di dati a un'area della cella.
1. Salva il file Excel su disco.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Applicazione del formato 3D al grafico**

Potresti aver bisogno di stili di grafici 3D in modo da poter ottenere solo i risultati per il tuo scenario. Le API Aspose.Cells forniscono il API pertinente per applicare la formattazione 3D di Excel 2007 Microsoft, come illustrato in questo articolo.

### **Impostazione del formato 3D sulla carta**

Di seguito viene fornito un esempio completo per dimostrare come creare un grafico e applicare la formattazione 3D di Excel 2007 Microsoft. Dopo aver eseguito il codice di esempio precedente, un istogramma (con effetti 3D) verrà aggiunto al foglio di lavoro come mostrato di seguito.

**Un istogramma con formattazione 3D**

![cose da fare:immagine_alt_testo](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 Per un elenco completo dei grafici 2D e 3D supportati, vedere[Tipi di grafici supportati per il rendering](/cells/it/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Argomenti avanzati**
- [Imposta l'immagine come sfondo Compila il grafico](/cells/it/java/set-picture-as-background-fill-in-the-chart/)
