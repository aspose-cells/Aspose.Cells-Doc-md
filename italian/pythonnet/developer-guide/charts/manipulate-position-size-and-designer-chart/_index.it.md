---
title: Manipolare Posizione, Dimensione e Progettazione del Grafico
description: Impara come utilizzare Aspose.Cells per Python via .NET per manipolare efficacemente la posizione, le dimensioni e il progettista del grafico in Microsoft Excel. La nostra guida dimostrerà come regolare queste proprietà per migliorare layout e visualizzazione.
keywords: Aspose.Cells per Python via .NET, Posizione, Dimensione, Progettista di Grafico, Microsoft Excel, Layout, Visualizzazione.
type: docs
weight: 45
url: /it/python-net/manipulate-position-size-and-designer-chart/
---

## **Posizione e Dimensione del Grafico**
A volte, si desidera modificare la posizione o le dimensioni del nuovo o esistente grafico all'interno del foglio di lavoro. Aspose.Cells per Python via .NET fornisce la proprietà [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) per farlo. È possibile utilizzare le sue sotto-proprietà per ridimensionare il grafico con nuovo **altezza** e **larghezza** o riposizionarlo con nuove coordinate **X** e **Y**.
### **Controllo Posizione e Dimensione del Grafico**
Per modificare la posizione (coordinate X, Y) o la dimensione (altezza, larghezza) del grafico, utilizzare queste proprietà:

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

L'esempio seguente spiega l'uso delle API sopra, carica il workbook esistente che contiene un grafico nel suo primo foglio. Quindi ridimensiona e riposiziona il grafico usando Aspose.Cells per Python via .NET.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Manipolazione dei Grafici del Designer**
Ci sono momenti in cui è necessario manipolare o modificare i grafici nei file di modelli di progettazione. Aspose.Cells per Python via .NET supporta pienamente la manipolazione dei contenuti e degli elementi del grafico del progettista. I dati, i contenuti del grafico, le immagini di sfondo e le formattazioni possono essere preservati con precisione.
### **Manipolazione dei Grafici del Designer nei File di Modello**
Per manipolare i grafici del designer nei file di modello, utilizzare le API correlate al grafico. Ad esempio, è possibile utilizzare la proprietà Worksheet.Charts per ottenere la collezione di grafici esistenti nel file di modello.
#### **Creazione di un Grafico**
L'esempio seguente mostra come creare un grafico a piramide. Manipoleremo successivamente questo grafico.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Manipolazione del Grafico**
L'esempio seguente mostra come manipolare il grafico esistente. In questo esempio, modifichiamo il grafico creato in precedenza. Nell'output generato, si noti che l'etichetta di data di un punto dati è stata impostata su 'Regno Unito, 30K'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Manipolazione di un Grafico a Linee nel Modello del Designer**
In questo esempio, manipoleremo un grafico a linee. Aggiungeremo alcune serie di dati al grafico esistente e ne cambieremo i colori delle linee.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

