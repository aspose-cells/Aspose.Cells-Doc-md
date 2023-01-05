---
title: 加载工作簿时筛选 VBA 项目
type: docs
weight: 70
url: /zh/java/filter-vba-project-while-loading-a-workbook/
---
## **可能的使用场景**
某些 .xlsm/.xslb 文件具有非常大量的宏（或非常非常长的宏）。 Aspose.Cells 在打开此类工作簿时将无条件加载此（元）数据。您可能需要通过 LoadDataFilterOptions 来控制这一点，当您真的只需要为大量工作簿提取工作表名称时，从而跳过这些不需要的内容。此过滤器是通过引入新选项 LoadDataFilterOptions.VBA 提供的。
## **示例代码**
以下示例代码加载一个工作簿，以便仅筛选 VBA。可以从以下链接下载用于测试此功能的示例文件：

[示例宏启用工作簿.xlsm](79527951.xlsm)

//设置加载选项，我们不想加载VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// 使用加载选项从示例 excel 文件创建工作簿对象
工作簿 book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// 以pdf格式保存输出
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
