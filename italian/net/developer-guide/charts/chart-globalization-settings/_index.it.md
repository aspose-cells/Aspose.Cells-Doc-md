---
title:  Utilizzo della classe ChartGlobalizationSettings per impostare una lingua diversa per il componente del grafico
type: docs
weight: 2200
url: /it/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Possibili scenari di utilizzo**

 Aspose.Cells API hanno esposto il file[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) class per gestire gli scenari in cui l'utente desidera impostare il componente del grafico in una lingua diversa. etichette personalizzate per subtotali in un foglio di calcolo.

##  **Introduzione alla classe ChartGlobalizationSettings**

 IL[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)class attualmente offre i seguenti 8 metodi che possono essere sovrascritti in una classe personalizzata per tradurre come nome AxisTitle, nome AxisUnit, nome ChartTitle e così via in una lingua diversa.
1. [**OttieniAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Ottiene il nome del titolo per l'asse.
1. [**OttieniNomeUnitàAsse**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Ottiene il nome dell'unità dell'asse.
1. [**OttieniNomeTitoloGrafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Ottiene il nome del titolo del grafico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Ottiene il nome di Decrease per Legend.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Ottiene il nome dell'aumento per Legend.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Ottiene il nome di Total per Legend.
1. [**Ottieni altro nome**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Ottiene il nome delle etichette "Altro" per Chart.
1. [**OttieniNomeSerie**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Ottiene il nome della serie nel grafico.

###  **Traduzione in lingua personalizzata**
Qui, creeremo un grafico a cascata basato sui seguenti dati. I nomi dei componenti del grafico verranno visualizzati in inglese nel grafico. Useremo un esempio in lingua turca per mostrare come visualizzare il titolo del grafico, i nomi di aumento/diminuzione della legenda, il nome totale e il titolo dell'asse in turco.

![cose da fare:image_alt_text](sample.png)

##  **Codice d'esempio**
 Il codice di esempio seguente carica il file[esempio di file Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Output generato dal codice di esempio

Questo è l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
