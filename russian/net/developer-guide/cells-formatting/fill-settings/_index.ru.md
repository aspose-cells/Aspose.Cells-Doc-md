---
title: Настройки заливки
description: Aspose.Cells  это библиотека .NET для работы с файлами электронных таблиц. Она поддерживает установку настроек заливки ячеек, позволяя пользователям настраивать фон и стиль ячеек. В этой статье будет рассмотрено, как использовать библиотеку Aspose.Cells для установки настроек заливки ячеек.
keywords: Aspose.Cells, Ячейки, Настройки заливки, Фон, Стиль
type: docs
weight: 50
url: /ru/net/cells-fill-settings/
---

## **Цвета и фоновые узоры**

Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры.

Aspose.Cells также поддерживает эти функции гибким образом. В этой теме мы узнаем, как использовать эти функции с использованием Aspose.Cells.

### **Настройка цветов и фоновых узоров**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

У класса [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) есть методы [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) и [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) предоставляет свойства для установки переднего и заднего цветов ячеек. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), которое содержит набор предопределенных типов фоновых узоров, приведенных ниже.

|**Фоновые узоры**|**Описание**|
| :- | :- |
|DiagonalCrosshatch|Представляет диагональный рисунок косой крест|
|DiagonalStripe|Представляет диагональную полосу|
|Gray6|Представляет 6,25% серый узор|
|Gray12|Представляет 12,5% серый узор|
|Gray25|Представляет 25% серый узор|
|Gray50|Представляет 50% серый узор|
|Gray75|Представляет 75% серый узор|
|HorizontalStripe|Представляет горизонтальный узор полосы|
|None|Представляет отсутствие фона|
|ReverseDiagonalStripe|Представляет обратный диагональный узор полосы|
|Solid|Представляет сплошной узор|
|ThickDiagonalCrosshatch|Представляет толстый диагональный крестовый узор|
|ThinDiagonalCrosshatch|Представляет тонкий диагональный крестовый узор|
|ThinDiagonalStripe|Представляет тонкий диагональный узор полосы|
|ThinHorizontalCrosshatch|Представляет тонкий горизонтальный крестовый узор|
|ThinHorizontalStripe|Представляет тонкий горизонтальный узор полосы|
|ThinReverseDiagonalStripe|Представляет тонкий обратный диагональный узор полосы|
|ThinVerticalStripe|Представляет тонкий вертикальный узор полосы|
|VerticalStripe|Представляет вертикальный узор полосы|

В приведенном ниже примере цвет переднего плана ячейки A1 установлен, но ячейка A2 настроена иметь как передний, так и фоновый цвета с фоновым узором вертикальных полос.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Важно знать**

{{% alert color="primary" %}}

- Чтобы установить передний или фоновый цвет ячейки, используйте свойства объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) или [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor). Оба свойства вступят в силу только в том случае, если свойство [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) будет настроено.
- Свойство [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) задает цвет тени ячейки.
  Свойство [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) указывает тип используемого фонового узора для переднего или фонового цвета. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) содержащее набор предопределенных типов фоновых узоров.
- Если вы выберете значение *BackgroundType.None* из перечисления [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype), то передний цвет не будет применен.
  Аналогично, фоновый цвет не будет применен, если вы выберете значения *BackgroundType.None* или *BackgroundType.Solid*.
- При извлечении цвета тени ячейки, если [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) равно *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) вернет *Color.Empty*.

{{% /alert %}}

### **Применение эффектов градиентного заливки**

Чтобы применить желаемые эффекты градиентного заливки к ячейке, используйте метод [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) объекта [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) соответственно.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Цвета и палитра**

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

С помощью Aspose.Cells можно использовать не только существующие цвета палитры, но и пользовательские цвета. Прежде чем использовать пользовательский цвет, сначала добавьте его в палитру.

Эта тема обсуждает, как добавить пользовательские цвета в палитру.

### **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56-цветную палитру Microsoft Excel. Для использования пользовательского цвета, который не определен в палитре, добавьте цвет в палитру.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит метод [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette), который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- Пользовательский цвет, пользовательский цвет, который будет добавлен.
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
