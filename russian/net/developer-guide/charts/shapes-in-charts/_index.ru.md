---
title: Фигуры в диаграммах
description: Узнайте, как использовать Aspose.Cells for .NET для добавления элементов управления и настройки диаграмм в Microsoft Excel. Наше руководство покажет, как манипулировать элементами диаграммы, настраивать форматирование и улучшать общий вид и удобство использования ваших диаграмм.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /ru/net/controls-in-charts/
---
{{% alert color="primary" %}}

Иногда вам нужно вставить в диаграмму объекты рисования, такие как метки, текстовые поля, изображения и т. д. Aspose.Cells может добавлять элементы управления на диаграмму во время выполнения.

{{% /alert %}}

##  **Добавление элемента управления меткой на диаграмму**

Метки предоставляют средства предоставления пользователям информации о содержимом электронной таблицы.
Aspose.Cells позволяет добавлять метки и манипулировать ими даже на диаграммах.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Аддлейбелинчарт**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), используемый для добавления элемента управления меткой на диаграмму. Ниже приведен список параметров, используемых для метода:

- **вершина**– вертикальное смещение метки от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **левый**– вертикальное смещение метки от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **высота** – высота метки, в единицах 1/4000 площади диаграммы.
- **ширина** – ширина метки, в единицах 1/4000 площади диаграммы.

 Метод возвращает[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)объект.[**Этикетка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) class представляет метку на диаграмме. В нем есть несколько важных членов:

- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(свойство) – указывает строку заголовка метки.
- [**Наполнять**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (свойство) – определяет атрибуты цвета заливки.

В следующем примере показано, как добавить метку на диаграмму. В примере используется файл дизайнера (**exp_piechart.xls**), содержащий диаграмму. Мы используем этот файл для вставки метки в диаграмму. Ниже приведен исходный код для добавления метки на диаграмму. Следующий вывод генерируется при выполнении кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **Добавление элемента управления TextBox в диаграмму**

Один из способов выделить важную информацию в отчете — использовать текстовое поле. Например, введите текст, чтобы выделить название компании или указать географический регион с самыми высокими продажами.[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Аддтекстбоксинчарт**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), который используется для добавления элемента управления текстовым полем на диаграмму. Ниже приведен список параметров, используемых для метода:

- **вершина** – вертикальное смещение текстового поля от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **левый** – вертикальное смещение текстового поля от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **высота** – высота текстового поля, в единицах 1/4000 площади диаграммы.
- **ширина** – ширина текстового поля, в единицах 1/4000 площади диаграммы.

 Метод возвращает[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) объект.[**Текстовое окно**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)класс представляет текстовое поле на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить в диаграмму текстовое поле, в котором будет отображаться заголовок диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больше смысла диаграмме или ее содержимому, или вставьте файл изображения бренда.

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **вершина** – вертикальное смещение картинки от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **левый** – вертикальное смещение картинки от левого верхнего угла в единицах 1/4000 площади диаграммы.
- **транслировать** – объект потока, который содержит данные изображения.
- **ширинаМасштаб** – масштаб ширины изображения, процентное значение.
- **высотаМасштаб** – масштаб высоты изображения, процентное значение.

 Метод возвращает[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) объект.[**Картина**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Класс представляет объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл для вставки изображения в диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **Добавление флажка на диаграмму**

 Aspose.Cells позволяет вставлять флажки в лист диаграммы с помощью[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) перечисление. В следующем примере показано добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![задача: image_alt_text](controls-in-charts_1.jpg)

[выходной файл](101089316.xlsx) созданный с помощью следующего фрагмента кода, прилагается для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **Предварительные темы**
- [Добавьте водяной знак WordArt в диаграмму](/cells/ru/net/add-wordart-watermark-to-chart/)
