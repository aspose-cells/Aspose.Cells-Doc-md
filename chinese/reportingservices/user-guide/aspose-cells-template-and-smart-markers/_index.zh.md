---
title: Aspose.Cells 模板和智能标记
type: docs
weight: 30
url: /zh/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells 模板是包含智能标记的 Microsoft Excel 工作簿。智能标记充当报表项的数据占位符，并在呈现时替换为相应的数据。智能标记有五种类型，如下所列。所有标记都可以通过 Aspose.Cells.Report.Designer 插入到模板中。也可以手动编辑。

{{% /alert %}} 
### **智能标记**
#### **数据标记**
的格式**数据标记**是 &=DataSetName.FieldName。例如： &=SalesDetail.sales 其中 SalesDetail 是数据集或查询的名称，sales 是其中一个字段的名称。在呈现时，数据标记将替换为 Reporting Services 提供的数据集的值。
#### **Reporting Services 公式标记**
Reporting Services 的格式**公式标记**是 &= 表达式。例如：&=sum(SalesDetail.sales)/100。表达式由函数、数据集字段、运算符等组成。在渲染时。 Reporting Services 公式标记替换为计算值。
#### **Reporting Services 全局变量标记**
Reporting Services 的格式**全局变量标记**是 &= 全局变量！变量的名称。例如： &=Globals!ExecutionTime 其中 ExecutionTime 是全局变量的名称。全局变量标记在渲染时被替换为全局变量值。
#### **Reporting Services 参数标记**
报告参数有两个属性：值和标签。最后，**参数标记**有两种格式： &= 参数！ ParamName.Value 和 &=Parameters！参数名称.标签。它们分别表示参数的名称和标签。在渲染时，参数标记将替换为用户输入的参数值。
#### **动态公式**
为了对插入行进行计算，请使用动态公式。**动态公式**允许您将 Microsoft Excel 的公式插入到单元格中，即使公式引用了将在导出过程中插入的行。它们可以对每个插入的行重复，或者仅用于为它们放置数据标记的单元格。

动态公式的格式为&=&=RepeatDynamicFormula。

动态公式允许以下附加选项：

- {r} – 当前行号。
- {2}、{-1} – 当前行号的偏移量。

**重复的动态公式和生成的 Excel 工作表** 

![待办事项：图片_替代_文本](aspose-cells-template-and-smart-markers_1.png)
