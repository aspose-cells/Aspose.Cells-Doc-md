---
title: Çalışma sayfanızı grafikler olmadan yüklemenize izin veren Aspose.Cells kullanmanıza olanak sağlar. Bu amaç için lütfen LoadOptions.LoadFilter özelliğini kullanın.
type: docs
weight: 750
url: /tr/java/load-source-excel-file-without-charts/
---

{{% alert color="primary" %}} 

Aspose.Cells, excel dosyanızı grafikler olmadan yüklemenize olanak tanır. Bu amaçla LoadOptions.LoadFilter özelliğini kullanınız.

{{% /alert %}} 
## **Grafikler olmadan kaynak excel dosyasını yükleme**
Aşağıdaki örnek kod, örnek excel dosyasını grafikler olmadan yükler ve çıktı olarak pdf formatında kaydeder.





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
