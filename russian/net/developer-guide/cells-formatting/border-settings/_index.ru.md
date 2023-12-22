---
title: Настройки границ
description: Как использовать библиотеку Aspose.Cells в C# для установки стиля границы и цвета ячеек. Регулируя ширину, стиль и цвет границы, вы получаете больше контроля над тем, как выглядят ячейки.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /ru/net/cells-border-settings/
---
##  **Добавление границ к номеру Cells**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от того, где она добавлена. Например, верхняя граница добавляется к верхнему положению ячейки. Пользователи также могут изменять стиль и цвет линий границ.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как и в Microsoft Excel.

###  **Добавление границ к номеру Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)метод в[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)Метод используется для установки стиля форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет свойства для добавления границ к ячейкам.

####  **Добавление границ к Cell**

Разработчики могут добавлять границы к ячейке с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) коллекция. Тип границы передается как индекс в[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) коллекция. Все типы границ предварительно определены в файле[**Тип границы**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) перечисление.

**Перечисление границ**

|**Типы границ**|**Описание**|
| :- | :- |
|Нижняя граница|Нижняя граница|
|ДиагональВниз|Диагональная линия сверху слева направо вниз|
|ДиагональВверх|Диагональная линия снизу слева направо вверх|
|Левая граница|Левая пограничная линия|
|Правая граница|Правая линия границы|
|TopBorder|Верхняя граница|

[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)коллекция хранит все границы. Каждая граница в[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Коллекция представлена[**Граница**](https://reference.aspose.com/cells/net/aspose.cells/border) объект, который предоставляет два свойства,[**Цвет**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) и[**Стиль линии**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)чтобы установить цвет и стиль линии границы соответственно.

Чтобы задать цвет линии границы, выберите цвет с помощью перечисления Color (часть .NET Framework) и назначьте его свойству Color объекта Border.

 Стиль линии границы задается путем выбора стиля линии из[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)перечисление.

**Перечисление CellBorderType**

|**Стили линий**|**Описание**|
| :- | :- |
|ДэшДот|Тонкая штрихпунктирная линия|
|тиреточкаточка|Тонкая штрихпунктирная линия|
|Пунктирная|Пунктир|
|Пунктирный|Пунктирная линия|
|Двойной|Двойная линия|
|Волосы|линия роста волос|
|MediumDashDot|Средняя штрихпунктирная линия|
|СреднийDashDotDot|Средняя штрихпунктирная линия|
|Средний пунктирный|Средняя пунктирная линия|
|Никто|Нет линии|
|Середина|Средняя линия|
|Наклоненная черточка|Наклонная средняя пунктирная линия|
|Толстый|Толстая линия|
|Тонкий|Тонкая линия|
Выберите один из стилей линий и затем назначьте его[**Граница**](https://reference.aspose.com/cells/net/aspose.cells/border) объекты[**Стиль линии**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Вам следует одновременно установить стиль и цвет линии. Две диагональные границы должны иметь одинаковый стиль и цвет.

{{% /alert %}}

####  **Добавление границ к диапазону Cells**

 Также можно добавить границы к диапазону ячеек, а не только к одной ячейке. Для этого сначала создайте диапазон ячеек, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) метод. Он принимает следующие параметры:

- Первая строка — первая строка диапазона.
- Первый столбец представляет первый столбец диапазона.
- Количество строк — количество строк в диапазоне.
- Количество столбцов — количество столбцов в диапазоне.

[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) метод возвращает[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект, содержащий указанный диапазон ячеек.[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект обеспечивает[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) метод, который принимает следующие параметры для добавления границы к диапазону ячеек:

-  *Тип границы** — тип границы, выбранный из[**Тип границы**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)перечисление.
-  *Стиль линии** — стиль линии границы, выбранный из[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)перечисление.
- *Цвет** — цвет линии, выбранный из списка Цвет.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
