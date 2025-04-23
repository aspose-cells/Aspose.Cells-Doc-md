---
title: 从模板文件加载工作簿时过滤数据类型
type: docs
weight: 680
url: /zh/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

有时，您希望在从模板文件构建工作簿时指定应加载的数据类型。过滤加载的数据可以提高您的特定目的的性能，尤其在使用 [LightCells APIs](/cells/zh/java/using-lightcells-api/) 时。请使用 [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) 属性来实现此目的。

{{% /alert %}} 
## **从模板文件加载工作簿时过滤数据类型**
以下示例代码仅在从给定链接下载的[template file](5472556.xlsx)中加载形状对象时加载工作簿。

以下屏幕截图显示了[模板文件](5472556.xlsx)的内容，并说明了因为已设置[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) 属性为 [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)，所以红色和黄色背景的数据将不会加载。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

以下屏幕截图显示了从给定链接下载的[output PDF](5472554.pdf)。在这里，你可以看到红色和黄色背景的数据不存在，但所有形状都在。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
