---
title: 加载源Excel文件而无图表
type: docs
weight: 750
url: /zh/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells允许您加载不含图表的Excel文件。请使用LoadOptions.LoadFilter属性来实现此目的。

{{% /alert %}} 
## **加载源Excel文件而无图表**
以下示例代码加载不含图表的示例Excel文件，并将其保存为输出PDF格式。





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






