---
title: Manipolare le dimensioni della posizione e il grafico del designer
description: Scopri come utilizzare Aspose.Cells for .NET per manipolare in modo efficace la posizione, le dimensioni e il grafico di progettazione in Microsoft Excel. La nostra guida mostrerà come regolare queste proprietà per migliorare il layout e la visualizzazione.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /it/net/manipulate-position-size-and-designer-chart/
---
##  **Posizione e dimensione del grafico**
 A volte è necessario modificare la posizione o la dimensione del grafico nuovo o esistente all'interno del foglio di lavoro. Aspose.Cells fornisce il[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) proprietà per raggiungere questo obiettivo. Puoi utilizzare le sue proprietà secondarie per ridimensionare il grafico con new**altezza** E**larghezza** o riposizionarlo con new**X** e **Y** coordinate.
###  **Controllo della posizione e delle dimensioni del grafico**
Per modificare la posizione del grafico (coordinate X, Y) o le dimensioni (altezza, larghezza), utilizza queste proprietà:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Grafico.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'esempio seguente spiega l'utilizzo delle API precedenti e carica la cartella di lavoro esistente che contiene un grafico nel suo primo foglio di lavoro. Quindi ridimensiona e riposiziona il grafico utilizzando Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Manipolazione dei grafici di progettazione**
Ci sono momenti in cui è necessario manipolare o modificare i grafici nei file modello di progettazione. Aspose.Cells supporta completamente la manipolazione dei contenuti e degli elementi dei grafici del designer. I dati, il contenuto del grafico, l'immagine di sfondo e le formattazioni possono essere conservati con precisione.
###  **Manipolazione dei grafici Designer nei file modello**
Per manipolare i grafici di progettazione nei file modello, utilizzare il grafico correlato API. Ad esempio, è possibile utilizzare la proprietà Worksheet.Charts per ottenere la raccolta di grafici esistente nel file modello.
####  **Creazione di un grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo questo grafico più avanti.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Manipolare il grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato sopra. Nell'output generato, nota che l'etichetta della data di un punto dati è stata impostata su "Regno Unito, 30K".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Manipolazione di un grafico a linee nel modello Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e cambieremo i colori delle linee.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

