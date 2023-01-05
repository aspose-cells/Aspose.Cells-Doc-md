---
title: Настройки границы
type: docs
weight: 40
url: /ru/net/cells-border-settings/
---
## **Добавление границ к Cells**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от того, где она добавлена. Например, верхняя граница добавляется к верхнему положению ячейки. Пользователи также могут изменять стиль и цвет линий границ.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как и в Microsoft Excel.

### **Добавление границ к Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)метод в[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)Метод используется для установки стиля форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет свойства для добавления границ к ячейкам.

#### **Добавление границ к Cell**

Разработчики могут добавлять границы к ячейке с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) коллекция. Тип границы передается как индекс[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) коллекция. Все типы границ предварительно определены в[**Тип границы**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) перечисление.

**Перечисление границы**

|**Типы границ**|**Описание**|
|:- |:- |
|нижняя граница|Нижняя граница|
|ДиагональВниз|Диагональная линия сверху слева направо вниз|
|ДиагональВверх|Диагональная линия снизу слева направо вверх|
|Левая граница|Левая пограничная линия|
|Правая граница|Правая пограничная линия|
|Верхняя граница|Верхняя граница|

[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)коллекция хранит все границы. Каждая граница в[**Границы**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) Коллекция представлена[**Граница**](https://reference.aspose.com/cells/net/aspose.cells/border) объект, который предоставляет два свойства,[**Цвет**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) и[**Стиль линии**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)чтобы установить цвет и стиль линии границы соответственно.

Чтобы задать цвет линии границы, выберите цвет с помощью перечисления Color (часть .NET Framework) и назначьте его свойству Color объекта Border.

 Стиль линии границы задается путем выбора стиля линии в[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)перечисление.

**Перечисление CellBorderType**

|**Стили линий**|**Описание**|
|:- |:- |
|DashDot|Тонкая штрихпунктирная линия|
|тиреточкаточка|Тонкая штрихпунктирная линия|
|Пунктирная|Пунктир|
|Пунктирный|Пунктирная линия|
|Двойной|Двойная линия|
|Волосы|Волосы|
|MediumDashDot|Средняя штрихпунктирная линия|
|MediumDashDotDot|Средняя штрихпунктирная линия|
|Средний пунктирный|Средняя пунктирная линия|
|Никто|Нет линии|
|Середина|Средняя линия|
|SlantedDashDot|Наклонная средняя штрихпунктирная линия|
|Толстый|Толстая линия|
|Тонкий|Тонкая линия|
Выберите один из стилей линий, а затем назначьте его[**Граница**](https://reference.aspose.com/cells/net/aspose.cells/border) объекты[**Стиль линии**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Вы должны установить стиль и цвет линии одновременно. Две диагональные линии границы должны иметь тот же стиль и цвет линии.

{{% /alert %}}

#### **Добавление границ к диапазону Cells**

Также можно добавить границы к диапазону ячеек, а не только к одной ячейке. Для этого сначала создайте диапазон ячеек, вызвав метод[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) метод. Он принимает следующие параметры:

- First Row, первая строка диапазона.
- Первый столбец представляет первый столбец диапазона.
- Количество строк, количество строк в диапазоне.
- Количество столбцов, количество столбцов в диапазоне.

[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) метод возвращает[**Спектр**](https://reference.aspose.com/cells/net/aspose.cells/range) объект, содержащий указанный диапазон ячеек.[**Спектр**](https://reference.aspose.com/cells/net/aspose.cells/range) объект обеспечивает[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) метод, который принимает следующие параметры для добавления границы к диапазону ячеек:

- **Тип границы** , тип границы, выбранный из[**Тип границы**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)перечисление.
- **Стиль линии** , стиль линии границы, выбранный из[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)перечисление.
- **Цвет**, цвет линии, выбранный из перечисления Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Цвета и палитра**

Палитра — это количество цветов, доступных для использования при создании изображения. Использование стандартизированной палитры в презентации позволяет пользователю создать единообразный вид. Каждый файл Excel Microsoft (97-2003) содержит палитру из 56 цветов, которые можно применять к ячейкам, шрифтам, линиям сетки, графическим объектам, заливкам и линиям диаграммы.

С Aspose.Cells можно использовать не только существующие цвета палитры, но и пользовательские цвета. Прежде чем использовать собственный цвет, сначала добавьте его в палитру.

В этом разделе обсуждается, как добавить пользовательские цвета в палитру.

### **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56-цветную палитру Excel Microsoft. Чтобы использовать пользовательский цвет, не определенный в палитре, добавьте этот цвет в палитру.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс предоставляет[**Изменить палитру**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) метод, который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- Пользовательский цвет, добавляемый пользовательский цвет.
- Индекс, индекс цвета в палитре, который заменит пользовательский цвет. Должно быть между 0-55.

В приведенном ниже примере пользовательский цвет (Орхидея) добавляется в палитру перед его применением к шрифту.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

В палитре всего 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный с использованием предыдущего цвета, изменяется. Поэтому при смене палитры будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97 - 2003), поскольку такого ограничения нет для XLSX или других расширенных форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}


