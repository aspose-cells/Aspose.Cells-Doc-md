---
title: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Узнайте, как сохранить одинарный префикс кавычки значения ячейки или диапазона с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, сохранить одинарный префикс комбинации значения ячейки или диапазона, скрыть ведущий апостроф или одинарный знак кавычки с помощью Python, показать ведущий апостроф или одинарный знак кавычки с помощью Python.
---

## **Возможные сценарии использования**

Когда вы вводите значение в ячейку, которое имеет ведущий апостроф или одинарный знак кавычки, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарный знак в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells для Python via .NET также скрывает ведущий апостроф или одинарный знак, как и Microsoft Excel, но устанавливает [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) как **true** для этой ячейки. Если вы установите пустой стиль ячейки, то [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) снова станет **false**. Для решения этой проблемы Aspose.Cells для Python via .NET предоставляет свойство [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), когда оно установлено в **false**, то [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) вообще не обновляется и его старое значение сохраняется. Это означает, что если старое значение свойства [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) было **true**, оно останется **true**, и если старое значение было **false**, оно останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий образец кода объясняет использование свойства [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), описанного ранее. Пожалуйста, прочтите комментарии внутри кода и посмотрите вывод консоли данного кода ниже для получения дополнительной помощи.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
