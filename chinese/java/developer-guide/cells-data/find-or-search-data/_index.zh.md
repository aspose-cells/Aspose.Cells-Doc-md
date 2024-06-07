---
title: 查找或搜索数据
type: docs
weight: 120
url: /zh/java/find-or-search-data/
---

{{% alert color="primary" %}} 

在Microsoft Excel中，用户可以搜索包含特定数据的单元格。例如，单击**编辑**，然后单击**查找**打开搜索对话框。用户输入一个值，然后单击**确定**进行搜索。Excel会突出显示匹配的字段。

**使用查找对话框查找包含特定值的单元格** 

![todo:image_alt_text](find-or-search-data_1.png)

在此示例中，搜索值为"橙子"。

Aspose.Cells允许开发人员搜索工作表中包含给定值的单元格。

{{% /alert %}} 
## **查找包含特定数据的单元格**
Aspose.Cells提供了一个表示Excel文件的类[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，该集合允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。

[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)，该集合代表工作表中的所有单元格。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合提供了几种方法来查找包含用户指定数据的单元格。以下更详细地讨论了其中一些方法。

所有查找方法都会返回包含指定搜索值的单元格引用。
## **查找包含公式的单元格**
开发人员可以通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法来查找工作表中的指定公式，将[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)设置为[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)并将其作为参数传递给[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法。

通常，[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法接受两个或更多参数：

- 要搜索的对象：表示需要在工作表中查找的对象。
- 上一个单元格：表示具有相同公式的上一个单元格。在从头开始搜索时，此参数可以设置为null。
- 查找选项：表示查找的条件。在下面的示例中，使用以下工作表数据来练习查找方法：

**示例工作表数据** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **搜索字符串**
搜索包含字符串值的单元格非常简单且灵活。有不同的搜索方式，例如搜索以特定字符或字符集开头的字符串的单元格。
### **搜索以特定字符开头的字符串**
要搜索字符串中的第一个字符，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法，将[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)设置为[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)并将其作为参数传递给[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **搜索以特定字符结尾的字符串**
Aspose.Cells也可以查找以特定字符结尾的字符串。要搜索字符串中的最后字符，请调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法，将[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)设置为[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)并将其作为参数传递给[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **使用正则表达式进行搜索：RegEx功能**
正则表达式提供了一种简洁灵活的方式来匹配(指定和识别)文本字符串，比如特定字符、单词或模式。

例如，正则表达式模式abc-*~~xyz~~匹配字符串"abc-123-xyz"、"abc-985-xyz"和"abc-pony-xyz"。*是通配符，所以该模式匹配任何以"abc"开头并以"-xyz"结尾的字符串，无论中间是什么字符。

Aspose.Cells允许您使用正则表达式进行搜索。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **高级主题**
- [查找具有特定样式的单元格](/cells/zh/java/find-cells-with-specific-style/)
- [使用原始值搜索数据](/cells/zh/java/search-data-using-original-values/)
