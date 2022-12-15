---
title: Creazione di un grafico a torta con linee guida
linktitle: Grafico a torta
type: docs
weight: 45
url: /it/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 Questo articolo spiega come creare da zero un grafico a torta con linee guida durante l'utilizzo dell'API Aspose.Cells for .NET. In Excel, l'opzione "Mostra linee guida" è impostata per impostazione predefinita, quindi quando crei un grafico a torta in Excel vengono mostrate le linee guida. Tuttavia, durante la creazione di un grafico simile con le API Aspose.Cells, è necessario impostare in modo esplicito il file[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) proprietà.

{{% /alert %}}

Per dimostrare l'utilizzo dell'API Aspose.Cells for .NET per creare un grafico a torta con linee guida, creeremo prima un nuovo[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) e inserisci alcuni dati che serviranno come origine dati della serie. Una volta inseriti i dati, aggiungeremo a[**Grafico**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) di tipo[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)alla raccolta di grafici e impostarne i diversi aspetti per ottenere la vista del grafico desiderata.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Finora abbiamo creato un grafico a torta e impostato i suoi diversi aspetti. Ora attiveremo le linee guida per il grafico. Si prega di notare che per mostrare le linee guida, dobbiamo spostare leggermente le etichette dei dati.

La parte di codice seguente attiva le linee direttrici, aggiorna il grafico e quindi calcola le posizioni delle etichette dei dati per spostarle di conseguenza.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Infine, il codice seguente salva il grafico in formato immagine e la cartella di lavoro in formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Grafico a torta risultante**|
|:- |
|![cose da fare:immagine_alt_testo](creating-pie-chart-with-leader-lines_1.png)|

## **Argomenti avanzati**
- [Colori di sezioni o settori personalizzati nel grafico a torta](/cells/it/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Scopri se i punti dati si trovano nella seconda torta o barra su un grafico a torta o a barre](/cells/it/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## articoli Correlati

- [Creazione di grafici](/cells/it/net/creating-charts/)
- [Personalizzare i grafici](/cells/it/net/customizing-charts/)
- [Formattazione dei dati nei grafici](/cells/it/net/data-formatting-in-charts/)
- [Impostazione dell'aspetto del grafico](/cells/it/net/setting-chart-appearance/)

