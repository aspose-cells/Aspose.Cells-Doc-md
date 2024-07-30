---
title: Cambia origine dati del grafico al foglio di lavoro di destinazione durante la copia di righe o intervalli
type: docs
weight: 850
url: /it/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possibili Scenari di Utilizzo**
Quando si copiano righe o intervalli che contengono grafici in un nuovo foglio di lavoro, l'origine dati del grafico non cambia. Ad esempio, se l'origine dati del grafico è =Foglio1!$A$1:$B$4, allora dopo la copia di righe o intervalli nel nuovo foglio di lavoro, l'origine dati rimarrà la stessa, cioè =Foglio1!$A$1:$B$4. Si fa sempre riferimento al vecchio foglio di lavoro cioè Foglio1. Questo è anche il comportamento di Microsoft Excel. Ma se si vuole che faccia riferimento al nuovo foglio di lavoro di destinazione, utilizzare la proprietà CopyOptions.ReferToDestinationSheet e impostarla su true durante la chiamata al metodo Cells.CopyRows(). Ora se il foglio di lavoro di destinazione è DestSheet, l'origine dati del tuo grafico cambierà da =Foglio1!$A$1:$B$4 a =DestSheet!$A$1:$B$4.
## **Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo**
Il codice di esempio seguente spiega l'uso della proprietà CopyOptions.ReferToDestinationSheet durante la copia di righe o intervalli contenenti il grafico in un nuovo foglio di lavoro. Il codice utilizza il [file di esempio Excel](5472284.xlsx) e genera il [file di Excel di output](5472283.xlsx). La schermata mostra che l'origine dati del grafico nel [file di Excel di output](5472283.xlsx) ora si riferisce a DestSheet anziché Sheet1.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






