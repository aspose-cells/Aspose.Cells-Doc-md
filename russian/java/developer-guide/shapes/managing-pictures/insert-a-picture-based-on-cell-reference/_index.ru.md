---
title: Вставить изображение на основе ссылки на ячейку
type: docs
weight: 90
url: /ru/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells поддерживает отображение содержимого ячейки листа в виде изображения. Вы можете привязать изображение к ячейке, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек привязан к графическому объекту, изменения данных автоматически отображаются в графическом объекте. Добавьте изображение на лист, вызвав метод [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) (инкапсулированной в объекте [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Укажите диапазон ячеек, используя метод [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) объекта [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

Ниже приведен скриншот файла, сгенерированного приведенным ниже кодом.

**Вставка изображения на основе ссылки на ячейку**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
