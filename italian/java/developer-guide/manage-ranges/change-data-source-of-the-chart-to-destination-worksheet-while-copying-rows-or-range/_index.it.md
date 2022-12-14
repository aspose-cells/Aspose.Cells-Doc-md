---
title: Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli
type: docs
weight: 850
url: /it/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Possibili scenari di utilizzo**
Quando copi righe o intervalli che contengono grafici in un nuovo foglio di lavoro, l'origine dati del grafico non cambia. Ad esempio, se l'origine dati del grafico è =Foglio1!$A$1:$B$4, dopo aver copiato le righe o l'intervallo nel nuovo foglio di lavoro, l'origine dati rimarrà la stessa, ovvero =Foglio1!$A$1:$B$4. Si riferisce ancora al vecchio foglio di lavoro, ad esempio Foglio1. Questo è anche il comportamento di Excel Microsoft. Ma se vuoi che faccia riferimento al nuovo foglio di lavoro di destinazione, usa la proprietà CopyOptions.ReferToDestinationSheet e impostala su true mentre chiami il metodo Cells.CopyRows(). Ora, se il foglio di lavoro di destinazione è DestSheet, l'origine dati del grafico cambierà da =Sheet1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.
## **Cambia l'origine dati del grafico nel foglio di lavoro di destinazione durante la copia di righe o intervalli**
Il codice di esempio seguente illustra l'utilizzo della proprietà CopyOptions.ReferToDestinationSheet durante la copia di righe o intervalli contenenti il grafico in un nuovo foglio di lavoro. Il codice utilizza il[file excel di esempio](5472284.xlsx) e genera il[file excel di output](5472283.xlsx) . Lo screenshot mostra che l'origine dati del grafico in[file excel di output](5472283.xlsx) ora si riferisce a DestSheet anziché a Sheet1.

![cose da fare:immagine_alt_testo](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






