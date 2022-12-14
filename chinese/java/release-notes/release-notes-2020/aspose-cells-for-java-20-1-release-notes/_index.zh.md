---
title: Aspose.Cells for Java 20.1 发行说明
type: docs
weight: 60
url: /zh/java/aspose-cells-for-java-20-1-release-notes/
---
{{% alert color="primary" %}}

此页面包含发行说明[Aspose.Cells for Java 20.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.1/).

{{% /alert %}}

|**钥匙**|**概括**|**类别**|
|:- |:- |:- |
|CELLSJAVA-41325|Cell.getValidation 方法为 ODS 返回 null|新功能|
|CELLSJAVA-43074|XLSX 到 PDF，使用 Oracle JDK 与 Open JDK 时 PDF 输出的差异|强化|
|CELLSJAVA-43083|不透明度未应用于柱形图|漏洞|
|CELLSJAVA-41879|%of、%of Row、%of ParentRowTotal、%ParentTotal 等在 pivot excel 输出中不起作用|漏洞|
|CELLSJAVA-43062|Cell 的默认背景颜色在输出 HTML 中是错误的|漏洞|
|CELLSJAVA-43063|SheetRender.toImage() 输出不正确|漏洞|
|CELLSJAVA-43070|calculateFormula() 不计算值|漏洞|
|CELLSJAVA-43086|百分比格式样式在挪威语言环境下应用不正确|漏洞|
|CELLSJAVA-43082|表格第一行中呈现的较小字体|漏洞|
|CELLSJAVA-41360|Cells 公式在PDF中显示，而在ODS中不显示|漏洞|
|CELLSJAVA-42786|ODS 到 XLSX - 折线图丢失线条和图例条目|漏洞|
|CELLSJAVA-42788|ODS 到 XLSX - 圆变成方|漏洞|
|CELLSJAVA-43073|无法在工作簿中访问 DataMashup 信息|漏洞|
|CELLSJAVA-43092|无法处理 Excel 文件|漏洞|

## **公共 API 和向后不兼容的更改**
以下是对公众 API 所做的任何更改的列表，例如添加、重命名、删除或弃用成员，以及对 Aspose.Cells for Java 所做的任何非向后兼容更改。如果您对列出的任何更改有疑虑，请在Aspose.Cells 支持论坛。
### **添加 ReplaceOptions.RegexKey 属性。**
指示搜索的键是否为正则表达式。如果**真的**然后搜索到的键（要替换的部分）将被视为用户指定的正则表达式。
### **删除过时的 ValidationCollection.Add(Aspose.Cells.Validation) 方法。**
请改用 ValidationCollection.Add(CellArea) 方法。
### **添加 PowerQueryFormula.FormulaDefinition 属性。**
获取幂查询公式的定义。
### **添加 DBConnection.PowerQueryFormula 属性。**
获取幂查询公式的定义。
### **添加 HtmlSaveOptions.ExportHeadings 属性。**
指示在将文件保存为 HTML 时是否导出标题。默认值为假。如果要将 HTML 文件导入 excel，请保持默认值。
### **添加 XAdESType 类**
XML 高级电子签名 (XAdES) 的类型。
### **添加 DigitalSignature.XAdESType 属性**
获取和设置 XML 高级电子签名 (XAdES) 的类型。默认值为无（XAdES 关闭）。
