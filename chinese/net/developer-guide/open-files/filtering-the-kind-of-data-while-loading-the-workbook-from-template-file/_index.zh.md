---
title: 在从模板文件构建工作簿时过滤数据类型
type: docs
weight: 400
url: /zh/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

有时，您希望在从模板文件构建工作簿时指定加载哪种数据。过滤加载的数据可以改善特定目的的性能，尤其是在使用[Lightcells APIs](/cells/zh/net/using-lightcells-api/)时。 请使用 [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) 属性来实现此目的。

{{% /alert %}}

以下示例代码仅加载形状对象，而不加载图表，它可以从给定链接下载的模板文件中加载。以下截图显示了模板文件的内容，并说明了红色数据和黄色背景数据不会被加载，因为已将[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)属性设置为[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

以下截图显示了可以从给定链接下载的输出PDF。在这里，您可以看到红色数据和黄色背景数据不存在，但所有形状都存在。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
