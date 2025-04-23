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
Методы [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle-int-) и класс [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) делают создание повторно используемых стилей удобным. Вот список всех возможных встроенных стилей:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-2)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-3)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-4)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-5)
- [СОРОК_ПРОЦЕНТОВ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-6)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-1)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-2)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-3)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-4)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-5)
- [ШЕСТЬДЕСЯТ_ПРОЦЕНТОВ_АКЦЕНТ_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-6)
- [ПЛОХО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [ВЫЧИСЛЕНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [ПРОВЕРКА_КЛЕТКИ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK-CELL)
- [ЗАПЯТАЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [ЗАПЯТАЯ_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA-1)
- [ВАЛЮТА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [ВАЛЮТА_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY-1)
- [ТЕКСТ_ОБЪЯСНЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY-TEXT)
- [ХОРОШО](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [ЗАГОЛОВОК_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-1)
- [ЗАГОЛОВОК_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-2)
- [ЗАГОЛОВОК_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-3)
- [ЗАГОЛОВОК_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-4)
- [ГИПЕРССЫЛКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [СЛЕДОВАВШАЯ_ГИПЕРССЫЛКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED-HYPERLINK)
- [ВВОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [СВЯЗАННЫЙ_ЯЧЕЙКА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED-CELL)
- [НЕЙТРАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [НОРМАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [ПРИМЕЧАНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [ВЫВОД](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [ПРОЦЕНТ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [ЗАГОЛОВОК](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [ИТОГ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [ТЕКСТ_ОПОВЕЩЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING-TEXT)
- [УРОВЕНЬ_СТРОКИ](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW-LEVEL)
- [УРОВЕНЬ_СТОЛБЦА](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN-LEVEL)

Ниже приведен код, демонстрирующий использование встроенных стилей.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
{{< app/cells/assistant language="java" >}}
