---
title: Управление изображениями
type: docs
weight: 10
url: /ru/python-net/managing-pictures/
---

Aspose.Cells для Python via .NET позволяет разработчикам добавлять изображения в таблицы во время выполнения. Более того, позиционирование этих изображений можно управлять во время выполнения, что более подробно обсуждается в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображение, отображающее содержимое определенных ячеек.

## **Добавление изображений**

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:
Просто вызовите метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) коллекции [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) принимает следующие параметры:

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения с полным путем.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Позиционирование изображений**

Есть два возможных способа управлять позиционированием изображений с помощью Aspose.Cells для Python via .NET:

- Пропорциональное позиционирование: определение положения пропорционально высоте и ширине строки.
- Абсолютное позиционирование: определение точного положения на странице, куда будет вставлено изображение, например, 40 пикселей слева и 20 пикселей под краем ячейки.

### **Пропорциональное позиционирование**

Разработчики могут размещать изображения пропорционально высоте строки и ширине столбца, используя свойства [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) и [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) объекта [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Одну картинку можно получить из коллекции [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection), указав ее индекс. В этом примере изображение размещается в ячейке F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Абсолютное позиционирование**

Разработчики могут также абсолютно позиционировать изображения, используя свойства [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) и [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) объекта [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). В этом примере изображение размещается в ячейке F6, 60 пикселей слева и 10 пикселей сверху от ячейки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Вставка изображения на основе ссылки на ячейку**

Aspose.Cells для Python via .NET позволяет отображать содержимое ячейки листа в виде фигуры изображения. Можно связать изображение с ячейкой, содержащей нужные данные. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения в данных этой ячейки или диапазона автоматически отображаются в графическом объекте.

Добавление изображения на лист, вызвав метод [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Укажите диапазон ячеек, используя атрибут [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) объекта [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Продвинутые темы**
- [Добавление набора условных значков с текстом ячейки](/cells/ru/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Вставить привязанное изображение из веб-адреса](/cells/ru/python-net/insert-a-linked-picture-from-web-address/)
- [Вставить изображение на основе ссылки на ячейку](/cells/ru/python-net/insert-a-picture-based-on-cell-reference/)
- [Загрузка веб-изображения из URL в лист Excel](/cells/ru/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
