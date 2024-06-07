---
title: 在加载工作簿时筛选 VBA 项目
type: docs
weight: 70
url: /zh/java/filter-vba-project-while-loading-a-workbook/
---

## **可能的使用场景**
一些.xlsm/.xslb文件具有大量的宏（或非常非常长的宏）。当打开此类工作簿时，Aspose.Cells将无条件加载这些（元数据）数据。然而，如果您只需为大量工作簿提取工作表名称而跳过这种不需要的内容，您可能需要通过LoadDataFilterOptions控制。这个过滤器是通过引入新的选项LoadDataFilterOptions.VBA提供的。
## **示例代码**
以下示例代码加载一个工作簿，使得只有VBA被过滤。用于测试此功能的示例文件可以从以下链接下载：

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// 设置加载选项，我们不需要加载VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// 使用加载选项从示例excel文件创建工作簿对象
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// 将输出保存为pdf格式
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
