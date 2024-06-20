---
title: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 1900
url: /ru/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Возможные сценарии использования**

Когда вы вводите значение в ячейку, которое имеет ведущий апостроф или одинарный знак кавычки, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарный знак в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает ведущий апостроф или одинарную кавычку, как и Microsoft Excel, но устанавливает [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) как **true** для этой ячейки. Если вы установили пустой стиль ячейки, то [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) снова становится **false**. Для решения этой проблемы Aspose.Cells предоставляет свойство [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix), когда оно установлено в **false**, то [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) вообще не обновляется, и его старое значение сохраняется. Это означает, что если старое значение свойства [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) было **true**, оно останется истинным, и если старое значение было ложным, оно останется ложным.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

В следующем образце кода объясняется использование свойства [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix), как уже описано. Пожалуйста, прочтите комментарии внутри кода и посмотрите вывод консоли кода ниже для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
