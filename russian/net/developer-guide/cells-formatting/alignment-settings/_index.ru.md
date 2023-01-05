---
title: Настройки выравнивания
type: docs
weight: 20
url: /ru/net/cells-alignment-settings/
---
## **Настройка параметров выравнивания**

### **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

Как видно из рисунка выше, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Текстовое управление.
- Текстовое направление.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и более подробно обсуждаются ниже.

### **Настройки выравнивания в Aspose.Cells**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

 Aspose.Cells предоставляет[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) методы для[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class, которые используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет полезные свойства для настройки параметров выравнивания.

 Выберите любой тип выравнивания текста с помощью[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) перечисление. Предопределенные типы выравнивания текста в[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)перечисление:

|**Типы выравнивания текста**|**Описание**|
|:- |:- |
|Нижний|Представляет выравнивание текста по нижнему краю|
|Центр|Представляет выравнивание текста по центру|
|CenterAcross|Представляет центр по выравниванию текста|
|Распределенный|Представляет распределенное выравнивание текста|
|Наполнять|Представляет выравнивание заливки текста|
|Общий|Представляет общее выравнивание текста|
|Оправдывать|Представляет выравнивание текста по ширине|
|Оставил|Представляет выравнивание текста по левому краю|
|Правильно|Представляет выравнивание текста по правому краю|
|Вершина|Представляет выравнивание текста по верхнему краю|
|JustifiedLow|Выравнивает текст по скорректированной длине кашиды для арабского текста.|
|ТайскийРаспределенный|Особенно распространен тайский текст, потому что каждый символ рассматривается как слово.|

{{% alert color="primary" %}}

 Вы также можете применить настройку распределения по выравниванию с помощью[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) имущество.

{{% /alert %}}

#### **Горизонтальное выравнивание**

 Использовать[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Горизонтальное выравнивание**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)свойство для выравнивания текста по горизонтали.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Вертикальное выравнивание**

 Подобно горизонтальному выравниванию, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Вертикальное выравнивание**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)свойство для выравнивания текста по вертикали.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Отступ**

 Можно установить уровень отступа текста в ячейке с помощью кнопки[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**уровень отступа**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Ориентация**

 Задайте ориентацию (поворот) текста в ячейке кнопкой[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Угол поворота**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Текстовое управление**

В следующем разделе обсуждается, как управлять текстом, устанавливая обтекание текстом, уменьшая размер и другие параметры форматирования.

##### **Обтекание текста**

 Обтекание текста в ячейке облегчает чтение: высота ячейки подстраивается под весь текст, вместо того, чтобы обрезать его или распространяться на соседние ячейки. Включите или выключите обтекание текстом с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Истекствраппед**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)имущество.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Уменьшение размера**

 Вариант переноса текста в поле — уменьшить размер текста, чтобы он соответствовал размерам ячейки. Это делается путем установки[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Истекствраппед**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) собственность на**истинный**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Объединение Cells**

 Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предлагает два подхода к этой задаче. Один из способов — позвонить в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) метод.[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Метод принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается слияние.
- Первый столбец: первый столбец, с которого начинается слияние.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 Другой способ - сначала вызвать[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) метод для создания диапазона ячеек, которые необходимо объединить.[**Создатьдиапазон**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) метод принимает тот же набор параметров, что и метод[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) рассмотренный выше метод и возвращает[**Спектр**](https://reference.aspose.com/cells/net/aspose.cells/range) объект.[**Спектр**](https://reference.aspose.com/cells/net/aspose.cells/range) объект также обеспечивает[**Объединить**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) метод, который объединяет диапазон, указанный в[**Спектр**](https://reference.aspose.com/cells/net/aspose.cells/range)объект.

##### **Направление текста**

Можно задать порядок чтения текста в ячейках. Порядок чтения — это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский — язык с письмом слева направо, а арабский — язык с письмом справа налево.

 Порядок чтения устанавливается с помощью[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) имущество. Aspose.Cells предоставляет предопределенные типы направления текста в[**Текстдиректионтипе**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)перечисление.

|**Типы направления текста**|**Описание**|
|:- |:- |
|Контекст|Порядок чтения соответствует языку первого введенного символа|
|Слева направо|Порядок чтения слева направо|
|Справа налево|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Предварительные темы**
- [Изменить выравнивание Cells и сохранить существующее форматирование](/cells/ru/net/change-cells-alignment-and-keep-existing-formatting/)
- [Разрывы строк и перенос текста](/cells/ru/net/line-breaks-and-text-wrapping/)

