---
title: Carica file excel di origine senza grafici
type: docs
weight: 750
url: /it/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells consente di caricare il file excel di origine senza grafici. Si prega di utilizzare la proprietà di caricamento LoadOptions.LoadFilter a tale scopo.

{{% /alert %}} 
## **Carica file excel di origine senza grafici**
Il codice di esempio seguente carica l'esempio di file excel senza grafici e lo salva in formato pdf di output.





{{< highlight java >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






