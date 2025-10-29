---
title: 用Golang通过C++在从模板文件加载工作簿时过滤数据类型
linktitle: 加载工作簿时的过滤数据
type: docs
weight: 400
url: /zh/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: 学习如何使用Aspose.Cells通过Golang via C++在加载模板文件时过滤特定数据类型。
---

{{% alert color="primary" %}}

有时，您希望在从模板文件构建工作簿时指定要加载的数据类型。过滤加载的数据可以提升性能，特别是在使用 [LightCells APIs](/cells/zh/cpp/using-lightcells-api/) 时。请使用 [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) 属性实现此功能。

{{% /alert %}}

以下示例代码仅在从[模板文件](5115552.xlsx)加载工作簿时加载形状对象，您可以从给定链接下载模板文件。下面的屏幕截图显示了[模板文件](5115552.xlsx)的内容，并且解释了红色和黄色背景中的数据将不会被加载，因为[**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/)属性已设置为[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

下面的屏幕截图显示了您可以从给定链接下载的[输出PDF](5115555.pdf)。在这里，您可以看到红色和黄色背景中的数据不存在，但所有形状都在那里。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
