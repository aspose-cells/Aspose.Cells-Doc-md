---
title: Modifica l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervallo
description: Scopri come modificare l'origine dati di un grafico in un foglio di lavoro di destinazione mentre copi righe o un intervallo in Aspose.Cells for .NET. La nostra guida ti mostrerà come aggiornare l'intervallo di dati del grafico e collegarlo al foglio di lavoro di destinazione, assicurando che le righe copiate o intervallo si riflettono accuratamente nel grafico.
keywords: Aspose.Cells for .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
##  **Possibili scenari di utilizzo**

Quando copi righe o un intervallo che contiene grafici in un nuovo foglio di lavoro, l'origine dati del grafico non cambia. Ad esempio, se l'origine dati del grafico è =Foglio1!$A$1:$B$4, dopo aver copiato le righe o l'intervallo nel nuovo foglio di lavoro, l'origine dati rimarrà la stessa, ovvero =Foglio1!$A$1:$B$4. Si riferisce ancora al vecchio foglio di lavoro, ovvero al Foglio1. Questo è anche il comportamento in Microsoft Excel. Ma se vuoi che faccia riferimento al nuovo foglio di lavoro di destinazione, utilizza il file[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)proprietà e impostarla su**VERO** mentre chiami il[**Cells.CopiaRighe()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)metodo. Ora se il tuo foglio di lavoro di destinazione è DestSheet, l'origine dati del tuo grafico cambierà da =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

##  **Modifica l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervallo**

Il seguente codice di esempio spiega l'utilizzo di[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) proprietà durante la copia di righe o intervalli contenenti grafici in un nuovo foglio di lavoro. Il codice utilizza il[file Excel di esempio](5113699.xlsx) e genera il[file Excel di output](5113697.xlsx).

![cose da fare:immagine_alt_testo](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
