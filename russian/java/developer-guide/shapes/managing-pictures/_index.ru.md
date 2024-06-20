---
title: Управление изображениями
type: docs
weight: 10
url: /ru/java/managing-pictures/
---

Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более подробно об этом будет рассказано в следующих разделах.

В этой статье объясняется, как добавлять изображения и как вставлять изображение, отображающее содержимое определенных ячеек.

## **Добавление изображений**

Добавление изображений в электронную таблицу очень просто. Для этого достаточно всего лишь нескольких строк кода.

Просто вызовите метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) коллекции [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) принимает следующие параметры:

- **Индекс верхнего левого ряда**, индекс верхнего левого ряда.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения с полным путем.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Расположение изображений**

Изображения можно расположить с использованием Aspose.Cells следующим образом:

- [Абсолютное позиционирование](/cells/ru/java/managing-pictures/#absolute-positioning).

### **Абсолютное позиционирование**

Разработчики могут абсолютно позиционировать изображения с помощью методов [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) и [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) объекта [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Продвинутые темы**
- [Вставить привязанное изображение из веб-адреса](/cells/ru/java/insert-a-linked-picture-from-web-address/)
- [Вставка изображения на основе ссылки на ячейку](/cells/ru/java/insert-a-picture-based-on-cell-reference/)
- [Вставка веб-изображения из URL-адреса в лист Excel](/cells/ru/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
