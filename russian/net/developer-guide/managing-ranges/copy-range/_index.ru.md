---
title: Копировать диапазоны Excel
linktitle: Копировать диапазоны
type: docs
weight: 105
url: /ru/net/copy-ranges-of-Excel/
---
## **Введение**

В Excel вы можете выбрать диапазон, скопировать диапазон, а затем вставить его с определенными параметрами на тот же рабочий лист, другие рабочие листы или другие файлы.

## **Копировать диапазоны с помощью Aspose.Cells**

 Aspose.Cells обеспечивает некоторую перегрузку[Диапазон.Копировать](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) способы копирования диапазона.
 А также[Диапазон.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) только стиль копирования диапазона;[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) только копируемое значение диапазона

## **Копировать диапазон**

Создание двух диапазонов: исходный диапазон, целевой диапазон, затем копирование исходного диапазона в целевой диапазон с помощью метода Range.Copy.

См. следующий код:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Вставить диапазон с параметрами**

Aspose.Cells поддерживает вставку диапазона определенного типа.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Копировать только данные диапазона.**
Также вы можете скопировать данные с помощью метода Range.CopyData в виде следующих кодов:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Предварительные темы**
- [Копировать высоты строк исходного диапазона в целевой диапазон](/cells/ru/net/copy-row-heights-of-source-range-to-destination-range/)


