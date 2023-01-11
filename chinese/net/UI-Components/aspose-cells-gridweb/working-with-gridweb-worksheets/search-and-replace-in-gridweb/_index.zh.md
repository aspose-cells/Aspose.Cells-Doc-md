﻿---
title: 在 GridWeb 中搜索和替换
type: docs
weight: 90
url: /zh/net/search-and-replace-in-gridweb/
---
{{% alert color="primary" %}} 

在大型电子表格中进行重复更改的最快方法之一是使用查找和替换功能。 Find 可帮助您找到文本字符串或数据，并将其替换为新值。 Aspose.Cells.GridWeb提供了这个功能。它使您能够通过一个简单的对话框在工作表客户端中搜索并替换为特定的文本字符串或值。它甚至允许您查找部分数据。

{{% /alert %}} 
## **使用查找/替换**
### **查找/替换对话框**
有两种方法可以打开“查找/替换”对话框：

1. 当控件处于活动状态时，按**CTRL+F**打开对话框，或按**CTRL+R**键打开对话框**代替**按钮启用。
1. 将光标移动到工作表中的单元格区域，然后单击鼠标右键。选择**寻找**要么**代替**从菜单中。

   **选择查找** 

![待办事项：图片_替代_文本](search-and-replace-in-gridweb_1.png)




显示样式对话框。

**查找/替换对话框** 

![待办事项：图片_替代_文本](search-and-replace-in-gridweb_2.png)
### **使用查找**
搜索：

1. 打开“查找/替换”对话框。
1. 在中键入要搜索的字符串**找什么**场地。
1. 点击**找下一个**搜索。

与您的查找条件相匹配的下一个单元格会突出显示。

{{% alert color="primary" %}} 

如果未找到您的搜索条件，则会显示一个对话框告诉您。

{{% /alert %}} 
### **搜索选项**
您可以在对话框中自定义一些搜索选项。下表列出了它们。

|**不。** |**选项名称** |**描述** |
|:- |:- |:- |
|1 |相符|指示是否在搜索时区分大小写。|
|2 |全字匹配|表示搜索时是否全词匹配。|
|3 |向上搜索|指示是否从下到上进行搜索。|
|4 |正则表达式|选中时，控件将在查找过程中将“查找内容”文本框中的字符串视为正则表达式。|
|5 |在公式/值中查找|选择公式后，如果存在公式或未格式化的值，控件将匹配单元格的公式或未格式化的值。选择值时，控件将仅匹配单元格的显示值。|
### **使用替换**
要替换文本或值：

1. 通过按打开“查找/替换”对话框**CTRL+F**，或选择右键单击一个单元格并选择**寻找**点击前**代替**.
1. 在中键入替换字符串**用。。。来代替**场地。
1. 点击**代替**.

要替换文本：

1. 打开对话框。
1. 输入要查找的文本**找什么**字段，以及您要在其中替换它的文本**用。。。来代替**场地。
1. 通过单击一次替换一个事件**找下一个**其次是**代替**.
1. 如果您非常确定工作表包含的内容，请单击**全部替换**.

{{% alert color="primary" %}} 

如果工作表未处于编辑模式，则**代替**按钮不显示。

{{% /alert %}}