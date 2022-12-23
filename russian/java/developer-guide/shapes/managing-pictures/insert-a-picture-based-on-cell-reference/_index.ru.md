---
title: Вставьте изображение на основе ссылки Cell
type: docs
weight: 90
url: /ru/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно отобразить данные или содержимое на изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки Cell

 Aspose.Cells поддерживает отображение содержимого ячейки рабочего листа в форме изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения данных автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод[**добавить изображение**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) метод[**Коллекция форм**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) объект). Укажите диапазон ячеек с помощью[**установитьФормула**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) метод[**Рисунок**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)объект.

Ниже приведен скриншот файла, который генерирует приведенный ниже код.

**Вставка изображения на основе ссылки на ячейку**

![дело:изображение_альтернативный_текст](insert-a-picture-based-on-cell-reference_1.png)

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
