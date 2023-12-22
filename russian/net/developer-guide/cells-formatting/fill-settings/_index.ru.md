---
title: Заполнить настройки
description: Aspose.Cells — это библиотека .NET для работы с файлами электронных таблиц. Он поддерживает настройку параметров заливки ячеек, позволяя пользователям настраивать фон и стиль ячеек. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для установки параметров заполнения ячеек.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /ru/net/cells-fill-settings/
---
##  **Цвета и фоновые узоры**

Microsoft Excel может устанавливать цвета переднего плана (контура) и фона (заливки) ячеек и фоновых узоров.

Aspose.Cells также гибко поддерживает эти функции. В этой теме мы научимся использовать эти функции с помощью Aspose.Cells.

###  **Настройка цветов и фоновых рисунков**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Каждый предмет в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)сорт.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) имеет[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) и[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) методы, которые используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет свойства для установки цветов переднего плана и фона ячеек. Aspose.Cells предоставляет[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)перечисление, содержащее набор предварительно определенных типов фоновых шаблонов, которые приведены ниже.

|**Фоновые узоры**|**Описание**|
| :- | :- |
|Диагональ|Представляет собой диагональную штриховку.|
|Диагональная Полоса|Представляет собой узор диагональных полос.|
|Серый6|Представляет 6,25% серого рисунка.|
|Серый12|Представляет 12,5% серого рисунка.|
|Серый25|Представляет 25 % серого рисунка.|
|Серый50|Представляет 50 % серого рисунка.|
|Грей75|Представляет 75 % серого рисунка.|
|Горизонтальная Полоса|Представляет собой узор горизонтальных полос.|
|Никто|Не представляет никакого фона|
|РеверсДиагональПолоса|Представляет собой узор из обратных диагональных полос.|
|Твердый|Представляет собой сплошной узор|
|ТолстыйДиагональный|Представляет собой толстую диагональную штриховку.|
|Тонкийдиагональный|Представляет собой тонкую диагональную штриховку.|
|ТонкаяДиагональнаяПолоса|Представляет собой узор из тонких диагональных полос.|
|ТонкийГоризонтальный|Представляет собой тонкую горизонтальную штриховку.|
|ТонкаяГоризонтальнаяПолоса|Представляет собой узор из тонких горизонтальных полос.|
|ТонкийРеверсДиагональнаяПолоса|Представляет собой узор из тонких обратных диагональных полос.|
|ТонкаяВертикальнаяПолоса|Представляет собой узор из тонких вертикальных полос.|
|Вертикальная полоса|Представляет собой рисунок вертикальных полос.|

В приведенном ниже примере установлен цвет переднего плана ячейки A1, но A2 настроен на использование как цвета переднего плана, так и цвета фона с фоновым узором в виде вертикальных полос.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Важно знать**

{{% alert color="primary" %}}

-  Чтобы установить цвет переднего плана или фона ячейки, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Цвет переднего плана**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) или[**Фоновый цвет**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) характеристики. Оба свойства вступят в силу, только если[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)свойство настроено.
- [**Цвет переднего плана**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)Свойство устанавливает цвет тени ячейки.
[**Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)Свойство определяет тип фонового рисунка, используемого для цвета переднего плана или фона. Aspose.Cells предоставляет перечисление,[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). который содержит набор предопределенных типов фоновых узоров.
-  Если вы выберете*ФонТип.Нет* значение из[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)перечисления, цвет переднего плана не применяется.
 Аналогично, цвет фона не применяется, если вы выберете*ФонТип.Нет* или*BackgroundType.Solid* ценности.
-  При получении цвета заливки/затенения ячейки, если[**Стиль.Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) есть *BackgroundType.None*,[**Стиль.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) вернет *Color.Empty*.

{{% /alert %}}

###  **Применение эффектов градиентной заливки**

 Чтобы применить к ячейке желаемые эффекты градиентной заливки, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**НаборДваЦветГрадиент**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)метод соответственно.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Цвета и палитра**

Палитра — это количество цветов, доступных для использования при создании изображения. Использование стандартизированной палитры в презентации позволяет пользователю создать единообразный вид. Каждый файл Excel Microsoft (97-2003) содержит палитру из 56 цветов, которые можно применять к ячейкам, шрифтам, линиям сетки, графическим объектам, заливкам и линиям диаграммы.

С Aspose.Cells можно использовать не только существующие цвета палитры, но и собственные цвета. Прежде чем использовать собственный цвет, сначала добавьте его в палитру.

В этом разделе обсуждается, как добавить в палитру собственные цвета.

###  **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56 цветовую палитру Excel Microsoft. Чтобы использовать пользовательский цвет, который не определен в палитре, добавьте цвет в палитру.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс обеспечивает[**Изменение палитры**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) метод, который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- Пользовательский цвет — добавляемый пользовательский цвет.
- Индекс — индекс цвета в палитре, который будет заменен пользовательским цветом. Должно быть между 0-55.

В приведенном ниже примере в палитру добавляется пользовательский цвет (Орхидея) перед его применением к шрифту.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

В палитре всего 56 цветов. Когда вы добавляете в палитру пользовательский цвет, палитра изменяется, и любой элемент в файле, отформатированный с использованием предыдущего цвета, изменяется. Поэтому, меняя палитру, будьте очень осторожны. Более того, это ограничение существует только в формате файла XLS (Excel 97–2003), поскольку такого ограничения нет для XLSX или других расширенных форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
