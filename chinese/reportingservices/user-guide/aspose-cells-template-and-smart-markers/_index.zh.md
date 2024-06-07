---
title: Aspose.Cells 模板和智能标记
type: docs
weight: 30
url: /zh/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells 模板是包含智能标记的 Microsoft Excel 工作簿。智能标记是报表元素的数据占位符，在渲染时将被相应的数据替换。智能标记有五种类型，如下所列。所有标记都可以由 Aspose.Cells.Report.Designer 插入模板。也可以手动编辑。 

{{% /alert %}} 
### **智能标记**
#### **数据标记**
数据标记的格式为 &=DataSetName.FieldName。例如：&=SalesDetail.sales，其中 SalesDetail 是数据集或查询的名称，sales 是其字段之一的名称。在渲染时，数据标记将被 Reporting Services 提供的数据集的值替换。
#### **报表服务公式标记**
Reporting Services 的**公式标记**的格式是 &=expression。例如：&=sum(SalesDetail.sales)/100。表达式由函数、数据集字段、运算符等组成。在渲染时，Reporting Services 的公式标记将被计算值替换。
#### **报表服务全局变量标记**
Reporting Services 的**全局变量标记**的格式是 &=Globals! Variable Name。例如：&=Globals!ExecutionTime，其中 ExecutionTime 是全局变量的名称。在渲染时，全局变量标记将被全局变量值替换。
#### **报表服务参数标记**
报表参数具有两个属性：值和标签。因此，**参数标记**有两种格式：&= Parameters! ParamName.Value 和 &=Parameters! ParamName.Label。它们分别表示参数的名称和标签。在渲染时，参数标记将被用户输入的参数值替换。
#### **动态公式**
为了对插入的行进行计算，使用动态公式。**动态公式**允许您即使公式引用导出过程中将插入的行，也可以将 Microsoft Excel 的公式插入到单元格中。它们可以重复用于每个插入的行，或仅用于放置了数据标记的单元格。

动态公式的格式为 &=&=RepeatDynamicFormula。

动态公式允许以下额外选项：

- {r} – 当前行号。
- {2}, {-1} – 相对于当前行号的偏移。

**重复动态公式和生成的 Excel 工作表** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
