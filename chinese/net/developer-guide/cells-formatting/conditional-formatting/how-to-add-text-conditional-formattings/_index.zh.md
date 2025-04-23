---
title: 如何添加文本条件格式
description: 如何在C#中使用Aspose.Cells库应用文本条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示效果。
keywords: Aspose.Cells，文本条件格式，C#，条件格式，格式设置
type: docs
weight: 70
url: /zh/net/how-to-add-text-conditional-formatting/
---

## **可能的使用场景**
在电子表格中使用基于文本的条件格式有助于突出显示符合特定文本条件的单元格。这可以改善数据分析并使在大量数据中查找关键信息变得更容易。以下是使用文本条件格式的一些原因：

1. 高亮特定文本：可以根据特定词语、短语或字符应用格式。例如，您可能希望突出显示所有包含“紧急”或“已完成”的单元格，以便轻松区分任务。
1. 识别模式或趋势：如果您处理类别或状态（如“高”、“中”、“低”），文本条件格式可以直观地区分它们，使跟踪进度或优先任务变得更容易。
1. 错误或数据录入提醒：文本格式可以标记不一致或错误的输入，如拼写错误、不完整的文本或错误的值。这在大量文本输入的数据集中尤其有用。
1. 提升可读性：使用颜色编码或改变文本样式（加粗、斜体等）有助于突出重要信息，提升整体可读性。
1. 动态反馈：可以设置规则，当文本符合某些条件时自动调整格式。这意味着随着数据变化，无需手动更新格式。

本质上，文本条件格式帮助您快速发现相关信息、错误和趋势，是管理和解释文本数据的强大工具。

## **如何使用Excel添加文本条件格式**
在Excel中添加基于文本的条件格式，请按照以下步骤操作：

1. 选择单元格范围：突出显示您希望应用条件格式的单元格。
1. 打开条件格式菜单：在Excel功能区的“开始”标签中，点击“条件格式”。
1. 选择“新建规则”：在下拉菜单中选择“新建规则”。
1. 选择“只格式化包含特定内容的单元格”：在新格式规则对话框中，选择“只格式化满足以下条件的单元格”，在“选择规则类型”部分。
1. 设置规则条件：在“格式单元格值”部分，从下拉菜单选择“特定文本”。根据你要应用的条件，选择“包含”、“以...开始”或“以...结束”。输入你要格式化的文本（例如，“紧急”或“已完成”）。
1. 选择格式：点击“格式”按钮。在“设置单元格格式”对话框中，可以选择字体颜色、填充颜色或其他格式设置。
1. 应用规则：设置好所需格式后，点击“确定”以应用规则。在新格式规则对话框中再次点击“确定”以关闭。
1. 查看结果：包含指定文本的单元格现在会应用对应的格式，方便快速识别相关信息。


## **如何使用编号Aspose.Cells for .NET添加文本条件格式**

Aspose.Cells完全支持在运行时对XLSX格式的Excel中提供的条件格式，包括高级条件格式类型如BeginsWith、ContainsBlank、ContainsText等。

### **当单元格值以特定文本开头时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **当单元格值包含空白时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **当单元格值包含错误时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **当单元格值包含特定文本时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **当单元格值包含重复值时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **当单元格值以特定文本结尾时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **当单元格值不为空白时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **当单元格值不包含错误时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **当单元格值不包含特定文本时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **当单元格值包含唯一值时进行格式设置**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
