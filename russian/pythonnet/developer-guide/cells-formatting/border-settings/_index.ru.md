---
title: Настройки границ
description: Как использовать библиотеку Aspose.Cells для Python via .NET для установки стиля границы и цвета ячеек. Регулируя ширину, стиль и цвет границы, вы получаете больше контроля над внешним видом и отображением ячеек.
keywords: Aspose.Cells для Python via .NET, Настройки границ ячейки, Ширина границы, Стиль границы, Цвет границы
type: docs
weight: 40
url: /ru/python-net/cells-border-settings/
---

## **Добавление границ в ячейки**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от того, куда она добавляется. Например, верхняя граница - это граница, добавленная в верхнюю часть ячейки. Пользователи также могут изменять стиль и цвет линий границ.

С Aspose.Cells для Python via .NET разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как в Microsoft Excel.

### **Добавление границ в ячейки**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), позволяющую получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Каждый элемент коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells для Python via .NET предоставляет метод [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) в классе [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Метод [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) используется для установки параметров форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) предоставляет свойства для добавления границ к ячейкам.

#### **Добавление границ к ячейке**

Разработчики могут добавлять границы к ячейке, используя коллекцию [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) объекта [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Тип границы передается в качестве индекса коллекции [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Все типы границ предварительно определены в перечислении [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).

Перечисление границ

|**Типы границ**|**Описание**|
| :- | :- |
|BOTTOM_BORDER|Линия нижней границы|
|DIAGONAL_DOWN|Диагональная линия сверху слева вниз направо|
|DIAGONAL_UP|Диагональная линия снизу слева вверх направо|
|LEFT_BORDER|Линия левой границы|
|RIGHT_BORDER|Линия правой границы|
|TOP_BORDER|Линия верхней границы|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Установка цвета линии границы осуществляется путем выбора цвета с использованием перечисления Color (часть .NET Framework) и присваивания его свойству Color объекта Border.

Стиль линии границы устанавливается путем выбора стиля линии из перечисления [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).

**Перечисление типов границ ячейки**

|**Стили линий**|**Описание**|
| :- | :- |
|DASH_DOT|Тонкая пунктирно-точечная линия|
|DASH_DOT_DOT|Тонкая двойная пунктирно-точечная линия|
|DASHED|Пунктирная линия|
|DOTTED|Точечная линия|
|DOUBLE|Двойная линия|
|HAIR|Линия тонкая как нить|
|MEDIUM_DASH_DOT|Средняя пунктирно-точечная линия|
|MEDIUM_DASH_DOT_DOT|Средняя двойная пунктирно-точечная линия|
|MEDIUM_DASHED|Средняя пунктирная линия|
|NONE|Нет линии|
|MEDIUM|Средняя линия|
|SLANTED_DASH_DOT|Наклонная пунктирная линия|
|THICK|Толстая линия|
|THIN|Тонкая линия|
Выберите один из стилей линий и затем назначьте его для свойства объекта [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Вы должны установить и стиль линии, и цвет одновременно. Двум диагональным граничным линиям следует иметь одинаковый стиль линии и цвет.

{{% /alert %}}

#### **Добавление границ для диапазона ячеек**

Также есть возможность добавить границы для диапазона ячеек, а не только для одной ячейки. Для этого сначала создайте диапазон ячеек, вызвав метод [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Он принимает следующие параметры:

- Первая строка, первая строка диапазона.
- Первый столбец, представляет первый столбец диапазона.
- Количество строк, количество строк в диапазоне.
- Количество столбцов, количество столбцов в диапазоне.

Метод [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) возвращает объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), который содержит указанный диапазон ячеек. Объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) предоставляет метод [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border), который принимает следующие параметры для добавления границы к диапазону ячеек:

- **Тип границы**, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- **Стиль линии**, стиль линии границы, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- **Цвет**, цвет линии, выбранный из перечисления Color.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

