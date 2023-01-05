---
title: 加载不带图表的源 excel 文件
type: docs
weight: 750
url: /zh/java/load-source-excel-file-without-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells 允许您加载没有图表的 excel 文件。为此，请使用 LoadOptions.LoadFilter 属性。

{{% /alert %}} 
## **加载不带图表的源 excel 文件**
以下示例代码加载不带图表的示例 excel 文件，并将其保存为输出 pdf 格式。





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






