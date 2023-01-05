---
title: Genera grafico elaborando marcatori intelligenti
type: docs
weight: 2100
url: /it/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells Le API forniscono il[**Workbook Designer**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)classe per lavorare con i marcatori intelligenti in cui la formattazione e le formule vengono inserite nei fogli di calcolo del designer e quindi elaborate[**Workbook Designer**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)class per riempire i dati in base agli Smart Marker specificati. È anche possibile creare grafici Excel elaborando gli Smart Marker, che richiederanno i seguenti passaggi.

- Creazione del foglio di calcolo del designer
- Elaborazione del foglio di calcolo del progettista rispetto all'origine dati specificata
- Creazione di grafici basati su dati popolati

{{% /alert %}}

## Creazione del foglio di calcolo del progettista

Un foglio di calcolo per designer è un semplice file Excel creato con l'applicazione Excel Microsoft o le API Aspose.Cells contenente la formattazione visiva, le formule e gli indicatori intelligenti, in cui i contenuti possono essere popolati in fase di esecuzione.

Per semplicità, creeremo il foglio di calcolo del progettista utilizzando Aspose.Cells for .NET API e successivamente lo elaboreremo rispetto a un'origine dati creata dinamicamente a scopo dimostrativo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Elaborazione del foglio di calcolo del progettista

Per elaborare il foglio di calcolo del designer, è necessario disporre di un'origine dati che corrisponda agli indicatori intelligenti utilizzati nel foglio di calcolo del designer. Ad esempio, abbiamo creato una voce Smart Marker come &=Sales.Year, che rappresenta la colonna Year nella DataTable Sales. Nel caso in cui una colonna corrispondente non sia disponibile nell'origine dati, le API Aspose.Cells salteranno l'elaborazione per quel particolare Smart Marker e, di conseguenza, i dati per quel particolare Smart Marker non verranno popolati.

Per dimostrare questo caso d'uso, creeremo l'origine dati da zero e la elaboreremo rispetto al foglio di calcolo del designer creato nel passaggio precedente. Tuttavia, in uno scenario in tempo reale, i dati potrebbero essere già disponibili per un'ulteriore elaborazione, pertanto è possibile ignorare la creazione dell'origine dati se i dati sono già disponibili.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

L'elaborazione degli Smart Marker è piuttosto semplice, come dimostrato dal seguente frammento di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Il frammento di codice precedente utilizza l'istanza esistente di[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe creata nel primo passaggio. Se hai già il file del foglio di calcolo del progettista su disco o memoria, puoi creare un'istanza di[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class caricando il foglio di calcolo del designer esistente.

{{% /alert %}}

## Creazione del grafico

 Una volta che i dati sono a posto, tutto ciò che dobbiamo fare è creare un grafico basato sull'origine dati. Per mantenere l'esempio semplice, useremo il[**Grafico.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)metodo in modo da non dover configurare ulteriormente il grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
