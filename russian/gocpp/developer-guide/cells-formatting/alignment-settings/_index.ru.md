---
title: Настройки выравнивания с Golang через C++
linktitle: Настройки выравнивания
description: В библиотеке Aspose.Cells вы можете использовать настройки выравнивания ячеек для настройки макета и отображения текста. Регулируя такие настройки, как горизонтальное выравнивание, вертикальное выравнивание и перенос текста, у вас есть больше контроля над тем, как текст распределяется в ячейках. В этом документе будут предоставлены подробные инструкции и образцовый код, чтобы помочь вам быстро освоить, как использовать Aspose.Cells для настройки выравнивания ячеек.
keywords: Aspose.Cells, настройка ячейки, горизонтальное выравнивание, вертикальное выравнивание, перенос текста
type: docs
weight: 20
url: /ru/go-cpp/cells-alignment-settings/
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

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Каждый элемент в коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) и [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) для класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) предоставляет полезные свойства для настройки настроек выравнивания.

Выберите любой тип выравнивания текста, используя перечисление [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/). Предопределенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) следующие:

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

Также можно применить установку равномерного распределения с использованием свойства [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/).

{{% /alert %}}

#### **Горизонтальное выравнивание**

Используйте свойство [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/) для горизонтального выравнивания текста.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Вертикальное выравнивание**

Аналогично горизонтальному выравниванию, используйте свойство [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/) для вертикального выравнивания текста.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Отступ**

Возможно установить уровень отступа текста в ячейке с помощью свойства [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Ориентация**

Установите ориентацию (поворот) текста в ячейке с помощью свойства [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

##### **Перенос текста**

Перенос текста в ячейке облегчает его чтение: высота ячейки подстраивается под весь текст, вместо его обрезки или выливания в смежные ячейки. Установите включение или отключение переноса текста с помощью свойства [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Уменьшение для подгонки**

Вариантом для переноса текста в поле является уменьшение размера текста для вписывания его в размеры ячейки. Это делается путем установки свойства [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/) в **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Объединение ячеек**

Как и в Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предоставляет два подхода к этой задаче. Один из способов - вызвать метод коллекции [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/). Метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
Другой способ - сначала вызвать метод коллекции [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/) для создания диапазона ячеек, которые будут объединены. Метод [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) принимает тот же набор параметров, что и метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/), обсуждаемый выше, и возвращает объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) также предоставляет метод [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/), который объединяет диапазон, указанный в объекте [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения задается свойством [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/). Aspose.Cells предоставляет предопределенные типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/cpp/line-breaks-and-text-wrapping/)
