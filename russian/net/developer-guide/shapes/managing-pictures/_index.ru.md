---
title: Управление изображениями
type: docs
weight: 10
url: /ru/net/managing-pictures/
---
Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более того, позиционированием этих картинок можно управлять во время выполнения, что более подробно обсуждается в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображения, отображающие содержимое определенных ячеек.

## **Добавление изображений**

Добавлять изображения в электронную таблицу очень просто. Требуется всего несколько строк кода:
 Просто позвоните в[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) метод[**Картинки**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) объект).[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)метод принимает следующие параметры:

- **Индекс верхней левой строки**, индекс верхней левой строки.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения вместе с путем.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Размещение изображений**

Есть два возможных способа управления позиционированием изображений с помощью Aspose.Cells:

- Пропорциональное позиционирование: определите положение, пропорциональное высоте и ширине строки.
- Абсолютное позиционирование: укажите точное положение на странице, куда будет вставлено изображение, например, на 40 пикселей левее и на 20 пикселей ниже края ячейки.

### **Пропорциональное позиционирование**

 Разработчики могут расположить изображения пропорционально высоте строки и ширине столбца, используя[**Верхняя дельтаX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) а также[**Верхняя дельтаY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) свойства[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) объект. А[**Картина**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) объект можно получить в[**Картинки**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)коллекции, передав ее индекс изображения. В этом примере изображение помещается в ячейку F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Абсолютное позиционирование**

 Разработчики также могут позиционировать изображения абсолютно, используя[**Оставил**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) а также[**верхний**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) свойства[**Картина**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)объект. В этом примере изображение помещается в ячейку F6, на 60 пикселей слева и на 10 пикселей сверху ячейки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Вставка изображения на основе ссылки Cell**

Aspose.Cells позволяет отображать содержимое ячейки рабочего листа в форме изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, которые вы вносите в данные в этой ячейке или диапазоне ячеек, автоматически отображаются в графическом объекте.

 Добавьте изображение на рабочий лист, вызвав метод[**Добавить изображение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) метод[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) объект). Укажите диапазон ячеек с помощью[**Формула**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) атрибут[**Картина**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)объект.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Предварительные темы**
- [Добавить условный набор значков с текстом Cell](/cells/ru/net/add-conditional-icons-set-with-the-cell-text/)
- [Вставить связанное изображение с веб-адреса](/cells/ru/net/insert-a-linked-picture-from-web-address/)
- [Вставьте изображение на основе ссылки Cell](/cells/ru/net/insert-a-picture-based-on-cell-reference/)
- [Загрузите веб-изображение из URL-адреса на лист Excel](/cells/ru/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

