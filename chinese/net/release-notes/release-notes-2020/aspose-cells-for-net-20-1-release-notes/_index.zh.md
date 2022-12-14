---
title: Aspose.Cells for .NET 20.1 发行说明
type: docs
weight: 70
url: /zh/net/aspose-cells-for-net-20-1-release-notes/
---
{{% alert color="primary" %}} 

此页面包含发行说明[Aspose.Cells for .NET 20.1](https://www.nuget.org/packages/Aspose.Cells/20.1.0).

{{% /alert %}} 

|**钥匙**|**概括**|**类别**|
|:- |:- |:- |
|CELLSNET-47026|支持“Rank Smallest to Largest”和“Rank Largest to Smallest”显示格式选项|新功能|
|CELLSNET-47030|保存为 HTML 时显示标题|新功能|
|CELLSNET-47089|支持DataField的所有数据显示格式|新功能|
|CELLSNET-47062|支持 STDEV.P 和 STDEV.S|新功能|
|CELLSNET-47070|使用选项支持类似于 Find() 的 Replace 函数中的 Regex|新功能|
|CELLSNET-46998|支持 XAdES 签名|新功能|
|CELLSNET-40174|在图表类型表中插入复选框|新功能|
|CELLSNET-43089|在将 ODS 转换为 XLSX 时支持条件格式|新功能|
|CELLSNET-43090|在将 ODS 转换为 XLSX 格式时支持数据验证|新功能|
|CELLSNET-47064|支持 .xlsx 文件图表中的形状。|强化|
|CELLSNET-47065|从 DataConnections 获取 PowerQuery|强化|
|CELLSNET-47066|获取类似于 MS Excel 的格式化 PowerQuery MCode|强化|
|CELLSNET-47008|以特定角度渲染图表图像时出现问题|漏洞|
|CELLSNET-47063|未安装字体时将 Excel 渲染到打印机问题|漏洞|
|CELLSNET-44237|数据透视表的数据字段的降序|漏洞|
|CELLSNET-47002|计算值显示为“#REF!”在生成的 PDF 中|漏洞|
|CELLSNET-47050|第一页上的某些字段未出现在输出 PDF 中|漏洞|
|CELLSNET-40733|打开 Office .ods 文件 - 条件格式不会保留|漏洞|
|CELLSNET-47039|ODS 文件中的 XY 散点图无法正常呈现|漏洞|
|CELLSNET-47040|ODS 文件中的网络图表未正确呈现|漏洞|
|CELLSNET-47060|支持自定义ods文件标题的XY|漏洞|
|CELLSNET-47072|Aspose.Cells抓取的Link路径与Excel的区别|漏洞|
|CELLSNET-47087|打印Aspose.Cells保存的excel文件时出现问题 for .NET|漏洞|
|CELLSNET-47082|公式计算挂起|漏洞|
### **公共 API 和向后不兼容的更改**
以下是对公众 API 所做的任何更改的列表，例如添加、重命名、删除或弃用成员，以及对 Aspose.Cells for .NET 所做的任何非向后兼容更改。如果您对列出的任何更改有疑虑，请在Aspose.Cells 支持论坛。
#### **添加 ReplaceOptions.RegexKey 属性。**
指示搜索的键是否为正则表达式。如果**真的**然后搜索到的键（要替换的部分）将被视为用户指定的正则表达式。
#### **添加 CustomImplementationFactory.CreateCultureInfo 方法。**
用户环境可能不支持某些文化。为避免此类情况出现异常，用户可以覆盖此方法以提供有效的 CultureInfo 实例。
#### **删除过时的 ValidationCollection.Add(Aspose.Cells.Validation) 方法。**
请改用 ValidationCollection.Add(CellArea) 方法。
#### **添加 PowerQueryFormula.FormulaDefinition 属性。**
获取幂查询公式的定义。
#### **添加 DBConnection.PowerQueryFormula 属性。**
获取幂查询公式的定义。
#### **添加 HtmlSaveOptions.ExportHeadings 属性。**
指示在将文件保存为 HTML 时是否导出标题。默认值为**错误的**.如果要将 HTML 文件导入 excel，请保持默认值。
#### **添加 XAdESType 类**
XML 高级电子签名 (XAdES) 的类型。
#### **添加 DigitalSignature.XAdESType 属性**
获取和设置 XML 高级电子签名 (XAdES) 的类型。默认值为无（XAdES 关闭）。
