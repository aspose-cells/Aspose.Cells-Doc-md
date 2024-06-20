---
title: Creazione di un Grafico a Torta con Linee di Guida
description: Scopri come utilizzare il Aspose.Cells for .NET per creare un grafico a torta con linee guida in Microsoft Excel. La nostra guida dimostrerà come aggiungere linee guida che collegano i punti dati alla leggenda e migliorano la chiarezza complessiva del grafico.
keywords: Aspose.Cells for .NET, Grafico a Torta, Linee Guida, Microsoft Excel, Visualizzazione dei Dati, Personalizzazione del Grafico.
linktitle: Grafico a Torta
type: docs
weight: 45
url: /it/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Questo articolo spiega come creare un grafico a torta con linee guida da zero utilizzando l'API Aspose.Cells for .NET. In Excel, l'opzione 'Mostra capi di linea' è impostata per impostazione predefinita, quindi quando si crea un grafico a torta in Excel, i capi di linea sono mostrati. Tuttavia, mentre si crea un grafico simile con le API Aspose.Cells, è necessario impostare esplicitamente la proprietà [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines).

{{% /alert %}}

Per dimostrare l'uso dell'API Aspose.Cells for .NET per creare un grafico a torta con linee guida, creeremo prima un nuovo [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) e inseriremo alcuni dati che serviranno come origine dei dati della serie. Una volta che i dati sono posizionati, aggiungeremo una [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) di tipo [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) alla collezione dei grafici e ne imposteremo gli aspetti differenti per ottenere la vista desiderata del grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Finora abbiamo creato un grafico a torta e ne abbiamo impostato gli aspetti differenti. Ora stiamo per attivare i capi di linea per il grafico. Si noti, per mostrare i capi di linea, dobbiamo spostare leggermente le etichette dei dati.

Il seguente pezzo di codice attiva i capi di linea, aggiorna il grafico e quindi calcola le posizioni delle etichette dei dati per spostarle di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Infine, il seguente codice salva il grafico in formato immagine e il workbook in formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Grafico a torta risultante**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Argomenti avanzati**
- [Colori delle fette personalizzate in un grafico a torta](/cells/it/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta](/cells/it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articoli correlati

- [Creazione di grafici](/cells/it/net/creating-charts/)
- [Personalizzazione dei grafici](/cells/it/net/customizing-charts/)
- [Formattazione dei dati nei grafici](/cells/it/net/data-formatting-in-charts/)
- [Impostazione dell'aspetto del grafico](/cells/it/net/setting-chart-appearance/)

