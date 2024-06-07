---
title: 使用内置样式
type: docs
weight: 480
url: /zh/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了一个庞大的可重用样式集合，可用于格式化电子表格文档中的单元格。我们可以在工作簿中使用内置样式，也可以创建自定义样式。

{{% /alert %}} 
## **如何使用内置样式**
方法[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\)) 和类[BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) 使创建可重用样式变得方便。以下是所有可能内置样式的列表:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [百分之二十重音符_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [百分之二十重音符_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [百分之二十重音符_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [百分之四十重音符_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [百分之四十重音符_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [百分之四十重音符_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [百分之四十重音符_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [百分之四十重音符_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [百分之四十重音符_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [百分之六十重音符_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [百分之六十重音符_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [百分之六十重音符_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [百分之六十重音符_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [百分之六十重音符_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [百分之六十重音符_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [重音符_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [重音符_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [重音符_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [重音符_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [重音符_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [重音符_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [坏](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [计算](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [检查单元格](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [逗号](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [逗号_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [货币](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [货币_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [说明文本](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [好](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [标题1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [标题2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [标题3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [标题4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [超链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [已访问的超链接](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [输入](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [关联单元格](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [中性](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
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
