---
title: Загрузить исходный файл Excel без диаграмм
type: docs
weight: 750
url: /ru/java/load-source-excel-file-without-charts/
---
{{% alert color="primary" %}} 

Aspose.Cells позволяет загружать файл Excel без диаграмм. Для этой цели используйте свойство LoadOptions.LoadFilter.

{{% /alert %}} 
## **Загрузить исходный файл Excel без диаграмм**
Следующий пример кода загружает образец файла Excel без диаграмм и сохраняет его в выходном формате PDF.





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






