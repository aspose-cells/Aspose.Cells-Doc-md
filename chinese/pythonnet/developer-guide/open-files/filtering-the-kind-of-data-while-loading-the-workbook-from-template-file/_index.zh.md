---
title: 从模板文件加载工作簿时过滤数据类型
type: docs
weight: 400
url: /zh/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

有时，您希望在从模板文件构建工作簿时，指定加载何种类型的数据。过滤加载的数据可以提高您的特定用途的性能。请使用 [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) 属性实现此目的。

{{% /alert %}}

以下示例代码仅在从[模板文件](5115552.xlsx)加载工作簿时加载形状对象，您可以从给定链接下载模板文件。下面的屏幕截图显示了[模板文件](5115552.xlsx)的内容，并且解释了红色和黄色背景中的数据将不会被加载，因为[**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter)属性已设置为[**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

下面的屏幕截图显示了您可以从给定链接下载的[输出PDF](5115555.pdf)。在这里，您可以看到红色和黄色背景中的数据不存在，但所有形状都在那里。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

