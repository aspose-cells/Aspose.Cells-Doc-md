---
title: Manipolare Posizione, Dimensione e Progettazione del Grafico
description: Scopri come utilizzare Aspose.Cells for .NET per manipolare efficacemente la posizione, la dimensione e la progettazione del grafico in Microsoft Excel. La nostra guida mostrerà come regolare queste proprietà per un layout e una visualizzazione migliorati.
keywords: Aspose.Cells for .NET, Posizione, Dimensione, Grafico di Progettazione, Microsoft Excel, Layout, Visualizzazione.
type: docs
weight: 45
url: /it/net/manipulate-position-size-and-designer-chart/
---

## **Posizione e Dimensione del Grafico**
A volte, si desidera cambiare la posizione o la dimensione del grafico nuovo o esistente all'interno del foglio di lavoro. Aspose.Cells fornisce la proprietà [Grafico.OggettoGrafico](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) per realizzare questo. È possibile utilizzare le sue sotto-proprietà per ridimensionare il grafico con una nuova **altezza** e **larghezza** o riposizionarlo con le nuove coordinate **X** e **Y**.
### **Controllo Posizione e Dimensione del Grafico**
Per modificare la posizione (coordinate X, Y) o la dimensione (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'esempio seguente spiega l'uso delle API sopra, carica il workbook esistente che contiene un grafico nel suo primo foglio di lavoro. Quindi ridimensiona e riposiziona il grafico utilizzando Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipolazione dei Grafici del Designer**
Ci sono momenti in cui è necessario manipolare o modificare i grafici nei file di modello del designer. Aspose.Cells supporta pienamente la manipolazione dei contenuti e degli elementi del grafico del designer. I dati, i contenuti del grafico, l'immagine di sfondo e le formattazioni possono essere preservati con precisione.
### **Manipolazione dei Grafici del Designer nei File di Modello**
Per manipolare i grafici del designer nei file di modello, utilizzare le API correlate al grafico. Ad esempio, è possibile utilizzare la proprietà Worksheet.Charts per ottenere la collezione di grafici esistenti nel file di modello.
#### **Creazione di un Grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo successivamente questo grafico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipolazione del Grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato in precedenza. Nell'output generato, si noti che l'etichetta di data di un punto dati è stata impostata su 'Regno Unito, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipolazione di un Grafico a Linee nel Modello del Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
