---
title: Сохранять префикс одиночной кавычки для значения или диапазона Cell.
type: docs
weight: 310
url: /ru/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранить префикс одинарной кавычки значения или диапазона Cell через Aspose.Cells for .NET API.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **Возможные сценарии использования**

Когда вы помещаете какое-либо значение в ячейку с ведущим апострофом или одинарной кавычкой, Excel Microsoft скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарную кавычку в строке формул, как показано на следующем снимке экрана.

![задача: image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells также скрывает ведущий апостроф или одинарную кавычку, например Microsoft Excel, но устанавливает[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) как**истинный** для этой ячейки. Если вы установите пустой стиль ячейки, то[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) становится**ЛОЖЬ** снова. Чтобы решить эту проблему, Aspose.Cells предоставляет[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) свойство, когда оно установлено**false**, тогда [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) вообще не обновляется и его старое значение сохраняется . Это означает, что если старое значение свойства [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) было **true**, оно останется **верным** и если старое значение было *false**, оно останется *false**.

##  **Сохранять префикс одиночной кавычки для значения или диапазона Cell.**

В следующем примере кода объясняется использование[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)имущество, как описано ранее. Пожалуйста, прочитайте комментарии внутри кода и посмотрите консольный вывод кода, приведенного ниже, для получения дополнительной помощи.

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **Консольный вывод**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
