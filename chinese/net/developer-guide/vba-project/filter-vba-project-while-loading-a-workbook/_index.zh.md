---
title: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 140
url: /zh/net/filter-vba-project-while-loading-a-workbook/
---

## **在C#中加载Excel工作簿时过滤VBA项目**

一些 .xlsm/.xslb 文件包含极其大量的宏（或者非常非常长的宏）。Aspose.Cells 在打开这样的工作簿时将无条件加载这些（元）数据。但是在需要提取大量工作簿的工作表名称时可能需要控制此行为 [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)，从而跳过这些不需要的内容。为此，引入了一个新选项，[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)。

## **示例代码**

以下示例代码加载工作簿，仅过滤 VBA。可以从以下链接下载用于测试此功能的示例文件：

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
