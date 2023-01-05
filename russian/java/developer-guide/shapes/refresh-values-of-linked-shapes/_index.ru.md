---
title: Обновить значения связанных фигур
type: docs
weight: 3000
url: /ru/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Иногда у вас есть связанная фигура в вашем файле Excel, которая связана с некоторой ячейкой. В Excel Microsoft изменение значения связанной ячейки также меняет значение связанной фигуры. Это также отлично работает с Aspose.Cells, если вы хотите сохранить книгу в формате XLS или XLSX. Однако, если вы хотите сохранить свою книгу в формате PDF или HTML, вам придется позвонить[**Рабочий лист.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) для обновления значения связанной фигуры.

{{% /alert %}}

## Пример

 На следующем снимке экрана показан исходный файл Excel, используемый в приведенном ниже примере кода. Он имеет связанный**Изображение 1** привязан к ячейке A1. Мы изменим значение ячейки A1 на Aspose.Cells, а затем позвоним[**Рабочий лист.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) метод для обновления значения**Изображение 1** и сохраните его в формате PDF.

![дело:изображение_альтернативный_текст](refresh-values-of-linked-shapes_1.png)

Вы можете скачать[исходный файл Excel](5472956.xlsx) и[вывод PDF](5472955.pdf) по указанным ссылкам.

### Java код для обновления значений связанных фигур

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
