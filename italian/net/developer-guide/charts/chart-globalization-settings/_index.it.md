---
title: Utilizzare la classe ChartGlobalizationSettings per impostare una lingua diversa per il componente del grafico 
description: Scopri come utilizzare la classe ChartGlobalizationSettings in Aspose.Cells for .NET per impostare lingue diverse per i componenti del grafico. La nostra guida ti aiuterà a capire come localizzare elementi del grafico, etichette e legende in lingue diverse, consentendoti di presentare i dati in modo culturalmente appropriato.
keywords: Aspose.Cells for .NET, grafici, globalizzazione del grafico, lingue, localizzazione, ChartGlobalizationSettings, elementi, etichette, leggende.
type: docs
weight: 2200
url: /it/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells hanno esposto la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) per gestire gli scenari in cui l'utente desidera impostare un componente del grafico in una lingua diversa, etichette personalizzate per i subtotali in un foglio di calcolo. 

## **Introduzione alla classe ChartGlobalizationSettings**

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) attualmente offre i seguenti 8 metodi che possono essere sovrascritti in una classe personalizzata per tradurre il nome di ElementoTitolo asse, nome di UnitàAsse, nome di TitoloGrafico e così via in una lingua diversa.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Ottiene il nome del Titolo per l'Asse.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Ottiene il Nome dell'Unità di Asse.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Ottiene il nome del Titolo del Grafico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Ottiene il nome di Diminuzione per la Leggenda.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Ottiene il nome di aumento per la Leggenda.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Ottiene il nome di Totale per la Leggenda.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Ottiene il nome delle etichette "Altro" per il Grafico.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Ottiene il nome di Serie nel Grafico.

### **Traduzione personalizzata**
Qui, creeremo un grafico a barre basato sui seguenti dati. I nomi dei componenti del grafico verranno visualizzati in inglese nel grafico. Useremo un esempio in lingua turca per mostrare come visualizzare il Titolo del Grafico, i nomi di Aumento/Diminuzione della Leggenda, il nome Totale e il Titolo dell'Asse in turco.

![todo:image_alt_text](sample.png)

## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
