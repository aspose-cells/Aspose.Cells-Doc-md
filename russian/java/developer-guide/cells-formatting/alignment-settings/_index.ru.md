---
title: Настройки выравнивания
type: docs
weight: 20
url: /ru/java/cells-alignment-settings/
---

## **Настройка настроек выравнивания**

## **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

Как видно на приведенной выше фигуре, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Управление текстом.
- Направление текста.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и обсуждаются более подробно ниже.

## **Настройки выравнивания в Aspose.Cells**

Aspose.Cells предоставляет методы [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) и [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) для класса [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) предоставляет полезные свойства для настройки настроек выравнивания.

Выберите любой тип выравнивания текста, используя перечисление [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype). Предопределенные типы выравнивания текста в перечислении [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) следующие:

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

Также можно применить установку равномерного распределения с использованием свойства [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed).

{{% /alert %}}

## **Горизонтальное и вертикальное выравнивание и отступ**

Используйте свойство [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) для выравнивания текста по горизонтали и свойство [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) для выравнивания текста по вертикали.
Возможно установить уровень отступа текста в ячейке с помощью свойства [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel). 
и это влияет только при горизонтальном выравнивании влево или вправо.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Ориентация**

Установите ориентацию (поворот) текста в ячейке с помощью свойства [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Управление текстом**

В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.

### **Перенос текста**

Перенос текста в ячейке делает его легче для чтения: высота ячейки настраивается, чтобы вместить весь текст, вместо его обрезания или переполнения в смежные ячейки. Установите перенос текста включенным или выключенным с помощью свойства [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Уменьшение для подгонки**

Опция переноса текста в ячейке - уменьшить размер текста, чтобы он соответствовал размерам ячейки. Это делается путем установки свойства [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) на **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Объединение ячеек**

Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предоставляет два подхода к этой задаче. Один из способов - вызвать метод [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-). Метод принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается объединение.
- Первая колонка: первая колонка, с которой начинается объединение.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Направление текста**

Можно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский язык - это язык слева направо, а арабский язык - это язык справа налево.

Порядок чтения устанавливается с помощью свойства [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection). Aspose.Cells предоставляет предопределенные типы направления текста в перечислении [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection).

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Продвинутые темы**
- [Изменение выравнивания ячеек и сохранение существующего форматирования](/cells/ru/java/change-cells-alignment-and-keep-existing-formatting/)
- [Перенос строк и перенос текста](/cells/ru/java/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="java" >}}
