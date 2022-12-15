---
title: Manipola la dimensione della posizione e il grafico del progettista
type: docs
weight: 45
url: /it/net/manipulate-position-size-and-designer-chart/
---
## **Posizione e dimensione del grafico**
 A volte, si desidera modificare la posizione o le dimensioni del grafico nuovo o esistente all'interno del foglio di lavoro. Aspose.Cells fornisce il[Grafico.GraficoOggetto](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) proprietà per raggiungere questo obiettivo. Puoi utilizzare le sue proprietà secondarie per ridimensionare il grafico con new**altezza** e**larghezza** o riposizionarlo con new** X** e**Coordinate Y**.
### **Controllo della posizione e delle dimensioni del grafico**
Per modificare la posizione (coordinate X, Y) o le dimensioni (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Grafico.Oggetto Grafico.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Grafico.GraficoOggetto.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'esempio seguente spiega l'utilizzo delle API di cui sopra, carica la cartella di lavoro esistente che contiene un grafico nel suo primo foglio di lavoro. Quindi ridimensiona e riposiziona il grafico utilizzando Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipolazione di grafici Designer**
A volte è necessario manipolare o modificare i grafici nei file modello del designer. Aspose.Cells supporta completamente la manipolazione dei contenuti e degli elementi del grafico del designer. I dati, i contenuti del grafico, l'immagine di sfondo e le formattazioni possono essere preservati con precisione.
### **Manipolazione di grafici Designer nei file modello**
Per manipolare i grafici del designer nei file modello, utilizza l'API relativa al grafico. Ad esempio, è possibile utilizzare la proprietà Worksheet.Charts per ottenere la raccolta di grafici esistente nel file modello.
#### **Creazione di un grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo questo grafico in seguito.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipolazione del grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato sopra. Nell'output generato, si noti che l'etichetta della data di un punto dati è stata impostata su "Regno Unito, 30K".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipolazione di un grafico a linee nel modello Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e cambieremo i loro colori di linea.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

