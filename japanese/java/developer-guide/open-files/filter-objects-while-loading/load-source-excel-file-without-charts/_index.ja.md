---
title: グラフなしでソース Excel ファイルを読み込む
type: docs
weight: 750
url: /ja/java/load-source-excel-file-without-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、グラフなしで Excel ファイルを読み込むことができます。この目的には LoadOptions.LoadFilter プロパティを使用してください。

{{% /alert %}} 
## **グラフなしでソース Excel ファイルを読み込む**
次のサンプル コードは、サンプルの Excel ファイルをグラフなしで読み込み、出力 pdf 形式で保存します。





{{< highlight "java" >}}

 //Specify the load options and filter the data

//We do not want to load charts

LoadOptions options = new LoadOptions();

options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options

Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format

workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);

{{< /highlight >}}






