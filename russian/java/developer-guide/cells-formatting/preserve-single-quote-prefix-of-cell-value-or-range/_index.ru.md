---
title: Сохранить префикс одиночной кавычки для значения или диапазона Cell
type: docs
weight: 1900
url: /ru/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Возможные сценарии использования**

Когда вы помещаете какое-либо значение в ячейку с начальным апострофом или одинарной кавычкой, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает начальный апостроф или одинарную кавычку в строке формул, как показано на следующем снимке экрана.

![дело:изображение_альтернативный_текст](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает начальный апостроф или одинарную кавычку, как Microsoft Excel, но устанавливает[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) в качестве**истинный** для этой ячейки. Если задать пустой стиль ячейки, то[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) становится**ЛОЖЬ** опять таки. Чтобы решить эту проблему, Aspose.Cells предоставляет[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) свойство, когда оно установлено**ЛОЖЬ**, тогда[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)вообще не обновляется и сохраняется его старое значение. Это означает, что если старое значение[**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)имущество было**истинный**, оно останется истинным, а если старое значение было ложным, оно останется ложным.

## **Сохранить префикс одиночной кавычки для значения или диапазона Cell**

В следующем примере кода объясняется использование[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)имущество, как описано ранее. Пожалуйста, прочтите комментарии внутри кода и просмотрите консольный вывод кода, приведенного ниже, для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
