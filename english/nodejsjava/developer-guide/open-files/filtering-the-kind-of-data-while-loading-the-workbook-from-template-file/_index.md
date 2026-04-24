---
title: Filtering the kind of data while loading the workbook from template file
type: docs
weight: 400
url: /nodejs-java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve performance for your specific purpose, especially when using [LightCells APIs](/cells/nodejs-java/using-lightcells-api/). Please use the [**LoadOptions.setLoadFilter()**](https://reference.aspose.com/cells/nodejs/LoadOptions#setLoadFilter) method for this purpose.

{{% /alert %}}

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx), which you can download from the given link. The following screenshot shows the [template file](5115552.xlsx) contents and also explains that the data in red color and yellow background will not be loaded because the [**LoadOptions.setLoadFilter()**](https://reference.aspose.com/cells/nodejs/LoadOptions#setLoadFilter) method has been set to **aspose.cells.LoadDataFilterOptions.ALL & ~aspose.cells.LoadDataFilterOptions.CELL_DAT**.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

The following screenshot shows the [output PDF](5115555.pdf), which you can download from the given link. Here you can see that the data in red color and yellow background is not present, but all shapes are there.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "Examples-Articles-FilterDataWhileLoadingWorkbook-1.js" >}}
<!--{{< app/cells/assistant language="csharp" >}}-->