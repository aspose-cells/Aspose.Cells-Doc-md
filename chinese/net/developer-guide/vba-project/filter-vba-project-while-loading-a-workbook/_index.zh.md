---
title: 加载工作簿时筛选 VBA 项目
type: docs
weight: 140
url: /zh/net/filter-vba-project-while-loading-a-workbook/
---
## **在 C# 中加载 Excel 工作簿时筛选 VBA 项目**

一些 .xlsm/.xslb 文件有大量的宏（或非常非常长的宏）。 Aspose.Cells 在打开此类工作簿时将无条件加载此（元）数据。你可能需要控制这个[**加载数据过滤器选项**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)当您真的只需要为大量工作簿提取工作表名称从而跳过这些不需要的内容时。这个过滤器是通过引入一个新的选项来提供的，[**加载数据过滤器选项.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **示例代码**

以下示例代码加载一个工作簿，以便仅筛选 VBA。可以从以下链接下载用于测试此功能的示例文件：

[示例宏启用工作簿.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
