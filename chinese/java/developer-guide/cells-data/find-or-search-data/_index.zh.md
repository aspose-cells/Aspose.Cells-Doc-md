---
title: 查找或搜索数据
type: docs
weight: 120
url: /zh/java/find-or-search-data/
---

{{% alert color="primary" %}} 

在Microsoft Excel中，用户可以搜索包含特定数据的单元格。例如，单击“编辑”，然后单击“查找”打开搜索对话框。用户输入一个值，然后点击“确定”进行搜索。Excel会突出显示匹配的字段。

使用查找对话框查找包含特定值的单元格 

![todo:image_alt_text](find-or-search-data_1.png)

在此示例中，搜索值为“Oranges”。

Aspose.Cells允许开发人员搜索工作表中包含给定值的单元格。

{{% /alert %}} 
## **查找包含特定数据的单元格**
Aspose.Cells提供了代表Excel文件的Workbook类。Workbook类包含WorksheetCollection，该集合允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。

Worksheet类提供了Cells集合，表示工作表中的所有单元格。Cells集合提供了几种用于查找工作表中包含用户指定数据的单元格的方法。以下将更详细地讨论其中的一些方法。

所有查找方法均返回包含指定搜索值的单元格引用。
## **查找包含公式的单元格**
开发者可以通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-)方法，设置[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)为[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)，并将其作为参数传递，来查找工作表中的特定公式。

通常，[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-)方法接受两个或多个参数：

- 要搜索的对象：表示需要在工作表中查找的对象。
- 上一个单元格：表示具有相同公式的上一个单元格。当从开始位置搜索时，可以将此参数设置为null。
- 查找选项：表示查找条件。在下面的示例中，使用以下工作表数据来练习查找方法：

**样本工作表数据** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **搜索字符串**
查找包含字符串值的单元格很容易和灵活。有不同的搜索方式，例如，搜索包含以特定字符或字符集开头的字符串的单元格，或设置包含的字符串以开始于特定字符或字符集。
### **搜索以特定字符开头的字符串**
若要查找字符串中的第一个字符，可以调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-)方法，设置[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)为[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START-WITH)，并将其作为参数传递。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **搜索以特定字符结尾的字符串**
Aspose.Cells还可以查找以特定字符结尾的字符串。若要查找字符串的最后字符，可以调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-)方法，设置[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)为[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END-WITH)，并将其作为参数传递。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **使用正则表达式进行搜索：正则表达式功能**
正则表达式提供了一种简洁灵活的方法来匹配（指定和识别）文本字符串，如特定字符、单词或模式。

例如，正则表达式模式abc-*~~xyz~~匹配字符串"abc-123-xyz"，"abc-985-xyz"和"abc-pony-xyz"。*是通配符，因此该模式匹配任何以"abc"开头且以"-xyz"结尾的字符串，不管中间是什么字符。

Aspose.Cells允许您使用正则表达式进行搜索。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **高级主题**
- [查找具有特定样式的单元格](/cells/zh/java/find-cells-with-specific-style/)
- [使用原始值搜索数据](/cells/zh/java/search-data-using-original-values/)
{{< app/cells/assistant language="java" >}}
