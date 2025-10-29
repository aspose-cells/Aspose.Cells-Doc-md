---
title: Настройки выравнивания
linktitle: Настройки выравнивания
description: В библиотеке Aspose.Cells вы можете использовать настройки выравнивания ячейки для регулировки расположения и отображения текста с помощью Node.js через C++. В этом документе подробно описаны шаги и пример кода использования Aspose.Cells для настроек выравнивания ячейки.
keywords: Aspose.Cells, выравнивание ячейки, горизонтальное выравнивание, вертикальное выравнивание, перенос текста Node.js через C++
type: docs
weight: 20
url: /ru/nodejs-cpp/cells-alignment-settings/
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

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получать доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) обеспечивает коллекцию [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

Aspose.Cells предоставляет методы [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) и [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) для класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell), используемые для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) содержит полезные свойства для настройки параметров выравнивания.

Выберите любой тип выравнивания текста с помощью перечисления [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype). Встроенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) включают:

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

Также вы можете применить настройку равномерного распределения с помощью метода [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-).

{{% /alert %}}

#### **Горизонтальное выравнивание**

Используйте метод [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), чтобы выровнять текст по горизонтали.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Вертикальное выравнивание**

Аналогично горизонтальному выравниванию, используйте метод [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) для вертикального выравнивания текста.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Отступ**

Можно установить уровень отступа текста в ячейке с помощью метода [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Ориентация**

Настройте ориентацию (поворот) текста в ячейке с помощью метода [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

##### **Перенос текста**

Перенос текста в ячейке облегчает чтение: высота ячейки автоматически подбирается под весь текст, избегая обрезки или стекания в соседние ячейки. Включите или выключите перенос текста с помощью метода [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Уменьшение для подгонки**

Вариант переноса текста в поле — уменьшить размер текста для вписывания в размер ячейки. Это делается установкой метода [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) в **true**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Объединение ячеек**

Как и в Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предлагает два способа выполнения этой задачи. Один способ — вызвать метод [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Метод [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) принимает параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


Другой способ — сначала вызвать метод [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) для создания диапазона ячеек для объединения. Метод [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) принимает те же параметры, что и выше, и возвращает объект [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range). Объект [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) также содержит метод [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--), объединяющий указанный диапазон в объекте [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).

##### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения устанавливается свойством [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). В Aspose.Cells есть предопределённые типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
