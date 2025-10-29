---
title: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранить префикс одной кавычки значения ячейки или диапазона через API Aspose.Cells for Node.js via C++.
keywords: Сохранить префикс одной кавычки значения ячейки или диапазона Node.js через C++, Скрыть ведущую апостроф или одинарную кавычку Node.js через C++, Показать ведущую апостроф или одинарную кавычку Node.js через C++
---

## **Возможные сценарии использования**

Когда вы вводите значение в ячейку, которое имеет ведущий апостроф или одинарный знак кавычки, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарный знак в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ также скрывает ведущую апостроф или одинарную кавычку, как в Microsoft Excel, но при этом устанавливает [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) в значение **true** для этой ячейки. Если задать для ячейки пустой стиль, то [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) снова станет **false**. Для решения этой проблемы Aspose.Cells for Node.js via C++ предоставляет метод [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-), при установке **false** значение не обновляется, а сохраняется старое. Это означает, что если старое значение [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) было **true**, оно останется **true**, а если было **false**, останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий пример кода иллюстрирует использование метода [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-), как описано ранее. Пожалуйста, прочитайте комментарии внутри кода и посмотрите вывод на консоль ниже для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
