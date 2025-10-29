---
title: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Иногда у вас есть пустая картинка, и необходимо отобразить данные или содержимое в картинке, установив ссылку на ячейку в строке формул. Aspose.Cells для Python via .NET поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells для Python via .NET поддерживает отображение содержимого ячейки листа в форме изображения. Можно связать картинку с ячейкой, содержащей данные, которые нужно отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, любые изменения данных в ячейке или диапазоне автоматически отображаются в графическом объекте. Добавьте изображение на лист, вызвав метод [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (обернутый в объект [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Укажите диапазон ячеек, используя атрибут [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) объекта [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

### Пример кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
