---
title: 在加载Excel工作簿时过滤VBA项目
type: docs
weight: 70
url: /zh/java/filter-vba-project-while-loading-a-workbook/
---

## **可能的使用场景**
一些 .xlsm/.xslb 文件具有大量的宏（或非常非常长的宏）。当打开此类工作簿时，Aspose.Cells 将无条件地加载此（元）数据。但是，当您真正只需要提取大量工作簿的表格名称而跳过这种不需要的内容时，您可能需要通过LoadDataFilterOptions来控制。这个过滤器通过引入新选项LoadDataFilterOptions.VBA来提供。
## **示例代码**
以下示例代码加载工作簿，只过滤VBA。用于测试该功能的示例文件可以从以下链接下载：

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// 设置加载选项，我们不想加载 VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// 使用加载选项从示例 Excel 文件创建工作簿对象
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// 以 pdf 格式保存输出
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
