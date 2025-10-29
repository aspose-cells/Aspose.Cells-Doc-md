---
title: Форматирование и изменение именованных диапазонов
type: docs
weight: 85
url: /ru/python-net/format-and-modify-named-ranges/
description: В этой статье показано, как форматировать и изменять именованные диапазоны с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python для Excel, Форматирование и изменение именованных диапазонов в Python, Установка цвета фона и атрибутов шрифта для именованного диапазона в Python, Добавление границ именованному диапазону в Python, Переименование именованного диапазона в Python, Объединение диапазонов в Python, Пересечение диапазонов в Python, Объединение ячеек в именованном диапазоне в Python.
---

## **Форматирование диапазонов**

### **Как установить цвет фона и атрибуты шрифта для именованного диапазона**

Чтобы применить форматирование, определите объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style), чтобы указать настройки стиля, и примените его к объекту [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

В следующем примере показано, как установить сплошной цвет заливки (цвет заливки) с настройками шрифта для диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Как добавить границы к именованному диапазону**

Возможно добавить границы к диапазону ячеек вместо одной ячейки. Объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) предоставляет метод [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor), который принимает следующие параметры для добавления границы к диапазону ячеек:

- Тип границы, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- Стиль линии, стиль линии, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- Цвет, цвет линии, выбранный из перечисления Color.

В следующем примере показано, как установить контурную границу для диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Как переименовать именованный диапазон**

Aspose.Cells позволяет переименовывать именованный диапазон по вашему желанию. Вы можете получить именованный диапазон и переименовать его, используя атрибут [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text). В следующем примере показано, как переименовать именованный диапазон.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Как выполнить объединение диапазонов**

Aspose.Cells предоставляет метод [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) для выполнения объединения диапазонов. В следующем примере показано, как выполнить объединение диапазонов.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Как найти пересечение диапазонов**

Aspose.Cells предоставляет метод [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) для пересечения двух диапазонов. Метод возвращает объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Чтобы проверить, пересекается ли диапазон с другим диапазоном, используйте метод [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range), который возвращает логическое значение. Ниже приведен пример того, как найти пересечение диапазонов.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Как объединить ячейки в именованном диапазоне**

Aspose.Cells предоставляет метод [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) для объединения ячеек в диапазоне. В следующем примере показано, как объединить отдельные ячейки именованного диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
