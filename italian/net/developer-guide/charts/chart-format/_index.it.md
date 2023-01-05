---
title: Impostazione dell'aspetto del grafico
linktitle: Formato grafico
type: docs
weight: 20
url: /it/net/setting-chart-appearance/
---
## **Impostazione dell'aspetto del grafico**
In Come creare un grafico abbiamo fornito una breve introduzione ai tipi di grafici e oggetti grafici offerti da Aspose.Cells e descritto come crearne uno. Questo articolo illustra come personalizzare l'aspetto dei grafici impostandone le proprietà:

- Impostazione dell'area del grafico.
- Impostazione delle linee del grafico.
- Applicazione di temi.
- Impostazione di titoli su grafici e assi.
- Lavorare con le linee della griglia.
### **Impostazione dell'area del grafico**
Esistono diversi tipi di aree in un grafico e Aspose.Cells offre la flessibilità di modificare l'aspetto di ciascuna area. Gli sviluppatori possono applicare diverse impostazioni di formattazione su un'area modificandone il colore di primo piano, il colore di sfondo e il formato di riempimento, ecc.

Nell'esempio fornito di seguito, abbiamo applicato diverse impostazioni di formattazione su diversi tipi di aree di un grafico. Queste aree includono:

- Area del grafico
- Zona cartografica
- SerieArea di raccolta
- Area di un singolo punto in una SeriesCollection

Il seguente frammento di codice mostra come impostare l'area del grafico.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Impostazione delle linee del grafico**
 Gli sviluppatori possono anche applicare diversi tipi di stili alle linee o agli indicatori di dati del file[SerieCollezione](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Il seguente frammento di codice mostra come impostare le linee del grafico utilizzando Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Applicazione di temi Microsoft Excel 2007/2010 ai grafici**
 Gli sviluppatori possono applicare diversi temi/colori di Excel Microsoft a[SerieCollezione](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)o altri oggetti cartografici come mostrato di seguito nell'esempio.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Impostazione dei titoli dei grafici o degli assi**
È possibile utilizzare Microsoft Excel per impostare i titoli di un grafico e i relativi assi in un ambiente WYSIWYG. Aspose.Cells consente inoltre agli sviluppatori di impostare i titoli di un grafico e i suoi assi in fase di esecuzione. Tutti i grafici e i relativi assi contengono a[Titolo](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)proprietà che può essere utilizzata per impostare i loro titoli come mostrato di seguito in un esempio.

Il seguente frammento di codice mostra come impostare titoli su grafici e assi.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Lavorare con le principali linee della griglia**
È possibile personalizzare l'aspetto delle principali linee della griglia. Nascondere o mostrare le linee della griglia o definirne il colore e altre impostazioni. Di seguito, mostriamo come nascondere le linee della griglia e come cambiarne il colore.
#### **Nascondere le principali linee della griglia**
Gli sviluppatori possono controllare la visibilità delle principali linee della griglia impostando il file[È visibile](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) proprietà del[Linea](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) opporsi a**VERO** o**falso**.

Il seguente frammento di codice mostra come nascondere le griglie principali. Dopo aver nascosto le linee della griglia principali, un istogramma verrà aggiunto al foglio di lavoro senza linee della griglia.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Modifica delle impostazioni della griglia principale**
Gli sviluppatori non possono solo controllare la visibilità delle principali linee della griglia, ma anche altre proprietà, incluso il colore, ecc.

Il seguente frammento di codice mostra come modificare il colore della griglia principale. Dopo aver impostato il colore delle linee della griglia principali, al foglio di lavoro verrà aggiunto un istogramma con le linee della griglia modificate.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Argomenti avanzati**
- [Impostare il codice del formato dei valori della serie di grafici](/cells/it/net/set-the-values-format-code-of-chart-series/)
- [Imposta l'immagine come sfondo Compila il grafico](/cells/it/net/set-picture-as-background-fill-in-the-chart/)
