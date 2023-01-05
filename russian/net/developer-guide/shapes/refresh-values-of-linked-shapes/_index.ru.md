---
title: Обновить значения связанных фигур
type: docs
weight: 3200
url: /ru/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Иногда у вас есть связанная фигура в вашем файле Excel, которая связана с некоторой ячейкой. В Excel Microsoft изменение значения связанной ячейки также меняет значение связанной фигуры. Это также отлично работает с Aspose.Cells, если вы хотите сохранить книгу в формате XLS или XLSX. Однако, если вы хотите сохранить свою книгу в формате PDF или HTML, вам придется позвонить[**Рабочий лист.Фигуры.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) метод для обновления значения связанной фигуры.

{{% /alert %}}

## Пример

 На следующем снимке экрана показан исходный файл Excel, используемый в приведенном ниже примере кода. Он имеет связанное изображение, связанное с ячейками от A1 до E4. Мы изменим значение ячейки B4 на Aspose.Cells, а затем вызовем[**Рабочий лист.Фигуры.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)способ обновить значение изображения и сохранить его в формате PDF.

![дело:изображение_альтернативный_текст](refresh-values-of-linked-shapes_1.jpg)

Вы можете скачать[исходный файл Excel](95584291.xlsx) и[вывод PDF](95584292.pdf) по указанным ссылкам.

### C# код для обновления значений связанных фигур

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
