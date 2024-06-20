---
title: Cargar archivo de Excel fuente sin gráficos
type: docs
weight: 750
url: /es/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells te permite cargar tu archivo de Excel sin gráficos. Utiliza la propiedad LoadOptions.LoadFilter para este propósito.

{{% /alert %}} 
## **Cargar archivo de Excel fuente sin gráficos**
El siguiente código de ejemplo carga el archivo de Excel de muestra sin gráficos y lo guarda en formato PDF de salida.





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






