---
title: Aspose.Cells Modello oggetto
type: docs
weight: 20
url: /it/python-net/aspose-cells-object-model/
---
{{% alert color="primary" %}}

Aspose.Cells Object Model fornisce informazioni sulle relazioni strutturali tra gli oggetti della libreria di classi Aspose.Cells.

{{% /alert %}}

La struttura di livello superiore del modello a oggetti Aspose.Cells è mostrata di seguito in modo gerarchico.

|**Struttura di primo livello del modello a oggetti Aspose.Cells**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_1.png)|
Come puoi vedere dalla figura sopra, la radice del modello a oggetti è l'oggetto Workbook. Di seguito viene fornita una breve descrizione di alcuni degli oggetti a scopo introduttivo.

## **Foglio di lavoroCollezione/Foglio di lavoro**

L'oggetto Workbook contiene WorksheetCollection, che rappresenta la raccolta di tutti gli oggetti Worksheet in un foglio di calcolo come mostrato di seguito:

|**Fogli di lavoro e oggetti del foglio di lavoro**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_2.png)|

## **Cells/Cell**

Ogni oggetto foglio di lavoro contiene un oggetto Cells che rappresenta la raccolta di tutti gli oggetti Cell in un foglio di lavoro come mostrato di seguito:

|**Cells & Cell oggetti**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_3.png)|
È possibile utilizzare l'oggetto Cell per ottenere e impostare il valore, lo stile, la formula e altre proprietà di una singola cella.

## **GraficoCollezione/Grafico**

L'oggetto Charts rappresenta una raccolta di tutti gli oggetti Chart in un foglio di lavoro. Ogni oggetto grafico è composto da diversi altri oggetti che lavorano insieme per creare e gestire grafici. La struttura del grafico in Aspose.Cells è mostrata nel diagramma seguente:

|**Modello a oggetti del grafico**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_4.png)|

## **CommentRaccolta/Commento**

Ogni oggetto Worksheet contiene anche un oggetto Comments che rappresenta la raccolta di tutti gli oggetti Comment in un foglio di lavoro come mostrato di seguito:

|**Commenti e oggetti commento**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_5.png)|
Un oggetto Comment viene utilizzato per aggiungere un commento a qualsiasi cella specificata nel foglio di lavoro.

## **RaccoltaInterruzionePaginaOrizzontale/InterruzionePaginaOrizzontale**

Ogni oggetto Worksheet contiene un oggetto HorizontalPageBreakCollection che rappresenta una raccolta di tutti gli oggetti HorizontalPageBreak in un foglio di lavoro come mostrato di seguito:

|**Oggetti HPageBreaks e HPageBreak**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_6.png)|
Un oggetto HorizontalPageBreak viene utilizzato per creare un'interruzione di pagina orizzontale nel foglio di lavoro.

## **Collegamento ipertestuale/collegamento ipertestuale**

Un oggetto Worksheet contiene anche un HyperlinkCollection che rappresenta una raccolta di tutti gli oggetti Hyperlink nel foglio di lavoro come mostrato di seguito:

|**Collegamenti ipertestuali e oggetti collegamento ipertestuale**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_7.png)|
Un oggetto Hyperlink rappresenta un collegamento ipertestuale nel foglio di lavoro. Gli sviluppatori possono impostare l'indirizzo del collegamento ipertestuale e altre proprietà correlate utilizzando l'oggetto Collegamento ipertestuale.

## **Raccolta di immagini/Immagine**

Ogni oggetto Worksheet contiene un oggetto PictureCollection che rappresenta una raccolta di tutti gli oggetti Picture in un foglio di lavoro come mostrato di seguito:

|**Immagini e oggetti immagine**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_8.png)|
Un oggetto Picture rappresenta un'immagine nel foglio di lavoro. Utilizzando l'oggetto Immagine, gli sviluppatori non possono solo aggiungere immagini nei loro fogli di lavoro, ma anche posizionare queste immagini in qualsiasi posizione. È anche possibile impostare bordi o altre proprietà delle immagini.

## **VerticalPageBreakCollection/VerticalPageBreak**

Ogni oggetto Worksheet contiene un oggetto VerticalPageBreakCollection che rappresenta una raccolta di tutti gli oggetti VerticalPageBreak in un foglio di lavoro come mostrato di seguito:

|**Oggetti VPageBreaks e VPageBreak**|
|:- |
|![cose da fare:immagine_alt_testo](aspose-cells-object-model_9.png)|
Un oggetto VerticalPageBreak viene utilizzato per creare un'interruzione di pagina verticale nel foglio di lavoro.
