---
title: Aspose.Cells中的智能标记功能
type: docs
weight: 30
url: /zh/net/smart-markers-feature-in-aspose-cells/
---

**智能标记**用于让Aspose.Cells知道在Microsoft Excel设计器电子表格中放置什么信息。智能标记允许您创建只包含特定信息和格式的模板。
## **设计器电子表格和智能标记**
设计器电子表格是包含视觉格式、公式和智能标记的标准Excel文件。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。将智能标记编写到要放置信息的单元格中。

所有智能标记均以&=开头。数据标记的示例是 &=Party.FullName。如果数据标记导致多个项目，例如，完整的行，则会自动移动下面的行，以便为所有新信息预留空间。因此，可以在数据标记后面的行上放置小计和总计，以便基于插入的数据进行计算。要在插入的行上进行计算，请使用动态公式。

智能标记由**数据源**和**字段名称**部分组成以获取大多数信息。特殊信息也可以通过变量和变量数组传递。变量总是只填充一个单元格，而变量数组可能填充多个。每个单元格只能使用一个数据标记。未使用的智能标记将被移除。

智能标记还可以包含参数。参数允许您修改信息的排列方式。它们作为逗号分隔的列表附加到智能标记的末尾。
### **智能标记选项**
- &=DataSource.FieldName
- &=数据源.字段名
- &=$变量名
- &=$变量数组
- &==动态公式
- &=&=重复动态公式
### **参数**
允许使用以下参数：

- noadd - 不要添加额外的行以适应数据。
- skip:n - 对每行数据跳过n行。
- ascending:n 或 descending:n - 对智能标记中的数据进行排序。如果n为1，则该列是排序器的第一个键。在处理数据源后对数据进行排序。例如 &=Table1.Field3(ascending:1)。
- horizontal - 从左到右写入数据，而不是从上到下。
- numeric - 尽可能将文本转换为数字。仅在.NET版本中支持。
- shift - 向下或向右移动，创建额外的行或列以适应数据。shift参数与Microsoft Excel中的操作方式相同。例如，在MS Excel中，当选择一系列单元格，右键单击并选择“插入”，然后指定“向下移动单元格”、“向右移动单元格”和其他选项时。简言之，shift参数用于垂直/正常（从上到下）或水平（从左到右）智能标记的相同功能。
- copystyle - 将基本单元格的样式复制到该列中的所有单元格。

参数**noadd**和**skip**可以组合在一起，以在交替行上插入数据。因为模板从底部向顶部处理，所以应该在首行添加noadd，以避免在交替行之前插入额外的行。

本节包括以下主题

- [在Aspose.Cells中对数据进行分组](/cells/zh/net/grouping-data-in-aspose-cells/)
- [Aspose.Cells中的图像标记](/cells/zh/net/image-markers-in-aspose-cells/)
- [在Aspose.Cells中使用匿名类型或自定义对象](/cells/zh/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [在Aspose.Cells中使用嵌套对象](/cells/zh/net/using-nested-objects-in-aspose-cells/)
