---
title: Ladda käll excel filen utan diagram
type: docs
weight: 750
url: /sv/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells tillåter dig att ladda din excelfil utan diagram. Använd LoadOptions.LoadFilter-egenskapen för detta ändamål.

{{% /alert %}} 
## **Ladda käll-excel-filen utan diagram**
Följande kodexempel laddar käll-excel-filen utan diagram och sparar den i utmatnings-pdf-format.





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
