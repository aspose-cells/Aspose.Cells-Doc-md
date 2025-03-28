---
title: Filtering the kind of data while loading the workbook from template file
type: docs
weight: 680
url: /java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Sometimes, you want to specify which kind of data should be loaded when building the workbook from a template file. Filtering loaded data can improve the performance for your special purpose, especially when using [LightCells APIs](/cells/java/using-lightcells-api/). Please use the [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) property for this purpose.

{{% /alert %}} 
## **Filtering the kind of data while loading the workbook from a template file**
The following sample code loads only shape objects while loading the workbook from the [template file](5472556.xlsx) which you can download from the given link.

The following screenshot shows the [template file](5472556.xlsx) contents and also explains that the data in Red color and Yellow background will not be loaded because the [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) property has been set to [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

The following screenshot shows the [output PDF](5472554.pdf) which you can download from the given link. Here you can see, the data in Red color and Yellow background is not present but all shapes are there.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}