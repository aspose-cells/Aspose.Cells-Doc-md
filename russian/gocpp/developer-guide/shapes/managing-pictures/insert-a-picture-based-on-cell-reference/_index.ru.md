---
title: Вставить изображение на основе ссылки на ячейку с помощью Golang через C++
linktitle: Вставка изображения на основе ссылки на ячейку
type: docs
weight: 150
url: /ru/go-cpp/insert-a-picture-based-on-cell-reference/
description: Узнайте, как вставить изображение на основе ссылки на ячейку с использованием Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда у вас есть пустое изображение, и вам нужно показать данные или содержимое в изображении, установив ссылку на ячейку в строке формул. Aspose.Cells поддерживает эту функцию (Microsoft Excel 2010).

{{% /alert %}}

## Вставка изображения на основе ссылки на ячейку

Aspose.Cells поддерживает отображение содержимого ячейки рабочего листа в виде изображения. Вы можете связать изображение с ячейкой, содержащей данные, которые вы хотите отобразить. Поскольку ячейка или диапазон ячеек связаны с графическим объектом, изменения, которые вы вносите в данные в этой ячейке или диапазоне ячеек, автоматически отображаются в графическом объекте. Добавьте изображение на рабочий лист, вызвав метод [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) коллекции [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Укажите диапазон ячеек, используя атрибут [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) объекта [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Пример кода

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
