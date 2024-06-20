---
title: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранить предшествующий одинарный знак кавычки значения ячейки или диапазона с помощью API Aspose.Cells for .NET.
keywords: Сохранить предшествующий одинарный знак кавычки значения ячейки или диапазона, Скрыть ведущий апостроф или одинарный знак кавычки, Показать ведущий апостроф или одинарный знак кавычки
---

## **Возможные сценарии использования**

Когда вы вводите значение в ячейку, которое имеет ведущий апостроф или одинарный знак кавычки, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарный знак в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает ведущий апостроф или одинарный знак кавычки, как и Microsoft Excel, но устанавливает [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) как **true** для этой ячейки. Если вы установите пустой стиль ячейки, то [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) снова станет **false**. Чтобы решить эту проблему, Aspose.Cells предоставляет свойство [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), при установке которого **false**, то [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) вообще не обновляется, и его старое значение сохраняется. Это означает, что если старое значение свойства [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) было **true**, то оно останется **true**, и если старое значение было **false**, то оно останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий образец кода объясняет использование свойства [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), описанного ранее. Пожалуйста, прочтите комментарии внутри кода и посмотрите вывод консоли данного кода ниже для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
