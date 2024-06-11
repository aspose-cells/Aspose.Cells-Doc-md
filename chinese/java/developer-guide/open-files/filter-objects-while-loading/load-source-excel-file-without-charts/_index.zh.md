---
title: 无图表加载源Excel文件
type: docs
weight: 750
url: /zh/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells允许你加载没有图表的Excel文件。请使用LoadOptions.LoadFilter属性来实现这一目的。

{{% /alert %}} 
## **无图表加载源Excel文件**
以下示例代码加载没有图表的样本Excel文件，并将其保存为输出PDF格式。





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






