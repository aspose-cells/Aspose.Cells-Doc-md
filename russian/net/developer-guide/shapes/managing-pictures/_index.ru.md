---
title: Управление изображениями
type: docs
weight: 10
url: /ru/net/managing-pictures/
---

Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более подробно об этом будет рассказано в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображение, отображающее содержимое определенных ячеек.

## **Добавление изображений**

Добавление изображений в электронную таблицу очень просто. Нужно лишь несколько строк кода:
Просто вызовите метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) коллекции [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) принимает следующие параметры:

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения с полным путем.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Позиционирование изображений**

Существует два возможных способа контроля позиционирования изображений с помощью Aspose.Cells:

- Пропорциональное позиционирование: определение положения пропорционально высоте и ширине строки.
- Абсолютное позиционирование: определение точного положения на странице, куда будет вставлено изображение, например, 40 пикселей слева и 20 пикселей под краем ячейки.

### **Пропорциональное позиционирование**

Разработчики могут размещать изображения пропорционально высоте строки и ширине столбца, используя свойства [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) и [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) объекта [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Одну картинку можно получить из коллекции [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection), указав ее индекс. В этом примере изображение размещается в ячейке F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Абсолютное позиционирование**

Разработчики могут также абсолютно позиционировать изображения, используя свойства [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) и [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) объекта [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). В этом примере изображение размещается в ячейке F6, 60 пикселей слева и 10 пикселей сверху от ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Вставка изображения на основе ссылки на ячейку**

Aspose.Cells позволяет отображать содержимое ячейки листа в виде изображения. Можно связать изображение с ячейкой, содержащей данные, которые нужно отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, внесенные в данные в этой ячейке или диапазоне ячеек, автоматически отобразятся в графическом объекте.

Добавление изображения на лист, вызвав метод [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Укажите диапазон ячеек, используя атрибут [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) объекта [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Продвинутые темы**
- [Добавление набора условных значков с текстом ячейки](/cells/ru/net/add-conditional-icons-set-with-the-cell-text/)
- [Вставить привязанное изображение из веб-адреса](/cells/ru/net/insert-a-linked-picture-from-web-address/)
- [Вставить изображение на основе ссылки на ячейку](/cells/ru/net/insert-a-picture-based-on-cell-reference/)
- [Загрузка веб-изображения из URL в лист Excel](/cells/ru/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

