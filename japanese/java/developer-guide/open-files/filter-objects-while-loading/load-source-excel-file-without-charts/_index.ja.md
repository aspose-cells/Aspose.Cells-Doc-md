---
title: チャートなしでソースエクセルファイルをロード
type: docs
weight: 750
url: /ja/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用して、チャートなしでエクセルファイルをロードすることができます。この目的のためにLoadOptions.LoadFilterプロパティを使用してください。

{{% /alert %}} 
## **チャートなしでソースエクセルファイルをロード**
以下のサンプルコードは、サンプルのエクセルファイルをチャートなしでロードし、それを出力PDF形式で保存します。





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






{{< app/cells/assistant language="java" >}}
