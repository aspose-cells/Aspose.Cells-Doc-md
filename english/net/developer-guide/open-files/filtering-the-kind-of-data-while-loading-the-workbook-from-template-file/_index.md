---
title: Filtering the kind of data while loading the workbook from template file
type: docs
weight: 400
url: /net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve performance for your specific purpose, especially when using [LightCells APIs](/cells/net/using-lightcells-api/). Please use the [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) property for this purpose.

{{% /alert %}}

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx), which you can download from the given link. The following screenshot shows the [template file](5115552.xlsx) contents and also explains that the data in red color and yellow background will not be loaded because the [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) property has been set to [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

The following screenshot shows the [output PDF](5115555.pdf), which you can download from the given link. Here you can see that the data in red color and yellow background is not present, but all shapes are there.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
