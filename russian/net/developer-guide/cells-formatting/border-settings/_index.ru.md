---
title: Настройки границ
description: Как использовать библиотеку Aspose.Cells на C#, чтобы задать стиль границы и цвет ячеек. Изменяя ширину, стиль и цвет границы, вы имеете больший контроль над тем, как будут выглядеть и выглядеть ячейки.
keywords: Aspose.Cells, настройки границ ячейки, C#, ширина границы, стиль границы, цвет границы
type: docs
weight: 40
url: /ru/net/cells-border-settings/
---

## **Добавление границ в ячейки**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от того, куда она добавляется. Например, верхняя граница - это граница, добавленная в верхнюю часть ячейки. Пользователи также могут изменять стиль и цвет линий границ.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их внешний вид таким же гибким способом, как в Microsoft Excel.

### **Добавление границ в ячейки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells предоставляет метод [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) в классе [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Метод [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) используется для установки стиля форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) предоставляет свойства для добавления границ к ячейкам.

#### **Добавление границ к ячейке**

Разработчики могут добавлять границы к ячейке, используя коллекцию [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) объекта [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Тип границы передается в качестве индекса коллекции [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Все типы границ предварительно определены в перечислении [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).

Перечисление границ

|**Типы границ**|**Описание**|
| :- | :- |
|BottomBorder|Линия нижней границы|
|DiagonalDown|Диагональная линия от верхнего левого до нижнего правого|
|DiagonalUp|Диагональная линия от нижнего левого до верхнего правого|
|LeftBorder|Линия левой границы|
|RightBorder|Линия правой границы|
|TopBorder|Линия верхней границы|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Установка цвета линии границы осуществляется путем выбора цвета с использованием перечисления Color (часть .NET Framework) и присваивания его свойству Color объекта Border.

Стиль линии границы устанавливается путем выбора стиля линии из перечисления [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).

**Перечисление типов границ ячейки**

|**Стили линий**|**Описание**|
| :- | :- |
|DashDot|Тонкая пунктирная линия|
|DashDotDot|Тонкая штрих-пунктирная линия|
|Dashed|Пунктирная линия|
|Dotted|Точечная линия|
|Double|Двойная линия|
|Hair|Линия минимальной толщины|
|MediumDashDot|Средняя штрих-пунктирная линия|
|MediumDashDotDot|Средняя штрих-точечно-пунктирная линия|
|MediumDashed|Средняя пунктирная линия|
|None|Нет линии|
|Medium|Средняя линия|
|SlantedDashDot|Наклоненная средняя штрих-пунктирная линия|
|Thick|Толстая линия|
|Thin|Тонкая линия|
Выберите один из стилей линий и затем назначьте его для свойства объекта [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Вы должны установить и стиль линии, и цвет одновременно. Двум диагональным граничным линиям следует иметь одинаковый стиль линии и цвет.

{{% /alert %}}

#### **Добавление границ для диапазона ячеек**

Также есть возможность добавить границы для диапазона ячеек, а не только для одной ячейки. Для этого сначала создайте диапазон ячеек, вызвав метод [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Он принимает следующие параметры:

- Первая строка, первая строка диапазона.
- Первый столбец, представляет первый столбец диапазона.
- Количество строк, количество строк в диапазоне.
- Количество столбцов, количество столбцов в диапазоне.

Метод [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) возвращает объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), который содержит указанный диапазон ячеек. Объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) предоставляет метод [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder), который принимает следующие параметры для добавления границы к диапазону ячеек:

- **Тип границы**, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- **Стиль линии**, стиль линии границы, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- **Цвет**, цвет линии, выбранный из перечисления Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
