---
title: 查找或搜索数据
type: docs
weight: 120
url: /zh/java/find-or-search-data/
---
{{% alert color="primary" %}} 

在 Microsoft Excel 中，用户可以搜索包含特定数据的单元格。例如，点击**编辑**接着**寻找**打开搜索对话框。用户输入一个值并点击**好的**搜索它。 Excel 突出显示匹配字段。

**使用“查找”对话框查找包含特定值的单元格** 

![待办事项：图片_替代_文本](find-or-search-data_1.png)

在此示例中，搜索值为“Oranges”。

Aspose.Cells 允许开发人员搜索工作表中的单元格以查找包含给定值的单元格。

{{% /alert %}} 
## **查找包含特定数据的 Cells**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , 表示一个 Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，一个允许访问 Excel 文件中的每个工作表的集合。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。

这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)，代表工作表中所有单元格的集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection 提供了多种方法来查找工作表中包含用户指定数据的单元格。下面将更详细地讨论其中一些方法。

所有查找方法都返回包含指定搜索值的任何单元格的单元格引用。
## **查找包含公式**
开发者可以通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) 方法，设置[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)到[LookInType.公式](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)并将其作为参数传递给[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

通常，[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) 方法接受两个或多个参数：

- 要搜索的对象：表示需要在工作表中查找的对象。
- previous Cell：代表上一个相同公式的单元格。从头开始搜索时可以将此参数设置为空。
- Find Options：表示查找条件。在下面的示例中，以下工作表数据用于练习查找方法：

**示例工作表数据** 

![待办事项：图片_替代_文本](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **搜索字符串**
搜索包含字符串值的单元格既简单又灵活。有多种搜索方式，例如，搜索包含以特定字符或字符集开头的字符串的单元格。
### **搜索以特定字符开头的字符串**
要搜索字符串中的第一个字符，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)方法，设置[查找选项.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)到[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)并将其作为参数传递给[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **搜索以特定字符结尾的字符串**
Aspose.Cells 也可以查找以特定字符结尾的字符串。要搜索字符串中的最后一个字符，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)方法，设置[查找选项.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)到[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)并将其作为参数传递给[寻找](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **使用正则表达式搜索：RegEx 功能**
正则表达式提供了一种简洁而灵活的方法来匹配（指定和识别）文本字符串，例如特定字符、单词或模式。

例如，正则表达式模式 abc-* ~~xyz~~ 匹配字符串“abc-123-xyz”、“abc-985-xyz”和“abc-pony-xyz”。*是一个通配符，因此该模式匹配任何以“abc”开头并以“-xyz”结尾的字符串，而不管中间的字符是什么。

Aspose.Cells 允许您使用正则表达式进行搜索。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **推进主题**
- [查找具有特定样式的单元格](/cells/zh/java/find-cells-with-specific-style/)
- [使用原始值搜索数据](/cells/zh/java/search-data-using-original-values/)
