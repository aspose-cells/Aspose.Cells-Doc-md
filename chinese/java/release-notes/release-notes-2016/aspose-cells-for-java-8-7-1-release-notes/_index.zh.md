---
title: Aspose.Cells for Java 8.7.1 发行说明
type: docs
weight: 130
url: /zh/java/aspose-cells-for-java-8-7-1-release-notes/
---
## **其他改进和变化**

|**钥匙** |**概括** |**类别** |
|:- |:- |:- |
|CELLSJAVA-41747 |支持计算FORMULATEXT函数|新功能|
|CELLSJAVA-41702 |在输出 HTML 文件中添加了额外的列|漏洞|
|CELLSJAVA-41708 |列从 HTML 输出中丢失|漏洞|
|CELLSJAVA-41720 |在将电子表格转换为 HTML 时以 SVG 格式保存图像会导致图像文件扩展名不正确|漏洞|
|CELLSJAVA-41721 |将电子表格转换为 HTML 时形状中的文本呈现不正确|漏洞|
|CELLSJAVA-41711 |保存为 HTML 时出现无限循环问题|漏洞|
|CELLSJAVA-41737 |Cell.DateTime 类型的 getStringValue 给出了不需要的值|漏洞|
|CELLSJAVA-41681 |使用 Chart.toImage 时图表标题超出图表边界|漏洞|
|CELLSJAVA-41691 |数据标签与图表图像格式的图表区域重叠|漏洞|
|CELLSJAVA-41692 |数据标签与图表 PDF 文件格式的图表区域重叠|漏洞|
|CELLSJAVA-41696 |Chart 的 PDF 文件格式中缺少底部和右侧边框|漏洞|
|CELLSJAVA-41712 |条形图的 PDF 中呈现的颜色不正确|漏洞|
|CELLSJAVA-41722 |Acrobat Reader 在加载 Aspose.Cells' 生成的 PDF 时显示错误|漏洞|
|CELLSJAVA-41724 |系列在 SVG 中完全不透明，与电子表格中的原始图表相反|漏洞|
|CELLSJAVA-41725 |SVG 图像与电子表格中的原始图表不同|漏洞|
|CELLSJAVA-41727 |DataLabel 的图片或纹理填充效果还没有渲染成 SVG|漏洞|
|CELLSJAVA-41728 |生成的 SVG 文件大小为 0KB|漏洞|
|CELLSJAVA-41741 |图片到 SVG 呈现空白/错误图像|漏洞|
|CELLSJAVA-41743 |输出 pdf 中缺少图形标题|漏洞|
|CELLSJAVA-41714 |FileFormatUtil.loadFormatToExtension 为 .ODP 文件返回 .ODS|漏洞|
|CELLSJAVA-41715 |重新保存 PerformanceReport.xlsb 后 Excel 2007 中的内容不可读|漏洞|
|CELLSJAVA-41731 |将 XLS 保存为 XLSB 时形状公式不刷新|漏洞|
|CELLSJAVA-41733 |Cell.getFormula 返回方括号中的工作表名称和电子表格文件路径的公式|漏洞|
|CELLSJAVA-41732 |异常：Workbook.calculateFormula() 方法上的“[0]Sheet1!B2-无效公式：堆栈中有多个标记”|例外|
## **公共 API 和向后不兼容的更改**
以下是对公众 API 所做的任何更改的列表，例如添加、重命名、删除或弃用成员，以及对 Aspose.Cells for Java 所做的任何非向后兼容更改。如果您对列出的任何更改有疑虑，请在Aspose.Cells 支持论坛。
### **添加 LookInType.OriginalValues 属性。**
仅从没有格式的原始值中查找对象。
## **笔记**
由于 Aspose.Cells for Java 的代码库与相关 .NET 版本的代码匹配，因此 Aspose.Cells for .NET v8.7.1 中包含的大部分更改、增强和修复也包含在此 Aspose.Cells for Java v8.7.1 中。
