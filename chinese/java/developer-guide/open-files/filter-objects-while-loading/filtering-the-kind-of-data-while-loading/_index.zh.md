---
title: 从模板文件加载工作簿时过滤数据类型
type: docs
weight: 680
url: /zh/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

有时，您希望指定在从模板文件构建工作簿时应加载哪种数据。过滤加载的数据可以提高您的特殊用途的性能，尤其是在使用时[LightCells API](/cells/zh/java/using-lightcells-api/) .请使用[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)为此目的的财产。

{{% /alert %}} 
## **从模板文件加载工作簿时筛选数据类型**
以下示例代码在从[模板文件](5472556.xlsx)您可以从给定的链接下载。

以下屏幕截图显示了[模板文件](5472556.xlsx)内容并解释了红色和黄色背景的数据将不会被加载，因为[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)属性已设置为[加载数据过滤器选项.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![待办事项：图像_替代_文本](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

以下屏幕截图显示了[输出PDF](5472554.pdf)您可以从给定的链接下载。在这里您可以看到，红色和黄色背景的数据不存在，但所有形状都在那里。

![待办事项：图像_替代_文本](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
