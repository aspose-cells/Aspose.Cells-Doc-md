---
title: Настройки выравнивания
description: В библиотеке Aspose.Cells вы можете использовать настройки выравнивания ячеек для настройки макета и отображения текста. Регулируя такие настройки, как горизонтальное выравнивание, вертикальное выравнивание и перенос текста, у вас есть больше контроля над тем, как текст распределяется в ячейках. В этом документе будут предоставлены подробные инструкции и образцовый код, чтобы помочь вам быстро освоить, как использовать Aspose.Cells для настройки выравнивания ячеек.
keywords: Aspose.Cells, настройка ячейки, горизонтальное выравнивание, вертикальное выравнивание, перенос текста
type: docs
weight: 20
url: /ru/net/cells-alignment-settings/
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

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и обсуждаются более подробно ниже.

### **Настройки выравнивания в Aspose.Cells**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) и [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) для класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) предоставляет полезные свойства для настройки настроек выравнивания.

Выберите любой тип выравнивания текста, используя перечисление [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype). Предопределенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) следующие:

|**Типы выравнивания текста**|**Описание**|
| :- | :- |
|Bottom|Представляет выравнивание текста по нижнему краю|
|Center|Представляет выравнивание текста по центру|
|CenterAcross|Представляет выравнивание текста по центру с наложением|
|Distributed|Представляет распределенное выравнивание текста|
|Fill|Представляет выравнивание текста по заливке|
|General|Представляет общее выравнивание текста|
|Justify|Представляет выравнивание текста по ширине|
|Left|Представляет выравнивание текста влево|
|Right|Представляет выравнивание текста вправо|
|Top|Представляет верхнее выравнивание текста|
|JustifiedLow|Выравнивает текст с настройкой длины кашиды для арабского текста.|
|ThaiDistributed|Распределяет текст на тайском, поскольку каждый символ рассматривается как слово.|

{{% alert color="primary" %}}

Также можно применить установку равномерного распределения с использованием свойства [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed).

{{% /alert %}}

#### **Горизонтальное выравнивание**

Используйте свойство [**HorizontalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) для горизонтального выравнивания текста.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Вертикальное выравнивание**

Аналогично горизонтальному выравниванию, используйте свойство [**VerticalAlignment**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) для вертикального выравнивания текста.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Отступ**

Возможно установить уровень отступа текста в ячейке с помощью свойства [**IndentLevel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Ориентация**

Установите ориентацию (поворот) текста в ячейке с помощью свойства [**RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

##### **Перенос текста**

Перенос текста в ячейке облегчает его чтение: высота ячейки подстраивается под весь текст, вместо его обрезки или выливания в смежные ячейки. Установите включение или отключение переноса текста с помощью свойства [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Уменьшение для подгонки**

Вариантом для переноса текста в поле является уменьшение размера текста для вписывания его в размеры ячейки. Это делается путем установки свойства [**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) в **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Объединение ячеек**

Как и в Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предоставляет два подхода к этой задаче. Один из способов - вызвать метод коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index). Метод [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Другой способ - сначала вызвать метод коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) для создания диапазона ячеек, которые будут объединены. Метод [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) принимает тот же набор параметров, что и метод [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index), обсуждаемый выше, и возвращает объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) также предоставляет метод [**Merge**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge), который объединяет диапазон, указанный в объекте [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

##### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения задается свойством [**TextDirection**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Aspose.Cells предоставляет предопределенные типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/net/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/net/line-breaks-and-text-wrapping/)

