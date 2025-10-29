---
title: 在加载工作簿时用Golang via C++过滤VBA项目
linktitle: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 140
url: /zh/go-cpp/filter-vba-project-while-loading-a-workbook/
description: 学习如何使用Aspose.Cells在加载Excel工作簿时用Golang via C++过滤VBA项目
---

## **用C++在加载Excel工作簿时过滤VBA项目**

一些.xlsm/.xslb文件包含大量宏（或非常长的宏）。Aspose.Cells在打开此类工作簿时会无条件加载这些（元）数据。当你只需要提取工作表名称时，可以通过[**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions)控制这个过程，以跳过不需要的内容。此过滤器通过引入新的选项[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions)实现。

## **示例代码**

以下示例代码加载工作簿，仅过滤 VBA。可以从以下链接下载用于测试此功能的示例文件：

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
