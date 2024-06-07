---
title: 在加载工作簿时筛选 VBA 项目
type: docs
weight: 140
url: /zh/net/filter-vba-project-while-loading-a-workbook/
---

## **在 C# 中加载 Excel 工作簿时筛选 VBA 项目**

有些 .xlsm/.xslb 文件包含大量宏（或非常长的宏）。当打开这样的工作簿时，Aspose.Cells 将无条件加载此（元）数据。 您可能需要通过 [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) 来控制此操作，当您真正只需要提取大量工作簿的工作表名称时，从而跳过这些不需要的内容。 通过引入一个新选项 [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)，提供此筛选功能。

## **示例代码**

下面的示例代码加载工作簿，从而仅筛选 VBA。 您可以从以下链接下载用于测试此功能的示例文件。

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
