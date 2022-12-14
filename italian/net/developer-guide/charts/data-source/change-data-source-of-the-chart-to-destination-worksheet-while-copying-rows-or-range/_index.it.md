---
title: Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli
type: docs
weight: 440
url: /it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Possibili scenari di utilizzo**

Quando copi righe o intervalli che contengono grafici in un nuovo foglio di lavoro, l'origine dati del grafico non cambia. Ad esempio, se l'origine dati del grafico è =Foglio1!$A$1:$B$4, dopo aver copiato le righe o l'intervallo nel nuovo foglio di lavoro, l'origine dati rimarrà la stessa, ovvero =Foglio1!$A$1:$B$4. Si riferisce ancora al vecchio foglio di lavoro, ad esempio Foglio1. Questo è anche il comportamento in Microsoft Excel. Ma se vuoi che faccia riferimento al nuovo foglio di lavoro di destinazione, usa il file[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet)proprietà e impostarlo su**VERO** mentre si chiama il[**Cells.CopyRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)metodo. Ora, se il foglio di lavoro di destinazione è DestSheet, l'origine dati del grafico cambierà da =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.

## **Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli**

 Il seguente codice di esempio spiega l'utilizzo di[**CopyOptions.ReferToDestinationSheet**](https://reference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) proprietà durante la copia di righe o intervalli contenenti grafici in un nuovo foglio di lavoro. Il codice utilizza il[file excel di esempio](5113699.xlsx) e genera il[file excel di output](5113697.xlsx).

![cose da fare:immagine_alt_testo](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
