---
title: Load source excel file without charts
type: docs
weight: 750
url: /java/load-source-excel-file-without-charts/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells allows you to load your excel file without charts. Please use LoadOptions.LoadFilter property for this purpose.

{{% /alert %}} 
## **Load source excel file without charts**
The following sample code loads the sample excel file without charts and saves it in output pdf format.





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
