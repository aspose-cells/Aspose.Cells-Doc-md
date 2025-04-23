---
title: Загрузить исходный файл Excel без графиков
type: docs
weight: 750
url: /ru/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет загружать файл Excel без графиков. Пожалуйста, используйте свойство LoadOptions.LoadFilter для этой цели.

{{% /alert %}} 
## **Загрузить исходный файл Excel без графиков**
В следующем образце кода загружается образцовый файл Excel без графиков и сохраняется в формате выходного PDF.





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
