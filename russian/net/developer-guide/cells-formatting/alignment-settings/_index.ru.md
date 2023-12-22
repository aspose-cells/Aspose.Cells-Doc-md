---
title: Настройки выравнивания
description: В библиотеке Aspose.Cells вы можете использовать настройки выравнивания ячеек для настройки макета и отображения текста. Настраивая такие параметры, как горизонтальное выравнивание, вертикальное выравнивание и перенос текста, вы получаете больше контроля над тем, как текст располагается в ячейках. Этот документ предоставит вам подробные инструкции и пример кода, которые помогут вам быстро понять, как использовать Aspose.Cells для настроек выравнивания ячеек.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /ru/net/cells-alignment-settings/
---
##  **Настройка параметров выравнивания**

###  **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, знаком с настройками выравнивания в Microsoft Excel.

Как видно на рисунке выше, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Текстовый контроль.
- Направление текста.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и более подробно обсуждаются ниже.

###  **Настройки выравнивания в Aspose.Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

 Aspose.Cells обеспечивает[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы для[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) класс, который используется для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет полезные свойства для настройки параметров выравнивания.

 Выберите любой тип выравнивания текста, используя кнопку[**Тексталигменттипе**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) перечисление. Предопределенные типы выравнивания текста в[**Тексталигменттипе**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)перечисление:

|**Типы выравнивания текста**|**Описание**|
| :- | :- |
|Нижний|Представляет выравнивание текста по нижнему краю|
|Центр|Представляет выравнивание текста по центру|
|ЦентрПоперек|Представляет центр выравнивания текста|
|Распределенный|Представляет распределенное выравнивание текста.|
|Наполнять|Представляет выравнивание текста заливки.|
|Общий|Представляет общее выравнивание текста.|
|Оправдывать|Представляет выравнивание текста по ширине.|
|Левый|Представляет выравнивание текста по левому краю.|
|Верно|Представляет выравнивание текста по правому краю.|
|Вершина|Представляет выравнивание текста по верхнему краю.|
|JustifiedLow|Выравнивает текст по скорректированной длине кашиды для арабского текста.|
|ТайскийРаспределенный|Особенно распределяет тайский текст, поскольку каждый символ рассматривается как слово.|

{{% alert color="primary" %}}

 Вы также можете применить параметр выравнивания распределенного распределения, используя команду[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) свойство.

{{% /alert %}}

####  **Горизонтальное выравнивание**

 Использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Горизонтальное выравнивание**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)свойство выравнивания текста по горизонтали.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **Вертикальное выравнивание**

 Подобно горизонтальному выравниванию, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Вертикальное выравнивание**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)свойство для выравнивания текста по вертикали.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **Отступ**

 Можно установить уровень отступа текста в ячейке с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Отступлевел**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **Ориентация**

 Задайте ориентацию (поворот) текста в ячейке с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Угол поворота**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **Текстовый контроль**

В следующем разделе обсуждается, как управлять текстом, устанавливая перенос текста, сжатие по размеру и другие параметры форматирования.

#####  **Перенос текста**

 Перенос текста в ячейке облегчает чтение: высота ячейки подстраивается под весь текст, а не обрезается или перетекает в соседние ячейки. Включите или отключите перенос текста с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Истекстобернутый**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **Сокращение, чтобы соответствовать**

 Вариант переноса текста в поле — уменьшить размер текста до размеров ячейки. Это делается путем установки[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Истекстобернутый**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)свойство в *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **Объединение Cells**

 Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предлагает два подхода к этой задаче. Один из способов – позвонить в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) метод.[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Метод принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой следует начать слияние.
- Первый столбец: первый столбец, с которого следует начать объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Другой способ — сначала позвонить в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) метод для создания диапазона ячеек, подлежащих объединению.[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) метод принимает тот же набор параметров, что и метод[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) метод, описанный выше, и возвращает[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект.[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range) объект также предоставляет[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) метод, который объединяет диапазон, указанный в[**Диапазон**](https://reference.aspose.com/cells/net/aspose.cells/range)объект.

#####  **Направление текста**

Есть возможность задать порядок чтения текста в ячейках. Порядок чтения — это визуальный порядок отображения символов, слов и т. д. Например, английский — это язык слева направо, а арабский — язык справа налево.

 Порядок чтения задается с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Текстдиректион**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) свойство. Aspose.Cells предоставляет предварительно определенные типы направления текста в[**Текстдиректионтипе**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)перечисление.

|**Типы направления текста**|**Описание**|
| :- | :- |
|Контекст|Порядок чтения соответствует языку первого введенного символа.|
|Слева направо|Порядок чтения слева направо|
|Справа налево|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **Предварительные темы**
- [Измените выравнивание Cells и сохраните существующее форматирование.](/cells/ru/net/change-cells-alignment-and-keep-existing-formatting/)
- [Разрывы строк и перенос текста](/cells/ru/net/line-breaks-and-text-wrapping/)

