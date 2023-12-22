---
title: Creazione di un grafico a torta con linee guida
description: Scopri come utilizzare Aspose.Cells for .NET per creare un grafico a torta con linee direttrici in Microsoft Excel. La nostra guida mostrerà come aggiungere linee guida che collegano i punti dati alla legenda e migliorano la chiarezza generale del tuo grafico.
keywords: Aspose.Cells for .NET, Pie Chart, Leader Lines, Microsoft Excel, Data Visualization, Chart Customization.
linktitle: Grafico a torta
type: docs
weight: 45
url: /it/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

Questo articolo spiega come creare da zero un grafico a torta con linee direttrici utilizzando Aspose.Cells for .NET API. In Excel, l'opzione "Mostra linee direttrici" è impostata per impostazione predefinita, quindi quando crei un grafico a torta in Excel vengono visualizzate le linee direttrici. Tuttavia, durante la creazione di un grafico simile con le API Aspose.Cells, è necessario impostare esplicitamente il file[**Serie.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) proprietà.

{{% /alert %}}

 Per dimostrare l'utilizzo di Aspose.Cells for .NET API per creare un grafico a torta con linee direttrici, creeremo prima un nuovo[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) e inserisci alcuni dati che fungeranno da origine dati della serie. Una volta che i dati saranno a posto, aggiungeremo a[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) di tipo[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)alla raccolta di grafici e impostarne i diversi aspetti per ottenere la visualizzazione del grafico desiderata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Finora abbiamo creato un grafico a torta e ne abbiamo definito i diversi aspetti. Ora attiveremo le linee guida per il grafico. Tieni presente che per mostrare le linee guida dobbiamo spostare leggermente le etichette dei dati.

La seguente parte di codice attiva le linee guida, aggiorna il grafico e quindi calcola le posizioni delle etichette dati per spostarle di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Infine, il codice seguente salva il grafico in formato immagine e la cartella di lavoro in formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Grafico a torta risultante**|
| :- |
|![cose da fare:immagine_alt_testo](creating-pie-chart-with-leader-lines_1.png)|

##  **Argomenti avanzati**
- [Colori personalizzati delle sezioni o dei settori nel grafico a torta](/cells/it/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Scopri se i punti dati si trovano nella seconda torta o nella barra di un grafico a torta o a barra della torta](/cells/it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

##  articoli Correlati

- [Creazione di grafici](/cells/it/net/creating-charts/)
- [Grafici personalizzati](/cells/it/net/customizing-charts/)
- [Formattazione dei dati nei grafici](/cells/it/net/data-formatting-in-charts/)
- [Impostazione dell'aspetto della carta](/cells/it/net/setting-chart-appearance/)

