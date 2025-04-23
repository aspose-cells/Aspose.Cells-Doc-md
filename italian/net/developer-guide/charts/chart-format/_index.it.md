---
title: Impostazione dell aspetto del grafico
description: Scopri come configurare l aspetto dei grafici in Aspose.Cells for .NET. La nostra guida ti mostrerà come modificare i layout, i colori, i caratteri e gli effetti dei grafici per ottenere lo stile visivo desiderato e migliorare i tuoi fogli di lavoro.
keywords: Aspose.Cells for .NET, creazione di grafici, aspetto dei grafici, layout, colori, font, effetti, fogli di lavoro.
linktitle: Formato del grafico
type: docs
weight: 20
url: /it/net/setting-chart-appearance/
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



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Impostazione delle Linee del Grafico**
Gli sviluppatori possono anche applicare diversi tipi di stili sulle linee o marcatori di dati della Serie di raccolta. Il seguente frammento di codice dimostra come impostare le linee del grafico utilizzando l'API Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Applicazione dei Temi Microsoft Excel 2007/2010 ai Grafici**
Gli sviluppatori possono applicare diversi temi/colori di Microsoft Excel a Serie di raccolta o altri oggetti grafici come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Impostare i Titoli dei Grafici o degli Assi**
È possibile utilizzare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG. Aspose.Cells consente anche agli sviluppatori di impostare i titoli di un grafico e dei suoi assi durante l'esecuzione. Tutti i grafici e i loro assi contengono una proprietà [Titolo](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) che può essere utilizzata per impostare i loro titoli come mostrato di seguito in un esempio.

Il seguente frammento di codice dimostra come impostare i titoli per grafici e assi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Lavorare con le linee di griglia principali**
È possibile personalizzare l'aspetto delle linee di griglia principali. Nascondere o mostrare le linee di griglia, o definire il loro colore e altre impostazioni. Di seguito, mostriamo come nascondere le linee di griglia e come cambiarne il colore.
#### **Nascondere le linee di griglia principali**
Gli sviluppatori possono controllare la visibilità delle linee di griglia principali impostando la proprietà [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) dell'oggetto [Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) su **true** o **false**.

Il seguente frammento di codice dimostra come nascondere le linee di griglia principali. Dopo aver nascosto le linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro che non avrà linee di griglia.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Modifica delle impostazioni delle linee di griglia principali**
Gli sviluppatori non possono solo controllare la visibilità delle linee di griglia principali, ma anche altre proprietà, inclusi il colore, ecc.

Il seguente frammento di codice dimostra come cambiare il colore delle linee di griglia principali. Dopo aver impostato il colore delle linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro con linee di griglia modificate.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Argomenti avanzati**
- [Impostare il codice di formato dei valori della serie del grafico](/cells/it/net/set-the-values-format-code-of-chart-series/)
- [Imposta l'immagine come riempimento di sfondo nel grafico](/cells/it/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
