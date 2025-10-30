---
title: Manipola posizione, dimensione e progettazione del grafico con Golang tramite C++
linktitle: Manipolare Posizione, Dimensione e Progettazione del Grafico
description: Impara come usare Aspose.Cells for C++ per manipolare efficacemente la posizione, la dimensione e la progettazione del grafico in Microsoft Excel. La nostra guida dimostrerà come regolare queste proprietà per migliorare layout e visualizzazione.
keywords: Aspose.Cells for C++, Posizione, Dimensione, Progettazione del Grafico, Microsoft Excel, Layout, Visualizzazione.
type: docs
weight: 45
url: /it/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Posizione e Dimensione del Grafico**
A volte si desidera cambiare la posizione o la dimensione del nuovo o esistente grafico all'interno del foglio di lavoro. Aspose.Cells fornisce la proprietà [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) per raggiungere questo scopo. Puoi usare le sue sotto-proprietà per ridimensionare il grafico con una nuova **altezza** e **larghezza** o riposizionarlo con nuove coordinate **X** e **Y**.

### **Controllo Posizione e Dimensione del Grafico**
Per modificare la posizione (coordinate X, Y) o la dimensione (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

L'esempio seguente spiega l'uso delle API sopra, carica il workbook esistente che contiene un grafico nel suo primo foglio di lavoro. Quindi ridimensiona e riposiziona il grafico utilizzando Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Manipolazione dei Grafici del Designer**
Ci sono momenti in cui è necessario manipolare o modificare i grafici nei file di modello del designer. Aspose.Cells supporta pienamente la manipolazione dei contenuti e degli elementi del grafico del designer. I dati, i contenuti del grafico, l'immagine di sfondo e le formattazioni possono essere preservati con precisione.

### **Manipolazione dei Grafici del Designer nei File di Modello**
Per manipolare i grafici del designer nei file di modello, utilizzare le API correlate al grafico. Ad esempio, è possibile utilizzare la proprietà Worksheet.Charts per ottenere la collezione di grafici esistenti nel file di modello.

#### **Creazione di un Grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo successivamente questo grafico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Manipolazione del Grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato in precedenza. Nell'output generato, si noti che l'etichetta di data di un punto dati è stata impostata su 'Regno Unito, 30K'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Manipolazione di un Grafico a Linee nel Modello del Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
