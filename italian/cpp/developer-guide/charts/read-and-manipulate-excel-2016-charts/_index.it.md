---
title: Leggere e manipolare grafici Excel 2016
type: docs
weight: 20
url: /it/cpp/read-and-manipulate-excel-2016-charts/
---
##  **Possibili scenari di utilizzo**
Aspose.Cells supporta la lettura e la manipolazione dei grafici Microsoft Excel 2016 che non sono presenti in Microsoft Excel 2013 o versioni precedenti.
##  **Leggere e manipolare grafici Excel 2016**
 Il codice di esempio seguente carica il file[file Excel di esempio](66519072.xlsx) che contiene i grafici di Excel 2016 nel primo foglio di lavoro. Legge tutti i grafici uno per uno e cambia il titolo in base al tipo di grafico. La schermata seguente mostra il file Excel di esempio prima dell'esecuzione del codice. Come puoi vedere, il titolo del grafico è lo stesso per tutti i grafici.

![cose da fare:immagine_alt_testo](read-and-manipulate-excel-2016-charts_1.png)

 La seguente schermata mostra il[file Excel di output](66519073.xlsx) dopo l'esecuzione del codice. Come puoi vedere, il titolo del grafico viene modificato in base al tipo di grafico.

![cose da fare:immagine_alt_testo](read-and-manipulate-excel-2016-charts_2.png)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-ReadAndManipulateExcel2016Charts-new.cpp" >}}
##  **Uscita della console**
Ecco l'output della console del codice di esempio riportato sopra quando eseguito con il file Excel di esempio fornito.

{{< highlight "java" >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}
