---
title: Использование встроенных стилей
type: docs
weight: 480
url: /ru/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет обширную коллекцию многократно используемых стилей для форматирования ячейки в документе электронной таблицы. Мы можем использовать встроенные стили в нашей книге и также создавать пользовательские стили.

{{% /alert %}} 
## **Как использовать встроенные стили**
Метод [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\)) и класс [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) делают удобным создание многократно используемых стилей. Вот список всех возможных встроенных стилей:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [ПЛОХО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [ВЫЧИСЛЕНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [ПРОВЕРКА_КЛЕТКИ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [ЗАПЯТАЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [ЗАПЯТАЯ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [ВАЛЮТА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [ВАЛЮТА_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [ТЕКСТ_ОБЪЯСНЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [ХОРОШО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [ЗАГОЛОВОК_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [ЗАГОЛОВОК_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [ЗАГОЛОВОК_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [ЗАГОЛОВОК_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [ГИПЕРССЫЛКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [СЛЕДОВАВШАЯ_ГИПЕРССЫЛКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [ВВОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [СВЯЗАННЫЙ_ЯЧЕЙКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [НЕЙТРАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [НОРМАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ПРИМЕЧАНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ВЫВОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [ПРОЦЕНТ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [ЗАГОЛОВОК](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [ИТОГ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [ТЕКСТ_ОПОВЕЩЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [УРОВЕНЬ_СТРОКИ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [УРОВЕНЬ_СТОЛБЦА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

Ниже приведен код, демонстрирующий использование встроенных стилей.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
