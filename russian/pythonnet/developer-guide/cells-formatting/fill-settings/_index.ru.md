---
title: Настройки заливки
description: Aspose.Cells — это библиотека Python для работы с файлами электронных таблиц. Она поддерживает установку настроек заливки ячеек, что позволяет пользователям настраивать фон и стиль ячеек. В этой статье будет описано, как использовать библиотеку Aspose.Cells для Python via .NET для установки настроек заливки ячеек.
keywords: Aspose.Cells для Python via .NET, ячейки, настройки заливки, фон, стиль
type: docs
weight: 50
url: /ru/python-net/cells-fill-settings/
---

## **Цвета и фоновые узоры**

Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры.

Aspose.Cells для Python via .NET также поддерживает эти функции в гибкой форме. В этом разделе мы научимся использовать эти функции с помощью Aspose.Cells.

### **Настройка цветов и фоновых узоров**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

У [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) есть методы [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) и [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) предоставляет свойства для установки цветов переднего и заднего фона ячеек. Aspose.Cells для Python via .NET предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), которое содержит набор предопределенных типов фоновых узоров, приведенных ниже.

|**Фоновые узоры**|**Описание**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Представляет диагональный крестовый узор|
|DIAGONAL_STRIPE|Представляет диагональную полосу|
|GRAY6|Представляет серый узор 6,25%|
|GRAY12|Представляет серый узор 12,5%|
|GRAY25|Представляет серый узор 25%|
|GRAY50|Представляет серый узор 50%|
|GRAY75|Представляет серый узор 75%|
|HORIZONTAL_STRIPE|Представляет горизонтальную полосу|
|NONE|Представляет отсутствие фона|
|REVERSE_DIAGONAL_STRIPE|Представляет обратную диагональную полосу|
|SOLID|Представляет сплошной узор|
|THICK_DIAGONAL_CROSSHATCH|Представляет толстый диагональный крест|
|THIN_DIAGONAL_CROSSHATCH|Представляет тонкий диагональный крест|
|THIN_DIAGONAL_STRIPE|Представляет тонкую диагональную полосу|
|THIN_HORIZONTAL_CROSSHATCH|Представляет тонкий горизонтальный крест|
|THIN_HORIZONTAL_STRIPE|Представляет тонкую горизонтальную полосу|
|THIN_REVERSE_DIAGONAL_STRIPE|Представляет тонкую обратную диагональную полосу|
|THIN_VERTICAL_STRIPE|Представляет тонкую вертикальную полосу|
|VERTICAL_STRIPE|Представляет вертикальную полосу|

В приведенном ниже примере цвет переднего плана ячейки A1 установлен, но ячейка A2 настроена иметь как передний, так и фоновый цвета с фоновым узором вертикальных полос.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **Важно знать**

{{% alert color="primary" %}}

- Чтобы установить передний или фоновый цвет ячейки, используйте свойства объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) или [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color). Оба свойства вступят в силу только в том случае, если свойство [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) будет настроено.
- Свойство [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) задает цвет тени ячейки.
  Свойство [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) задает тип фонового узора, используемого для цвета переднего плана или фона. Aspose.Cells для Python via .NET предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), содержащее набор предопределенных типов фоновых узоров.
- Если вы выберете значение *BackgroundType.None* из перечисления [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype), то передний цвет не будет применен.
  Аналогично, фоновый цвет не будет применен, если вы выберете значения *BackgroundType.None* или *BackgroundType.Solid*.
- При извлечении цвета тени ячейки, если [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) равно *BackgroundType.None*, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) вернет *Color.Empty*.

{{% /alert %}}

### **Применение эффектов градиентного заливки**

Чтобы применить желаемые эффекты градиентного заливки к ячейке, используйте метод [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) объекта [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) соответственно.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **Цвета и палитра**

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

С Aspose.Cells для Python via .NET можно использовать не только существующие цвета палитры, но и настраиваемые цвета. Перед использованием пользовательского цвета добавьте его в палитру.

Эта тема обсуждает, как добавить пользовательские цвета в палитру.

### **Добавление пользовательских цветов в палитру**

Aspose.Cells для Python via .NET поддерживает 56 цветов палитры Microsoft Excel. Чтобы использовать пользовательский цвет, которого нет в палитре, добавьте его в палитру.

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) предоставляет метод [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette), принимает следующие параметры для добавления пользовательского цвета с целью изменения палитры:

- Пользовательский цвет, пользовательский цвет, который будет добавлен.
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}

{{< app/cells/assistant language="python-net" >}}
