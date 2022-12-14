---
title: Управление изображениями
type: docs
weight: 10
url: /ru/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет разработчикам добавлять изображения в электронные таблицы во время выполнения. Более того, позиционированием этих картинок можно управлять во время выполнения, что более подробно обсуждается в следующих разделах.

Aspose.Cells for Java поддерживает только форматы изображений: BMP, JPEG, PNG, GIF.

Индексы, используемые в примерах, начинаются с 0.

{{% /alert %}}

## **Добавление изображений**

Добавлять изображения в электронную таблицу очень просто. Требуется всего несколько строк кода.

 Просто позвоните в[**добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) метод[**Картинки**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) объект).[**добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) принимает следующие параметры:

- **Индекс верхней левой строки**, индекс верхней левой строки.
- **Индекс верхнего левого столбца**, индекс верхнего левого столбца.
- **Имя файла изображения**, имя файла изображения вместе с путем.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Расположение изображений**

Изображения можно разместить с помощью Aspose.Cells следующим образом:

- [Абсолютное позиционирование](/cells/ru/java/managing-pictures/#absolute-positioning).

### **Абсолютное позиционирование**

 Разработчики могут позиционировать изображения абсолютно с помощью[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) а также[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) методы[**Картина**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)объект.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Предварительные темы**
- [Вставить связанное изображение с веб-адреса](/cells/ru/java/insert-a-linked-picture-from-web-address/)
- [Вставьте изображение на основе ссылки Cell](/cells/ru/java/insert-a-picture-based-on-cell-reference/)
- [Вставьте веб-изображение из URL-адреса в рабочий лист Excel](/cells/ru/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
