---
title: Сохранить префикс одиночной кавычки для значения или диапазона Cell
type: docs
weight: 310
url: /ru/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Возможные сценарии использования**

Когда вы помещаете какое-либо значение в ячейку с начальным апострофом или одинарной кавычкой, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает начальный апостроф или одинарную кавычку в строке формул, как показано на следующем снимке экрана.

![дело:изображение_альтернативный_текст](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает начальный апостроф или одинарную кавычку, как Microsoft Excel, но устанавливает[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) в качестве**истинный** для этой ячейки. Если задать пустой стиль ячейки, то[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) становится**ЛОЖЬ** опять таки. Чтобы решить эту проблему, Aspose.Cells предоставляет[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) свойство, когда оно установлено**ЛОЖЬ** , тогда[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)вообще не обновляется и сохраняется его старое значение. Это означает, что если старое значение[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)имущество было**истинный** , останется**истинный** и если старое значение было**ЛОЖЬ** , останется**ЛОЖЬ**.

## **Сохранить префикс одиночной кавычки для значения или диапазона Cell**

 В следующем примере кода объясняется использование[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)имущество, как описано ранее. Пожалуйста, прочтите комментарии внутри кода и просмотрите консольный вывод кода, приведенного ниже, для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
