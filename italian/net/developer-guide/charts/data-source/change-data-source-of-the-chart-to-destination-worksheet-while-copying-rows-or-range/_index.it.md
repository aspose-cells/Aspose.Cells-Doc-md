---
title: Cambia origine dati del grafico al foglio di lavoro di destinazione durante la copia di righe o intervalli
description: Scopri come modificare la fonte dati di un grafico a un foglio di lavoro di destinazione durante la copia di righe o di un intervallo in Aspose.Cells for .NET. La nostra guida ti mostrerà come aggiornare l intervallo di dati del grafico e collegarlo al foglio di lavoro di destinazione, garantendo che le righe o l intervallo copiato siano riflessi con precisione nel grafico.
keywords: Aspose.Cells for .NET, creazione di grafici, fonte dati, foglio di lavoro di destinazione, righe, intervallo, copia, aggiornamento, intervallo di dati, collegamento.
type: docs
weight: 440
url: /it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possibili Scenari di Utilizzo**

Quando si copiano righe o intervalli che contengono grafici in un nuovo foglio di lavoro, la fonte dati del grafico non cambia. Ad esempio, se la fonte dati del grafico è =Foglio1!$A$1:$B$4, allora dopo aver copiato righe o un intervallo in un nuovo foglio di lavoro, la fonte dati rimarrà la stessa, cioè =Foglio1!$A$1:$B$4. Si fa ancora riferimento al vecchio foglio di lavoro, cioè Foglio1. Questo è anche il comportamento in Microsoft Excel. Ma se vuoi che faccia riferimento al nuovo foglio di lavoro di destinazione, allora utilizza la proprietà [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) e impostala su **true** durante la chiamata del metodo [**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index). Ora se il tuo foglio di lavoro di destinazione è DestSheet, allora la fonte dati del tuo grafico cambierà da =Foglio1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo**

Il codice di esempio seguente spiega l'uso della proprietà [**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) durante la copia di righe o intervalli contenenti grafici in un nuovo foglio di lavoro. Il codice utilizza il [file Excel di esempio](5113699.xlsx) e genera l'[output del file Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
