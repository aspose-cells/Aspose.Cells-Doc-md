---
title: 使用内置样式
type: docs
weight: 480
url: /zh/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了大量可重复使用的样式来格式化电子表格文档中的单元格。我们可以在工作簿中使用内置样式，也可以创建自定义样式。

{{% /alert %}} 
## **如何使用内置样式**
方法[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\))和类[BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)使得方便创建可重复使用的样式。这里是所有可能内置样式的列表：

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [四十_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [四十_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [四十_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [四十_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [六十_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [六十_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [六十_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [六十_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [六十_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [六十_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [坏](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [计算](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [检查单元格](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [逗号](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [逗号_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [货币](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [货币_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [解释性文本](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [好](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [标题_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [标题_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [标题_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [标题_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [超链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [已访问的超链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [输入](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [链接的单元格](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [中立](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [普通](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [注释](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [输出](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [百分比](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [标题](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [总计](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [警告文本](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [行级别](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [列级别](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

以下代码演示了如何使用内置样式。

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
