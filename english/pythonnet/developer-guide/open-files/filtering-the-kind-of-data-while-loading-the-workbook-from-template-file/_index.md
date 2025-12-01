---
title: Filtering the kind of data while loading the workbook from template file
type: docs
weight: 400
url: /python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve the performance for your special purpose. Please use the [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) property for this purpose.

{{% /alert %}}

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx) which you can download from the given link. The following screenshot shows the [template file](5115552.xlsx) contents and also explains that the data in Red color and Yellow background will not be loaded because [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) property has been set to [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

The following screenshot shows the [output PDF](5115555.pdf) which you can download from the given link. Here you can see, the data in Red color and Yellow background is not present but all shapes are there.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
