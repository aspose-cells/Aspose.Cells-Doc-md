---
title: Modello di oggetto Aspose.Cells
type: docs
weight: 20
url: /it/python-net/aspose-cells-object-model/
---

{{% alert color="primary" %}}

Il modello di oggetto Aspose.Cells fornisce informazioni sulle relazioni strutturali tra gli oggetti della libreria di classi Aspose.Cells.

{{% /alert %}}

La struttura di livello superiore del modello di oggetto Aspose.Cells è mostrata di seguito in modo gerarchico.

|**Struttura di livello superiore del modello di oggetto Aspose.Cells**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Come si può vedere dalla figura precedente, la radice del modello di oggetto è l'oggetto Workbook. Una breve descrizione di alcuni degli oggetti è fornita di seguito a scopo introduttivo.

## **WorksheetCollection/Worksheet**

L'oggetto Workbook contiene la WorksheetCollection, che rappresenta la raccolta di tutti gli oggetti Worksheet in un foglio di calcolo, come mostrato di seguito:

|**Fogli di lavoro e oggetti fogli di lavoro**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Ogni oggetto foglio di lavoro contiene un oggetto Celle che rappresenta la collezione di tutte le celle in un foglio di lavoro come mostrato di seguito:

|**Celle e oggetti cella**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
È possibile utilizzare l'oggetto Cella per ottenere e impostare il valore, lo stile, la formula e altre proprietà di una singola cella.

## **ChartCollection/Chart**

L'oggetto Grafici rappresenta una collezione di tutti gli oggetti Grafico in un foglio di lavoro. Ogni oggetto Grafico è composto da diversi altri oggetti che lavorano insieme per creare e gestire i grafici. La struttura del grafico in Aspose.Cells è mostrata nel diagramma sottostante:

|**Modello di oggetto del grafico**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|

## **CommentCollection/Comment**

Ogni oggetto foglio di lavoro contiene anche un oggetto Commenti che rappresenta la collezione di tutti gli oggetti Commento in un foglio di lavoro come mostrato di seguito:

|**Commenti e oggetti commento**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Un oggetto Commento viene utilizzato per aggiungere un commento a una cella specificata nel foglio di lavoro.

## **HorizontalPageBreakCollection/HorizontalPageBreak**

Ogni oggetto foglio di lavoro contiene una Collezione interruzioni di pagina orizzontale che rappresenta una collezione di tutte le interruzioni di pagina orizzontale in un foglio di lavoro come mostrato di seguito:

|**InterruzioniPagina & Oggetti Interruzione di pagina**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Un oggetto Interruzione di pagina orizzontale viene utilizzato per creare un'interruzione di pagina orizzontale nel foglio di lavoro.

## **HyperlinkCollection/Hyperlink**

Un oggetto foglio di lavoro contiene anche una Collezione collegamenti ipertestuali che rappresenta una collezione di tutti gli oggetti collegamento ipertestuale nel foglio di lavoro come mostrato di seguito:

|**Collegamenti ipertestuali e oggetti collegamento ipertestuale**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Un oggetto Collegamento ipertestuale rappresenta un collegamento ipertestuale nel foglio di lavoro. Gli sviluppatori possono impostare l'indirizzo del collegamento ipertestuale e altre proprietà correlate utilizzando l'oggetto Collegamento ipertestuale.

## **PictureCollection/Picture**

Ciascun oggetto Worksheet contiene un oggetto PictureCollection che rappresenta una collezione di tutti gli oggetti Picture in un foglio di lavoro come mostrato di seguito:

|**Immagine e oggetti Immagine**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Un oggetto Picture rappresenta un'immagine nel foglio di lavoro. Utilizzando l'oggetto Picture, gli sviluppatori possono non solo aggiungere immagini nei propri fogli di lavoro ma anche posizionare queste immagini in qualsiasi posizione. È anche possibile impostare i bordi o altre proprietà delle immagini.

## **VerticalPageBreakCollection/VerticalPageBreak**

Ciascun oggetto Worksheet contiene un oggetto VerticalPageBreakCollection che rappresenta una collezione di tutte le interruzioni di pagina verticali in un foglio di lavoro come mostrato di seguito:

|**VPageBreaks e oggetti VPageBreak**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Un oggetto VerticalPageBreak viene utilizzato per creare un'interruzione di pagina verticale nel foglio di lavoro.
{{< app/cells/assistant language="python-net" >}}
