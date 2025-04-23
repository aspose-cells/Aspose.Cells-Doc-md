---
title: Genera un grafico elaborando i marcatori intelligenti
description: Scopri come generare grafici con i marcatori intelligenti utilizzando Aspose.Cells for .NET. La nostra guida ti mostrerà come elaborare i marcatori intelligenti e le loro proprietà per migliorare l aspetto e l usabilità dei tuoi grafici.
keywords: Aspose.Cells for .NET, generazione del grafico, marcatori intelligenti, aspetto, usabilità, elaborazione.
type: docs
weight: 2100
url: /it/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells forniscono la classe [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) per lavorare con i marcatori intelligenti, dove la formattazione e le formule sono inserite nei fogli di calcolo del designer e quindi elaborate con la classe [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) per riempire i dati in base ai marcatori intelligenti specificati. È inoltre possibile creare grafici di Excel elaborando i marcatori intelligenti, il che richiederà i seguenti passaggi.

- Creazione del foglio di calcolo del designer
- Elaborazione del foglio di calcolo del designer in base alla fonte dati specificata
- Creazione del grafico in base ai dati popolati

{{% /alert %}}

## Creazione del foglio di calcolo del designer

Un foglio di calcolo del designer è un semplice file di Excel creato con l'applicazione Microsoft Excel o le API di Aspose.Cells che contiene la formattazione visiva, formule e marcatori intelligenti, dove i contenuti possono essere popolati durante l'esecuzione.

Per semplicità, creeremo il foglio di calcolo del designer utilizzando l'API Aspose.Cells for .NET e successivamente lo elaboreremo in base a una fonte dati creata in modo dinamico a scopo dimostrativo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Elaborazione del foglio di calcolo del designer

Per elaborare il foglio di calcolo del designer, è necessario disporre di una fonte dati che corrisponda ai marcatori intelligenti utilizzati nel foglio di calcolo del designer. Ad esempio, abbiamo creato un'entrata del marcatore intelligente come &=Sales.Year, che rappresenta la colonna Year nella DataTable Sales. Nel caso in cui una colonna corrispondente non sia disponibile nella fonte dati, le API di Aspose.Cells salteranno l'elaborazione per quel particolare marcatore intelligente e, di conseguenza, i dati per quel particolare marcatore intelligente non verranno popolati.

Per dimostrare questo caso d'uso, creeremo la fonte dati da zero e la elaboreremo in base al foglio di calcolo del designer creato nel passaggio precedente. Tuttavia, in uno scenario in tempo reale, i dati potrebbero già essere disponibili per ulteriore elaborazione, quindi è possibile saltare la creazione della fonte dati se i dati sono già disponibili.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

L'elaborazione dei marcatori intelligenti è abbastanza semplice come dimostrato dal seguente frammento di codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

Il frammento di codice sopra utilizza l'istanza esistente della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) creata nel primo passaggio. Se hai già il file di foglio di calcolo del designer su disco o in memoria, puoi creare un'istanza della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) caricando il foglio di calcolo del designer esistente.

{{% /alert %}}

## Creazione di un grafico

Una volta che i dati sono in posizione, tutto ciò di cui abbiamo bisogno è creare un grafico basato sulla fonte di dati. Per mantenere l'esempio semplice, useremo il metodo [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) in modo da non dover configurare ulteriormente il grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
