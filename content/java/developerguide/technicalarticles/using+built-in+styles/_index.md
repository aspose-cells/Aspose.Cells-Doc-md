---
title : "Using Built-in Styles" 
description : "" 
weight : 12514 
toc : false
type: docs
url: /java/developerguide/technicalarticles/using+built-in+styles/
---

# Aspose.Cells for Java : Using Built-in Styles


Aspose.Cells provides a vast collection of re-usable styles to format a cell in a spreadsheet document. We can use built-in styles in our workbook and also create custom styles.

### How to use Built-in Styles

The method [Workbook.createBuiltinStyle](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#createBuiltinStyle(int)) and class [BuiltinStyleType](https://apireference.aspose.com/java/cells/com.aspose.cells/BuiltinStyleType) make it convenient to create re-usable styles. Here is a list of all possible built-in styles:

*   [TWENTY\_PERCENT\_ACCENT\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
*   [TWENTY\_PERCENT\_ACCENT\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
*   [TWENTY\_PERCENT\_ACCENT\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
*   [TWENTY\_PERCENT\_ACCENT\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
*   [TWENTY\_PERCENT\_ACCENT\_5](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
*   [TWENTY\_PERCENT\_ACCENT\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
*   [FORTY\_PERCENT\_ACCENT\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
*   [FORTY\_PERCENT\_ACCENT\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
*   [FORTY\_PERCENT\_ACCENT\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
*   [FORTY\_PERCENT\_ACCENT\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
*   [FORTY\_PERCENT\_ACCENT\_5](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
*   [FORTY\_PERCENT\_ACCENT\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
*   [SIXTY\_PERCENT\_ACCENT\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
*   [SIXTY\_PERCENT\_ACCENT\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
*   [SIXTY\_PERCENT\_ACCENT\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
*   [SIXTY\_PERCENT\_ACCENT\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
*   [SIXTY\_PERCENT\_ACCENT\_5](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
*   [SIXTY\_PERCENT\_ACCENT\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
*   [ACCENT\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_1)
*   [ACCENT\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_2)
*   [ACCENT\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_3)
*   [ACCENT\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_4)
*   [ACCENT\_5](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_5)
*   [ACCENT\_6](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ACCENT_6)
*   [BAD](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#BAD)
*   [CALCULATION](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#CALCULATION)
*   [CHECK\_CELL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#CHECK_CELL)
*   [COMMA](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#COMMA)
*   [COMMA\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#COMMA_1)
*   [CURRENCY](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#CURRENCY)
*   [CURRENCY\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#CURRENCY_1)
*   [EXPLANATORY\_TEXT](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
*   [GOOD](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#GOOD)
*   [HEADER\_1](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#HEADER_1)
*   [HEADER\_2](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#HEADER_2)
*   [HEADER\_3](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#HEADER_3)
*   [HEADER\_4](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#HEADER_4)
*   [HYPERLINK](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#HYPERLINK)
*   [FOLLOWED\_HYPERLINK](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
*   [INPUT](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#INPUT)
*   [LINKED\_CELL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#LINKED_CELL)
*   [NEUTRAL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#NEUTRAL)
*   [NORMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#NORMAL)
*   [NOTE](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#NOTE)
*   [OUTPUT](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#OUTPUT)
*   [PERCENT](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#PERCENT)
*   [TITLE](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TITLE)
*   [TOTAL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#TOTAL)
*   [WARNING\_TEXT](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#WARNING_TEXT)
*   [ROW\_LEVEL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#ROW_LEVEL)
*   [COLUMN\_LEVEL](https://apireference.aspose.com/java/cells/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

The following code demonstrates how to use built-in styles.

![image](https://docs2.aspose.com/cells/java/attachments/5276319/5472496.png)


