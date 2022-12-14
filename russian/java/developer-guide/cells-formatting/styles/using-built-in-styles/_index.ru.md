---
title: Использование встроенных стилей
type: docs
weight: 480
url: /ru/java/using-built-in-styles/
---
{{% alert color="primary" %}} 

Aspose.Cells предоставляет обширную коллекцию повторно используемых стилей для форматирования ячейки в табличном документе. Мы можем использовать встроенные стили в нашей книге, а также создавать собственные стили.

{{% /alert %}} 
## **Как использовать встроенные стили**
 Метод[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\) ) и класс[Тип встроенного стиля](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)сделать удобным создание повторно используемых стилей. Вот список всех возможных встроенных стилей:

- [20_ПРОЦЕНТ_АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [20_ПРОЦЕНТ_АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [20_ПРОЦЕНТ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [20_ПРОЦЕНТ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [20_ПРОЦЕНТ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [20_ПРОЦЕНТ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [СОРОК_ПРОЦЕНТ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [ПЛОХО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [РАСЧЕТ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [CHECK_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [ЗАПЯТАЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [COMMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [ВАЛЮТА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [ВАЛЮТА_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [EXPLANATORY_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [ХОРОШИЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [HEADER_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [HEADER_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [HEADER_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [ЗАГОЛОВОК_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [ГИПЕРССЫЛКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [FOLLOWED_HYPERLINK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [ВХОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [LINKED_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [НЕЙТРАЛЬНО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [ОБЫЧНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ПРИМЕЧАНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ВЫХОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [ПРОЦЕНТ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [ЗАГЛАВИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [ОБЩИЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [WARNING_TEXT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [ROW_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [COLUMN_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

Следующий код демонстрирует, как использовать встроенные стили.

![дело:изображение_альтернативный_текст](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
