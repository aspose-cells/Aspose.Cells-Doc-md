---  
title: Настройки заливки
linktitle: Настройки заливки  
description: Узнайте, как настраивать параметры заливки, фон и стиль ячеек с помощью библиотеки Aspose.Cells для Node.js через C++.  
keywords: Aspose.Cells, ячейки, настройки заливки, фон, стиль, Node.js через C++  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/cells-fill-settings/  
---  

## **Цвета и фоновые узоры**  

Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры.  

Aspose.Cells также поддерживает эти функции гибким образом. В этой теме мы узнаем, как использовать эти функции с использованием Aspose.Cells.  

### **Настройка цветов и фоновых узоров**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), которая позволяет получить доступ к каждому листу в Excel-файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Класс [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) имеет методы [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) и [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-), которые используются для получения и установки формата ячейки. Класс [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) предоставляет свойства для настройки цветов переднего плана и фона ячеек. Aspose.Cells содержит перечисление [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), которое включает набор предварительно заданных типов вариантов фона, приведённых ниже.  

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **Важно знать**  

{{% alert color="primary" %}}  

- Для установки цвета переднего плана или фона ячейки используйте методы [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) объекта [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) или [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-). Обе методы вступят в силу только при настройке свойства [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).  
- Метод [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) устанавливает оттеночный цвет ячейки.  
  Метод [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) задаёт тип используемого шаблона фона для цвета переднего плана или фона. В Aspose.Cells есть перечисление [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), содержащее набор предопределённых типов шаблонов фона.  
- Если выбрать значение *BackgroundType.None* из перечисления [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype), цвет переднего плана не применяется.  
  Аналогично, фоновый цвет не будет применен, если вы выберете значения *BackgroundType.None* или *BackgroundType.Solid*.  
- При извлечении цвета тени ячейки, если [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) равно *BackgroundType.None*, [**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) вернет *Color.Empty*.  

{{% /alert %}}  

### **Применение эффектов градиентного заливки**  

Чтобы применить желаемый эффект градиентной заливки к ячейке, используйте метод [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) соответствующим образом.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **Цвета и палитра**  

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.  

С помощью Aspose.Cells можно использовать не только существующие цвета палитры, но и пользовательские цвета. Прежде чем использовать пользовательский цвет, сначала добавьте его в палитру.  

Эта тема обсуждает, как добавить пользовательские цвета в палитру.  

### **Добавление пользовательских цветов в палитру**  

Aspose.Cells поддерживает 56-цветную палитру Microsoft Excel. Для использования пользовательского цвета, который не определен в палитре, добавьте цвет в палитру.  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит метод [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-), принимающий следующие параметры для добавления пользовательского цвета и изменения палитры:  

- Пользовательский цвет, пользовательский цвет, который будет добавлен.  
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.  

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
