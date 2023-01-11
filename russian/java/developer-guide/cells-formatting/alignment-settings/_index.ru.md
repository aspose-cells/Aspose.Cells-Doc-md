﻿---
title: Настройки выравнивания
type: docs
weight: 20
url: /ru/java/cells-alignment-settings/
---
## **Настройка параметров выравнивания**

## **Настройки выравнивания в Microsoft Excel**

Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

Как видно из рисунка выше, существуют различные варианты выравнивания:

- Выравнивание текста (горизонтальное и вертикальное)
- Отступ.
- Ориентация.
- Текстовое управление.
- Текстовое направление.

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и более подробно обсуждаются ниже.

## **Настройки выравнивания в Aspose.Cells**

 Aspose.Cells предоставляет[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) и[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) методы для[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) class, которые используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/java/com.aspose.cells/style)Класс предоставляет полезные свойства для настройки параметров выравнивания.

 Выберите любой тип выравнивания текста с помощью[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) перечисление. Предопределенные типы выравнивания текста в[**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)перечисление:

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

 Вы также можете применить настройку распределения по выравниванию с помощью[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) имущество.

{{% /alert %}}

## **Горизонтальное, вертикальное выравнивание и отступ**

 Использовать[**Горизонтальное выравнивание**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) свойство для выравнивания текста по горизонтали и[**Вертикальное выравнивание**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)свойство для выравнивания текста по вертикали.
 Можно установить уровень отступа текста в ячейке с помощью кнопки[**уровень отступа**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) имущество
и tt действует только тогда, когда Горизонтальное выравнивание установлено влево или вправо.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Ориентация**

 Задайте ориентацию (поворот) текста в ячейке кнопкой[**Угол поворота**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Текстовое управление**

В следующем разделе обсуждается, как управлять текстом, устанавливая обтекание текстом, уменьшая размер и другие параметры форматирования.

### **Обтекание текста**

 Обтекание текста в ячейке облегчает чтение: высота ячейки подстраивается под весь текст, вместо того, чтобы обрезать его или распространяться на соседние ячейки. Включите или выключите обтекание текстом с помощью[**Истекствраппед**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Уменьшение размера**

 Вариант переноса текста в поле — уменьшить размер текста, чтобы он соответствовал размерам ячейки. Это делается путем установки[**Уменьшать до размеров**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) имущество. к**истинный**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Объединение Cells**

 Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну. Aspose.Cells предлагает два подхода к этой задаче. Один из способов — позвонить в[**Объединить**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) метод. Метод принимает следующие параметры для объединения ячеек:

- Первая строка: первая строка, с которой начинается слияние.
- Первый столбец: первый столбец, с которого начинается слияние.
- Количество строк: количество строк для объединения.
- Количество столбцов: количество столбцов для объединения.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Направление текста**

Можно задать порядок чтения текста в ячейках. Порядок чтения — это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский — язык с письмом слева направо, а арабский — язык с письмом справа налево.

 Порядок чтения устанавливается с помощью[**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) имущество. Aspose.Cells предоставляет предопределенные типы направления текста в[**Текстдиректионтипе**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)перечисление.

|**Типы направления текста**|**Описание**|
|:- |:- |
|Контекст|Порядок чтения соответствует языку первого введенного символа|
|Слева направо|Порядок чтения слева направо|
|Справа налево|Порядок чтения справа налево|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Предварительные темы**
- [Изменить выравнивание Cells и сохранить существующее форматирование](/cells/ru/java/change-cells-alignment-and-keep-existing-formatting/)
- [Разрывы строк и перенос текста](/cells/ru/java/line-breaks-and-text-wrapping/)