---
title: Формы в диаграммах
description: Узнайте, как использовать Aspose.Cells для Python via .NET для добавления элементов управления и настройки диаграмм в Microsoft Excel. Наше руководство продемонстрирует, как управлять элементами диаграммы, изменять форматирование и улучшать внешний вид и удобство использования ваших диаграмм.
keywords: Aspose.Cells для Python via .NET, элементы управления диаграммами, настройка диаграмм, Microsoft Excel, элементы диаграммы, форматирование.
type: docs
weight: 70
url: /ru/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

Иногда необходимо вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в диаграмму. Aspose.Cells для Python via .NET может добавлять элементы управления в диаграмму во время выполнения.

{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки обеспечивают возможность предоставления пользователям информации о содержании листа.
Aspose.Cells для Python via .NET позволяет добавлять и управлять метками даже в диаграммах.

Класс [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) содержит метод с именем [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart), используемый для добавления элемента управления меткой в график. Ниже приведен список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области графика.

Метод возвращает объект [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). Класс [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) представляет собой метку в графике. Он имеет несколько важных членов:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (свойство) – указывает строку заголовка метки.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (свойство) – указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в график. В примере используется файл дизайнера (**exp_piechart.xls**), в котором есть график. Мы используем этот файл для вставки метки в график. Ниже приведен исходный код для добавления метки в график. При выполнении кода генерируется следующий вывод.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчете – использование текстового поля. Например, введите текст для выделения названия компании или для указания географического региона с наибольшими продажами. Класс [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart), который используется для добавления элемента управления текстовым полем в график. Ниже приведен список параметров, используемых для метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

Метод возвращает объект [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox). Класс [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) представляет собой текстовый блок на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить текстовое поле на диаграмму для отображения заголовка диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Добавление изображения на диаграмму**

Aspose.Cells для Python via .NET позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больше значения диаграмме или её содержимому, или вставьте брендовый файл изображения.

Класс [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

Метод возвращает объект [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Класс [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) представляет собой объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. Пример использует предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить изображение на диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Добавление флажка на диаграмму**

Aspose.Cells для Python via .NET позволяет вставлять флажки в лист диаграммы с помощью перечисления [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype). Следующий пример демонстрирует добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_1.jpg)

Ссылка на [выходной файл](101089316.xlsx), сгенерированный следующим фрагментом кода, прикреплена для вашего ознакомления.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Продвинутые темы**
- [Добавить водяной знак WordArt на диаграмму](/cells/ru/python-net/add-wordart-watermark-to-chart/)
