---
title: Настройки заполнения
type: docs
weight: 50
url: /ru/net/cells-fill-settings/
---
## **Цвета и фоновые узоры**

Microsoft В Excel можно установить цвета переднего плана (контура) и фона (заливки) ячеек и узоров фона.

Aspose.Cells также гибко поддерживает эти функции. В этой теме мы научимся использовать эти функции, используя Aspose.Cells.

### **Настройка цветов и фоновых рисунков**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция. Каждый элемент в[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция представляет собой объект[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)учебный класс.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) имеет[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) а также[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) методы, которые используются для получения и установки форматирования ячейки.[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style)Класс предоставляет свойства для установки цветов переднего плана и фона ячеек. Aspose.Cells предоставляет[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)перечисление, содержащее набор предопределенных типов фоновых узоров, которые приведены ниже.

|**Фоновые узоры**|**Описание**|
|:- |:- |
|Диагональ|Представляет диагональную штриховку|
|ДиагональПолоса|Представляет собой рисунок диагональной полосы|
|Серый6|Представляет 6,25% серого узора|
|Серый12|Представляет 12,5% серый узор|
|Серый25|Представляет 25% серый узор|
|Серый50|Представляет 50% серый шаблон|
|серый75|Представляет 75% серый узор|
|ГоризонтальнаяПолоса|Представляет собой рисунок с горизонтальной полосой|
|Никто|Не представляет фона|
|ОбратныйДиагональПолоса|Представляет собой узор из обратных диагональных полос.|
|Твердый|Представляет сплошной узор|
|ТолстыйДиагональ|Представляет толстую диагональную штриховку|
|ТонкийДиагональный|Представляет образец тонкой диагональной штриховки|
|ТонкийДиагональПолоса|Представляет собой узор из тонких диагональных полос.|
|ТонкийГоризонтальный|Представляет собой тонкую горизонтальную штриховку|
|ТонкийГоризонтальнаяПолоса|Представляет собой узор из тонких горизонтальных полос.|
|тонкийобратныйдиагональполоса|Представляет собой узор из тонких обратных диагональных полос.|
|ТонкийВертикальныйПолоса|Представляет собой узор из тонких вертикальных полос.|
|Вертикальная полоса|Представляет собой рисунок с вертикальными полосами|

В приведенном ниже примере установлен цвет переднего плана ячейки A1, но ячейка A2 настроена так, чтобы иметь цвета переднего плана и фона с фоновым узором с вертикальными полосами.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Важно знать**

{{% alert color="primary" %}}

-  Чтобы установить цвет переднего плана или фона ячейки, используйте кнопку[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Цвет переднего плана**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) или же[**Фоновый цвет**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) характеристики. Оба свойства вступят в силу, только если[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)свойство настроено.
- [**Цвет переднего плана**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)Свойство задает цвет тени ячейки.
[**Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)Свойство указывает тип фонового узора, используемого для цвета переднего плана или фона. Aspose.Cells предоставляет перечисление,[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)который содержит набор предопределенных типов фоновых узоров.
-  Если вы выберете*BackgroundType.Нет* значение из[**Тип фона**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)перечисление, цвет переднего плана не применяется.
 Аналогично, цвет фона не применяется, если вы выбираете*BackgroundType.Нет* или же*BackgroundType.Solid* ценности.
-  При получении цвета заливки/затенения ячейки, если[**Стиль.Шаблон**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) является*BackgroundType.Нет*, [**Стиль.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) вернется*Цвет.Пустой*.

{{% /alert %}}

### **Применение эффектов градиентной заливки**

 Чтобы применить нужные эффекты градиентной заливки к ячейке, используйте[**Стиль**](https://reference.aspose.com/cells/net/aspose.cells/style) объекты[**УстановитьДваЦветГрадиент**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)метод соответственно.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

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

В палитре всего 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный с использованием предыдущего цвета, изменяется. Поэтому при смене палитры будьте очень осторожны. Более того, это ограничение относится только к формату файлов XLS (Excel 97–2003), поскольку такого ограничения нет для XLSX или других расширенных форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
