---
title: Filtering the kind of data while loading the workbook from a template file with Golang via C++
linktitle: Filtering Data While Loading Workbook
type: docs
weight: 400
url: /go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Learn how to filter specific data types while loading a workbook from a template file using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve performance for your specific purpose, especially when using [LightCells APIs](/cells/cpp/using-lightcells-api/). Please use the [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) property for this purpose.

{{% /alert %}}

The following sample code loads only shape objects while loading the workbook from the [template file](5115552.xlsx) which you can download from the given link. The following screenshot shows the [template file](5115552.xlsx) contents and also explains that the data in red color and yellow background will not be loaded because the [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) property has been set to [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

The following screenshot shows the [output PDF](5115555.pdf) which you can download from the given link. Here you can see that the data in red color and yellow background is not present, but all shapes are there.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}