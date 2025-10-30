---
title: Creazione di un Grafico a Torta con Linee di Guida
description: Impara come usare Aspose.Cells per Python via .NET per creare un grafico a torta con linee di collegamento in Microsoft Excel. La nostra guida dimostrerà come aggiungere linee di collegamento che connettono i punti dati alla legenda e migliorano la chiarezza generale del grafico.
keywords: Aspose.Cells per Python via .NET, Grafico a Torta, Linee di collegamento, Microsoft Excel, Visualizzazione dei dati, Personalizzazione del grafico.
linktitle: Grafico a Torta
type: docs
weight: 45
url: /it/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Questo articolo spiega come creare un grafico a torta con linee di collegamento da zero utilizzando l'API Aspose.Cells per Python via .NET. In Excel, l'opzione 'Mostra linee di collegamento' è impostata di default, quindi quando si crea un grafico a torta in Excel, le linee di collegamento vengono mostrate. Tuttavia, mentre si crea un grafico simile con le API Aspose.Cells per Python via .NET, è necessario impostare esplicitamente la proprietà [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines).

{{% /alert %}}

Per dimostrare l'uso dell'API Aspose.Cells per Python via .NET per creare un grafico a torta con linee di collegamento, prima creeremo un nuovo [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) e inseriremo alcuni dati che serviranno come fonte della serie di dati. Una volta che i dati sono in posizione, aggiungeremo un [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) di tipo [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) alla collezione di grafici e imposteremo i suoi aspetti diversi per ottenere la visualizzazione desiderata del grafico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Finora abbiamo creato un grafico a torta e ne abbiamo impostato gli aspetti differenti. Ora stiamo per attivare i capi di linea per il grafico. Si noti, per mostrare i capi di linea, dobbiamo spostare leggermente le etichette dei dati.

Il seguente pezzo di codice attiva i capi di linea, aggiorna il grafico e quindi calcola le posizioni delle etichette dei dati per spostarle di conseguenza.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Infine, il seguente codice salva il grafico in formato immagine e il workbook in formato XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Grafico a torta risultante**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Argomenti avanzati**
- [Colori delle fette personalizzate in un grafico a torta](/cells/it/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta](/cells/it/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articoli correlati

- [Creazione di grafici](/cells/it/python-net/creating-charts/)
- [Personalizzazione dei grafici](/cells/it/python-net/customizing-charts/)
- [Formattazione dei dati nei grafici](/cells/it/python-net/data-formatting-in-charts/)
- [Impostazione dell'aspetto del grafico](/cells/it/python-net/setting-chart-appearance/)

{{< app/cells/assistant language="python-net" >}}
