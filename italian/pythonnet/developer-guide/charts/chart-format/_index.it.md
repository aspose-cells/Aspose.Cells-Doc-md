---
title: Impostazione dell aspetto del grafico
description: Scopri come configurare l aspetto dei grafici in Aspose.Cells per Python via .NET. La nostra guida ti mostrerà come modificare layout, colori, font ed effetti per ottenere lo stile visivo desiderato e migliorare i tuoi fogli di lavoro.
keywords: Aspose.Cells per Python via .NET, creazione grafici, aspetto grafico, layout, colori, font, effetti, fogli di lavoro.
linktitle: Formato del grafico
type: docs
weight: 20
url: /it/python-net/setting-chart-appearance/
---

## **Impostazione dell'aspetto del grafico**
In Come Creare un Grafico abbiamo fornito una breve introduzione ai tipi di grafici e agli oggetti grafico offerti da Aspose.Cells per Python via .NET, e descritto come crearne uno. Questo articolo discute come personalizzare l'aspetto dei grafici impostando le loro proprietà:

- Impostazione dell'area del grafico.
- Impostazione delle linee del grafico.
- Applicazione dei temi.
- Impostazione dei titoli dei grafici e degli assi.
- Lavorare con linee della griglia.
### **Impostazione dell'Area del Grafico**
Ci sono diversi tipi di aree in un grafico e Aspose.Cells per Python via .NET offre la flessibilità di modificare l'aspetto di ogni area. Gli sviluppatori possono applicare impostazioni di formattazione diverse su un'area modificando il suo colore di primo piano, colore di sfondo e formato riempimento, ecc.

Nell'esempio di seguito, abbiamo applicato diverse impostazioni di formattazione su diversi tipi di aree di un grafico. Queste aree includono:

- Area del tracciato
- Area del grafico
- Area di raccolta serie
- Area di un singolo punto in una Serie di raccolta

Il seguente frammento di codice dimostra come impostare l'area del grafico.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartArea-1.py" >}}

### **Impostazione delle Linee del Grafico**
Gli sviluppatori possono anche applicare diversi stili sulle linee o sui marcatori dei [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection). Il seguente esempio di codice mostra come impostare le linee del grafico usando l'API di Aspose.Cells per Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingChartLines-1.py" >}}

### **Applicazione dei Temi Microsoft Excel 2007/2010 ai Grafici**
Gli sviluppatori possono applicare temi o colori di Microsoft Excel su [SeriesCollection](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) o altri oggetti grafici come mostrato nell'esempio sotto.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ApplyingThemes-1.py" >}}

### **Impostare i Titoli dei Grafici o degli Assi**
Puoi usare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG. Aspose.Cells per Python via .NET consente anche agli sviluppatori di impostare i titoli di un grafico e dei suoi assi a runtime. Tutti i grafici e i loro assi contengono una proprietà [Chart.title](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/title) che può essere usata per impostare i titoli come mostrato nell'esempio sotto.

Il seguente frammento di codice dimostra come impostare i titoli per grafici e assi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-SettingTitlesAxes-1.py" >}}

### **Lavorare con le linee di griglia principali**
È possibile personalizzare l'aspetto delle linee di griglia principali. Nascondere o mostrare le linee di griglia, o definire il loro colore e altre impostazioni. Di seguito, mostriamo come nascondere le linee di griglia e come cambiarne il colore.

#### **Nascondere le linee di griglia principali**
Gli sviluppatori possono controllare la visibilità delle linee guida principali impostando la proprietà [is_visible](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line/is_visible) dell'oggetto [Line](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/line) su **true** o **false**.

Il seguente frammento di codice dimostra come nascondere le linee di griglia principali. Dopo aver nascosto le linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro che non avrà linee di griglia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-MajorGridlines-1.py" >}}

#### **Modifica delle impostazioni delle linee di griglia principali**
Gli sviluppatori non possono solo controllare la visibilità delle linee di griglia principali, ma anche altre proprietà, inclusi il colore, ecc.

Il seguente frammento di codice dimostra come cambiare il colore delle linee di griglia principali. Dopo aver impostato il colore delle linee di griglia principali, verrà aggiunto un grafico a colonne al foglio di lavoro con linee di griglia modificate.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsAppearance-ChangingMajorGridlines-1.py" >}}

## **Argomenti avanzati**
- [Impostare il codice di formato dei valori della serie del grafico](/cells/it/python-net/set-the-values-format-code-of-chart-series/)
- [Imposta l'immagine come riempimento di sfondo nel grafico](/cells/it/python-net/set-picture-as-background-fill-in-the-chart/)
