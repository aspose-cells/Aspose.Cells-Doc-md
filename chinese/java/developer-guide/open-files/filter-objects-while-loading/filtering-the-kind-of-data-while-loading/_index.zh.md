---
title: 在从模板文件构建工作簿时过滤数据类型
type: docs
weight: 680
url: /zh/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

有时，您希望指定在从模板文件构建工作簿时应加载哪种数据。过滤加载的数据可以提高特定目的的性能，特别是在使用[LightCells APIs](/cells/zh/java/using-lightcells-api/)时。请使用[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)属性来实现此目的。

{{% /alert %}} 
## **在从模板文件加载工作簿时过滤数据类型**
以下示例代码在从给定链接下载的[模板文件](5472556.xlsx)加载工作簿时仅加载形状对象。

以下屏幕截图显示了[模板文件](5472556.xlsx)的内容，并解释了红色数据和黄色背景的数据将不被加载，因为已将[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)属性设置为[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

以下屏幕截图显示了从给定链接下载的[输出 PDF](5472554.pdf)。您可以看到，红色数据和黄色背景数据不在其中，但所有形状都在其中。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
