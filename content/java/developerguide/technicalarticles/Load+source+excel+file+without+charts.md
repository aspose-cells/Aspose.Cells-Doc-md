+++
title = "Load source excel file without charts" 
description = "" 
weight = 12542 
+++

Aspose.Cells for Java : Load source excel file without charts  

# Aspose.Cells for Java : Load source excel file without charts


Aspose.Cells allows you to load your excel file without charts. Please use `LoadOptions.LoadFilter` property for this purpose.

#### Load source excel file without charts

The following sample code loads the sample excel file without charts and saves it in output pdf format.


{{< code lang="cs" >}}
//Specify the load options and filter the data
//We do not want to load charts
LoadOptions options = new LoadOptions();
options.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART));

//Load the workbook with specified load options
Workbook workbook = new Workbook("sample.xlsx", options);

//Save the workbook in output format
workbook.save("LoadExcelFileWithoutChart_out.pdf", SaveFormat.PDF);
{{< /code >}}

