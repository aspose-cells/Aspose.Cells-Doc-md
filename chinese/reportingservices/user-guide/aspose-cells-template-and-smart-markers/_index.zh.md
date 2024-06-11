---
title: Aspose.Cells模板和智能标记
type: docs
weight: 30
url: /zh/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells模板是一个包含智能标记的Microsoft Excel工作簿。智能标记作为报告项的数据占位符，在呈现时将被相应的数据替换。有五种类型的智能标记，如下所示。所有这些标记都可以由Aspose.Cells.Report.Designer插入模板。也可以手动编辑。 

{{% /alert %}} 
### **智能标记**
#### **数据标记**
**数据标记**的格式是&=DataSetName.FieldName。例如：&=SalesDetail.sales，其中SalesDetail是数据集或查询的名称，sales是其字段中的一个名称。在呈现时，数据标记将被Reporting Services提供的数据集的值替换。
#### **报告服务公式标记**
报告服务的**公式标记**的格式是&=expression。例如：&=sum(SalesDetail.sales)/100。表达式包括函数、数据集字段、运算符等。在呈现时，报告服务的公式标记将被计算值替换。
#### **报告服务全局变量标记**
报告服务的**全局变量标记**的格式是&=Globals! Variable Name。例如：&=Globals!ExecutionTime，其中ExecutionTime是全局变量的名称。在呈现时，全局变量标记将被全局变量值替换。
#### **报告服务参数标记**
报告参数有两个属性：值和标签。因此，**参数标记**有两种格式：&=Parameters! ParamName.Value 和 &=Parameters! ParamName.Label。它们分别表示参数的名称和标签。在呈现时，参数标记将被用户输入的参数值替换。
#### **动态公式**
为了对插入的行进行计算，使用动态公式。**动态公式**允许您在导出过程中插入Microsoft Excel的公式，即使公式引用将在导出过程中插入的行。它们可以为每个插入的行重复或仅用于为其放置数据标记的单元格。

动态公式的格式是&=&=RepeatDynamicFormula。

动态公式允许以下额外选项：

- {r} – 当前行号。
- {2}, {-1} – 相对于当前行号的偏移量。

**重复动态公式及其生成的Excel工作表** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
