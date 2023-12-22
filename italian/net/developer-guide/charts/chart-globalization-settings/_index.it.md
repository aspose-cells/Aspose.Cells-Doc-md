---
title:  Utilizzo della classe ChartGlobalizationSettings per impostare una lingua diversa per il componente grafico
description: Scopri come utilizzare la classe ChartGlobalizationSettings in Aspose.Cells for .NET per impostare lingue diverse per i componenti del grafico. La nostra guida ti aiuterà a capire come localizzare gli elementi del grafico, le etichette e le legende in diverse lingue, permettendoti di presentare i tuoi dati in un modo culturalmente appropriato.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /it/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Possibili scenari di utilizzo**

 Aspose.Cells Le API hanno esposto il file[**GraficoGlobalizzazioneImpostazioni**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) classe per gestire gli scenari in cui l'utente desidera impostare il componente grafico su una lingua diversa. etichette personalizzate per i totali parziali in un foglio di calcolo.

##  **Introduzione alla classe ChartGlobalizationSettings**

 IL[**GraficoGlobalizzazioneImpostazioni**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)La classe attualmente offre i seguenti 8 metodi che possono essere sovrascritti in una classe personalizzata per tradurre come il nome AxisTitle, il nome AxisUnit, il nome ChartTitle e così via in una lingua diversa.
1. [**OttieniNomeTitoloAsse**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Ottiene il nome del titolo per l'asse.
1. [**OttieniNomeUnitàAsse**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Ottiene il nome dell'unità dell'asse.
1. [**OttieniNomeTitoloGrafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Ottiene il nome del titolo del grafico.
1. [**OttieniLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Ottiene il nome di Diminuzione per Legend.
1. [**OttieniLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Ottiene il nome dell'aumento per Legend.
1. [**OttieniNomeTotaleLegend**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Ottiene il nome Total for Legend.
1. [**OttieniAltroNome**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Ottiene il nome delle etichette "Altro" per il grafico.
1. [**Ottieninomeserie**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Ottiene il nome della serie nel grafico.

###  **Traduzione linguistica personalizzata**
Qui creeremo un grafico a cascata basato sui seguenti dati. I nomi dei componenti della carta verranno visualizzati in inglese nella carta. Utilizzeremo un esempio in lingua turca per mostrare come visualizzare il titolo del grafico, i nomi di aumento/diminuzione della legenda, il nome totale e il titolo dell'asse in turco.

![cose da fare:immagine_alt_testo](sample.png)

##  **Codice d'esempio**
 Il codice di esempio seguente carica il file[file Excel di esempio](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Output generato dal codice di esempio

Questo è l'output della console del codice di esempio riportato sopra.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
