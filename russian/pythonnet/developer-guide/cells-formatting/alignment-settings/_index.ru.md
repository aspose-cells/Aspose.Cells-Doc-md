---
title: Настройки выравнивания
description: В библиотеке Aspose.Cells для Python via .NET вы можете использовать настройки выравнивания ячеек для изменения макета и отображения текста. Путем настройки таких параметров, как горизонтальное выравнивание, вертикальное выравнивание и перенос текста, вы получаете больший контроль над тем, как текст отображается в ячейках. В этом документе приведены подробные шаги и пример кода, которые помогут вам быстро понять, как использовать Aspose.Cells для Python via .NET для настройки выравнивания ячеек.
keywords: Aspose.Cells для Python via .NET, выравнивание ячеек, горизонтальное выравнивание, вертикальное выравнивание, перенос текста
type: docs
weight: 20
url: /ru/python-net/cells-alignment-settings/
---

## **Настройка настроек выравнивания**

### **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

Как видно на приведенной выше фигуре, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Управление текстом.
- Направление текста.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells для Python via .NET и подробно обсуждаются ниже.

### **Настройки выравнивания в Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получать доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Каждый элемент в коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells для Python via .NET предоставляет методы [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) и [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) для класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell), используемые для получения и установки формата ячейки. Класс [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) предоставляет полезные свойства для настройки параметров выравнивания.

Выберите любой тип выравнивания текста, используя перечисление [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype). Предопределенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) следующие:

|**Типы выравнивания текста**|**Описание**|
| :- | :- |
|GENERAL|Представляет общий текстовый выравнивание|
|BOTTOM|Представляет нижнее выравнивание текста|
|CENTER|Представляет центрирование текста|
|CENTER_ACROSS|Представляет выравнивание по центру через ячейки|
|DISTRIBUTED|Представляет распределенное выравнивание текста|
|FILL|Представляет заливку текста|
|JUSTIFY|Представляет оправданное выравнивание текста|
|LEFT|Обозначает выравнивание текста по левому краю|
|RIGHT|Обозначает выравнивание текста по правому краю|
|TOP|Обозначает выравнивание текста по верхнему краю|
|JUSTIFIED_LOW|Выравнивает текст с учетом скорректированной длины кашиды для арабского текста|
|THAI_DISTRIBUTED|Специально распределяет тайский текст, потому что каждый символ считается словом|

{{% alert color="primary" %}}

Также можно применить установку равномерного распределения с использованием свойства [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed).

{{% /alert %}}

#### **Горизонтальное выравнивание**

Используйте свойство [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) для горизонтального выравнивания текста.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Вертикальное выравнивание**

Аналогично горизонтальному выравниванию, используйте свойство [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) для вертикального выравнивания текста.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Отступ**

Возможно установить уровень отступа текста в ячейке с помощью свойства [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Ориентация**

Установите ориентацию (поворот) текста в ячейке с помощью свойства [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

##### **Перенос текста**

Перенос текста в ячейке облегчает его чтение: высота ячейки подстраивается под весь текст, вместо его обрезки или выливания в смежные ячейки. Установите включение или отключение переноса текста с помощью свойства [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Уменьшение для подгонки**

Вариантом для переноса текста в поле является уменьшение размера текста для вписывания его в размеры ячейки. Это делается путем установки свойства [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) в **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Объединение ячеек**

Как Microsoft Excel, Aspose.Cells для Python via .NET поддерживает объединение нескольких ячеек в одну. Aspose.Cells для Python via .NET предлагает два способа выполнения этой задачи. Один способ — вызвать метод [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/). Метод [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

Другой способ - сначала вызвать метод коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) для создания диапазона ячеек, которые будут объединены. Метод [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) принимает тот же набор параметров, что и метод [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge), обсуждаемый выше, и возвращает объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) также предоставляет метод [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge), который объединяет диапазон, указанный в объекте [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

##### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения устанавливается с помощью свойства [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Aspose.Cells для Python via .NET предоставляет предустановленные типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|CONTEXT|Порядок чтения соответствует языку первого введенного символа|
|LEFT_TO_RIGHT|Порядок чтения слева направо|
|RIGHT_TO_LEFT|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/python-net/line-breaks-and-text-wrapping/)


