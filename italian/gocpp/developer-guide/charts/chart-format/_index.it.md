---
title: Impostare l’aspetto del grafico con Golang via C++
linktitle: Formato del grafico
description: Impara come configurare l’aspetto dei grafici in Aspose.Cells for C++. La nostra guida ti mostrerà come modificare layout, colori, font ed effetti per ottenere lo stile visivo desiderato e migliorare i tuoi fogli di lavoro.
keywords: Aspose.Cells for C++, grafici, aspetto del grafico, layout, colori, font, effetti, fogli di lavoro.
type: docs
weight: 20
url: /it/go-cpp/setting-chart-appearance/
---

## **Impostazione dell'aspetto del grafico**
Nella guida su Come creare un grafico abbiamo dato una breve introduzione ai tipi di grafici e oggetti grafici offerti da Aspose.Cells, e descritto come crearne uno. Questo articolo discute come personalizzare l'aspetto dei grafici impostandone le proprietà:

- Impostazione dell'area del grafico.
- Impostazione delle linee del grafico.
- Applicazione dei temi.
- Impostazione dei titoli dei grafici e degli assi.
- Lavorare con linee della griglia.

### **Impostazione dell'Area del Grafico**
Ci sono diversi tipi di aree in un grafico e Aspose.Cells offre la flessibilità di modificare l'aspetto di ciascuna area. Gli sviluppatori possono applicare diverse impostazioni di formattazione su un'area cambiandone il colore di primo piano, il colore di sfondo e il formato di riempimento, ecc.

Nell'esempio di seguito, abbiamo applicato diverse impostazioni di formattazione su diversi tipi di aree di un grafico. Queste aree includono:

- Area del tracciato
- Area del grafico
- Area di raccolta serie
- Area di un singolo punto in una Serie di raccolta

Il seguente frammento di codice dimostra come impostare l'area del grafico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **Impostazione delle Linee del Grafico**
Gli sviluppatori possono anche applicare diversi tipi di stili sui linee o sui marcatori dei dati di [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/). Il seguente esempio di codice mostra come impostare le linee del grafico utilizzando l’API di Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Applicazione dei Temi Microsoft Excel 2007/2010 ai Grafici**
Gli sviluppatori possono applicare diversi temi/Colori di Microsoft Excel a [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) o altri oggetti del grafico come mostrato nell’esempio.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **Impostare i Titoli dei Grafici o degli Assi**
Puoi usare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG. Aspose.Cells consente anche agli sviluppatori di impostare i titoli di un grafico e dei suoi assi in tempo reale. Tutti i grafici e i loro assi contengono una proprietà [Title](https://reference.aspose.com/cells/go-cpp/title/) che può essere utilizzata per impostare i loro titoli come mostrato nell’esempio.

Il seguente frammento di codice dimostra come impostare i titoli per grafici e assi.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **Lavorare con le linee di griglia principali**
È possibile personalizzare l'aspetto delle linee di griglia principali. Nascondere o mostrare le linee di griglia, o definire il loro colore e altre impostazioni. Di seguito, mostriamo come nascondere le linee di griglia e come cambiarne il colore.

#### **Nascondere le linee di griglia principali**
Gli sviluppatori possono controllare la visibilità delle linee di griglia principali impostando la proprietà [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) dell'oggetto [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) su **true** o **false**.

Il seguente frammento di codice dimostra come nascondere le linee di griglia principali. Dopo aver nascosto le linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro che non avrà linee di griglia.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **Modifica delle impostazioni delle linee di griglia principali**
Gli sviluppatori non possono solo controllare la visibilità delle linee di griglia principali, ma anche altre proprietà, inclusi il colore, ecc.

Il seguente frammento di codice dimostra come cambiare il colore delle linee di griglia principali. Dopo aver impostato il colore delle linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro con linee di griglia modificate.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **Argomenti avanzati**
- [Impostare il codice di formato dei valori della serie del grafico](/cells/it/cpp/set-the-values-format-code-of-chart-series/)
- [Imposta l'immagine come riempimento di sfondo nel grafico](/cells/it/cpp/set-picture-as-background-fill-in-the-chart/)
