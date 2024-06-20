---
title: Формы в диаграммах
description: Узнайте, как использовать Aspose.Cells for .NET для добавления элементов управления и настройки графиков в Microsoft Excel. Наш руководство продемонстрирует, как манипулировать элементами графика, настраивать форматирование и улучшать общий вид и удобство использования ваших графиков.
keywords: Aspose.Cells for .NET, Элементы управления графиком, Настройка графика, Microsoft Excel, Элементы графика, Форматирование.
type: docs
weight: 70
url: /ru/net/controls-in-charts/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в график. Aspose.Cells может добавлять элементы управления в график во время выполнения.

{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки обеспечивают возможность предоставления пользователям информации о содержании листа.
Aspose.Cells позволяет добавлять и манипулировать метками даже в графиках.

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) содержит метод с именем [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), используемый для добавления элемента управления меткой в график. Ниже приведен список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области графика.

Метод возвращает объект [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). Класс [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) представляет собой метку в графике. Он имеет несколько важных членов:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (свойство) – указывает строку заголовка метки.
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (свойство) – указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в график. В примере используется файл дизайнера (**exp_piechart.xls**), в котором есть график. Мы используем этот файл для вставки метки в график. Ниже приведен исходный код для добавления метки в график. При выполнении кода генерируется следующий вывод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчете – использование текстового поля. Например, введите текст для выделения названия компании или для указания географического региона с наибольшими продажами. Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), который используется для добавления элемента управления текстовым полем в график. Ниже приведен список параметров, используемых для метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

Метод возвращает объект [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox). Класс [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) представляет собой текстовый блок на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить текстовое поле на диаграмму для отображения заголовка диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больший смысл диаграмме или ее содержимому, или вставьте файл изображения бренда.

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

Метод возвращает объект [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Класс [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) представляет собой объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. Пример использует предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить изображение на диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Добавление флажка на диаграмму**

Aspose.Cells позволяет вставлять флажки на лист диаграммы, используя перечисление [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype). В следующем примере показано добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_1.jpg)

Ссылка на [выходной файл](101089316.xlsx), сгенерированный следующим фрагментом кода, прикреплена для вашего ознакомления.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Продвинутые темы**
- [Добавить водяной знак WordArt на диаграмму](/cells/ru/net/add-wordart-watermark-to-chart/)
