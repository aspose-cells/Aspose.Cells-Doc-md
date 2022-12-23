---
title: Вставьте изображение на основе ссылки Cell
type: docs
weight: 150
url: /ru/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно отобразить данные или содержимое на изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки Cell

Aspose.Cells поддерживает отображение содержимого ячейки рабочего листа в форме изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, которые вы вносите в данные в этой ячейке или диапазоне ячеек, автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод[**Добавить изображение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) метод[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) коллекция (инкапсулированная в[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) объект). Укажите диапазон ячеек с помощью[**Формула**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) атрибут[**Рисунок**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)объект.

### Пример кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
