---
title: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells поддерживает отображение содержимого ячейки рабочего листа в виде изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, которые вы вносите в данные в этой ячейке или диапазоне ячеек, автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Укажите диапазон ячеек, используя атрибут [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) объекта [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

### Пример кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
