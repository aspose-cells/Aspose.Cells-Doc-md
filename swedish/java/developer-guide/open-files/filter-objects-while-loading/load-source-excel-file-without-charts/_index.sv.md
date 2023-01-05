---
title: Ladda källexcel-fil utan diagram
type: docs
weight: 750
url: /sv/java/load-source-excel-file-without-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells låter dig ladda din excel-fil utan diagram. Använd egenskapen LoadOptions.LoadFilter för detta ändamål.

{{% /alert %}} 
## **Ladda källexcel-fil utan diagram**
Följande exempelkod laddar excel-exempelfilen utan diagram och sparar den i utdata-pdf-format.





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






