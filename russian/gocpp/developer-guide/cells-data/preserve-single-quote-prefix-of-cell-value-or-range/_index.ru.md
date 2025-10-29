---
title: Сохранить префикс одинарной кавычки значения ячейки или диапазона с Golang через C++
linktitle: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранять префикс одинарной кавычки значения ячейки или диапазона через API Aspose.Cells for C++.
keywords: Сохранить предшествующий одинарный знак кавычки значения ячейки или диапазона, Скрыть ведущий апостроф или одинарный знак кавычки, Показать ведущий апостроф или одинарный знак кавычки
---

## **Возможные сценарии использования**

Когда вы вставляете значение в ячейку с ведущей апострофом или одинарной кавычкой, Microsoft Excel скрывает её, но при выборе ячейки она отображается в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает ведущую апостроф или одинарную кавычку, как в Microsoft Excel, но устанавливает [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) в значение **true** для этой ячейки. Если вы установите пустой стиль ячейки, то [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) снова станет **false**. Чтобы решить эту проблему, Aspose.Cells предоставляет свойство [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), при установке которого в **false** [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) не обновляется вовсе, и сохраняется его старое значение. Это означает, что если старое значение свойства [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) было **true**, оно останется **true**, а если — **false**, то останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий пример кода иллюстрирует использование свойства [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/), как было описано ранее. Обратите внимание на комментарии внутри кода и посмотрите вывод в консоли ниже для получения дополнительной информации.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
