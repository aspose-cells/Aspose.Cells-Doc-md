---
title: Элементы управления в диаграммах
linktitle: Фигуры в диаграмме
type: docs
weight: 60
url: /ru/java/controls-in-charts/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в график. Aspose.Cells может добавлять элементы управления в график во время выполнения.

{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки предоставляют средство информирования пользователей о содержании электронной таблицы. Aspose.Cells позволяет добавлять и управлять метками даже в диаграммах.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) предоставляет метод с названием [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-), используемый для добавления контрольной метки к диаграмме. Ниже приведен список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области диаграммы.

Метод возвращает объект класса [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label), где класс [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) представляет метку в диаграмме. Он имеет несколько важных членов, как показано ниже:

- свойство [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) указывает строку заголовка метки.
- свойство [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в диаграмму. В примере используется файл дизайнера, в котором есть диаграмма. Мы используем этот файл для вставки метки в диаграмму.

Ниже приведен снимок экрана файла дизайнера.

**Диаграмма дизайнера**

![todo:image_alt_text](controls-in-charts_1.png)

Ниже приведен исходный код для добавления метки в диаграмму. При выполнении кода генерируется следующий вывод.

**Метка добавлена в диаграмму**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчете – использование текстового поля. Например, введите текст для выделения названия компании или для указания географического региона с наибольшими продажами. Класс [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) предоставляет метод с именем [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-), который используется для добавления элемента управления текстовым полем в график. Ниже приведен список параметров, используемых для метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** - горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

Метод возвращает объект класса [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox), где класс [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) представляет текстовое поле в диаграмме.

В следующем примере показано, как добавить текстовое поле в диаграмму. В примере используется предыдущий файл дизайнера с диаграммой. Мы используем этот файл, чтобы вставить текстовое поле в диаграмму и показать название диаграммы.

Ниже приведен исходный код для добавления текстового поля в диаграмму. Ниже приведен результат выполнения кода.

**В диаграмму добавлено текстовое поле**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больший смысл диаграмме или ее содержимому, или вставьте файл изображения бренда.

Класс [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) предоставляет метод с именем [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-), который используется для добавления объекта изображения на диаграмму. Ниже приведен список параметров, используемых для метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

Метод возвращает объект класса [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture), где класс [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) представляет объект изображения в диаграмме.

В следующем примере показано, как добавить изображение в диаграмму. Пример использует предыдущий файл дизайнера с диаграммой. Мы используем этот файл, чтобы вставить изображение в диаграмму.

Ниже приведен исходный код для добавления изображения в диаграмму. Ниже приведен результат выполнения кода.

**Вставлено изображение в диаграмму**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Добавление флажка на диаграмму**

Aspose.Cells позволяет вам вставлять флажки в лист диаграммы, используя перечисление [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType). Приведенный ниже пример демонстрирует добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_5.jpg)

Сгенерированный кодом сниппет выходной файл [output file](InsertCheckboxInChartSheet_out.xlsx) прилагается для вашего ознакомления.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
